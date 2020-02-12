from django import forms
from django.forms import formset_factory
from django.utils.safestring import mark_safe

from flex_forms.components import BaseButton, FlexButton
from flex_forms.components import StaticFlexField
from flex_forms.forms import FlexForm, StaticFieldset, FlexFormset


class TestFlexFormInheritance(FlexForm):
    """
    Form for testing static fields inheritance.
    """

    field_15 = StaticFlexField(data='Success', label='The static field is inherited')


class FlexFormTest(TestFlexFormInheritance):
    """
    Test of flex forms.
    """

    css_classes = ['flex-form']
    grid = {
        'User Info': ['field_1', 'field_2'],
        '_1': ['field_3', ['field_4', 'field_5'], 'field_6'],
        '_2': ['field_7', 'field_8'],
        '_3': ['field_9', 'field_10', ['field_14', 'field_15']],
        '_4': ['field_11'],
        '_5': ['field_12'],
        '_6': ['button'],
    }

    field_1 = forms.CharField(
        label='Username',
        help_text='Help text example',
        widget=forms.TextInput(
            attrs={
                'field_group_class': 'icon-right',
                'icon': mark_safe('<i class="material-icons">landscape</i>'),
                'placeholder': 'Field with icon',
                'readonly': True
            }
        )
    )
    field_2 = forms.CharField(label='Password')
    field_3 = forms.CharField(label='Country')
    field_4 = forms.CharField(label='City', required=False)
    field_5 = forms.CharField(label='Phone')
    field_6 = forms.CharField(label='Your kitty name', help_text='For example: Maksik')
    field_7 = forms.CharField(label='About you', help_text='Tell us something about yourself', widget=forms.Textarea())
    field_8 = forms.CharField(label='Address')
    field_9 = forms.BooleanField(label='Like dogs?', widget=forms.CheckboxInput())
    field_10 = forms.BooleanField(
        label='Programmer?',
        widget=forms.RadioSelect(
            choices=(('0', 'No'), ('1', 'Yes')),
            attrs={
                'field_group_class': 'radio-as-button radio-as-row',
            }
        )
    )
    field_11 = forms.CharField(
        label='Scientist?',
        widget=forms.Select(
            choices=(('0', 'Yes'), ('1', 'No')),
        )
    )
    field_12 = forms.MultipleChoiceField(
        label='Fruits?',
        choices=(('0', 'Apple'), ('1', 'Mango')),
        widget=forms.CheckboxSelectMultiple(attrs={
            'field_group_class': 'checkbox-as-button checkbox-as-row',
        })
    )
    field_13 = StaticFlexField(
        data='Example', label='Example', help_text='Example',
        field_group_class='icon-right', icon=mark_safe('<i class="material-icons">landscape</i>')
    )
    field_14 = StaticFlexField(data='Example', label='Example')

    button = FlexButton(button=BaseButton('Submit'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['field_1'].disabled = True


class StaticFlexFormTest(StaticFieldset):
    """
    Test of static flex forms.
    """

    css_classes = ['flex-form']
    grid = {
        'User Info': ['field_1', 'field_2']
    }

    field_1 = StaticFlexField(data='Example 1', label='Example 1')
    field_2 = StaticFlexField(data='Example 2', label='Example 2')


class FlexFormSetTest(FlexFormset):
    """
    Test of flex formsets.
    """

    css_classes = ['flex-form']


simple_formset = formset_factory(FlexFormTest, FlexFormSetTest, extra=4)
