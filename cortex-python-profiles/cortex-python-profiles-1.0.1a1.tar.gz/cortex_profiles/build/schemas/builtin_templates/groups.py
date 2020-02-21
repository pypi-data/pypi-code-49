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

from cortex_common.types import ProfileFacetSchema
from cortex_common.utils import AttrsAsDict


class ImplicitGroupDescriptions(AttrsAsDict):
    """
    What are the description of the built in groups?
    """
    ATTRIBUTE_TYPE = "What tags capture of the different classifications of the attributes?"
    CLASSIFICATIONS = "What tags help classify attributes?"
    SUBJECTS = "What tags represent the conceptual essences of attributes?"
    INTERACTION = "What tags capture the different interactions attributes can be optionally related to?"
    APP_ASSOCIATED = "What tags capture the different apps attributes can be optionally related to?"
    ALGO_ASSOCIATED = "What tags capture the different algos attributes can be optionally related to?"
    CONCEPT_ASSOCIATED = "What tags capture the different concepts attributes can be optionally related to?"
    USAGE = "What tags capture how an attribute is intended to be used?"


class ImplicitGroups(AttrsAsDict):
    """
    What are the built in groups?
    """
    ATTRIBUTE_TYPE = ProfileFacetSchema(  #type:ignore
        name="attr", label="ATTR-TYPE", description=ImplicitGroupDescriptions.ATTRIBUTE_TYPE)
    CLASSIFICATIONS = ProfileFacetSchema(  #type:ignore
        name="info", label="INFO-TYPE", description=ImplicitGroupDescriptions.CLASSIFICATIONS)
    SUBJECTS = ProfileFacetSchema(  #type:ignore
        name="subject", label="SUBJECTS", description=ImplicitGroupDescriptions.SUBJECTS)
    INTERACTION = ProfileFacetSchema(  #type:ignore
        name="interaction", label="INTERACTIONS", description=ImplicitGroupDescriptions.INTERACTION)
    APP_ASSOCIATED = ProfileFacetSchema(  #type:ignore
        name="app", label="APPS", description=ImplicitGroupDescriptions.APP_ASSOCIATED)
    ALGO_ASSOCIATED = ProfileFacetSchema(  #type:ignore
        name="algo", label="INSIGHTS", description=ImplicitGroupDescriptions.ALGO_ASSOCIATED)
    CONCEPT_ASSOCIATED = ProfileFacetSchema(  #type:ignore
        name="concept", label="CONCEPTS", description=ImplicitGroupDescriptions.CONCEPT_ASSOCIATED)
    USAGE = ProfileFacetSchema(  #type:ignore
        name="usage", label="USAGE", description=ImplicitGroupDescriptions.USAGE)
