"""input_handlers.py: module for handling all different types of user inputs."""


def input_integers(message):
    """Handle inputs if they are supposed to be integers"""
    while True:
        answer = input(message)
        try:
            answer_int = int(answer)
            return answer_int
        except ValueError:
            if answer.casefold() == "none":
                return None
            else:
                print('Please enter an integer')


def input_string(message):
    """Handle inputs if they are supposed to be strings"""
    while True:
        answer = input(message)
        if isinstance(answer, str):
            if answer.casefold() == "none":
                return None
            else:
                return answer
        else:
            print('Please enter an integer')