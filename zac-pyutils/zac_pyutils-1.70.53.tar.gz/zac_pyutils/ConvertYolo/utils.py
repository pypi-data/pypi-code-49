# reference: https://github.com/zzh8829/yolov3-tf2/issues/43

import numpy as np
import tensorflow as tf
import cv2
import sys
import os
from PIL import Image

YOLOV3_LAYER_LIST = [
    'yolo_darknet',
    'yolo_conv_0',
    'yolo_output_0',
    'yolo_conv_1',
    'yolo_output_1',
    'yolo_conv_2',
    'yolo_output_2',
]

YOLOV3_TINY_LAYER_LIST = [
    'yolo_darknet',
    'yolo_conv_0',
    'yolo_output_0',
    'yolo_conv_1',
    'yolo_output_1',
]


def load_darknet_weights(model, weights_file, tiny=False):
    wf = open(weights_file, 'rb')
    major, minor, revision, seen, _ = np.fromfile(wf, dtype=np.int32, count=5)

    if tiny:
        layers = YOLOV3_TINY_LAYER_LIST
    else:
        layers = YOLOV3_LAYER_LIST

    for layer_name in layers:
        sub_model = model.get_layer(layer_name)
        for i, layer in enumerate(sub_model.layers):
            if not layer.name.startswith('conv2d'):
                continue
            batch_norm = None
            if i + 1 < len(sub_model.layers) and \
                    sub_model.layers[i + 1].name.startswith('batch_norm'):
                batch_norm = sub_model.layers[i + 1]

            print(f"{sub_model.name}/{layer.name} {'bn' if batch_norm else 'bias'}")

            filters = layer.filters
            size = layer.kernel_size[0]
            in_dim = layer.input_shape[-1]

            if batch_norm is None:
                conv_bias = np.fromfile(wf, dtype=np.float32, count=filters)
            else:
                # darknet [beta, gamma, mean, variance]
                bn_weights = np.fromfile(
                    wf, dtype=np.float32, count=4 * filters)
                # tf [gamma, beta, mean, variance]
                bn_weights = bn_weights.reshape((4, filters))[[1, 0, 2, 3]]

            # darknet shape (out_dim, in_dim, height, width)
            conv_shape = (filters, in_dim, size, size)
            conv_weights = np.fromfile(
                wf, dtype=np.float32, count=np.product(conv_shape))
            # tf shape (height, width, in_dim, out_dim)
            conv_weights = conv_weights.reshape(
                conv_shape).transpose([2, 3, 1, 0])

            if batch_norm is None:
                layer.set_weights([conv_weights, conv_bias])
            else:
                layer.set_weights([conv_weights])
                batch_norm.set_weights(bn_weights)

    assert len(wf.read()) == 0, 'failed to read all data'
    wf.close()


def draw_outputs(img_inp, outputs, class_names):
    boxes, objectness, classes, nums = outputs
    wh = np.flip(img_inp.shape[0:2])
    pixel_max_v=255 if np.max(img_inp)>1 else 1
    img = img_inp.copy()
    for i in range(nums):
        x1y1 = tuple((np.array(boxes[i][0:2]) * wh).astype(np.int32))
        x2y2 = tuple((np.array(boxes[i][2:4]) * wh).astype(np.int32))
        img = cv2.rectangle(img, x1y1, x2y2, (pixel_max_v, 0, 0), 2)
        # cv2.putText 参数: 图片，添加的文字，左上角坐标，字体，字体大小，颜色，字体粗细
        img = cv2.putText(img, '{}={:.4f}'.format(
            class_names[int(classes[i])], objectness[i]),
            x1y1, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, pixel_max_v), 2)
    return img


def draw_labels(x, y, class_names):
    img = x.numpy()
    boxes, classes = tf.split(y, (4, 1), axis=-1)
    classes = classes[..., 0]
    wh = np.flip(img.shape[0:2])
    for i in range(len(boxes)):
        x1y1 = tuple((np.array(boxes[i][0:2]) * wh).astype(np.int32))
        x2y2 = tuple((np.array(boxes[i][2:4]) * wh).astype(np.int32))
        img = cv2.rectangle(img, x1y1, x2y2, (255, 0, 0), 2)
        img = cv2.putText(img, class_names[classes[i]],
                          x1y1, cv2.FONT_HERSHEY_COMPLEX_SMALL,
                          1, (0, 0, 255), 2)
    return img


def freeze_all(model, frozen=True):
    model.trainable = not frozen
    if isinstance(model, tf.keras.Model):
        for l in model.layers:
            freeze_all(l, frozen)


def trace_model_call(model):
    from tensorflow.python.framework import tensor_spec
    from tensorflow.python.eager import def_function
    from tensorflow.python.util import nest
    
    inputs = model.inputs
    input_names = model.input_names

    input_signature = []
    for input_tensor, input_name in zip(inputs, input_names):
        input_signature.append(tensor_spec.TensorSpec(
            shape=input_tensor.shape, dtype=input_tensor.dtype,
            name=input_name))

    @def_function.function(input_signature=input_signature, autograph=False)
    def _wrapped_model(*args):
        inputs = args[0] if len(input_signature) == 1 else list(args)
        outputs_list = nest.flatten(model(inputs=inputs))
        output_names = model.output_names
        return {"{}_{}".format(kv[0], i): kv[1] for i, kv in enumerate(
            zip(output_names, outputs_list))}

    return _wrapped_model


if __name__ == "__main__":
    print(sys.argv)
    try:
        opt=sys.argv[1]
    except Exception as e:
        print("USAGE: python utils.py {convert,detect}")
        sys.exit(0)
    
    if opt=="convert":
        try:
            classes=int(sys.argv[2])
            darknet_weight_fp=sys.argv[3]
        except:
            print("USAGE: python utils.py convert <classes_num> <darknet_weight_fp>")
            print("Example: python utils.py convert 4 ./custom_w/yolo_w_final.weights")
            sys.exit(0)

        pb_fp=os.path.splitext(darknet_weight_fp)[0]+"_pb"
        print(f"opt:{opt}\nclasses:{classes}\ndarknet_weight_fp:{darknet_weight_fp}\npb_fp:{pb_fp}")

        from _Yolo_v3 import YoloV3
        yolo = YoloV3(classes=classes)

        load_darknet_weights(yolo,darknet_weight_fp)

        # 测试是否正常
        img = np.random.random((1, 320, 320, 3)).astype(np.float32)
        output = yolo(img)
        print("available.")
        
        # yolo.save_weights(os.path.splitext(darknet_weight_fp)[0]+"_ckpt")
        tf.saved_model.save(yolo, pb_fp, signatures=trace_model_call(yolo))
    elif opt=="detect":
        try:
            class_names_fp=sys.argv[2]
            tf_weight_fp=sys.argv[3]
            img_fp=sys.argv[4]
        except:
            print("USAGE: python utils.py detect <classes_names_fp> <tf_weight_fp> <img_fp>")
            sys.exit(0)
        with open(class_names_fp,"r") as fr:
            class_names=[i.strip() for i in fr.readlines()]
            classes=len(class_names)
        print(f"class_names: {','.join(class_names)}")    

        # init yolo
        from _Yolo_v3 import YoloV3
        yolo = YoloV3(classes=classes)
        # load_darknet_weights(yolo,darknet_weight_fp)
        yolo.load_weights(tf_weight_fp)

        # detect img
        img = np.array(Image.open(img_fp).resize((416,416)))
        img = np.expand_dims(img,axis=0)
        boxes, scores, classes, nums = yolo(img)
        img = draw_outputs(img, (boxes[0], scores[0], classes[0], nums[0]), class_names)
        cv2.imwrite("./utils_detected.jpg", img)
        pass
    else:
        print("USAGE: python utils.py {convert,detect}")