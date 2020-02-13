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

from majormode.perseus.model.enum import Enum

# Occupancy of an heritage (excluding places of worship).
HeritageOccupancy = Enum(
    'vacant',
    'part_occupied',
    'occupied',
    'unknown',
    'n_a'
)

HeritageOwnerType = Enum(
    'local_authority',
    'private',
    'religious_organization',
    'multiple_owners'
)

# Priority for action is assessed on a scale of `A` to `F`, where `A` is
# the highest priority for a site which is deteriorating rapidly with no
# solution to secure its future, and `F` is the lowest priority.
#
# For buildings and structures and places of worship the following
# priority categories are used as an indication of trend and as a means
# of prioritising action:
HeritageAtRiskActionPriority = Enum(
    # Immediate risk of further rapid deterioration or loss of fabric; no
    # solution agreed.
    'A',

    # Immediate risk of further rapid deterioration or loss of fabric;
    # solution agreed but not yet implemented.
    'B',

    # Slow decay; no solution agreed.
    'C',

    # Slow decay; solution agreed but not yet implemented.
    'D',

    # Under repair or in fair to good repair, but no user identified; or
    # under threat of vacancy with no obvious new user (applicable only to
    # buildings capable of beneficial use).
    'E',

    # Repair scheme in progress and (where applicable) end use or user
    # identified; functionally redundant buildings with new use agreed but
    # not yet implemented.
    'F'
)

# Condition for buildings, including places of worship.
#
# For sites that cover areas (scheduled monuments (archaeology
# assessments) and parks and gardens) one overall condition category is
# recorded. The category may relate only to the part of the site or
# monument that is at risk and not the whole site.
#
# If a site has suffered from heritage crime it is noted in the summary.
# Heritage crime is defined as any offence which harms the heritage
# asset or its setting and includes arson, graffiti, lead theft and
# vandalism.
HeritageCondition = Enum(
    # Extensive significant problems.
    #
    # A building where there has been structural failure or where there are
    # clear signs of structural instability; where applicable, if there has
    # been loss of significant areas of roof covering, leading to major
    # deterioration of the interior; or where there has been a major fire or
    # other disaster affecting most of the building. The classification will
    # include derelict buildings and would include buildings which are
    # incomplete.
    'bad',

    # Generally unsatisfactory with major localised problems.
    #
    # A building or structure where there has been general deterioration of
    # the building fabric. There will obviously be faults likely to lead to
    # structural failure, such as an area of missing tiles though the roof
    # structure appears to be sound, and/or deterioration masonry or timber
    # frame, and/or defective rainwater goods. A building with numerous
    # failings would fall into this class. This classification could include
    # a building where there has been a fire or other disaster.
    'poor',

    # Generally satisfactory but with significant localised problems.
    #
    # A building which is structurally sound but in need of minor repair, or
    # showing lack of general maintenance e.g. decayed window frames or
    # gutters blocked or signs of water ingress.
    'fair',

    # Generally satisfactory but with minor.
    #
    # Structurally sound, water-tight with no significant repairs needed.
    'good'
)

# Principal designation of an heritage.
HeritageDesignation = Enum(
    # Listed Building and Structure (LB): When a building is recognised as
    # being of special architectural or historic interest it is added to the
    # statutory list. Structures that might not be classified as
    # 'buildings' ­ such as railings, gate piers, walls, war memorials,
    # gravestones, post boxes and telephone boxes ­ can all be Listed
    # Buildings.
    'LB',

    # Listed Place of Worship (LPW).
    'LPW',

    # Scheduled Monument (SM), Archaeological Site or Historic Building:
    # Historic buildings and archaeological sites of national importance are
    # given legal protection by being placed on a 'Schedule' of monuments.
    # Examples of Scheduled Monuments are Roman remains, burial mounds,
    # castles, bridges, earthworks, the remains of deserted villages, and
    # industrial sites. Scheduled Monuments can not include ecclesiastical
    # or residential buildings (except for associated caretaker’s dwellings),
    # and unlike Listed Buildings they are not assigned grades.
    'SM',

    # Registered Park and Garden (RPG): Planned open spaces, including
    # public parks, cemeteries, the grounds of private houses, and town
    # squares.
    'RGP',

    # Registered Battlefield (RB).
    'RB',

    # Protected Wreck Site (PWS).
    'PWS',

    # Conservation Area (CA).
    'CA'
)

# Buildings are given one of three grades which denote their level of
# importance, Grade I being the highest and Grade II the lowest.
HeritageGrade = Enum(
    # Grade I: Buildings of exceptional interest.
    'I',

    # Grade II*: Particularly important buildings of more than special
    # interest.
    'II*',

    # Grade II: buildings that are of special interest, warranting every
    # effort to preserve them
    'II'
)


HeritageAtRiskReportStatus = Enum(
    'draft',
    'deleted',
    'disabled',
    'enabled',
    'pending',
)
