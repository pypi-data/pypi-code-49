# ===== default imports beginning =======
from datetime import datetime;

# =============================
# ===== custom imports beginning =======
import json;

# ======== imports end =============
# =============================

class ModelWrapper:
    """
    Important: no method should write to stdout.
    Do not use print() or any other methods, that do.
    """

    hot_log_length = 100;
    # this is the length of a lists saving latest input and output values with timestamps

    def __init__(self, path_to_artifacts):
        """
        path_to_artifacts is a compulsory argument, never omit it in the __init__() declaration;
        it will convey a path to all files deployed to a server;
        if a model is needed to be loaded to memory before scroring, do it here.
        """
        # path_to_model = "{}/".format(path_to_artifacts);

        self.status = "Alive and kicking"; #PRIVATE

        #######################
        ###  hot log lists are to be used for monitoring and as sources of data to store
        ### for general purposes
        #######################
        self.inputs_hot_log = [];
        self.outputs_hot_log = [];
        self.hot_log_timestamps_stack = [];
        #######################

        return None;

    def __call__(self, data_json):

        preprocessed_data = self.preprocess(data_json);
        score = self.predict(preprocessed_data);
        prediction = self.postprocess(score);

        return prediction;

    def preprocess(self, data_json):
        """
        Code here data preprocessing to be consumed by the model.
        e.g. unpacking json, base64-encoded data and so on.
        """

        the_timestamp = datetime.now();
        timestamp_string = str(the_timestamp);
        data = json.loads(data_json);

        preprocessing_result = data; # here some transformations on the data might go

        self.hot_log_timestamps_stack.append(timestamp_string);

        if len(self.inputs_hot_log) >= self.hot_log_length:
            self.inputs_hot_log.pop(0);

        self.inputs_hot_log.append(
            {
                "timestamp": timestamp_string,
                "the_data": preprocessing_result            
            });

        return preprocessing_result

    def predict(self, inputs):
        """
        Code here a model invocation to score prepared input data
        """
        
        score = repr(inputs);

        return score;

    def postprocess(self, data):
        """
        Code here model's prediction preparation before sending it back to requester
        or to anywhere else (e.g. to the next model of a scoring pipeline)
        """
        
        prediction = {"prediction": data};

        timestamp_string = self.hot_log_timestamps_stack.pop(0);

        if len(self.outputs_hot_log) >= self.hot_log_length:
            self.outputs_hot_log.pop(0);

        self.outputs_hot_log.append(
            {
                "timestamp": timestamp_string,
                "the_data": prediction            
            });


        prediction_json = json.dumps(prediction);

        return prediction_json;

    def lifeSign(self):
        return self.status;