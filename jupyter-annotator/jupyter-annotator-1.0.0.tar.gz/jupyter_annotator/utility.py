def string_to_list(string):
    lst = string.split(',')
    lst = [x.strip() for x in lst]
    return lst

def list_to_string(lst):
    return ',   '.join(lst)

def most_common(lst): 
    """https://stackoverflow.com/questions/1518522/find-the-most-common-element-in-a-list
    """
    return max(set(lst), key = lst.count) 