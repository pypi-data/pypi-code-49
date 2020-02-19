# -*- coding: utf-8 -*-

# Author: Petr Dlouhý <petr.dlouhy@auto-mat.cz>
#
# Copyright (C) 2017 o.s. Auto*Mat
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

from django.test import TestCase
from flexible_filter_conditions.test_utils.test_app.models import TestModel

from model_mommy import mommy


class TestStr(TestCase):
    """ Test NamedCondition.__str__() """
    def test_str(self):
        t = mommy.make(
            "flexible_filter_conditions.NamedCondition",
            name="Foo condition",
        )
        self.assertEqual(str(t), "Foo condition")


class TestConditionString(TestCase):
    """ Test Condition.condition_string() """

    def test_and(self):
        """ Test if and operation works """
        t = mommy.make(
            "flexible_filter_conditions.Condition",
            named_condition__name="Foo condition",
            operation="and",
        )
        self.assertEqual(t.condition_string(), "()")

    def test_nor(self):
        """ Test if nor operation works """
        t = mommy.make(
            "flexible_filter_conditions.Condition",
            named_condition__name="Foo condition",
            operation="or",
            negate=True,
        )
        self.assertEqual(t.condition_string(), "not(())")

    def test_more_operands(self):
        """ Testing more operands """
        t = mommy.make(
            "flexible_filter_conditions.Condition",
            named_condition__name="Foo condition",
            operation="or",
            negate=True,
        )
        mommy.make("flexible_filter_conditions.Condition", operation="and", conds=t)
        mommy.make("flexible_filter_conditions.Condition", operation="or", negate=True, conds=t)
        self.assertEqual(t.condition_string(), "not((() or not(())))")


class TestFiltering(TestCase):
    def test_user_condition_filter_or(self):
        mommy.make("TestModel", test_field="Foo value")
        mommy.make("TestModel", test_field="Bar value")
        self.named_condition = mommy.make(
            "NamedCondition",
            name="Foo condition",
        )
        self.condition = mommy.make(
            "Condition",
            named_condition=self.named_condition,
            operation="or",
        )
        mommy.make(
            'TerminalCondition',
            variable="TestModel.test_field",
            value="Bar value",
            operation="=",
            condition=self.condition,
        )
        mommy.make(
            'TerminalCondition',
            variable="TestModel.test_field",
            value="Foo value",
            operation="=",
            condition=self.condition,
        )

        q = self.named_condition.filter_queryset(TestModel.objects.all(), 'foo-action')
        self.assertEqual(q.count(), 2)

    def test_user_condition_filter_and(self):
        mommy.make("TestModel", test_field="Foo value")
        mommy.make("TestModel", test_field="Bar value")
        self.named_condition = mommy.make(
            "NamedCondition",
            name="Foo condition",
        )
        self.condition = mommy.make(
            "Condition",
            named_condition=self.named_condition,
            operation="and",
        )
        mommy.make(
            'TerminalCondition',
            variable="TestModel.test_field",
            value="value",
            operation="contains",
            condition=self.condition,
        )
        mommy.make(
            'TerminalCondition',
            variable="TestModel.test_field",
            value="Bar",
            operation="contains",
            condition=self.condition,
        )

        q = self.named_condition.filter_queryset(TestModel.objects.all(), 'foo-action')
        self.assertEqual(q.count(), 1)
        self.assertEqual(q.first().test_field, "Bar value")

    def test_user_condition_filter_xor(self):
        mommy.make("TestModel", test_field="Foo value")
        mommy.make("TestModel", test_field="Bar value")
        mommy.make("TestModel", test_field="Bar balue")
        self.named_condition = mommy.make(
            "NamedCondition",
            name="Foo condition",
        )
        self.condition = mommy.make(
            "Condition",
            named_condition=self.named_condition,
            operation="xor",
        )
        mommy.make(
            'TerminalCondition',
            variable="TestModel.test_field",
            value="value",
            operation="contains",
            condition=self.condition,
        )
        mommy.make(
            'TerminalCondition',
            variable="TestModel.test_field",
            value="Bar",
            operation="contains",
            condition=self.condition,
        )

        q = self.named_condition.filter_queryset(TestModel.objects.all(), 'foo-action')
        self.assertEqual(q.count(), 2)
        self.assertSetEqual(set(q.values_list('test_field', flat=True)), {"Foo value", "Bar balue"})

    def test_user_condition_filter_action(self):
        mommy.make("TestModel", test_field="Foo value")
        mommy.make("TestModel", test_field="Bar value")
        self.named_condition = mommy.make(
            "NamedCondition",
            name="Foo condition",
        )
        self.condition = mommy.make(
            "Condition",
            named_condition=self.named_condition,
            operation="and",
        )
        mommy.make(
            'TerminalCondition',
            variable="TestModel.test_field",
            value="Bar value",
            operation="=",
            condition=self.condition,
        )
        mommy.make(
            'TerminalCondition',
            variable="action",
            value="foo-action",
            operation="=",
            condition=self.condition,
        )

        q = self.named_condition.filter_queryset(TestModel.objects.all(), 'foo-action')
        self.assertEqual(q.count(), 1)

        q = self.named_condition.filter_queryset(TestModel.objects.all(), 'bar-action')
        self.assertEqual(q.count(), 0)

    def test_user_condition_filter_conds_of_conds(self):
        mommy.make("TestModel", test_field="Foo value")
        mommy.make("TestModel", test_field="Bar value")
        mommy.make("TestModel", test_field="Baz value")
        mommy.make("TestModel", test_field="Baz balue")
        self.named_condition = mommy.make(
            "NamedCondition",
            name="Foo condition",
        )
        self.condition = mommy.make(
            "Condition",
            named_condition=self.named_condition,
            operation="and",
        )
        mommy.make(
            'TerminalCondition',
            variable="TestModel.test_field",
            value="value",
            operation="contains",
            condition=self.condition,
        )
        self.condition1 = mommy.make(
            'Condition',
            operation="or",
            conds=self.condition,
        )
        mommy.make(
            'TerminalCondition',
            variable="TestModel.test_field",
            value="Bar",
            operation="contains",
            condition=self.condition1,
        )
        mommy.make(
            'TerminalCondition',
            variable="TestModel.test_field",
            value="Baz",
            operation="contains",
            condition=self.condition1,
        )

        q = self.named_condition.filter_queryset(TestModel.objects.all(), 'foo-action')
        self.assertEqual(q.count(), 2)
        self.assertSetEqual(set(q.values_list('test_field', flat=True)), {"Baz value", "Bar value"})

    def test_user_condition_filter_conds_of_conds_double(self):
        mommy.make("TestModel", test_field="Foo value")
        mommy.make("TestModel", test_field="Bar value")
        mommy.make("TestModel", test_field="Baz value")
        mommy.make("TestModel", test_field="Baz balue")
        self.named_condition = mommy.make(
            "NamedCondition",
            name="Foo condition",
        )
        self.condition = mommy.make(
            "Condition",
            named_condition=self.named_condition,
            operation="and",
        )
        mommy.make(
            'TerminalCondition',
            variable="TestModel.test_field",
            value="value",
            operation="contains",
            condition=self.condition,
        )
        self.condition1 = mommy.make(
            'Condition',
            operation="or",
            conds=self.condition,
        )
        self.condition2 = mommy.make(
            'Condition',
            operation="and",
            conds=self.condition,
        )
        mommy.make(
            'TerminalCondition',
            variable="TestModel.test_field",
            value="Bar",
            operation="contains",
            condition=self.condition1,
        )
        mommy.make(
            'TerminalCondition',
            variable="TestModel.test_field",
            value="Baz",
            operation="contains",
            condition=self.condition1,
        )
        mommy.make(
            'TerminalCondition',
            variable="TestModel.test_field",
            value="va",
            operation="contains",
            condition=self.condition2,
        )
        mommy.make(
            'TerminalCondition',
            variable="TestModel.test_field",
            value="lue",
            operation="contains",
            condition=self.condition2,
        )

        q = self.named_condition.filter_queryset(TestModel.objects.all(), 'foo-action')
        self.assertEqual(q.count(), 2)
        self.assertSetEqual(set(q.values_list('test_field', flat=True)), {"Baz value", "Bar value"})
