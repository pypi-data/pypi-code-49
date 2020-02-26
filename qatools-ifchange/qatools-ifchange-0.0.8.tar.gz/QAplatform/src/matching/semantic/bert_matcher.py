"""
gRPC and REST client 
pre-process text and get predictions from models
"""
import sys
import json
import requests
from src.matching.semantic.bert.similarity import SimProcessor
from src.matching.matching_base import MatchingBase
import tensorflow as tf
tf.logging.set_verbosity(tf.logging.ERROR)

class BertMatcher(MatchingBase):
    def __init__(self, *args, **kwargs):
        super(BertMatcher, self).__init__(*args, **kwargs)
        self.model_name = 'matching'
        self.model_version = self.config['model_version']
        self.max_seq_length = 512
        self.ip = self.config['server_ip']
        self.rest_port = self.config['server_port']

        # REST
        self.model_base_url = 'http://{}:{}/v1/models/matching/versions/{}:predict'.format(self.ip, self.rest_port, self.model_version)
        self.max_seq_length = self.config['max_seq_length']
        # init
        self.vocab = self.config['vocab_file']
        self.dp = SimProcessor(self.vocab, self.max_seq_length)

    def predict(self, texts):
        
        features = self.dp.generate_from_input(texts)
        return self.rest_client(features)

    def rest_client(self, features):
        headers = {"content-type": "application/json"}
        model_url = self.model_base_url
        features = json.dumps({"signature_name": "serving_default", "instances": features})
        json_response = requests.post(model_url, data=features, headers=headers)
        if json_response.status_code == 200:
            predictions = json.loads(json_response.text)['predictions']
        else:
            predictions = None
        return predictions

    def compute_similarity(self, query_info, retrived_indices):
        
        query = query_info.textclean
        tuples = [(query, self.dict_map['corpus'][0][s]) for s in retrived_indices]
        
        predictions = self.predict(tuples)
        preds = [x[1] for x in predictions]
        return preds

