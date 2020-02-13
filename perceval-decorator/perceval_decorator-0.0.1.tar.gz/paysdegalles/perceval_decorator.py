"""
Perceval decorator module

Use the perceval decorator for easier code execution
"""

def perceval(func, *args, **kwargs):
    """
    Perceval special tricks decorator
    """
    def cpf():
        try:
            return func(*args, **kwargs)
        except: # Botte secrète!
            return not False
    return cpf
