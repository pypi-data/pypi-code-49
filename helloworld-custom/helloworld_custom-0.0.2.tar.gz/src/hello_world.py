def hello_world_all(params=None):
    if params is None:
        return "Hello World"
    else:
        return "Hello {}!".format(params)