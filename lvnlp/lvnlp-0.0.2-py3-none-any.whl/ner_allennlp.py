import logging
import os
import re
import sys
from typing import Tuple, List
from allennlp.data.tokenizers import Token
from allennlp.predictors import Predictor

logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.DEBUG)


def substitute_text(text, substitutions: List[Tuple[int, int, str]]):
    substitutions.sort(key=lambda x: x[0], reverse=True)
    substituted_text = text
    for sub_start, sub_end, sub_text in substitutions:
        substituted_text = text[:sub_start] + sub_text + substituted_text[sub_end:]
    return substituted_text


class WsTokenizer:
    RE_WORD_PUNKT_TOKENIZER = re.compile(r'\n|\w+|[^\w\s]+')

    def __init__(self, min_sentence_newlines=1):
        self.min_sentence_newlines = min_sentence_newlines

    def _spans(self, s):
        return [(s[m.start():m.end()], m.start(), m.end()) for m in WsTokenizer.RE_WORD_PUNKT_TOKENIZER.finditer(s)]

    def words(self, s):
        return [w for w, _, _ in self._spans(s) if w != '\n']

    def sentences(self, text):
        return [text[sent[0][1]:sent[-1][2]] for sent in self.tokenize(text)]

    def tokenize(self, s):
        sentences = []
        sentence = []
        newline_count = 0
        for w, s, e in self._spans(s):
            if w == '\n':
                newline_count += 1
            else:
                newline_count = 0
                sentence.append((w, s, e))

            if newline_count > self.min_sentence_newlines and sentence:
                sentences.append(sentence)
                sentence = []
        if sentence:
            sentences.append(sentence)
        return sentences


@Predictor.register('tagger')
class TaggerPredictor(Predictor):
    def __init__(self, model, dataset_reader):
        super().__init__(model, dataset_reader)
        self._tokenizer = WsTokenizer()

    def get_spans(self, text, labels, start_offsets, end_offsets):
        spans = []
        prev_label = None
        prev_start = -1
        prev_end = -1
        for l, s, e in zip(labels, start_offsets, end_offsets):
            prefix, label, *_ = l.split('-', 1) + [None]
            if prefix == 'B' or prefix == 'U' or (prev_label and prev_label != label):
                # new tag starts
                if prev_label:
                    spans.append({'text': text[prev_start:prev_end], 'label': prev_label, 'start': prev_start, 'end': prev_end})
                prev_label = label
                prev_start = s
                prev_end = e
            elif label is None:
                # outside
                if prev_label:
                    spans.append({'text': text[prev_start:prev_end], 'label': prev_label, 'start': prev_start, 'end': prev_end})
                prev_label = None
                prev_start = -1
                prev_end = -1
            else:
                # tag continues
                prev_end = e
        if prev_label:
            spans.append({'text': text[prev_start:prev_end], 'label': prev_label, 'start': prev_start, 'end': prev_end})
        return spans

    def get_entities(self, text):
        res = []
        sentences = self._tokenizer.tokenize(text)
        instances = [self._dataset_reader.text_to_instance([Token(t[0]) for t in s]) for s in sentences]
        output_instances = self.predict_batch_instance(instances)
        for s, oi in zip(sentences, output_instances):
            res += self.get_spans(text, oi.get('tags'), [x[1] for x in s], [x[2] for x in s])
        return res

    def predict(self, sentence: str):
        return self.predict_json({"sentence": sentence})

    def _json_to_instance(self, json_dict):
        sentence = json_dict["sentence"]
        tokens = [Token(w) for w in self._tokenizer.words(sentence)]
        return self._dataset_reader.text_to_instance(tokens)

    @classmethod
    def make_app(cls, ner_model=None):
        from flask import Flask, jsonify, request
        NER_MODEL = os.getenv('NER_MODEL', ner_model)

        app = Flask(__name__)
        app.ner = TaggerPredictor.from_path(NER_MODEL, 'tagger')

        @app.route('/', methods=['GET', 'POST'])
        def api_ner():
            req = request.get_json(force=True, silent=True) or request.values
            text = req['text'] or ''
            try:
                entities = app.ner.get_entities(text)
                return jsonify(entities)
            except Exception as e:
                logger.exception('Exception on ner {}... {}'.format(repr(text), e))
                return jsonify({'error': str(e)}), 500
        return app

    @classmethod
    def run_app(cls, ner_model=None, port=8800):
        app = cls.make_app(ner_model=ner_model)
        PORT = os.getenv('PORT', port)
        HOST = os.getenv('HOST', '0.0.0.0')

        print('RUN API %r %r' % (HOST, PORT))
        app.run(host=HOST, port=int(PORT), debug=False, threaded=False)


if __name__ == '__main__':
    TaggerPredictor.run_app(ner_model=sys.argv[1])
