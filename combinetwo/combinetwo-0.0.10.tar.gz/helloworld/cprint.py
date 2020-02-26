def say_hello(name=None):
    if name == None:
        return 'Hello, World!'
    else:
        return f'Hello {name}!'