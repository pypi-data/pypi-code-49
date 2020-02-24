import numpy as np
from .classObj import Operation


class Namespace:
    """
    Class Namespace
    """

    def __init__(self, refid: str, name: str):
        """
        Constructor
        :param refid: the namespace xml id
        :param name: the namespace name
        """
        self.refid = refid
        self.name = name
        self.classes = []
        self.functions = []

    def add_class(self, clss_refid: str):
        """
        add a class to the namespace
        :param clss_refid: the class refid
        :return:
        """
        self.classes = np.append(self.classes, clss_refid)

    def add_func(self,func: Operation):
        """
        add a function to the namespace
        :param func: the function object
        :return:
        """
        self.functions = np.append(self.functions, func)

    def to_string(self):
        """
        create a string for displaying the object
        :return: the object as a string
        :rtype: str
        """

        res = "Namespace "+self.name+"\n"
        res += "  Classes:\n"
        for c in self.classes:
            res += "    "+c+"\n"
        res += "  Functions:\n"
        for f in self.functions:
            res += "    " + f.to_string() + "\n"
        return res

    def __str__(self):
        return self.to_string()
