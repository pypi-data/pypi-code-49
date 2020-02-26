import importlib
import os


def load_func(config):
    bath_path = config['name']
    bath_type = config['type']
    other_parms = {k:config[k] for k in config if k not in ["name", "type"]} 
    print(bath_path)
    m = importlib.import_module(bath_path)
    func = getattr(m, bath_type)
    return func, other_parms

def loaddata(path):
    idx2ques = {}
    idx2label = {}
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            items = line.strip().split("\t")
            idx2ques[int(items[-1])] = items[0]
            idx2label[int(items[-1])] = items[1]
    print("load data done")
    return idx2ques, idx2label

def loaddict(dict_config):
    all_dict = {}
    for config in dict_config:
        dict_name = config['name']
        dict_path = config['path']
        if not os.path.exists(dict_path):
            raise FileExistsError(f"dict load failed, {dict_path} not exist")
        with open(dict_path, 'r', encoding='utf-8') as f:
            all_dict[dict_name] = [line.strip() for line in f.readlines()]
    return all_dict

class QueryInfo(object):
    def __init__(self, text):
        self.text = text
        self.textclean = None
        self.terminfo = None
        self.embinfo = None

class ResultInfo(object):
    def __init__(self):
        self.retrieval = {}
        self.matching = {}
        self.ranking = {}
