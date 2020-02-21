from symmetric import router, app


@router("/wenawena")
def sesese():
    return "Hola Mundo!"


@router("/add")
def another_function(a, b):
    return a + b


if __name__ == '__main__':
    app.run()
