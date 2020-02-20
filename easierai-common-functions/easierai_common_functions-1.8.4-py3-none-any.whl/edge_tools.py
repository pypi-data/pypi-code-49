import tensorflow as tf
from tensorflow.keras import backend as K
import numpy
import common_functions.constants as constants

class Edge_Toolkit:

    def __init__(self, logging):
        self.logger = logging
        self.samples = None
        pass

    def convert_model_lite(self, calibration_data, model_name="model", tf_model_dir=None, keras_model=None):
        self.samples = calibration_data

        if tf_model_dir is not None:
            converter = tf.lite.TFLiteConverter.from_saved_model(tf_model_dir)
        else:
            
            if tf.__version__.split(".")[0] == '1':
                keras_model.save("../storage/" + model_name + "." + constants.MODEL_EXTENSION)
                # Clear graph in prep for next step.
                try:
                    K.clear_session()
                except Exception as e:
                    pass                
                converter = tf.lite.TFLiteConverter.from_keras_model_file("../storage/" + model_name + "." + constants.MODEL_EXTENSION)
            else:    
                converter = tf.lite.TFLiteConverter.from_keras_model(keras_model)

        converter.representative_dataset = self.representative_dataset_gen
        converter.optimizations = [tf.lite.Optimize.DEFAULT]

        try:
            tflite_model = converter.convert()
        except Exception as e:
            self.logger.error("Error converting model to tf lite: " + str(e))
            return False

        if tf_model_dir is not None:
            open('../storage/' + tf_model_dir + "/" + model_name + "." + constants.TF_LITE_EXTENSION, "wb").write(
                tflite_model)
            self.logger.info("Converted tf model " + str(tf_model_dir) + " to tf lite")
        else:
            open('../storage/' + model_name + "." + constants.TF_LITE_EXTENSION, "wb").write(
                tflite_model)
            # Clear graph in prep for next step.
            try:
                K.clear_session()
            except Exception as e:
                pass
            self.logger.info("Converted keras model " + model_name + " to tf lite")
        return True

    def convert_model_tpu(self, calibration_data, model_name="model", tf_model_dir=None, keras_model=None):
        try:
            K.clear_session()
        except Exception as e:
            pass
        self.samples = calibration_data

        if tf_model_dir is not None:
            converter = tf.lite.TFLiteConverter.from_saved_model(tf_model_dir)
        else:
            if tf.__version__.split(".")[0] == '1':
                keras_model.save("../storage/" + model_name + "." + constants.MODEL_EXTENSION)
                try:
                    K.clear_session()
                except Exception as e:
                    pass
                converter = tf.lite.TFLiteConverter.from_keras_model_file("../storage/" + model_name + "." + constants.MODEL_EXTENSION)
            else:    
                converter = tf.lite.TFLiteConverter.from_keras_model(keras_model)

        if tf.__version__.split(".")[0] == '1':
            converter.target_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]        
        else:
            converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
        converter.representative_dataset = self.representative_dataset_gen
        converter.inference_input_type = tf.uint8
        converter.inference_output_type = tf.uint8
        converter.optimizations = [tf.lite.Optimize.DEFAULT]

        try:
            tflite_model = converter.convert()
        except Exception as e:
            self.logger.error("Error converting model to tf lite: " + str(e))
            return

        if tf_model_dir is not None:
            open('../storage/' + tf_model_dir + "/" + model_name + "." + constants.TF_LITE_EXTENSION, "wb").write(
                tflite_model)
            try:
                K.clear_session()
            except Exception as e:
                pass
            self.logger.info("Converted tf model " + str(tf_model_dir) + " to tf lite specific for TPU")

            cmd = ['edgetpu_compiler',
                "../storage/" + tf_model_dir + "/" + model_name + "." + constants.TF_LITE_EXTENSION, '-o', args['output']]
        else:
            try:
                open('../storage/' + model_name + "." + constants.TF_LITE_EXTENSION, "wb").write(
                    tflite_model)
                try:
                    K.clear_session()
                except Exception as e:
                    pass
                self.logger.info("Converted keras model " + model_name + " to tf lite specific for TPU")
            except Exception as e:
                self.logger.error("Error saving tf lite model to file: " + str(e))
                try:
                    K.clear_session()
                except Exception as e:
                    pass
                return False

            cmd = ['edgetpu_compiler', '-o', '../storage',
                "../storage/" +  model_name + "." + constants.TF_LITE_EXTENSION]
        
        try:
            res = subprocess.run(cmd, stdout=subprocess.PIPE)
        except FileNotFoundError as e:
            self.logger.error('The edge tpu complier is not installed: ' + str(e))
            return False
        except Exception as e:
            self.logger.error('The edge tpu complier throwed an error: ' + str(e))
            return False
        return True

    def representative_dataset_gen(self):
        for i in range(len(self.samples)):
            data = numpy.array(self.samples[i: i + 1], dtype=numpy.float32)
            yield [data]
