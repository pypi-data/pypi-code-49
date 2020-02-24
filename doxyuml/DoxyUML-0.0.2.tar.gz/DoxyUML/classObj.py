from typing import List
import abc
import numpy as np


class Member(metaclass=abc.ABCMeta):
    """
    Class Member
    """

    def __init__(self,name:str,privacy:str,typ:str):
        """
        Constructor
        :param name: the member name
        :type name: str
        :param privacy: the member privacy
        :type privacy: str (public, private or protected)
        :param typ: the member type
        :type typ: str
        """

        assert(privacy in ["public", "private",  "protected" ])

        self.name = name
        self.privacy = privacy
        self.type = typ
        self.brief_desc = ""
        self._xrefsect = []  # xref sections for custom doxygen tags

        self.header_location = ""  # header file location
        self.body_location = ""  # cpp file location

    @property
    def xrefsect(self):
        return self._xrefsect

    @abc.abstractmethod
    def to_string(self):
        """
        create a string for displaying the object
        :return: the object as a string
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def to_graphviz(self):
        """
        create a string for embedding in a Graphviz node
        :return: the object as a string
        :rtype: str
        """
        pass


class Attribute(Member):
    """
    Class attribute
    """

    def __init__(self, name: str, privacy: str, typ: str):
        """
        Constructor
        :param name: the attribute name
        :type name: str
        :param privacy: the attribute privacy
        :type privacy: str
        :param typ: the attribute type
        :type typ: str
        """

        Member.__init__(self, name, privacy,typ)

    def to_string(self):
        """
        create a string for displaying the object
        :return: the object as a string
        :rtype: str
        """
        res = "  " + self.privacy + " " + self.type + " " + self.name
        return res

    def to_graphviz(self):
        """
        create a string for embedding in a Graphviz node
        :return: the string
        """
        s = "+ "

        if self.privacy == "private":
            s = "- "
        elif self.privacy == "protected":
            s = "# "

        s += self.name + ": " + self.type
        return s


class Operation(Member):
    """
    Class operation
    """

    def __init__(self, name: str, privacy: str, retType: str, args: List[str]):
        """

        :param name: the operation name
        :type name: str
        :param privacy: the operation privacy
        :type privacy: str
        :param retType: the return type
        :type retType: str
        :param args: the operation arguments
        :type args: List[str]
        """

        Member.__init__(self, name, privacy, retType)
        self.arguments = args

    def to_string(self):
        """
        create a string for displaying the object
        :return: the object as a string
        :rtype: str
        """
        res = "  " + self.privacy + " " + self.type + " " + self.name +"("+", ".join(self.arguments)+")"
        for sec in  self.xrefsect:
            if sec._title == "task":
                res += " task: " + sec._description
        return res

    def to_graphviz(self):
        s = "+"
        if self.privacy == "private":
            s = "- "
        elif self.privacy == "protected":
            s = "# "
        s += self.name
        s += "("
        if self.arguments:
            s += ", ".join(self.arguments)
        s += ")" ": "
        s += str(self.type)
        return s


class ObjClass:
    """
    OOP class object
    """

    def __init__(self, refid: str, name: str, stereotype: str = ""):
        """
        Constructor
        :param refid: xml refid
        :param name: the Class name
        :type name: str
        :param sterotype: the Class stereotype
        :type stereotype: str
        """
        self.refid = refid
        self.name = name
        self.stereotype = stereotype
        self.generalization = []  # list of base classes
        self.attributes = []
        self.operations = []
        self.aggregation = []
        self.composition = []


    def add_attributes(self,att):
        self.attributes = np.append(self.attributes,att)

    def add_operations(self,op):
        self.operations = np.append(self.operations,op)

    def add_generalizations(self,gens):
        self.generalization = np.append(self.generalization,gens)

    def add_aggregations(self,agg):
        self.aggregation = np.append(self.aggregation, agg)

    def add_compositions(self,comp):
        self.composition = np.append(self.composition,comp)

    def to_string(self):
        """
        create a string for displaying the object
        :return: the object as a string
        :rtype: str
        """

        res = self.stereotype+" Class "+self.name+"\n"

        res += "Generalization:\n"
        for g in self.generalization:
            res += "  " + g + "\n"

        res += "Aggregations:\n"
        for a in self.aggregation:
            res += "  " + a + "\n"

        res += "Composition:\n"
        for c in self.composition:
            res += "  " + c + "\n"

        res += "Attributes:\n"
        for a in self.attributes:
            res += "  "+a.to_string()+"\n"

        res += "Operations:\n"
        for o in self.operations:
            res += "  " + o.to_string()+"\n"

        return res

    def __str__(self):
        return self.to_string()

    def to_graphviz_node(self):
        """
        create a str describing a graphviz node for UML representation
        :return: the node in string
        """
        # s = "{"
        s = ""
        s += self.stereotype + " " + self.name
        s += "|"
        for a in self.attributes:
            s += a.to_graphviz() + "\l"
        s += "|"
        for o in self.operations:
            s += o.to_graphviz() + "\l"
        # s += "}"
        # print(s)
        return s


class XRefSect:
    """
    class to describe xrefsect doxygen tags
    """
    def __init__(self, id, title, desc):
        self._id = id
        self._title = title
        self._description = desc

    @property
    def title(self):
        return self._title

    @property
    def description(self):
        return self._description

    def __str__(self):
        return self._title + " " + self._description


if __name__ == "__main__":

    obj = ObjClass("rectangle")

    obj.add_attributes([Attribute("m_width","private","float"),Attribute("m_height","private","float")])
    obj.add_operations([Operation("area", "public", "float", "")])

    print(obj.to_string())
