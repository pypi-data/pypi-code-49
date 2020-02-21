"""
Copyright 2019 Cognitive Scale, Inc. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import attr
import pydash


__all__ = [
    "OptionalDescriber",
    "Subject",
    "Verb",
]

@attr.s(frozen=True)
class OptionalDescriber(object):
    """
    A representation of an adjective/adverb.
    """
    id = attr.ib(type=str)
    adjective = attr.ib(type=str)
    adverb = attr.ib(type=str)
    include = attr.ib(type=bool)
    optionalAdjective = attr.ib(type=str)
    optionalAdverb = attr.ib(type=str)

    @optionalAdjective.default
    def defaultOptionalAdjective(self):
        if self.include:
            return self.adjective
        return ""

    @optionalAdverb.default
    def defaultOptionalAdverb(self):
        if self.include:
            return self.adverb
        return ""


@attr.s(frozen=True)
class Subject(object):
    """
    A representation of a subject in different tenses.
    TODO: See if the operations here can be done in an NLP based library.
    """
    id = attr.ib(type=str)
    singular = attr.ib(type=str)
    Singular = attr.ib(type=str)
    plural = attr.ib(type=str)
    Plural = attr.ib(type=str)
    acronym = attr.ib(type=str, default="")

    @singular.default
    def defaultsingular(self):
        return f"{pydash.lower_case(self.id.split('/')[-1])}"

    @Singular.default
    def defaultSingular(self):
        return pydash.title_case(self.singular or self.defaultsingular())

    @plural.default
    def defaultplural(self):
        return f"{self.singular or self.defaultsingular()}s"

    @Plural.default
    def defaultPlural(self):
        return pydash.title_case(self.plural or self.defaultplural())


@attr.s(frozen=True)
class Verb(object):
    """
    A representation of a verb in different tenses.
    TODO: See if the operations here can be done in an NLP based library.
    """
    id = attr.ib(type=str)
    verb = attr.ib(type=str)
    past = attr.ib(type=str, default="")
    verbInitiatedBySubject = attr.ib(type=bool, default=True)
    Verb = attr.ib(type=str)
    verbStatement = attr.ib(type=str)
    Past = attr.ib(type=str)

    @Verb.default
    def defaultVerb(self):
        return pydash.title_case(self.verb)

    @Past.default
    def defaultPast(self):
        return pydash.title_case(self.past)

    @verbStatement.default
    def defaultVerbStatement(self):
        return "{} to".format(self.verb) if not self.verbInitiatedBySubject else "{} by".format(self.verb)
