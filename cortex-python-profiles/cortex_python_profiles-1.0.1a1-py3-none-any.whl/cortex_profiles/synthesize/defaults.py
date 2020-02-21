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

from cortex_profiles.datamodel.constants import DOMAIN_CONCEPTS

# TODO ... Add this to the configurable universe ...

PROFILE_TYPES = [
    "cortex/end-user-profile",
    "cortex/investor-profile",
    "cortex/medical-client-profile",
    "cortex/shopper-profile"
]

INTERACTION_CONFIG = [
    {
        "interaction": "presented",
        "durationOrientedInteraction": False,
        "initiatedByProfile": False,
        "subsetOf": [],
        "mutuallyExlusiveOf": []
    },
    {
        "interaction": "viewed",
        "durationOrientedInteraction": True,
        "initiatedByProfile": True,
        "subsetOf": [("presented", 10, 25)],
        "mutuallyExlusiveOf": ["ignored"]
    },
    {
        "interaction": "ignored",
        "durationOrientedInteraction": False,
        "initiatedByProfile": True,
        "subsetOf": [("presented", 10, 25)],
        "mutuallyExlusiveOf": ["viewed"]
    },
    {
        "interaction": "liked",
        "durationOrientedInteraction": False,
        "initiatedByProfile": True,
        "subsetOf": [("viewed", 10, 50)],
        "mutuallyExlusiveOf": ["disliked"]
    },
    {
        "interaction": "disliked",
        "durationOrientedInteraction": False,
        "initiatedByProfile": True,
        "subsetOf": [("viewed", 10, 35)],
        "mutuallyExlusiveOf": ["liked"]
    }
]

APPS = [ "FNI", "CTI" ]

INSIGHT_TYPES_PER_APP = {
    "CTI": [
        "RetirementInsights",
        "FundOptimizationInsights"
        "InvestmentInsights",
    ],
    "FNI": [
        "FinancialNewsInsights",
        "CompanyMergerInsights",
        "CLevelChangeInsights",
    ]
}

LIMITS_ON_COUNTS_CONCEPTS_OF_TYPE_PER_CONCEPT_SET = {
    DOMAIN_CONCEPTS.PERSON: {"min": 1, "max": 1},
    DOMAIN_CONCEPTS.COMPANY: {"min": 1, "max": 1},
    DOMAIN_CONCEPTS.COUNTRY: {"min": 1, "max": 1},
    DOMAIN_CONCEPTS.CURRENCY: {"min": 1, "max": 1},
    DOMAIN_CONCEPTS.WEBSITE: {"min": 1, "max": 1},
}