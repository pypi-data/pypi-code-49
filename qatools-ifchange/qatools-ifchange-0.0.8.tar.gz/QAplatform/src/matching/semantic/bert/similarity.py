"""
进行文本相似度预测的示例。可以直接运行进行预测。
参考了项目：https://github.com/chdd/bert-utils

"""

from .run_classifier import InputExample, DataProcessor, convert_examples_to_features
import src.matching.semantic.bert.tokenization as tokenization


# os.environ['CUDA_VISIBLE_DEVICES'] = '1'


class SimProcessor(DataProcessor):

    def __init__(self, vocab, max_sent_len):
        self.vocab = vocab
        self.max_sent_len = max_sent_len
        self.tokenizer = tokenization.FullTokenizer(vocab_file=self.vocab, do_lower_case=True)

    def get_sentence_examples(self, questions):
        examples = []
        for index, data in enumerate(questions):
            guid = 'test-%d' % index
            text_a = tokenization.convert_to_unicode(str(data[0]))
            text_b = tokenization.convert_to_unicode(str(data[1]))
            label = str(0)
            examples.append(InputExample(guid=guid, text_a=text_a, text_b=text_b, label=label))
        return examples

    def get_labels(self):
        return ['0', '1']

    def generate_from_input(self, sentences):
        #tokenizer = tokenization.FullTokenizer(vocab_file=self.vocab, do_lower_case=True)

        predict_examples = self.get_sentence_examples(sentences)
        features = convert_examples_to_features(predict_examples, self.get_labels(), self.max_sent_len,
                                                self.tokenizer)
        res = []
        for feature in features:

            res += [{
                'input_ids': feature.input_ids,
                'input_mask': feature.input_mask,
                'segment_ids': feature.segment_ids,
                'label_ids': 0
            }]
        return res
    #
# if __name__ == '__main__':
#     sim = BertSim()
#     sim.start_model()
#     sim.predict_sentences([("我喜欢妈妈做的汤", "妈妈做的汤我很喜欢喝")])
