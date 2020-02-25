from django.test import SimpleTestCase

from django import forms

from .templatetags import toolkit
from .apps import ToolkitConfig


# Object that will have to fake being a Model
class TestObject:

    class Meta:
        test = 'a'

    def __init__(self):
        self._meta = self.Meta

    def get_absolute_url(self, pk=None):
        return '/test/' + str(pk)


class ToolkitTestCase(SimpleTestCase):

    def test_apps(self):
        # Fairly pointless test, but needed for 100% coverage
        self.assertEqual(ToolkitConfig.name, 'toolkit')

    def test_spacer(self):
        self.assertEqual(toolkit.spacer('X'), ' X')
        self.assertEqual(toolkit.spacer(''), '')
        self.assertEqual(toolkit.spacer(None), '')
        self.assertEqual(toolkit.spacer(False), '')
        self.assertEqual(toolkit.spacer(True), ' True')

    def test_field_css(self):
        # CharField
        form = forms.Form()
        raw_field = forms.CharField(label='test')
        field = forms.BoundField(form, raw_field, 'test_field')
        self.assertEqual(toolkit.field_css(field, 'test-css'),
                         '<input type="text" name="test_field" class="test-css" placeholder="test" required id="id_test_field">')
        # CharField with TextArea widget
        raw_field = forms.CharField(label='test', widget=forms.Textarea)
        field = forms.BoundField(form, raw_field, 'test_field')
        self.assertEqual(toolkit.field_css(field, 'test-css'),
                         '<textarea name="test_field" cols="40" rows="10" class="test-css" required id="id_test_field">\n</textarea>')
        # ChoiceField with Select widget
        raw_field = forms.ChoiceField(label='test', choices=((0, 'A'), (1, 'B'), (2, 'C')))
        field = forms.BoundField(form, raw_field, 'test_field')
        self.assertEqual(toolkit.field_css(field, 'test-css'),
                         '<select name="test_field" class="test-css" id="id_test_field">\n  <option value="0">A</option>\n\n  <option value="1">B</option>\n\n  <option value="2">C</option>\n\n</select>')
        # EmailField
        raw_field = forms.EmailField(label='test')
        field = forms.BoundField(form, raw_field, 'test_field')
        self.assertEqual(toolkit.field_css(field, 'test-css'),
                         '<input type="email" name="test_field" class="test-css" placeholder="test" required id="id_test_field">')
        # BooleanField with CheckboxInput widget
        raw_field = forms.BooleanField(label='test')
        field = forms.BoundField(form, raw_field, 'test_field')
        self.assertEqual(toolkit.field_css(field, 'test-css'),
                         '<input type="checkbox" name="test_field" class="test-css" required id="id_test_field">')

    def test_is_field(self):
        # CharField
        form = forms.Form()
        raw_field = forms.CharField(label='test')
        field = forms.BoundField(form, raw_field, 'test_field')
        self.assertEqual(toolkit.is_field(field, None), 'charfield')
        self.assertTrue(toolkit.is_field(field, 'charfield'))
        # CharField with TextArea widget (...which of course doesn't change the result here)
        raw_field = forms.CharField(label='test', widget=forms.Textarea)
        field = forms.BoundField(form, raw_field, 'test_field')
        self.assertEqual(toolkit.is_field(field, None), 'charfield')
        self.assertTrue(toolkit.is_field(field, 'charfield'))
        # ChoiceField with Select widget
        raw_field = forms.ChoiceField(label='test', choices=((0, 'A'), (1, 'B'), (2, 'C')))
        field = forms.BoundField(form, raw_field, 'test_field')
        self.assertEqual(toolkit.is_field(field, None), 'choicefield')
        self.assertTrue(toolkit.is_field(field, 'choicefield'))
        # EmailField
        raw_field = forms.EmailField(label='test')
        field = forms.BoundField(form, raw_field, 'test_field')
        self.assertEqual(toolkit.is_field(field, None), 'emailfield')
        self.assertTrue(toolkit.is_field(field, 'emailfield'))
        # BooleanField with CheckboxInput widget
        raw_field = forms.BooleanField(label='test')
        field = forms.BoundField(form, raw_field, 'test_field')
        self.assertEqual(toolkit.is_field(field, None), 'booleanfield')
        self.assertTrue(toolkit.is_field(field, 'booleanfield'))

    def test_is_widget(self):
        # CharField
        form = forms.Form()
        raw_field = forms.CharField(label='test')
        field = forms.BoundField(form, raw_field, 'test_field')
        self.assertEqual(toolkit.is_widget(field, None), 'textinput')
        self.assertTrue(toolkit.is_widget(field, 'textinput'))
        # CharField with TextArea widget
        raw_field = forms.CharField(label='test', widget=forms.Textarea)
        field = forms.BoundField(form, raw_field, 'test_field')
        self.assertEqual(toolkit.is_widget(field, None), 'textarea')
        self.assertTrue(toolkit.is_widget(field, 'textarea'))
        # ChoiceField with Select widget
        raw_field = forms.ChoiceField(label='test', choices=((0, 'A'), (1, 'B'), (2, 'C')))
        field = forms.BoundField(form, raw_field, 'test_field')
        self.assertEqual(toolkit.is_widget(field, None), 'select')
        self.assertTrue(toolkit.is_widget(field, 'select'))
        # EmailField
        raw_field = forms.EmailField(label='test')
        field = forms.BoundField(form, raw_field, 'test_field')
        self.assertEqual(toolkit.is_widget(field, None), 'emailinput')
        self.assertTrue(toolkit.is_widget(field, 'emailinput'))
        # BooleanField with CheckboxInput widget
        raw_field = forms.BooleanField(label='test')
        field = forms.BoundField(form, raw_field, 'test_field')
        self.assertEqual(toolkit.is_widget(field, None), 'checkboxinput')
        self.assertTrue(toolkit.is_widget(field, 'checkboxinput'))

    def test_subset(self):
        test = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
        self.assertEqual(toolkit.subset(test, 'a'), [1])
        self.assertEqual(toolkit.subset(test, 'b,c'), [2, 3])
        # Key not in dict
        with self.assertRaises(KeyError):
            toolkit.subset(test, 'f')
        # Empty key
        with self.assertRaises(KeyError):
            toolkit.subset(test, 'a,,b')
        # No extra whitespace allowed
        with self.assertRaises(KeyError):
            toolkit.subset(test, ' a ')

    def test_csvlist(self):
        test = 'a,b,c,d,e'
        self.assertEqual(toolkit.csvlist(test, 0), 'a')
        self.assertEqual(toolkit.csvlist(test, 2), 'c')
        self.assertEqual(toolkit.csvlist(test, 4), 'e')
        # Extra whitespace
        test = 'a , b , c , d , e '
        self.assertEqual(toolkit.csvlist(test, 2), ' c ')
        # Index out of range
        with self.assertRaises(IndexError):
            toolkit.csvlist(test, 5)
        # Not comma-separated string
        test = 'a;b;c;d;e'
        with self.assertRaises(IndexError):
            toolkit.csvlist(test, 1)

    def test_get_absolute_url(self):
        model = TestObject()
        self.assertEqual(toolkit.get_absolute_url(model, 1), '/test/1')

    def test_call_method(self):
        model = TestObject()
        self.assertEqual(toolkit.call_method(model, 'get_absolute_url', pk=2), '/test/2')

    def test_meta(self):
        model = TestObject()
        self.assertEqual(toolkit.meta(model, 'test'), 'a')

    def test_concat(self):
        self.assertEqual(toolkit.concat('a', 'b'), 'ab')
        # 1 + 1 = 11 (this is where "add" filter would return 2)
        self.assertEqual(toolkit.concat(1, 1), '11')
