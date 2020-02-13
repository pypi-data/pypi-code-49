# Copyright (C) 2019 Heritage Observatory.  All rights reserved.
#
# This software is the confidential and proprietary information of
# Heritage Observatory or one of its subsidiaries.  You shall not
# disclose this confidential information and shall use it only in
# accordance with the terms of the license agreement or other applicable
# agreement you entered into with Heritage Observatory.
#
# HERITAGE OBSERVATORY MAKES NO REPRESENTATIONS OR WARRANTIES ABOUT THE
# SUITABILITY OF THE SOFTWARE, EITHER EXPRESS OR IMPLIED, INCLUDING BUT
# NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR
# A PARTICULAR PURPOSE, OR NON-INFRINGEMENT.  HERITAGE OBSERVATORY SHALL
# NOT BE LIABLE FOR ANY LOSSES OR DAMAGES SUFFERED BY LICENSEE AS A
# RESULT OF USING, MODIFYING OR DISTRIBUTING THIS SOFTWARE OR ITS
# DERIVATIVES.

from majormode.perseus.model.obj import Object
from majormode.perseus.utils import cast

from heobs.constant.report import HeritageAtRiskActionPriority
from heobs.constant.report import HeritageCondition
from heobs.constant.report import HeritageDesignation
from heobs.constant.report import HeritageGrade
from heobs.constant.report import HeritageOccupancy
from heobs.constant.report import HeritageOwnerType


class HeritageAtRiskReport(Object):
    def __init__(
            self,
            action_priority=None,
            condition=None,
            designation=None,
            grade=None,
            occupancy=None,
            owner_type=None):
        super().__init__()
        self.action_priority = action_priority
        self.designation = designation
        self.condition = condition
        self.grade = grade
        self.occupancy = occupancy
        self.owner_type = owner_type

    @staticmethod
    def from_json(payload):
        return payload and HeritageAtRiskReport(
            action_priority=cast.string_to_enum(payload.get('action_priority'), HeritageAtRiskActionPriority),
            condition=cast.string_to_enum(payload.get('condition'), HeritageCondition),
            designation=cast.string_to_enum(payload.get('designation'), HeritageDesignation),
            grade=cast.string_to_enum(payload.get('grade'), HeritageGrade),
            occupancy=cast.string_to_enum(payload.get('occupancy'), HeritageOccupancy),
            owner_type=cast.string_to_enum(payload.get('owner_type'), HeritageOwnerType)
        )
