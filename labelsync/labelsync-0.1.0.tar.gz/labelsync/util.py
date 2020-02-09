import hashlib

def map_to_dictionary(labels, id_key):
    """Turns list of labels into a dictionary indexed by id_key parameter

        :param list labels: labels list to be indexed
        :param string id_key: key to be used as an index
        :return: dictionary of labels
    """
    result = {}
    for label in labels:
        result[label[id_key]] = label
    return result

def hash_str(*strings):
    """Hash list of strings to sha1 hexdigest
    """
    h = hashlib.sha1()
    for string in strings:
        h.update(string.encode())
    return h.hexdigest()
