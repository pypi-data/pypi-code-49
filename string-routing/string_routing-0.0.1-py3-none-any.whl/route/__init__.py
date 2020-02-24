"""
 Basic exception to alert the dev that the trigger they are calling does not exist
 Easier to view the code in a try, catch clause.
"""
class RouteException(Exception):

    def __init__(self):
        super().__init__("No route set for that link.")

"""
    Main Class: StringRouter
    Creates a dictionary of routes and the reference to each function
    Allows the decorator to link the function to the name
    Allows the trigger to map the links to the functions and execute
"""

class StringRouter:
    """
        Basic beginner route allocation
    """
    def __init__(self):
        self.routes = {}

    """
        :decorator: to route the functions to a link keyword
    """
    def route(self, link):
        def wrapper(function):
            self.routes[link] = function
            return function
        return wrapper

    """
        Trigger. Call on the string to execute its linked function
    """
    def trigger(self, link):
        function = self.routes.get(link)
        if function:
            return function()
        else:
            raise RouteException()

    def __str__(self):
        return str(self.routes)