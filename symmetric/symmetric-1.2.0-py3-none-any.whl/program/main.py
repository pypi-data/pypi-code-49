from symmetric import symmetric


@symmetric.router("/sample")
def some_function():
    """Greets the world."""
    return "Hello World!"


@symmetric.router("/add")
def another_function(a, b=372):
    """
    Adds :a and :b and returns the result of
    that operation.
    """
    return a + b
