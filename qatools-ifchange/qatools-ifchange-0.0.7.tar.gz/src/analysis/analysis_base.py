class AnalysisBase:
    def process(self, text):
        raise NotImplementedError(
            "Analysis plugin must have sigle-process function")

    def value_process(self, data_dict):
        '''
        data_dict repr {idx1: text1,  idx2:text2...}
        '''
        return {idx: self.process(text) for idx, text in data_dict.items()}
