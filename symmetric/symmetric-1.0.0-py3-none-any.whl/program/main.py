from symmetric import symmetric


@symmetric.router("/wenawena")
def sesese():
    return "Hola Mundo!"


@symmetric.router("/add")
def another_function(a, b):
    return a + b


if __name__ == '__main__':
    symmetric.run()
