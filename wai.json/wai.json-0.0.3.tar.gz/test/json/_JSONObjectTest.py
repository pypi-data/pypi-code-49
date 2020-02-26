from wai.test import AbstractTest
from wai.test.decorators import RegressionTest, Test, ExceptionTest

from json import loads

from wai.json.object import JSONObject
from wai.json.object.property import *


class JSONObjectTest(AbstractTest):
    """
    Unit tests for JSON objects.
    """
    @classmethod
    def subject_type(cls):
        # Default test subject is a plain object
        return JSONObject

    @Test
    def properties(self, subject: JSONObject):
        """
        Test creating a new sub-class of JSONObject.
        """
        class TestObject(JSONObject):
            a = NumberProperty()
            b = StringProperty()
            c = BoolProperty()
            d = EnumProperty(values=(1, 2, "three", "blue"))
            e = ConstantProperty(value="test")
            f = ArrayProperty(element_property=NumberProperty())
            g = MapProperty(value_property=StringProperty())
            h = JSONObjectProperty(object_type=JSONObject)
            i = AnyOfProperty(sub_properties=(NumberProperty(), StringProperty()))
            j = AllOfProperty(sub_properties=(NumberProperty(multiple_of=3), NumberProperty(multiple_of=5)))
            k = OneOfProperty(sub_properties=(NumberProperty(multiple_of=3), NumberProperty(multiple_of=5)))

    @Test
    def set_additional_property(self, subject: JSONObject):
        subject.set_property("test", 13)

        self.assertDictEqual(subject.to_raw_json(), {"test": 13})
