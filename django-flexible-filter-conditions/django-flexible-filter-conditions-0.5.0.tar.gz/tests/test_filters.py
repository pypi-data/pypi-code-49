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

from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase

from flexible_filter_conditions.admin_filters import UserConditionFilter
from flexible_filter_conditions.test_utils.test_app.models import TestModel

from model_mommy import mommy


class FilterTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.request = self.factory.get("")


class FixtureFilterTests(FilterTestCase):
    def setUp(self):
        mommy.make("TestModel", test_field="Foo value")
        mommy.make("TestModel", test_field="Bar value")
        self.condition = mommy.make(
            "flexible_filter_conditions.Condition",
            named_condition__name="Foo condition",
            operation="and",
        )
        mommy.make(
            'TerminalCondition',
            variable="TestModel.test_field",
            value="Foo value",
            operation="=",
            condition=self.condition,
        )
        super().setUp()

    def test_user_condition_filter(self):
        f = UserConditionFilter(self.request, {"user_condition": self.condition.named_condition.pk}, TestModel, None)
        q = f.queryset(self.request, TestModel.objects.all())
        self.assertEqual(q.count(), 1)

    def test_user_condition_filter_without_query(self):
        f = UserConditionFilter(self.request, {}, TestModel, None)
        q = f.queryset(self.request, TestModel.objects.all())
        self.assertEqual(q.count(), 2)
