import requests

STEPS_TOKENIZATION = 'tokenizer'
STEPS_MORPHOLOGY = 'morpho'
STEPS_NER = 'ner'
STEPS_PARSER = 'parser'


def nlppipe_run(text, steps=None):
    if not steps:
        steps = [STEPS_MORPHOLOGY, STEPS_NER]

    data = {'text': text} if isinstance(text, str) else text

    r = requests.post('http://nlp.ailab.lv/api/nlp', json={'data': data, 'steps': steps})
    doc = r.json()['data']
    return doc
