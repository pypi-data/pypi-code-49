# Copyright (C) 2009-2020 Martin Slouf <martinslouf@users.sourceforge.net>
#
# This file is a part of Summer.
#
# Summer is free software; you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation; either version 3 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA

import typing
import ldap3
import summer

from .model import Category, Item, DeclarativeFooEntity, User


#
# category #
#


class CategoryDao(summer.CodeEntityDao):
    def __init__(self, session_factory: summer.SessionFactory):
        super().__init__(session_factory, Category)

    def sample_method1(self) -> typing.List[Category]:
        return [i for i in self.query.all()]

    def sample_method2(self) -> typing.List[Category]:
        return [i for i in self.query.all()]


class CategoryManager(object):
    def __init__(self, category_dao: CategoryDao):
        self.category_dao = category_dao

    @summer.transactional
    def find(self, category_filter: summer.Filter) -> typing.List[Category]:
        return self.category_dao.find(category_filter)

    @summer.transactional
    def save(self, category: Category) -> Category:
        return self.category_dao.save(category)

    @summer.transactional
    def sample_method3(self) -> typing.List[Category]:
        return self.category_dao.sample_method1() + self.category_dao.sample_method2()


#
# item #
#


class ItemDao(summer.CodeEntityDao):
    def __init__(self, session_factory: summer.SessionFactory):
        super().__init__(session_factory, Item)

    def sample_method1(self) -> typing.List[Item]:
        return [i for i in self.query.all()]

    def sample_method2(self) -> typing.List[Item]:
        return [i for i in self.query.all()]


class ItemManager(object):
    def __init__(self, item_dao: ItemDao):
        self.item_dao = item_dao

    @summer.transactional
    def sample_method3(self) -> typing.List[Item]:
        return self.item_dao.sample_method1() + self.item_dao.sample_method2()


#
# DeclarativeFooEntity #
#

class DeclarativeFooEntityDao(summer.EntityDao):
    def __init__(self, session_factory: summer.SessionFactory):
        super().__init__(session_factory, DeclarativeFooEntity)


class DeclarativeFooEntityManager(object):

    def __init__(self, declarative_foo_entity_dao: DeclarativeFooEntityDao):
        self.dao = declarative_foo_entity_dao

    @summer.transactional
    def find(self) -> typing.List[DeclarativeFooEntity]:
        return self.dao.find(summer.Filter())

    @summer.transactional
    def save(self, foo: DeclarativeFooEntity) -> DeclarativeFooEntity:
        return self.dao.save(foo)


#
# user #
#


class UserDao(summer.LdapEntityDao):
    def __init__(self, ldap_session_factory: summer.LdapSessionFactory):
        summer.LdapEntityDao.__init__(self, ldap_session_factory, User)

    def find(self) -> typing.List[User]:
        """Gets all users."""
        session = self.session
        base = "ou=users,%s" % (self.base,)
        result = session.search(search_base=base,
                                search_filter="(cn=*)",
                                search_scope=ldap3.SUBTREE,
                                attributes=["cn", "userPassword"])
        users: typing.List[User] = []
        if result:
            for entry in session.response:
                attrs = entry["attributes"]
                login = attrs["cn"][0]
                crypt = attrs["userPassword"][0]
                user = User(login, crypt)
                users.append(user)
        return users


class UserManager(object):
    def __init__(self, user_dao: UserDao):
        self.user_dao = user_dao

    @summer.ldapaop
    def find(self) -> list:
        return self.user_dao.find()
