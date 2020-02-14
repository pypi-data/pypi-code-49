
def generate_list_get_param(name: str, data: list) -> str:
    return f'&{name}[]='.join(value for value in data)

def convert(word: str) -> str:
    return ''.join(x.capitalize() or '_' for x in word.split('_'))