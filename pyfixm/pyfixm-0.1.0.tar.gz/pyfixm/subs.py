#!/usr/bin/env python

#
# Generated Sun Feb  9 08:33:58 2020 by generateDS.py version 2.35.12.
# Python 3.8.1 (default, Dec 30 2019, 15:43:37)  [GCC 9.2.0]
#
# Command line options:
#   ('-o', '/pyfixm/__init__.py')
#   ('-s', '/pyfixm/subs.py')
#
# Command line arguments:
#   /xsd/base_schema.xsd
#
# Command line:
#   /usr/bin/generateDS -o "/pyfixm/__init__.py" -s "/pyfixm/subs.py" /xsd/base_schema.xsd
#
# Current working directory (os.getcwd()):
#   pyfixm
#

import os
import sys
from lxml import etree as etree_

import ??? as supermod

def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        parser = etree_.ETCompatXMLParser()
    try:
        if isinstance(infile, os.PathLike):
            infile = os.path.join(infile)
    except AttributeError:
        pass
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

def parsexmlstring_(instring, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    element = etree_.fromstring(instring, parser=parser, **kwargs)
    return element

#
# Globals
#

ExternalEncoding = ''
SaveElementTreeNode = True

#
# Data representation classes
#


class AerodromeReferenceTypeSub(supermod.AerodromeReferenceType):
    def __init__(self, extensiontype_=None, **kwargs_):
        super(AerodromeReferenceTypeSub, self).__init__(extensiontype_,  **kwargs_)
supermod.AerodromeReferenceType.subclass = AerodromeReferenceTypeSub
# end class AerodromeReferenceTypeSub


class IcaoAerodromeReferenceTypeSub(supermod.IcaoAerodromeReferenceType):
    def __init__(self, code=None, **kwargs_):
        super(IcaoAerodromeReferenceTypeSub, self).__init__(code,  **kwargs_)
supermod.IcaoAerodromeReferenceType.subclass = IcaoAerodromeReferenceTypeSub
# end class IcaoAerodromeReferenceTypeSub


class RunwayPositionAndTimeTypeSub(supermod.RunwayPositionAndTimeType):
    def __init__(self, runwayName=None, runwayTime=None, **kwargs_):
        super(RunwayPositionAndTimeTypeSub, self).__init__(runwayName, runwayTime,  **kwargs_)
supermod.RunwayPositionAndTimeType.subclass = RunwayPositionAndTimeTypeSub
# end class RunwayPositionAndTimeTypeSub


class StandPositionAndTimeTypeSub(supermod.StandPositionAndTimeType):
    def __init__(self, standName=None, terminalName=None, standTime=None, **kwargs_):
        super(StandPositionAndTimeTypeSub, self).__init__(standName, terminalName, standTime,  **kwargs_)
supermod.StandPositionAndTimeType.subclass = StandPositionAndTimeTypeSub
# end class StandPositionAndTimeTypeSub


class UnlistedAerodromeReferenceTypeSub(supermod.UnlistedAerodromeReferenceType):
    def __init__(self, name=None, point=None, **kwargs_):
        super(UnlistedAerodromeReferenceTypeSub, self).__init__(name, point,  **kwargs_)
supermod.UnlistedAerodromeReferenceType.subclass = UnlistedAerodromeReferenceTypeSub
# end class UnlistedAerodromeReferenceTypeSub


class SignificantPointTypeSub(supermod.SignificantPointType):
    def __init__(self, extensiontype_=None, **kwargs_):
        super(SignificantPointTypeSub, self).__init__(extensiontype_,  **kwargs_)
supermod.SignificantPointType.subclass = SignificantPointTypeSub
# end class SignificantPointTypeSub


class ContactInformationTypeSub(supermod.ContactInformationType):
    def __init__(self, name=None, title=None, address=None, onlineContact=None, phoneFax=None, extensiontype_=None, **kwargs_):
        super(ContactInformationTypeSub, self).__init__(name, title, address, onlineContact, phoneFax, extensiontype_,  **kwargs_)
supermod.ContactInformationType.subclass = ContactInformationTypeSub
# end class ContactInformationTypeSub


class OnlineContactTypeSub(supermod.OnlineContactType):
    def __init__(self, email=None, **kwargs_):
        super(OnlineContactTypeSub, self).__init__(email,  **kwargs_)
supermod.OnlineContactType.subclass = OnlineContactTypeSub
# end class OnlineContactTypeSub


class PostalAddressTypeSub(supermod.PostalAddressType):
    def __init__(self, administrativeArea=None, city=None, countryCode=None, countryName=None, deliveryPoint=None, postalCode=None, **kwargs_):
        super(PostalAddressTypeSub, self).__init__(administrativeArea, city, countryCode, countryName, deliveryPoint, postalCode,  **kwargs_)
supermod.PostalAddressType.subclass = PostalAddressTypeSub
# end class PostalAddressTypeSub


class TelephoneContactTypeSub(supermod.TelephoneContactType):
    def __init__(self, facimile=None, voice=None, **kwargs_):
        super(TelephoneContactTypeSub, self).__init__(facimile, voice,  **kwargs_)
supermod.TelephoneContactType.subclass = TelephoneContactTypeSub
# end class TelephoneContactTypeSub


class UnitSectorAirspaceTypeSub(supermod.UnitSectorAirspaceType):
    def __init__(self, airspaceType=None, valueOf_=None, **kwargs_):
        super(UnitSectorAirspaceTypeSub, self).__init__(airspaceType, valueOf_,  **kwargs_)
supermod.UnitSectorAirspaceType.subclass = UnitSectorAirspaceTypeSub
# end class UnitSectorAirspaceTypeSub


class AltitudeTypeSub(supermod.AltitudeType):
    def __init__(self, ref=None, uom=None, valueOf_=None, extensiontype_=None, **kwargs_):
        super(AltitudeTypeSub, self).__init__(ref, uom, valueOf_, extensiontype_,  **kwargs_)
supermod.AltitudeType.subclass = AltitudeTypeSub
# end class AltitudeTypeSub


class VerticalRateTypeSub(supermod.VerticalRateType):
    def __init__(self, uom=None, valueOf_=None, **kwargs_):
        super(VerticalRateTypeSub, self).__init__(uom, valueOf_,  **kwargs_)
supermod.VerticalRateType.subclass = VerticalRateTypeSub
# end class VerticalRateTypeSub


class AirspeedInIasOrMachTypeSub(supermod.AirspeedInIasOrMachType):
    def __init__(self, uom=None, valueOf_=None, extensiontype_=None, **kwargs_):
        super(AirspeedInIasOrMachTypeSub, self).__init__(uom, valueOf_, extensiontype_,  **kwargs_)
supermod.AirspeedInIasOrMachType.subclass = AirspeedInIasOrMachTypeSub
# end class AirspeedInIasOrMachTypeSub


class AngleTypeSub(supermod.AngleType):
    def __init__(self, uom=None, valueOf_=None, extensiontype_=None, **kwargs_):
        super(AngleTypeSub, self).__init__(uom, valueOf_, extensiontype_,  **kwargs_)
supermod.AngleType.subclass = AngleTypeSub
# end class AngleTypeSub


class DimensionsTypeSub(supermod.DimensionsType):
    def __init__(self, height=None, length=None, width=None, **kwargs_):
        super(DimensionsTypeSub, self).__init__(height, length, width,  **kwargs_)
supermod.DimensionsType.subclass = DimensionsTypeSub
# end class DimensionsTypeSub


class DistanceTypeSub(supermod.DistanceType):
    def __init__(self, uom=None, valueOf_=None, extensiontype_=None, **kwargs_):
        super(DistanceTypeSub, self).__init__(uom, valueOf_, extensiontype_,  **kwargs_)
supermod.DistanceType.subclass = DistanceTypeSub
# end class DistanceTypeSub


class GroundspeedTypeSub(supermod.GroundspeedType):
    def __init__(self, uom=None, valueOf_=None, **kwargs_):
        super(GroundspeedTypeSub, self).__init__(uom, valueOf_,  **kwargs_)
supermod.GroundspeedType.subclass = GroundspeedTypeSub
# end class GroundspeedTypeSub


class LengthTypeSub(supermod.LengthType):
    def __init__(self, uom=None, valueOf_=None, **kwargs_):
        super(LengthTypeSub, self).__init__(uom, valueOf_,  **kwargs_)
supermod.LengthType.subclass = LengthTypeSub
# end class LengthTypeSub


class PressureTypeSub(supermod.PressureType):
    def __init__(self, uom=None, valueOf_=None, **kwargs_):
        super(PressureTypeSub, self).__init__(uom, valueOf_,  **kwargs_)
supermod.PressureType.subclass = PressureTypeSub
# end class PressureTypeSub


class TemperatureTypeSub(supermod.TemperatureType):
    def __init__(self, uom=None, valueOf_=None, **kwargs_):
        super(TemperatureTypeSub, self).__init__(uom, valueOf_,  **kwargs_)
supermod.TemperatureType.subclass = TemperatureTypeSub
# end class TemperatureTypeSub


class TrueAirspeedOrMachTypeSub(supermod.TrueAirspeedOrMachType):
    def __init__(self, uom=None, valueOf_=None, **kwargs_):
        super(TrueAirspeedOrMachTypeSub, self).__init__(uom, valueOf_,  **kwargs_)
supermod.TrueAirspeedOrMachType.subclass = TrueAirspeedOrMachTypeSub
# end class TrueAirspeedOrMachTypeSub


class VolumeTypeSub(supermod.VolumeType):
    def __init__(self, uom=None, valueOf_=None, **kwargs_):
        super(VolumeTypeSub, self).__init__(uom, valueOf_,  **kwargs_)
supermod.VolumeType.subclass = VolumeTypeSub
# end class VolumeTypeSub


class WeightTypeSub(supermod.WeightType):
    def __init__(self, uom=None, valueOf_=None, **kwargs_):
        super(WeightTypeSub, self).__init__(uom, valueOf_,  **kwargs_)
supermod.WeightType.subclass = WeightTypeSub
# end class WeightTypeSub


class WindDirectionTypeSub(supermod.WindDirectionType):
    def __init__(self, uom=None, valueOf_=None, **kwargs_):
        super(WindDirectionTypeSub, self).__init__(uom, valueOf_,  **kwargs_)
supermod.WindDirectionType.subclass = WindDirectionTypeSub
# end class WindDirectionTypeSub


class WindspeedTypeSub(supermod.WindspeedType):
    def __init__(self, uom=None, valueOf_=None, **kwargs_):
        super(WindspeedTypeSub, self).__init__(uom, valueOf_,  **kwargs_)
supermod.WindspeedType.subclass = WindspeedTypeSub
# end class WindspeedTypeSub


class GeographicLocationTypeSub(supermod.GeographicLocationType):
    def __init__(self, srsName='urn:ogc:def:crs:EPSG::4326', pos=None, extensiontype_=None, **kwargs_):
        super(GeographicLocationTypeSub, self).__init__(srsName, pos, extensiontype_,  **kwargs_)
supermod.GeographicLocationType.subclass = GeographicLocationTypeSub
# end class GeographicLocationTypeSub


class OrganizationTypeSub(supermod.OrganizationType):
    def __init__(self, name=None, otherOrganization=None, contact=None, **kwargs_):
        super(OrganizationTypeSub, self).__init__(name, otherOrganization, contact,  **kwargs_)
supermod.OrganizationType.subclass = OrganizationTypeSub
# end class OrganizationTypeSub


class PersonTypeSub(supermod.PersonType):
    def __init__(self, name=None, contact=None, **kwargs_):
        super(PersonTypeSub, self).__init__(name, contact,  **kwargs_)
supermod.PersonType.subclass = PersonTypeSub
# end class PersonTypeSub


class PersonOrOrganizationTypeSub(supermod.PersonOrOrganizationType):
    def __init__(self, organization=None, person=None, **kwargs_):
        super(PersonOrOrganizationTypeSub, self).__init__(organization, person,  **kwargs_)
supermod.PersonOrOrganizationType.subclass = PersonOrOrganizationTypeSub
# end class PersonOrOrganizationTypeSub


class TimeSpanTypeSub(supermod.TimeSpanType):
    def __init__(self, beginPosition=None, endPosition=None, **kwargs_):
        super(TimeSpanTypeSub, self).__init__(beginPosition, endPosition,  **kwargs_)
supermod.TimeSpanType.subclass = TimeSpanTypeSub
# end class TimeSpanTypeSub


class MultiTimeTypeSub(supermod.MultiTimeType):
    def __init__(self, actual=None, estimated=None, extensiontype_=None, **kwargs_):
        super(MultiTimeTypeSub, self).__init__(actual, estimated, extensiontype_,  **kwargs_)
supermod.MultiTimeType.subclass = MultiTimeTypeSub
# end class MultiTimeTypeSub


class ReportedTimeTypeSub(supermod.ReportedTimeType):
    def __init__(self, time=None, centre=None, source=None, system=None, timestamp=None, **kwargs_):
        super(ReportedTimeTypeSub, self).__init__(time, centre, source, system, timestamp,  **kwargs_)
supermod.ReportedTimeType.subclass = ReportedTimeTypeSub
# end class ReportedTimeTypeSub


class TargetMultiTimeTypeSub(supermod.TargetMultiTimeType):
    def __init__(self, actual=None, estimated=None, target=None, extensiontype_=None, **kwargs_):
        super(TargetMultiTimeTypeSub, self).__init__(actual, estimated, target, extensiontype_,  **kwargs_)
supermod.TargetMultiTimeType.subclass = TargetMultiTimeTypeSub
# end class TargetMultiTimeTypeSub


class TimeSequenceTypeSub(supermod.TimeSequenceType):
    def __init__(self, approval=None, begin=None, end=None, ready=None, request=None, **kwargs_):
        super(TimeSequenceTypeSub, self).__init__(approval, begin, end, ready, request,  **kwargs_)
supermod.TimeSequenceType.subclass = TimeSequenceTypeSub
# end class TimeSequenceTypeSub


class FeatureTypeSub(supermod.FeatureType):
    def __init__(self, centre=None, source=None, system=None, timestamp=None, extensiontype_=None, **kwargs_):
        super(FeatureTypeSub, self).__init__(centre, source, system, timestamp, extensiontype_,  **kwargs_)
supermod.FeatureType.subclass = FeatureTypeSub
# end class FeatureTypeSub


class AtcUnitReferenceTypeSub(supermod.AtcUnitReferenceType):
    def __init__(self, delegated=None, sectorIdentifier=None, extensiontype_=None, **kwargs_):
        super(AtcUnitReferenceTypeSub, self).__init__(delegated, sectorIdentifier, extensiontype_,  **kwargs_)
supermod.AtcUnitReferenceType.subclass = AtcUnitReferenceTypeSub
# end class AtcUnitReferenceTypeSub


class IdentifiedUnitReferenceTypeSub(supermod.IdentifiedUnitReferenceType):
    def __init__(self, delegated=None, sectorIdentifier=None, unitIdentifier=None, **kwargs_):
        super(IdentifiedUnitReferenceTypeSub, self).__init__(delegated, sectorIdentifier, unitIdentifier,  **kwargs_)
supermod.IdentifiedUnitReferenceType.subclass = IdentifiedUnitReferenceTypeSub
# end class IdentifiedUnitReferenceTypeSub


class UnknownUnitReferenceTypeSub(supermod.UnknownUnitReferenceType):
    def __init__(self, delegated=None, sectorIdentifier=None, unitNameOrAltId=None, unitLocation=None, **kwargs_):
        super(UnknownUnitReferenceTypeSub, self).__init__(delegated, sectorIdentifier, unitNameOrAltId, unitLocation,  **kwargs_)
supermod.UnknownUnitReferenceType.subclass = UnknownUnitReferenceTypeSub
# end class UnknownUnitReferenceTypeSub


class AirspeedChoiceTypeSub(supermod.AirspeedChoiceType):
    def __init__(self, airspeed=None, airspeedRange=None, **kwargs_):
        super(AirspeedChoiceTypeSub, self).__init__(airspeed, airspeedRange,  **kwargs_)
supermod.AirspeedChoiceType.subclass = AirspeedChoiceTypeSub
# end class AirspeedChoiceTypeSub


class AirspeedRangeTypeSub(supermod.AirspeedRangeType):
    def __init__(self, lowerSpeed=None, upperSpeed=None, **kwargs_):
        super(AirspeedRangeTypeSub, self).__init__(lowerSpeed, upperSpeed,  **kwargs_)
supermod.AirspeedRangeType.subclass = AirspeedRangeTypeSub
# end class AirspeedRangeTypeSub


class AltitudeChoiceTypeSub(supermod.AltitudeChoiceType):
    def __init__(self, altitude=None, altitudeRange=None, **kwargs_):
        super(AltitudeChoiceTypeSub, self).__init__(altitude, altitudeRange,  **kwargs_)
supermod.AltitudeChoiceType.subclass = AltitudeChoiceTypeSub
# end class AltitudeChoiceTypeSub


class BeaconCodeTypeSub(supermod.BeaconCodeType):
    def __init__(self, ssrMode=None, valueOf_=None, **kwargs_):
        super(BeaconCodeTypeSub, self).__init__(ssrMode, valueOf_,  **kwargs_)
supermod.BeaconCodeType.subclass = BeaconCodeTypeSub
# end class BeaconCodeTypeSub


class GloballyUniqueFlightIdentifierTypeSub(supermod.GloballyUniqueFlightIdentifierType):
    def __init__(self, codeSpace='urn:uuid', valueOf_=None, **kwargs_):
        super(GloballyUniqueFlightIdentifierTypeSub, self).__init__(codeSpace, valueOf_,  **kwargs_)
supermod.GloballyUniqueFlightIdentifierType.subclass = GloballyUniqueFlightIdentifierTypeSub
# end class GloballyUniqueFlightIdentifierTypeSub


class GroundspeedChoiceTypeSub(supermod.GroundspeedChoiceType):
    def __init__(self, groundspeed=None, groundspeedRange=None, **kwargs_):
        super(GroundspeedChoiceTypeSub, self).__init__(groundspeed, groundspeedRange,  **kwargs_)
supermod.GroundspeedChoiceType.subclass = GroundspeedChoiceTypeSub
# end class GroundspeedChoiceTypeSub


class GroundspeedRangeTypeSub(supermod.GroundspeedRangeType):
    def __init__(self, lowerSpeed=None, upperSpeed=None, **kwargs_):
        super(GroundspeedRangeTypeSub, self).__init__(lowerSpeed, upperSpeed,  **kwargs_)
supermod.GroundspeedRangeType.subclass = GroundspeedRangeTypeSub
# end class GroundspeedRangeTypeSub


class LateralOfftrackTypeSub(supermod.LateralOfftrackType):
    def __init__(self, offtrackReason=None, offtrackDistance=None, **kwargs_):
        super(LateralOfftrackTypeSub, self).__init__(offtrackReason, offtrackDistance,  **kwargs_)
supermod.LateralOfftrackType.subclass = LateralOfftrackTypeSub
# end class LateralOfftrackTypeSub


class NameValueListTypeSub(supermod.NameValueListType):
    def __init__(self, nameValue=None, **kwargs_):
        super(NameValueListTypeSub, self).__init__(nameValue,  **kwargs_)
supermod.NameValueListType.subclass = NameValueListTypeSub
# end class NameValueListTypeSub


class NameValuePairTypeSub(supermod.NameValuePairType):
    def __init__(self, name=None, value=None, **kwargs_):
        super(NameValuePairTypeSub, self).__init__(name, value,  **kwargs_)
supermod.NameValuePairType.subclass = NameValuePairTypeSub
# end class NameValuePairTypeSub


class OfftrackDistanceTypeSub(supermod.OfftrackDistanceType):
    def __init__(self, direction=None, distance=None, **kwargs_):
        super(OfftrackDistanceTypeSub, self).__init__(direction, distance,  **kwargs_)
supermod.OfftrackDistanceType.subclass = OfftrackDistanceTypeSub
# end class OfftrackDistanceTypeSub


class RadioFrequencyTypeSub(supermod.RadioFrequencyType):
    def __init__(self, uom=None, valueOf_=None, **kwargs_):
        super(RadioFrequencyTypeSub, self).__init__(uom, valueOf_,  **kwargs_)
supermod.RadioFrequencyType.subclass = RadioFrequencyTypeSub
# end class RadioFrequencyTypeSub


class SpeedTypeSub(supermod.SpeedType):
    def __init__(self, uom=None, speedCondition=None, valueOf_=None, **kwargs_):
        super(SpeedTypeSub, self).__init__(uom, speedCondition, valueOf_,  **kwargs_)
supermod.SpeedType.subclass = SpeedTypeSub
# end class SpeedTypeSub


class VerticalRangeTypeSub(supermod.VerticalRangeType):
    def __init__(self, lowerBound=None, upperBound=None, **kwargs_):
        super(VerticalRangeTypeSub, self).__init__(lowerBound, upperBound,  **kwargs_)
supermod.VerticalRangeType.subclass = VerticalRangeTypeSub
# end class VerticalRangeTypeSub


class ExtensionTypeSub(supermod.ExtensionType):
    def __init__(self, centre=None, source=None, system=None, timestamp=None, **kwargs_):
        super(ExtensionTypeSub, self).__init__(centre, source, system, timestamp,  **kwargs_)
supermod.ExtensionType.subclass = ExtensionTypeSub
# end class ExtensionTypeSub


class AircraftTypeSub(supermod.AircraftType):
    def __init__(self, centre=None, source=None, system=None, timestamp=None, aircraftAddress=None, aircraftColours=None, aircraftPerformance=None, aircraftQuantity=None, engineType=None, registration=None, wakeTurbulence=None, aircraftType=None, capabilities=None, **kwargs_):
        super(AircraftTypeSub, self).__init__(centre, source, system, timestamp, aircraftAddress, aircraftColours, aircraftPerformance, aircraftQuantity, engineType, registration, wakeTurbulence, aircraftType, capabilities,  **kwargs_)
supermod.AircraftType.subclass = AircraftTypeSub
# end class AircraftTypeSub


class AircraftCapabilitiesTypeSub(supermod.AircraftCapabilitiesType):
    def __init__(self, standardCapabilities=None, communication=None, navigation=None, surveillance=None, survival=None, **kwargs_):
        super(AircraftCapabilitiesTypeSub, self).__init__(standardCapabilities, communication, navigation, surveillance, survival,  **kwargs_)
supermod.AircraftCapabilitiesType.subclass = AircraftCapabilitiesTypeSub
# end class AircraftCapabilitiesTypeSub


class AircraftTypeTypeSub(supermod.AircraftTypeType):
    def __init__(self, icaoModelIdentifier=None, otherModelData=None, **kwargs_):
        super(AircraftTypeTypeSub, self).__init__(icaoModelIdentifier, otherModelData,  **kwargs_)
supermod.AircraftTypeType.subclass = AircraftTypeTypeSub
# end class AircraftTypeTypeSub


class CommunicationCapabilitiesTypeSub(supermod.CommunicationCapabilitiesType):
    def __init__(self, otherCommunicationCapabilities=None, otherDataLinkCapabilities=None, selectiveCallingCode=None, communicationCode=None, dataLinkCode=None, **kwargs_):
        super(CommunicationCapabilitiesTypeSub, self).__init__(otherCommunicationCapabilities, otherDataLinkCapabilities, selectiveCallingCode, communicationCode, dataLinkCode,  **kwargs_)
supermod.CommunicationCapabilitiesType.subclass = CommunicationCapabilitiesTypeSub
# end class CommunicationCapabilitiesTypeSub


class NavigationCapabilitiesTypeSub(supermod.NavigationCapabilitiesType):
    def __init__(self, otherNavigationCapabilities=None, navigationCode=None, performanceBasedCode=None, **kwargs_):
        super(NavigationCapabilitiesTypeSub, self).__init__(otherNavigationCapabilities, navigationCode, performanceBasedCode,  **kwargs_)
supermod.NavigationCapabilitiesType.subclass = NavigationCapabilitiesTypeSub
# end class NavigationCapabilitiesTypeSub


class SurveillanceCapabilitiesTypeSub(supermod.SurveillanceCapabilitiesType):
    def __init__(self, otherSurveillanceCapabilities=None, surveillanceCode=None, **kwargs_):
        super(SurveillanceCapabilitiesTypeSub, self).__init__(otherSurveillanceCapabilities, surveillanceCode,  **kwargs_)
supermod.SurveillanceCapabilitiesType.subclass = SurveillanceCapabilitiesTypeSub
# end class SurveillanceCapabilitiesTypeSub


class DinghyTypeSub(supermod.DinghyType):
    def __init__(self, covered=None, quantity=None, totalCapacity=None, colour=None, **kwargs_):
        super(DinghyTypeSub, self).__init__(covered, quantity, totalCapacity, colour,  **kwargs_)
supermod.DinghyType.subclass = DinghyTypeSub
# end class DinghyTypeSub


class DinghyColourTypeSub(supermod.DinghyColourType):
    def __init__(self, colourCode=None, otherColour=None, **kwargs_):
        super(DinghyColourTypeSub, self).__init__(colourCode, otherColour,  **kwargs_)
supermod.DinghyColourType.subclass = DinghyColourTypeSub
# end class DinghyColourTypeSub


class SurvivalCapabilitiesTypeSub(supermod.SurvivalCapabilitiesType):
    def __init__(self, survivalEquipmentRemarks=None, dinghyInformation=None, emergencyRadioCode=None, lifeJacketCode=None, survivalEquipmentCode=None, **kwargs_):
        super(SurvivalCapabilitiesTypeSub, self).__init__(survivalEquipmentRemarks, dinghyInformation, emergencyRadioCode, lifeJacketCode, survivalEquipmentCode,  **kwargs_)
supermod.SurvivalCapabilitiesType.subclass = SurvivalCapabilitiesTypeSub
# end class SurvivalCapabilitiesTypeSub


class AdditionalHandlingInformationTypeSub(supermod.AdditionalHandlingInformationType):
    def __init__(self, responsibleAgent=None, **kwargs_):
        super(AdditionalHandlingInformationTypeSub, self).__init__(responsibleAgent,  **kwargs_)
supermod.AdditionalHandlingInformationType.subclass = AdditionalHandlingInformationTypeSub
# end class AdditionalHandlingInformationTypeSub


class AirWaybillTypeSub(supermod.AirWaybillType):
    def __init__(self, airWaybillNumber=None, valueOf_=None, **kwargs_):
        super(AirWaybillTypeSub, self).__init__(airWaybillNumber, valueOf_,  **kwargs_)
supermod.AirWaybillType.subclass = AirWaybillTypeSub
# end class AirWaybillTypeSub


class DangerousGoodsTypeSub(supermod.DangerousGoodsType):
    def __init__(self, centre=None, source=None, system=None, timestamp=None, aircraftLimitation=None, guidebookNumber=None, onboardLocation=None, shipment=None, airWayBill=None, handlingInformation=None, packageGroup=None, shippingInformation=None, **kwargs_):
        super(DangerousGoodsTypeSub, self).__init__(centre, source, system, timestamp, aircraftLimitation, guidebookNumber, onboardLocation, shipment, airWayBill, handlingInformation, packageGroup, shippingInformation,  **kwargs_)
supermod.DangerousGoodsType.subclass = DangerousGoodsTypeSub
# end class DangerousGoodsTypeSub


class DeclarationTextTypeSub(supermod.DeclarationTextType):
    def __init__(self, compliance=None, consignor=None, shipper=None, **kwargs_):
        super(DeclarationTextTypeSub, self).__init__(compliance, consignor, shipper,  **kwargs_)
supermod.DeclarationTextType.subclass = DeclarationTextTypeSub
# end class DeclarationTextTypeSub


class ShippingInformationTypeSub(supermod.ShippingInformationType):
    def __init__(self, dangerousGoodsScreeningLocation=None, departureCountry=None, destinationCountry=None, originCountry=None, shipmentAuthorizations=None, subsidiaryHazardClassAndDivision=None, supplementaryInformation=None, aerodromeOfLoading=None, aerodromeOfUnloading=None, consignee=None, declarationText=None, shipper=None, transferAerodromes=None, **kwargs_):
        super(ShippingInformationTypeSub, self).__init__(dangerousGoodsScreeningLocation, departureCountry, destinationCountry, originCountry, shipmentAuthorizations, subsidiaryHazardClassAndDivision, supplementaryInformation, aerodromeOfLoading, aerodromeOfUnloading, consignee, declarationText, shipper, transferAerodromes,  **kwargs_)
supermod.ShippingInformationType.subclass = ShippingInformationTypeSub
# end class ShippingInformationTypeSub


class StructuredPostalAddressTypeSub(supermod.StructuredPostalAddressType):
    def __init__(self, name=None, title=None, address=None, onlineContact=None, phoneFax=None, **kwargs_):
        super(StructuredPostalAddressTypeSub, self).__init__(name, title, address, onlineContact, phoneFax,  **kwargs_)
supermod.StructuredPostalAddressType.subclass = StructuredPostalAddressTypeSub
# end class StructuredPostalAddressTypeSub


class AllPackedInOneTypeSub(supermod.AllPackedInOneType):
    def __init__(self, numberOfPackages=None, qValue=None, **kwargs_):
        super(AllPackedInOneTypeSub, self).__init__(numberOfPackages, qValue,  **kwargs_)
supermod.AllPackedInOneType.subclass = AllPackedInOneTypeSub
# end class AllPackedInOneTypeSub


class DangerousGoodsDimensionsTypeSub(supermod.DangerousGoodsDimensionsType):
    def __init__(self, grossWeight=None, netWeight=None, volume=None, **kwargs_):
        super(DangerousGoodsDimensionsTypeSub, self).__init__(grossWeight, netWeight, volume,  **kwargs_)
supermod.DangerousGoodsDimensionsType.subclass = DangerousGoodsDimensionsTypeSub
# end class DangerousGoodsDimensionsTypeSub


class DangerousGoodsPackageTypeSub(supermod.DangerousGoodsPackageType):
    def __init__(self, compatibilityGroup=None, dangerousGoodsLimitation=None, dangerousGoodsQuantity=None, marinePollutantIndicator=None, overpackIndicator=None, packingGroup=None, packingInstructionNumber=None, productName=None, properShippingName=None, reportableQuantity=None, shipmentType=None, supplementaryInformation=None, technicalName=None, typeOfPackaging=None, unNumber=None, allPackedInOne=None, hazardClass=None, packageDimensions=None, radioactiveMaterials=None, shipmentDimensions=None, subsidiaryHazardClass=None, temperatures=None, **kwargs_):
        super(DangerousGoodsPackageTypeSub, self).__init__(compatibilityGroup, dangerousGoodsLimitation, dangerousGoodsQuantity, marinePollutantIndicator, overpackIndicator, packingGroup, packingInstructionNumber, productName, properShippingName, reportableQuantity, shipmentType, supplementaryInformation, technicalName, typeOfPackaging, unNumber, allPackedInOne, hazardClass, packageDimensions, radioactiveMaterials, shipmentDimensions, subsidiaryHazardClass, temperatures,  **kwargs_)
supermod.DangerousGoodsPackageType.subclass = DangerousGoodsPackageTypeSub
# end class DangerousGoodsPackageTypeSub


class DangerousGoodsPackageGroupTypeSub(supermod.DangerousGoodsPackageGroupType):
    def __init__(self, shipmentUseIndicator=None, dangerousGoodsPackage=None, shipmentDimensions=None, **kwargs_):
        super(DangerousGoodsPackageGroupTypeSub, self).__init__(shipmentUseIndicator, dangerousGoodsPackage, shipmentDimensions,  **kwargs_)
supermod.DangerousGoodsPackageGroupType.subclass = DangerousGoodsPackageGroupTypeSub
# end class DangerousGoodsPackageGroupTypeSub


class HazardClassTypeSub(supermod.HazardClassType):
    def __init__(self, hazardDivision=None, valueOf_=None, **kwargs_):
        super(HazardClassTypeSub, self).__init__(hazardDivision, valueOf_,  **kwargs_)
supermod.HazardClassType.subclass = HazardClassTypeSub
# end class HazardClassTypeSub


class TemperaturesTypeSub(supermod.TemperaturesType):
    def __init__(self, controlTemperature=None, emergencyTemperature=None, flashpointTemperature=None, **kwargs_):
        super(TemperaturesTypeSub, self).__init__(controlTemperature, emergencyTemperature, flashpointTemperature,  **kwargs_)
supermod.TemperaturesType.subclass = TemperaturesTypeSub
# end class TemperaturesTypeSub


class RadioactiveMaterialTypeSub(supermod.RadioactiveMaterialType):
    def __init__(self, category=None, criticalitySafetyIndex=None, fissileExceptedIndicator=None, transportIndex=None, radionuclide=None, **kwargs_):
        super(RadioactiveMaterialTypeSub, self).__init__(category, criticalitySafetyIndex, fissileExceptedIndicator, transportIndex, radionuclide,  **kwargs_)
supermod.RadioactiveMaterialType.subclass = RadioactiveMaterialTypeSub
# end class RadioactiveMaterialTypeSub


class RadioactiveMaterialActivityTypeSub(supermod.RadioactiveMaterialActivityType):
    def __init__(self, uom=None, valueOf_=None, **kwargs_):
        super(RadioactiveMaterialActivityTypeSub, self).__init__(uom, valueOf_,  **kwargs_)
supermod.RadioactiveMaterialActivityType.subclass = RadioactiveMaterialActivityTypeSub
# end class RadioactiveMaterialActivityTypeSub


class RadionuclideTypeSub(supermod.RadionuclideType):
    def __init__(self, lowDispersibleMaterialIndicator=None, physicalChemicalForm=None, radionuclideId=None, radionuclideName=None, specialFormIndicator=None, activity=None, **kwargs_):
        super(RadionuclideTypeSub, self).__init__(lowDispersibleMaterialIndicator, physicalChemicalForm, radionuclideId, radionuclideName, specialFormIndicator, activity,  **kwargs_)
supermod.RadionuclideType.subclass = RadionuclideTypeSub
# end class RadionuclideTypeSub


class FlightArrivalTypeSub(supermod.FlightArrivalType):
    def __init__(self, centre=None, source=None, system=None, timestamp=None, arrivalFleetPrioritization=None, arrivalSequenceNumber=None, earliestInBlockTime=None, filedRevisedDestinationStar=None, landingLimits=None, standardInstrumentArrival=None, approachFix=None, approachTime=None, arrivalAerodrome=None, arrivalAerodromeAlternate=None, arrivalAerodromeOriginal=None, arrivalFix=None, arrivalFixTime=None, filedRevisedDestinationAerodrome=None, runwayPositionAndTime=None, standPositionAndTime=None, extensiontype_=None, **kwargs_):
        super(FlightArrivalTypeSub, self).__init__(centre, source, system, timestamp, arrivalFleetPrioritization, arrivalSequenceNumber, earliestInBlockTime, filedRevisedDestinationStar, landingLimits, standardInstrumentArrival, approachFix, approachTime, arrivalAerodrome, arrivalAerodromeAlternate, arrivalAerodromeOriginal, arrivalFix, arrivalFixTime, filedRevisedDestinationAerodrome, runwayPositionAndTime, standPositionAndTime, extensiontype_,  **kwargs_)
supermod.FlightArrivalType.subclass = FlightArrivalTypeSub
# end class FlightArrivalTypeSub


class DepartureActivityTimesTypeSub(supermod.DepartureActivityTimesType):
    def __init__(self, boardingTime=None, deIcingTime=None, groundHandlingTime=None, startupTime=None, **kwargs_):
        super(DepartureActivityTimesTypeSub, self).__init__(boardingTime, deIcingTime, groundHandlingTime, startupTime,  **kwargs_)
supermod.DepartureActivityTimesType.subclass = DepartureActivityTimesTypeSub
# end class DepartureActivityTimesTypeSub


class FlightDepartureTypeSub(supermod.FlightDepartureType):
    def __init__(self, centre=None, source=None, system=None, timestamp=None, departureFleetPrioritization=None, departureSlot=None, earliestOffBlockTime=None, standardInstrumentDeparture=None, departureAerodrome=None, departureFix=None, departureFixTime=None, departureTimes=None, offBlockReadyTime=None, runwayPositionAndTime=None, standPositionAndTime=None, takeoffAlternateAerodrome=None, takeoffWeight=None, extensiontype_=None, **kwargs_):
        super(FlightDepartureTypeSub, self).__init__(centre, source, system, timestamp, departureFleetPrioritization, departureSlot, earliestOffBlockTime, standardInstrumentDeparture, departureAerodrome, departureFix, departureFixTime, departureTimes, offBlockReadyTime, runwayPositionAndTime, standPositionAndTime, takeoffAlternateAerodrome, takeoffWeight, extensiontype_,  **kwargs_)
supermod.FlightDepartureType.subclass = FlightDepartureTypeSub
# end class FlightDepartureTypeSub


class FlightEmergencyTypeSub(supermod.FlightEmergencyType):
    def __init__(self, centre=None, source=None, system=None, timestamp=None, actionTaken=None, emergencyDescription=None, otherInformation=None, phase=None, contact=None, originator=None, **kwargs_):
        super(FlightEmergencyTypeSub, self).__init__(centre, source, system, timestamp, actionTaken, emergencyDescription, otherInformation, phase, contact, originator,  **kwargs_)
supermod.FlightEmergencyType.subclass = FlightEmergencyTypeSub
# end class FlightEmergencyTypeSub


class LastContactTypeSub(supermod.LastContactType):
    def __init__(self, centre=None, source=None, system=None, timestamp=None, lastContactTime=None, lastContactUnit=None, contactFrequency=None, position=None, **kwargs_):
        super(LastContactTypeSub, self).__init__(centre, source, system, timestamp, lastContactTime, lastContactUnit, contactFrequency, position,  **kwargs_)
supermod.LastContactType.subclass = LastContactTypeSub
# end class LastContactTypeSub


class LastPositionReportTypeSub(supermod.LastPositionReportType):
    def __init__(self, determinationMethod=None, timeAtPosition=None, position=None, **kwargs_):
        super(LastPositionReportTypeSub, self).__init__(determinationMethod, timeAtPosition, position,  **kwargs_)
supermod.LastPositionReportType.subclass = LastPositionReportTypeSub
# end class LastPositionReportTypeSub


class RadioCommunicationFailureTypeSub(supermod.RadioCommunicationFailureType):
    def __init__(self, centre=None, source=None, system=None, timestamp=None, radioFailureRemarks=None, remainingComCapability=None, contact=None, **kwargs_):
        super(RadioCommunicationFailureTypeSub, self).__init__(centre, source, system, timestamp, radioFailureRemarks, remainingComCapability, contact,  **kwargs_)
supermod.RadioCommunicationFailureType.subclass = RadioCommunicationFailureTypeSub
# end class RadioCommunicationFailureTypeSub


class AltitudeInTransitionTypeSub(supermod.AltitudeInTransitionType):
    def __init__(self, ref=None, uom=None, crossingCondition=None, valueOf_=None, **kwargs_):
        super(AltitudeInTransitionTypeSub, self).__init__(ref, uom, crossingCondition, valueOf_,  **kwargs_)
supermod.AltitudeInTransitionType.subclass = AltitudeInTransitionTypeSub
# end class AltitudeInTransitionTypeSub


class BoundaryCrossingTypeSub(supermod.BoundaryCrossingType):
    def __init__(self, crossingTime=None, altitude=None, altitudeInTransition=None, crossingPoint=None, crossingSpeed=None, offtrack=None, **kwargs_):
        super(BoundaryCrossingTypeSub, self).__init__(crossingTime, altitude, altitudeInTransition, crossingPoint, crossingSpeed, offtrack,  **kwargs_)
supermod.BoundaryCrossingType.subclass = BoundaryCrossingTypeSub
# end class BoundaryCrossingTypeSub


class HandoffTypeSub(supermod.HandoffType):
    def __init__(self, coordinationStatus=None, receivingUnit=None, transferringUnit=None, extensiontype_=None, **kwargs_):
        super(HandoffTypeSub, self).__init__(coordinationStatus, receivingUnit, transferringUnit, extensiontype_,  **kwargs_)
supermod.HandoffType.subclass = HandoffTypeSub
# end class HandoffTypeSub


class UnitBoundaryTypeSub(supermod.UnitBoundaryType):
    def __init__(self, delegated=None, sectorIdentifier=None, unitBoundaryIndicator=None, boundaryCrossingCoordinated=None, boundaryCrossingProposed=None, downstreamUnit=None, handoff=None, upstreamUnit=None, extensiontype_=None, **kwargs_):
        super(UnitBoundaryTypeSub, self).__init__(delegated, sectorIdentifier, unitBoundaryIndicator, boundaryCrossingCoordinated, boundaryCrossingProposed, downstreamUnit, handoff, upstreamUnit, extensiontype_,  **kwargs_)
supermod.UnitBoundaryType.subclass = UnitBoundaryTypeSub
# end class UnitBoundaryTypeSub


class CoordinationStatusTypeSub(supermod.CoordinationStatusType):
    def __init__(self, abrogationReason=None, coordinationStatus=None, nonStandardCommunicationReason=None, releaseConditions=None, **kwargs_):
        super(CoordinationStatusTypeSub, self).__init__(abrogationReason, coordinationStatus, nonStandardCommunicationReason, releaseConditions,  **kwargs_)
supermod.CoordinationStatusType.subclass = CoordinationStatusTypeSub
# end class CoordinationStatusTypeSub


class CpdlcConnectionTypeSub(supermod.CpdlcConnectionType):
    def __init__(self, atnLogonParameters=None, connectionStatus=None, fans1ALogonParameters=None, frequencyUsage=None, sendCpldcIndicator=None, receivingUnitFrequency=None, **kwargs_):
        super(CpdlcConnectionTypeSub, self).__init__(atnLogonParameters, connectionStatus, fans1ALogonParameters, frequencyUsage, sendCpldcIndicator, receivingUnitFrequency,  **kwargs_)
supermod.CpdlcConnectionType.subclass = CpdlcConnectionTypeSub
# end class CpdlcConnectionTypeSub


class AirspaceConstraintTypeSub(supermod.AirspaceConstraintType):
    def __init__(self, constrainedAirspace=None, airspaceControlledEntryTime=None, extensiontype_=None, **kwargs_):
        super(AirspaceConstraintTypeSub, self).__init__(constrainedAirspace, airspaceControlledEntryTime, extensiontype_,  **kwargs_)
supermod.AirspaceConstraintType.subclass = AirspaceConstraintTypeSub
# end class AirspaceConstraintTypeSub


class BeaconCodeAssignmentTypeSub(supermod.BeaconCodeAssignmentType):
    def __init__(self, currentBeaconCode=None, previousBeaconCode=None, reassignedBeaconCode=None, reassigningUnit=None, **kwargs_):
        super(BeaconCodeAssignmentTypeSub, self).__init__(currentBeaconCode, previousBeaconCode, reassignedBeaconCode, reassigningUnit,  **kwargs_)
supermod.BeaconCodeAssignmentType.subclass = BeaconCodeAssignmentTypeSub
# end class BeaconCodeAssignmentTypeSub


class ClearedFlightInformationTypeSub(supermod.ClearedFlightInformationType):
    def __init__(self, clearedFlightLevel=None, clearedSpeed=None, directRouting=None, heading=None, offtrackClearance=None, rateOfClimbDescend=None, extensiontype_=None, **kwargs_):
        super(ClearedFlightInformationTypeSub, self).__init__(clearedFlightLevel, clearedSpeed, directRouting, heading, offtrackClearance, rateOfClimbDescend, extensiontype_,  **kwargs_)
supermod.ClearedFlightInformationType.subclass = ClearedFlightInformationTypeSub
# end class ClearedFlightInformationTypeSub


class ControlElementTypeSub(supermod.ControlElementType):
    def __init__(self, airspace=None, arrivalAerodrome=None, **kwargs_):
        super(ControlElementTypeSub, self).__init__(airspace, arrivalAerodrome,  **kwargs_)
supermod.ControlElementType.subclass = ControlElementTypeSub
# end class ControlElementTypeSub


class DirectRoutingTypeSub(supermod.DirectRoutingType):
    def __init__(self, from_=None, to=None, **kwargs_):
        super(DirectRoutingTypeSub, self).__init__(from_, to,  **kwargs_)
supermod.DirectRoutingType.subclass = DirectRoutingTypeSub
# end class DirectRoutingTypeSub


class EnRouteTypeSub(supermod.EnRouteType):
    def __init__(self, centre=None, source=None, system=None, timestamp=None, fleetPrioritization=None, alternateAerodrome=None, beaconCodeAssignment=None, boundaryCrossings=None, cleared=None, controlElement=None, cpdlcConnection=None, pointout=None, position=None, extensiontype_=None, **kwargs_):
        super(EnRouteTypeSub, self).__init__(centre, source, system, timestamp, fleetPrioritization, alternateAerodrome, beaconCodeAssignment, boundaryCrossings, cleared, controlElement, cpdlcConnection, pointout, position, extensiontype_,  **kwargs_)
supermod.EnRouteType.subclass = EnRouteTypeSub
# end class EnRouteTypeSub


class PointoutTypeSub(supermod.PointoutType):
    def __init__(self, originatingUnit=None, receivingUnit=None, **kwargs_):
        super(PointoutTypeSub, self).__init__(originatingUnit, receivingUnit,  **kwargs_)
supermod.PointoutType.subclass = PointoutTypeSub
# end class PointoutTypeSub


class ActualSpeedTypeSub(supermod.ActualSpeedType):
    def __init__(self, calculated=None, pilotReported=None, surveillance=None, **kwargs_):
        super(ActualSpeedTypeSub, self).__init__(calculated, pilotReported, surveillance,  **kwargs_)
supermod.ActualSpeedType.subclass = ActualSpeedTypeSub
# end class ActualSpeedTypeSub


class AircraftPositionTypeSub(supermod.AircraftPositionType):
    def __init__(self, centre=None, source=None, system=None, timestamp=None, positionTime=None, reportSource=None, actualSpeed=None, altitude=None, followingPosition=None, nextPosition=None, position=None, track=None, extensiontype_=None, **kwargs_):
        super(AircraftPositionTypeSub, self).__init__(centre, source, system, timestamp, positionTime, reportSource, actualSpeed, altitude, followingPosition, nextPosition, position, track, extensiontype_,  **kwargs_)
supermod.AircraftPositionType.subclass = AircraftPositionTypeSub
# end class AircraftPositionTypeSub


class PlannedReportingPositionTypeSub(supermod.PlannedReportingPositionType):
    def __init__(self, positionEstimatedTime=None, position=None, positionAltitude=None, **kwargs_):
        super(PlannedReportingPositionTypeSub, self).__init__(positionEstimatedTime, position, positionAltitude,  **kwargs_)
supermod.PlannedReportingPositionType.subclass = PlannedReportingPositionTypeSub
# end class PlannedReportingPositionTypeSub


class AircraftOperatorTypeSub(supermod.AircraftOperatorType):
    def __init__(self, operatorCategory=None, operatingOrganization=None, **kwargs_):
        super(AircraftOperatorTypeSub, self).__init__(operatorCategory, operatingOrganization,  **kwargs_)
supermod.AircraftOperatorType.subclass = AircraftOperatorTypeSub
# end class AircraftOperatorTypeSub


class EnRouteDiversionTypeSub(supermod.EnRouteDiversionType):
    def __init__(self, diversionRecoveryInformation=None, **kwargs_):
        super(EnRouteDiversionTypeSub, self).__init__(diversionRecoveryInformation,  **kwargs_)
supermod.EnRouteDiversionType.subclass = EnRouteDiversionTypeSub
# end class EnRouteDiversionTypeSub


class FlightTypeSub(supermod.FlightType):
    def __init__(self, centre=None, source=None, system=None, timestamp=None, flightFiler=None, flightType=None, remarks=None, agreed=None, aircraftDescription=None, arrival=None, controllingUnit=None, dangerousGoods=None, departure=None, emergency=None, enRoute=None, enRouteDiversion=None, extensions=None, flightIdentification=None, flightStatus=None, gufi=None, negotiating=None, operator=None, originator=None, radioCommunicationFailure=None, rankedTrajectories=None, routeToRevisedDestination=None, specialHandling=None, supplementalData=None, extensiontype_=None, **kwargs_):
        super(FlightTypeSub, self).__init__(centre, source, system, timestamp, flightFiler, flightType, remarks, agreed, aircraftDescription, arrival, controllingUnit, dangerousGoods, departure, emergency, enRoute, enRouteDiversion, extensions, flightIdentification, flightStatus, gufi, negotiating, operator, originator, radioCommunicationFailure, rankedTrajectories, routeToRevisedDestination, specialHandling, supplementalData, extensiontype_,  **kwargs_)
supermod.FlightType.subclass = FlightTypeSub
# end class FlightTypeSub


class FlightIdentificationTypeSub(supermod.FlightIdentificationType):
    def __init__(self, aircraftIdentification=None, majorCarrierIdentifier=None, marketingCarrierFlightIdentifier=None, extensiontype_=None, **kwargs_):
        super(FlightIdentificationTypeSub, self).__init__(aircraftIdentification, majorCarrierIdentifier, marketingCarrierFlightIdentifier, extensiontype_,  **kwargs_)
supermod.FlightIdentificationType.subclass = FlightIdentificationTypeSub
# end class FlightIdentificationTypeSub


class OriginatorTypeSub(supermod.OriginatorType):
    def __init__(self, aftnAddress=None, flightOriginator=None, **kwargs_):
        super(OriginatorTypeSub, self).__init__(aftnAddress, flightOriginator,  **kwargs_)
supermod.OriginatorType.subclass = OriginatorTypeSub
# end class OriginatorTypeSub


class SupplementalDataTypeSub(supermod.SupplementalDataType):
    def __init__(self, fuelEndurance=None, personsOnBoard=None, pilotInCommand=None, extensiontype_=None, **kwargs_):
        super(SupplementalDataTypeSub, self).__init__(fuelEndurance, personsOnBoard, pilotInCommand, extensiontype_,  **kwargs_)
supermod.SupplementalDataType.subclass = SupplementalDataTypeSub
# end class SupplementalDataTypeSub


class RankedTrajectoryTypeSub(supermod.RankedTrajectoryType):
    def __init__(self, assignedIndicator=None, identifier=None, maximumAcceptableDelay=None, routeTrajectoryPair=None, extensiontype_=None, **kwargs_):
        super(RankedTrajectoryTypeSub, self).__init__(assignedIndicator, identifier, maximumAcceptableDelay, routeTrajectoryPair, extensiontype_,  **kwargs_)
supermod.RankedTrajectoryType.subclass = RankedTrajectoryTypeSub
# end class RankedTrajectoryTypeSub


class MeteorologicalDataTypeSub(supermod.MeteorologicalDataType):
    def __init__(self, temperature=None, windDirection=None, windSpeed=None, **kwargs_):
        super(MeteorologicalDataTypeSub, self).__init__(temperature, windDirection, windSpeed,  **kwargs_)
supermod.MeteorologicalDataType.subclass = MeteorologicalDataTypeSub
# end class MeteorologicalDataTypeSub


class Point4DTypeSub(supermod.Point4DType):
    def __init__(self, srsName='urn:ogc:def:crs:EPSG::4326', pos=None, time=None, altitude=None, pointRange=None, **kwargs_):
        super(Point4DTypeSub, self).__init__(srsName, pos, time, altitude, pointRange,  **kwargs_)
supermod.Point4DType.subclass = Point4DTypeSub
# end class Point4DTypeSub


class PointRangeTypeSub(supermod.PointRangeType):
    def __init__(self, lateralRange=None, temporalRange=None, verticalRange=None, **kwargs_):
        super(PointRangeTypeSub, self).__init__(lateralRange, temporalRange, verticalRange,  **kwargs_)
supermod.PointRangeType.subclass = PointRangeTypeSub
# end class PointRangeTypeSub


class TemporalRangeTypeSub(supermod.TemporalRangeType):
    def __init__(self, earliest=None, latest=None, **kwargs_):
        super(TemporalRangeTypeSub, self).__init__(earliest, latest,  **kwargs_)
supermod.TemporalRangeType.subclass = TemporalRangeTypeSub
# end class TemporalRangeTypeSub


class TrajectoryTypeSub(supermod.TrajectoryType):
    def __init__(self, trajectoryPoint=None, **kwargs_):
        super(TrajectoryTypeSub, self).__init__(trajectoryPoint,  **kwargs_)
supermod.TrajectoryType.subclass = TrajectoryTypeSub
# end class TrajectoryTypeSub


class TrajectoryChangeTypeSub(supermod.TrajectoryChangeType):
    def __init__(self, constrainedAirspace=None, specialActivityAirspace=None, **kwargs_):
        super(TrajectoryChangeTypeSub, self).__init__(constrainedAirspace, specialActivityAirspace,  **kwargs_)
supermod.TrajectoryChangeType.subclass = TrajectoryChangeTypeSub
# end class TrajectoryChangeTypeSub


class TrajectoryPointTypeSub(supermod.TrajectoryPointType):
    def __init__(self, altimeterSetting=None, metData=None, point=None, predictedAirspeed=None, predictedGroundspeed=None, referencePoint=None, trajectoryChange=None, trajectoryChangeType=None, **kwargs_):
        super(TrajectoryPointTypeSub, self).__init__(altimeterSetting, metData, point, predictedAirspeed, predictedGroundspeed, referencePoint, trajectoryChange, trajectoryChangeType,  **kwargs_)
supermod.TrajectoryPointType.subclass = TrajectoryPointTypeSub
# end class TrajectoryPointTypeSub


class TrajectoryRoutePairTypeSub(supermod.TrajectoryRoutePairType):
    def __init__(self, route=None, trajectory=None, **kwargs_):
        super(TrajectoryRoutePairTypeSub, self).__init__(route, trajectory,  **kwargs_)
supermod.TrajectoryRoutePairType.subclass = TrajectoryRoutePairTypeSub
# end class TrajectoryRoutePairTypeSub


class AbstractRoutePointTypeSub(supermod.AbstractRoutePointType):
    def __init__(self, airTrafficType=None, clearanceLimit=None, delayAtPoint=None, flightRules=None, point=None, extensiontype_=None, **kwargs_):
        super(AbstractRoutePointTypeSub, self).__init__(airTrafficType, clearanceLimit, delayAtPoint, flightRules, point, extensiontype_,  **kwargs_)
supermod.AbstractRoutePointType.subclass = AbstractRoutePointTypeSub
# end class AbstractRoutePointTypeSub


class ElapsedTimeLocationTypeSub(supermod.ElapsedTimeLocationType):
    def __init__(self, longitude=None, point=None, region=None, **kwargs_):
        super(ElapsedTimeLocationTypeSub, self).__init__(longitude, point, region,  **kwargs_)
supermod.ElapsedTimeLocationType.subclass = ElapsedTimeLocationTypeSub
# end class ElapsedTimeLocationTypeSub


class EstimatedElapsedTimeTypeSub(supermod.EstimatedElapsedTimeType):
    def __init__(self, elapsedTime=None, location=None, **kwargs_):
        super(EstimatedElapsedTimeTypeSub, self).__init__(elapsedTime, location,  **kwargs_)
supermod.EstimatedElapsedTimeType.subclass = EstimatedElapsedTimeTypeSub
# end class EstimatedElapsedTimeTypeSub


class ExpandedRouteTypeSub(supermod.ExpandedRouteType):
    def __init__(self, routePoint=None, extensiontype_=None, **kwargs_):
        super(ExpandedRouteTypeSub, self).__init__(routePoint, extensiontype_,  **kwargs_)
supermod.ExpandedRouteType.subclass = ExpandedRouteTypeSub
# end class ExpandedRouteTypeSub


class ExpandedRoutePointTypeSub(supermod.ExpandedRoutePointType):
    def __init__(self, airTrafficType=None, clearanceLimit=None, delayAtPoint=None, flightRules=None, point=None, estimatedTime=None, constraint=None, estimatedLevel=None, **kwargs_):
        super(ExpandedRoutePointTypeSub, self).__init__(airTrafficType, clearanceLimit, delayAtPoint, flightRules, point, estimatedTime, constraint, estimatedLevel,  **kwargs_)
supermod.ExpandedRoutePointType.subclass = ExpandedRoutePointTypeSub
# end class ExpandedRoutePointTypeSub


class RouteTypeSub(supermod.RouteType):
    def __init__(self, centre=None, source=None, system=None, timestamp=None, airfileRouteStartTime=None, flightDuration=None, initialFlightRules=None, routeText=None, climbSchedule=None, descentSchedule=None, estimatedElapsedTime=None, expandedRoute=None, initialCruisingSpeed=None, requestedAltitude=None, segment=None, extensiontype_=None, **kwargs_):
        super(RouteTypeSub, self).__init__(centre, source, system, timestamp, airfileRouteStartTime, flightDuration, initialFlightRules, routeText, climbSchedule, descentSchedule, estimatedElapsedTime, expandedRoute, initialCruisingSpeed, requestedAltitude, segment, extensiontype_,  **kwargs_)
supermod.RouteType.subclass = RouteTypeSub
# end class RouteTypeSub


class RoutePointTypeSub(supermod.RoutePointType):
    def __init__(self, airTrafficType=None, clearanceLimit=None, delayAtPoint=None, flightRules=None, point=None, constraint=None, **kwargs_):
        super(RoutePointTypeSub, self).__init__(airTrafficType, clearanceLimit, delayAtPoint, flightRules, point, constraint,  **kwargs_)
supermod.RoutePointType.subclass = RoutePointTypeSub
# end class RoutePointTypeSub


class RouteSegmentTypeSub(supermod.RouteSegmentType):
    def __init__(self, airway=None, routePoint=None, extensiontype_=None, **kwargs_):
        super(RouteSegmentTypeSub, self).__init__(airway, routePoint, extensiontype_,  **kwargs_)
supermod.RouteSegmentType.subclass = RouteSegmentTypeSub
# end class RouteSegmentTypeSub


class SpeedScheduleTypeSub(supermod.SpeedScheduleType):
    def __init__(self, initialSpeed=None, subsequentSpeed=None, **kwargs_):
        super(SpeedScheduleTypeSub, self).__init__(initialSpeed, subsequentSpeed,  **kwargs_)
supermod.SpeedScheduleType.subclass = SpeedScheduleTypeSub
# end class SpeedScheduleTypeSub


class RouteConstraintOrPreferenceTypeSub(supermod.RouteConstraintOrPreferenceType):
    def __init__(self, constraintType=None, extensiontype_=None, **kwargs_):
        super(RouteConstraintOrPreferenceTypeSub, self).__init__(constraintType, extensiontype_,  **kwargs_)
supermod.RouteConstraintOrPreferenceType.subclass = RouteConstraintOrPreferenceTypeSub
# end class RouteConstraintOrPreferenceTypeSub


class SpeedConstraintTypeSub(supermod.SpeedConstraintType):
    def __init__(self, constraintType=None, positionQualification=None, speed=None, timeConstraint=None, **kwargs_):
        super(SpeedConstraintTypeSub, self).__init__(constraintType, positionQualification, speed, timeConstraint,  **kwargs_)
supermod.SpeedConstraintType.subclass = SpeedConstraintTypeSub
# end class SpeedConstraintTypeSub


class TimeConstraintTypeSub(supermod.TimeConstraintType):
    def __init__(self, constraintType=None, requiredTime=None, timeQualification=None, **kwargs_):
        super(TimeConstraintTypeSub, self).__init__(constraintType, requiredTime, timeQualification,  **kwargs_)
supermod.TimeConstraintType.subclass = TimeConstraintTypeSub
# end class TimeConstraintTypeSub


class FlightStatusTypeSub(supermod.FlightStatusType):
    def __init__(self, centre=None, source=None, system=None, timestamp=None, accepted=None, airborneHold=None, airfile=None, flightCycle=None, missedApproach=None, suspended=None, extensiontype_=None, **kwargs_):
        super(FlightStatusTypeSub, self).__init__(centre, source, system, timestamp, accepted, airborneHold, airfile, flightCycle, missedApproach, suspended, extensiontype_,  **kwargs_)
supermod.FlightStatusType.subclass = FlightStatusTypeSub
# end class FlightStatusTypeSub


class CmsAccuracyTypeSub(supermod.CmsAccuracyType):
    def __init__(self, uom=None, phase=None, type_=None, valueOf_=None, **kwargs_):
        super(CmsAccuracyTypeSub, self).__init__(uom, phase, type_, valueOf_,  **kwargs_)
supermod.CmsAccuracyType.subclass = CmsAccuracyTypeSub
# end class CmsAccuracyTypeSub


class NasAircraftTypeSub(supermod.NasAircraftType):
    def __init__(self, equipmentQualifier=None, nasWakeTurbulence=None, tfmsSpecialAircraftQualifier=None, accuracy=None, **kwargs_):
        super(NasAircraftTypeSub, self).__init__(equipmentQualifier, nasWakeTurbulence, tfmsSpecialAircraftQualifier, accuracy,  **kwargs_)
supermod.NasAircraftType.subclass = NasAircraftTypeSub
# end class NasAircraftTypeSub


class NasPerformanceBasedAccuracyTypeSub(supermod.NasPerformanceBasedAccuracyType):
    def __init__(self, cmsFieldType=None, **kwargs_):
        super(NasPerformanceBasedAccuracyTypeSub, self).__init__(cmsFieldType,  **kwargs_)
supermod.NasPerformanceBasedAccuracyType.subclass = NasPerformanceBasedAccuracyTypeSub
# end class NasPerformanceBasedAccuracyTypeSub


class AboveAltitudeTypeSub(supermod.AboveAltitudeType):
    def __init__(self, ref=None, uom=None, valueOf_=None, **kwargs_):
        super(AboveAltitudeTypeSub, self).__init__(ref, uom, valueOf_,  **kwargs_)
supermod.AboveAltitudeType.subclass = AboveAltitudeTypeSub
# end class AboveAltitudeTypeSub


class AltFixAltAltitudeTypeSub(supermod.AltFixAltAltitudeType):
    def __init__(self, point=None, post=None, pre=None, **kwargs_):
        super(AltFixAltAltitudeTypeSub, self).__init__(point, post, pre,  **kwargs_)
supermod.AltFixAltAltitudeType.subclass = AltFixAltAltitudeTypeSub
# end class AltFixAltAltitudeTypeSub


class BlockAltitudeTypeSub(supermod.BlockAltitudeType):
    def __init__(self, above=None, below=None, **kwargs_):
        super(BlockAltitudeTypeSub, self).__init__(above, below,  **kwargs_)
supermod.BlockAltitudeType.subclass = BlockAltitudeTypeSub
# end class BlockAltitudeTypeSub


class NasAltitudeTypeSub(supermod.NasAltitudeType):
    def __init__(self, above=None, altFixAlt=None, block=None, simple=None, vfr=None, vfrOnTop=None, vfrOnTopPlus=None, vfrPlus=None, **kwargs_):
        super(NasAltitudeTypeSub, self).__init__(above, altFixAlt, block, simple, vfr, vfrOnTop, vfrOnTopPlus, vfrPlus,  **kwargs_)
supermod.NasAltitudeType.subclass = NasAltitudeTypeSub
# end class NasAltitudeTypeSub


class SimpleAltitudeTypeSub(supermod.SimpleAltitudeType):
    def __init__(self, ref=None, uom=None, valueOf_=None, extensiontype_=None, **kwargs_):
        super(SimpleAltitudeTypeSub, self).__init__(ref, uom, valueOf_, extensiontype_,  **kwargs_)
supermod.SimpleAltitudeType.subclass = SimpleAltitudeTypeSub
# end class SimpleAltitudeTypeSub


class VfrAltitudeTypeSub(supermod.VfrAltitudeType):
    def __init__(self, **kwargs_):
        super(VfrAltitudeTypeSub, self).__init__( **kwargs_)
supermod.VfrAltitudeType.subclass = VfrAltitudeTypeSub
# end class VfrAltitudeTypeSub


class VfrOnTopAltitudeTypeSub(supermod.VfrOnTopAltitudeType):
    def __init__(self, **kwargs_):
        super(VfrOnTopAltitudeTypeSub, self).__init__( **kwargs_)
supermod.VfrOnTopAltitudeType.subclass = VfrOnTopAltitudeTypeSub
# end class VfrOnTopAltitudeTypeSub


class VfrOnTopPlusAltitudeTypeSub(supermod.VfrOnTopPlusAltitudeType):
    def __init__(self, ref=None, uom=None, valueOf_=None, **kwargs_):
        super(VfrOnTopPlusAltitudeTypeSub, self).__init__(ref, uom, valueOf_,  **kwargs_)
supermod.VfrOnTopPlusAltitudeType.subclass = VfrOnTopPlusAltitudeTypeSub
# end class VfrOnTopPlusAltitudeTypeSub


class VfrPlusAltitudeTypeSub(supermod.VfrPlusAltitudeType):
    def __init__(self, ref=None, uom=None, valueOf_=None, **kwargs_):
        super(VfrPlusAltitudeTypeSub, self).__init__(ref, uom, valueOf_,  **kwargs_)
supermod.VfrPlusAltitudeType.subclass = VfrPlusAltitudeTypeSub
# end class VfrPlusAltitudeTypeSub


class NasArrivalTypeSub(supermod.NasArrivalType):
    def __init__(self, centre=None, source=None, system=None, timestamp=None, arrivalFleetPrioritization=None, arrivalSequenceNumber=None, earliestInBlockTime=None, filedRevisedDestinationStar=None, landingLimits=None, standardInstrumentArrival=None, approachFix=None, approachTime=None, arrivalAerodrome=None, arrivalAerodromeAlternate=None, arrivalAerodromeOriginal=None, arrivalFix=None, arrivalFixTime=None, filedRevisedDestinationAerodrome=None, runwayPositionAndTime=None, standPositionAndTime=None, arrivalCenter=None, arrivalPoint=None, arrivalSlot=None, holdStatus=None, scheduledInBlockTime=None, slotYielded=None, runwayArrivalTime=None, **kwargs_):
        super(NasArrivalTypeSub, self).__init__(centre, source, system, timestamp, arrivalFleetPrioritization, arrivalSequenceNumber, earliestInBlockTime, filedRevisedDestinationStar, landingLimits, standardInstrumentArrival, approachFix, approachTime, arrivalAerodrome, arrivalAerodromeAlternate, arrivalAerodromeOriginal, arrivalFix, arrivalFixTime, filedRevisedDestinationAerodrome, runwayPositionAndTime, standPositionAndTime, arrivalCenter, arrivalPoint, arrivalSlot, holdStatus, scheduledInBlockTime, slotYielded, runwayArrivalTime,  **kwargs_)
supermod.NasArrivalType.subclass = NasArrivalTypeSub
# end class NasArrivalTypeSub


class RunwayAcceptableSlotSubstitutionTypeSub(supermod.RunwayAcceptableSlotSubstitutionType):
    def __init__(self, earliest=None, latest=None, **kwargs_):
        super(RunwayAcceptableSlotSubstitutionTypeSub, self).__init__(earliest, latest,  **kwargs_)
supermod.RunwayAcceptableSlotSubstitutionType.subclass = RunwayAcceptableSlotSubstitutionTypeSub
# end class RunwayAcceptableSlotSubstitutionTypeSub


class RunwayArrivalTimeTypeSub(supermod.RunwayArrivalTimeType):
    def __init__(self, airlineEstimated=None, earliest=None, original=None, preferred=None, slotSubstitution=None, tfmsEstimated=None, **kwargs_):
        super(RunwayArrivalTimeTypeSub, self).__init__(airlineEstimated, earliest, original, preferred, slotSubstitution, tfmsEstimated,  **kwargs_)
supermod.RunwayArrivalTimeType.subclass = RunwayArrivalTimeTypeSub
# end class RunwayArrivalTimeTypeSub


class NasAdvisoryTypeSub(supermod.NasAdvisoryType):
    def __init__(self, advisoryNumber=None, advisoryType=None, advisoryUpdateTime=None, **kwargs_):
        super(NasAdvisoryTypeSub, self).__init__(advisoryNumber, advisoryType, advisoryUpdateTime,  **kwargs_)
supermod.NasAdvisoryType.subclass = NasAdvisoryTypeSub
# end class NasAdvisoryTypeSub


class NasRerouteTypeSub(supermod.NasRerouteType):
    def __init__(self, rerouteIdentifier=None, rerouteInclusionIndicator=None, rerouteName=None, rerouteProtectedSegment=None, rerouteType=None, **kwargs_):
        super(NasRerouteTypeSub, self).__init__(rerouteIdentifier, rerouteInclusionIndicator, rerouteName, rerouteProtectedSegment, rerouteType,  **kwargs_)
supermod.NasRerouteType.subclass = NasRerouteTypeSub
# end class NasRerouteTypeSub


class NasTmiTypeSub(supermod.NasTmiType):
    def __init__(self, advisories=None, reroute=None, **kwargs_):
        super(NasTmiTypeSub, self).__init__(advisories, reroute,  **kwargs_)
supermod.NasTmiType.subclass = NasTmiTypeSub
# end class NasTmiTypeSub


class NasHandoffTypeSub(supermod.NasHandoffType):
    def __init__(self, coordinationStatus=None, receivingUnit=None, transferringUnit=None, event=None, acceptingUnit=None, **kwargs_):
        super(NasHandoffTypeSub, self).__init__(coordinationStatus, receivingUnit, transferringUnit, event, acceptingUnit,  **kwargs_)
supermod.NasHandoffType.subclass = NasHandoffTypeSub
# end class NasHandoffTypeSub


class NasUnitBoundaryTypeSub(supermod.NasUnitBoundaryType):
    def __init__(self, delegated=None, sectorIdentifier=None, unitBoundaryIndicator=None, boundaryCrossingCoordinated=None, boundaryCrossingProposed=None, downstreamUnit=None, handoff=None, upstreamUnit=None, boundaryCrossingActual=None, **kwargs_):
        super(NasUnitBoundaryTypeSub, self).__init__(delegated, sectorIdentifier, unitBoundaryIndicator, boundaryCrossingCoordinated, boundaryCrossingProposed, downstreamUnit, handoff, upstreamUnit, boundaryCrossingActual,  **kwargs_)
supermod.NasUnitBoundaryType.subclass = NasUnitBoundaryTypeSub
# end class NasUnitBoundaryTypeSub


class NasDepartureTypeSub(supermod.NasDepartureType):
    def __init__(self, centre=None, source=None, system=None, timestamp=None, departureFleetPrioritization=None, departureSlot=None, earliestOffBlockTime=None, standardInstrumentDeparture=None, departureAerodrome=None, departureFix=None, departureFixTime=None, departureTimes=None, offBlockReadyTime=None, runwayPositionAndTime=None, standPositionAndTime=None, takeoffAlternateAerodrome=None, takeoffWeight=None, departureCenter=None, departurePoint=None, scheduledOffBlockTime=None, targetMAEntryTime=None, runwayDepartureTime=None, **kwargs_):
        super(NasDepartureTypeSub, self).__init__(centre, source, system, timestamp, departureFleetPrioritization, departureSlot, earliestOffBlockTime, standardInstrumentDeparture, departureAerodrome, departureFix, departureFixTime, departureTimes, offBlockReadyTime, runwayPositionAndTime, standPositionAndTime, takeoffAlternateAerodrome, takeoffWeight, departureCenter, departurePoint, scheduledOffBlockTime, targetMAEntryTime, runwayDepartureTime,  **kwargs_)
supermod.NasDepartureType.subclass = NasDepartureTypeSub
# end class NasDepartureTypeSub


class RunwayDepartureTimeTypeSub(supermod.RunwayDepartureTimeType):
    def __init__(self, airlineEstimated=None, earliest=None, original=None, preferred=None, tfmEstimated=None, **kwargs_):
        super(RunwayDepartureTimeTypeSub, self).__init__(airlineEstimated, earliest, original, preferred, tfmEstimated,  **kwargs_)
supermod.RunwayDepartureTimeType.subclass = RunwayDepartureTimeTypeSub
# end class RunwayDepartureTimeTypeSub


class AirspaceAcceptableSlotSubstitutionTypeSub(supermod.AirspaceAcceptableSlotSubstitutionType):
    def __init__(self, earliest=None, latest=None, **kwargs_):
        super(AirspaceAcceptableSlotSubstitutionTypeSub, self).__init__(earliest, latest,  **kwargs_)
supermod.AirspaceAcceptableSlotSubstitutionType.subclass = AirspaceAcceptableSlotSubstitutionTypeSub
# end class AirspaceAcceptableSlotSubstitutionTypeSub


class AirspaceEntryTimeTypeSub(supermod.AirspaceEntryTimeType):
    def __init__(self, earliest=None, initial=None, original=None, slotSubstitution=None, tfmsEstimated=None, **kwargs_):
        super(AirspaceEntryTimeTypeSub, self).__init__(earliest, initial, original, slotSubstitution, tfmsEstimated,  **kwargs_)
supermod.AirspaceEntryTimeType.subclass = AirspaceEntryTimeTypeSub
# end class AirspaceEntryTimeTypeSub


class AirspaceExitTimeTypeSub(supermod.AirspaceExitTimeType):
    def __init__(self, tfmsEstimated=None, **kwargs_):
        super(AirspaceExitTimeTypeSub, self).__init__(tfmsEstimated,  **kwargs_)
supermod.AirspaceExitTimeType.subclass = AirspaceExitTimeTypeSub
# end class AirspaceExitTimeTypeSub


class NasAirspaceConstraintTypeSub(supermod.NasAirspaceConstraintType):
    def __init__(self, constrainedAirspace=None, airspaceControlledEntryTime=None, arrivalSlot=None, holdStatus=None, yieldedSlot=None, entryTime=None, exitTime=None, **kwargs_):
        super(NasAirspaceConstraintTypeSub, self).__init__(constrainedAirspace, airspaceControlledEntryTime, arrivalSlot, holdStatus, yieldedSlot, entryTime, exitTime,  **kwargs_)
supermod.NasAirspaceConstraintType.subclass = NasAirspaceConstraintTypeSub
# end class NasAirspaceConstraintTypeSub


class NasClearedFlightInformationTypeSub(supermod.NasClearedFlightInformationType):
    def __init__(self, clearedFlightLevel=None, clearedSpeed=None, directRouting=None, heading=None, offtrackClearance=None, rateOfClimbDescend=None, clearanceHeading=None, clearanceSpeed=None, clearanceText=None, **kwargs_):
        super(NasClearedFlightInformationTypeSub, self).__init__(clearedFlightLevel, clearedSpeed, directRouting, heading, offtrackClearance, rateOfClimbDescend, clearanceHeading, clearanceSpeed, clearanceText,  **kwargs_)
supermod.NasClearedFlightInformationType.subclass = NasClearedFlightInformationTypeSub
# end class NasClearedFlightInformationTypeSub


class NasEnRouteTypeSub(supermod.NasEnRouteType):
    def __init__(self, centre=None, source=None, system=None, timestamp=None, fleetPrioritization=None, alternateAerodrome=None, beaconCodeAssignment=None, boundaryCrossings=None, cleared=None, controlElement=None, cpdlcConnection=None, pointout=None, position=None, expectedFurtherClearanceTime=None, **kwargs_):
        super(NasEnRouteTypeSub, self).__init__(centre, source, system, timestamp, fleetPrioritization, alternateAerodrome, beaconCodeAssignment, boundaryCrossings, cleared, controlElement, cpdlcConnection, pointout, position, expectedFurtherClearanceTime,  **kwargs_)
supermod.NasEnRouteType.subclass = NasEnRouteTypeSub
# end class NasEnRouteTypeSub


class NasAirspeedChoiceTypeSub(supermod.NasAirspeedChoiceType):
    def __init__(self, classified=None, nasAirspeed=None, **kwargs_):
        super(NasAirspeedChoiceTypeSub, self).__init__(classified, nasAirspeed,  **kwargs_)
supermod.NasAirspeedChoiceType.subclass = NasAirspeedChoiceTypeSub
# end class NasAirspeedChoiceTypeSub


class NasCoordinationTypeSub(supermod.NasCoordinationType):
    def __init__(self, coordinationTime=None, coordinationTimeHandling=None, delayTimeToAbsorb=None, coordinationFix=None, **kwargs_):
        super(NasCoordinationTypeSub, self).__init__(coordinationTime, coordinationTimeHandling, delayTimeToAbsorb, coordinationFix,  **kwargs_)
supermod.NasCoordinationType.subclass = NasCoordinationTypeSub
# end class NasCoordinationTypeSub


class NasFlightTypeSub(supermod.NasFlightType):
    def __init__(self, centre=None, source=None, system=None, timestamp=None, flightFiler=None, flightType=None, remarks=None, agreed=None, aircraftDescription=None, arrival=None, controllingUnit=None, dangerousGoods=None, departure=None, emergency=None, enRoute=None, enRouteDiversion=None, extensions=None, flightIdentification=None, flightStatus=None, gufi=None, negotiating=None, operator=None, originator=None, radioCommunicationFailure=None, rankedTrajectories=None, routeToRevisedDestination=None, specialHandling=None, supplementalData=None, currentRVSMCompliance=None, futureRVSMCompliance=None, tfmsFlightClass=None, assignedAltitude=None, coordination=None, flightIdentificationPrevious=None, flightIntent=None, flightPlan=None, interimAltitude=None, nasTmi=None, requestedAirspeed=None, requestedAltitude=None, **kwargs_):
        super(NasFlightTypeSub, self).__init__(centre, source, system, timestamp, flightFiler, flightType, remarks, agreed, aircraftDescription, arrival, controllingUnit, dangerousGoods, departure, emergency, enRoute, enRouteDiversion, extensions, flightIdentification, flightStatus, gufi, negotiating, operator, originator, radioCommunicationFailure, rankedTrajectories, routeToRevisedDestination, specialHandling, supplementalData, currentRVSMCompliance, futureRVSMCompliance, tfmsFlightClass, assignedAltitude, coordination, flightIdentificationPrevious, flightIntent, flightPlan, interimAltitude, nasTmi, requestedAirspeed, requestedAltitude,  **kwargs_)
supermod.NasFlightType.subclass = NasFlightTypeSub
# end class NasFlightTypeSub


class NasFlightIdentificationTypeSub(supermod.NasFlightIdentificationType):
    def __init__(self, aircraftIdentification=None, majorCarrierIdentifier=None, marketingCarrierFlightIdentifier=None, computerId=None, siteSpecificPlanId=None, **kwargs_):
        super(NasFlightIdentificationTypeSub, self).__init__(aircraftIdentification, majorCarrierIdentifier, marketingCarrierFlightIdentifier, computerId, siteSpecificPlanId,  **kwargs_)
supermod.NasFlightIdentificationType.subclass = NasFlightIdentificationTypeSub
# end class NasFlightIdentificationTypeSub


class NasSupplementalDataTypeSub(supermod.NasSupplementalDataType):
    def __init__(self, fuelEndurance=None, personsOnBoard=None, pilotInCommand=None, additionalFlightInformation=None, **kwargs_):
        super(NasSupplementalDataTypeSub, self).__init__(fuelEndurance, personsOnBoard, pilotInCommand, additionalFlightInformation,  **kwargs_)
supermod.NasSupplementalDataType.subclass = NasSupplementalDataTypeSub
# end class NasSupplementalDataTypeSub


class ArrivalMovementAreaHoldInformationTypeSub(supermod.ArrivalMovementAreaHoldInformationType):
    def __init__(self, estimatedExitTime=None, holdIntent=None, **kwargs_):
        super(ArrivalMovementAreaHoldInformationTypeSub, self).__init__(estimatedExitTime, holdIntent,  **kwargs_)
supermod.ArrivalMovementAreaHoldInformationType.subclass = ArrivalMovementAreaHoldInformationTypeSub
# end class ArrivalMovementAreaHoldInformationTypeSub


class DeicingInformationTypeSub(supermod.DeicingInformationType):
    def __init__(self, deicingIntent=None, deicingLocation=None, **kwargs_):
        super(DeicingInformationTypeSub, self).__init__(deicingIntent, deicingLocation,  **kwargs_)
supermod.DeicingInformationType.subclass = DeicingInformationTypeSub
# end class DeicingInformationTypeSub


class DepartureMovementAreaHoldInformationTypeSub(supermod.DepartureMovementAreaHoldInformationType):
    def __init__(self, estimatedEntryTime=None, holdIntent=None, **kwargs_):
        super(DepartureMovementAreaHoldInformationTypeSub, self).__init__(estimatedEntryTime, holdIntent,  **kwargs_)
supermod.DepartureMovementAreaHoldInformationType.subclass = DepartureMovementAreaHoldInformationTypeSub
# end class DepartureMovementAreaHoldInformationTypeSub


class FlightIntentTypeSub(supermod.FlightIntentType):
    def __init__(self, intendedArrivalSpot=None, intendedDepartureSpot=None, standReturnIntent=None, arrival=None, deicing=None, departure=None, **kwargs_):
        super(FlightIntentTypeSub, self).__init__(intendedArrivalSpot, intendedDepartureSpot, standReturnIntent, arrival, deicing, departure,  **kwargs_)
supermod.FlightIntentType.subclass = FlightIntentTypeSub
# end class FlightIntentTypeSub


class NasFlightPlanTypeSub(supermod.NasFlightPlanType):
    def __init__(self, centre=None, source=None, system=None, timestamp=None, flightPlanRemarks=None, identifier=None, **kwargs_):
        super(NasFlightPlanTypeSub, self).__init__(centre, source, system, timestamp, flightPlanRemarks, identifier,  **kwargs_)
supermod.NasFlightPlanType.subclass = NasFlightPlanTypeSub
# end class NasFlightPlanTypeSub


class AbstractMessageTypeSub(supermod.AbstractMessageType):
    def __init__(self, metadata=None, extensiontype_=None, **kwargs_):
        super(AbstractMessageTypeSub, self).__init__(metadata, extensiontype_,  **kwargs_)
supermod.AbstractMessageType.subclass = AbstractMessageTypeSub
# end class AbstractMessageTypeSub


class FeatureMessageTypeSub(supermod.FeatureMessageType):
    def __init__(self, metadata=None, feature=None, **kwargs_):
        super(FeatureMessageTypeSub, self).__init__(metadata, feature,  **kwargs_)
supermod.FeatureMessageType.subclass = FeatureMessageTypeSub
# end class FeatureMessageTypeSub


class FlightMessageTypeSub(supermod.FlightMessageType):
    def __init__(self, metadata=None, flight=None, **kwargs_):
        super(FlightMessageTypeSub, self).__init__(metadata, flight,  **kwargs_)
supermod.FlightMessageType.subclass = FlightMessageTypeSub
# end class FlightMessageTypeSub


class MessageCollectionTypeSub(supermod.MessageCollectionType):
    def __init__(self, message=None, **kwargs_):
        super(MessageCollectionTypeSub, self).__init__(message,  **kwargs_)
supermod.MessageCollectionType.subclass = MessageCollectionTypeSub
# end class MessageCollectionTypeSub


class MessageMetadataTypeSub(supermod.MessageMetadataType):
    def __init__(self, gumi=None, generationLocation=None, validTimeSpan=None, **kwargs_):
        super(MessageMetadataTypeSub, self).__init__(gumi, generationLocation, validTimeSpan,  **kwargs_)
supermod.MessageMetadataType.subclass = MessageMetadataTypeSub
# end class MessageMetadataTypeSub


class NasAircraftPositionTypeSub(supermod.NasAircraftPositionType):
    def __init__(self, centre=None, source=None, system=None, timestamp=None, positionTime=None, reportSource=None, actualSpeed=None, altitude=None, followingPosition=None, nextPosition=None, position=None, track=None, coastIndicator=None, targetPositionTime=None, targetAltitude=None, targetPosition=None, trackVelocity=None, **kwargs_):
        super(NasAircraftPositionTypeSub, self).__init__(centre, source, system, timestamp, positionTime, reportSource, actualSpeed, altitude, followingPosition, nextPosition, position, track, coastIndicator, targetPositionTime, targetAltitude, targetPosition, trackVelocity,  **kwargs_)
supermod.NasAircraftPositionType.subclass = NasAircraftPositionTypeSub
# end class NasAircraftPositionTypeSub


class NasPositionAltitudeTypeSub(supermod.NasPositionAltitudeType):
    def __init__(self, ref=None, uom=None, invalid=None, valueOf_=None, **kwargs_):
        super(NasPositionAltitudeTypeSub, self).__init__(ref, uom, invalid, valueOf_,  **kwargs_)
supermod.NasPositionAltitudeType.subclass = NasPositionAltitudeTypeSub
# end class NasPositionAltitudeTypeSub


class NasVelocityTypeSub(supermod.NasVelocityType):
    def __init__(self, x=None, y=None, **kwargs_):
        super(NasVelocityTypeSub, self).__init__(x, y,  **kwargs_)
supermod.NasVelocityType.subclass = NasVelocityTypeSub
# end class NasVelocityTypeSub


class NasAdaptedRouteTypeSub(supermod.NasAdaptedRouteType):
    def __init__(self, nasRouteAlphanumeric=None, nasRouteIdentifier=None, extensiontype_=None, **kwargs_):
        super(NasAdaptedRouteTypeSub, self).__init__(nasRouteAlphanumeric, nasRouteIdentifier, extensiontype_,  **kwargs_)
supermod.NasAdaptedRouteType.subclass = NasAdaptedRouteTypeSub
# end class NasAdaptedRouteTypeSub


class NasExpandedRouteTypeSub(supermod.NasExpandedRouteType):
    def __init__(self, routePoint=None, routeImpactList=None, **kwargs_):
        super(NasExpandedRouteTypeSub, self).__init__(routePoint, routeImpactList,  **kwargs_)
supermod.NasExpandedRouteType.subclass = NasExpandedRouteTypeSub
# end class NasExpandedRouteTypeSub


class NasRouteTypeSub(supermod.NasRouteType):
    def __init__(self, centre=None, source=None, system=None, timestamp=None, airfileRouteStartTime=None, flightDuration=None, initialFlightRules=None, routeText=None, climbSchedule=None, descentSchedule=None, estimatedElapsedTime=None, expandedRoute=None, initialCruisingSpeed=None, requestedAltitude=None, segment=None, atcIntendedRoute=None, localIntendedRoute=None, nasRouteText=None, adaptedArrivalDepartureRoute=None, adaptedDepartureRoute=None, holdFix=None, nasadaptedArrivalRoute=None, **kwargs_):
        super(NasRouteTypeSub, self).__init__(centre, source, system, timestamp, airfileRouteStartTime, flightDuration, initialFlightRules, routeText, climbSchedule, descentSchedule, estimatedElapsedTime, expandedRoute, initialCruisingSpeed, requestedAltitude, segment, atcIntendedRoute, localIntendedRoute, nasRouteText, adaptedArrivalDepartureRoute, adaptedDepartureRoute, holdFix, nasadaptedArrivalRoute,  **kwargs_)
supermod.NasRouteType.subclass = NasRouteTypeSub
# end class NasRouteTypeSub


class NasRoutePointTypeSub(supermod.NasRoutePointType):
    def __init__(self, airTrafficType=None, clearanceLimit=None, delayAtPoint=None, flightRules=None, point=None, nasFlightRules=None, **kwargs_):
        super(NasRoutePointTypeSub, self).__init__(airTrafficType, clearanceLimit, delayAtPoint, flightRules, point, nasFlightRules,  **kwargs_)
supermod.NasRoutePointType.subclass = NasRoutePointTypeSub
# end class NasRoutePointTypeSub


class NasRouteSegmentTypeSub(supermod.NasRouteSegmentType):
    def __init__(self, airway=None, routePoint=None, reEntryCount=None, reEntrySpecial=None, **kwargs_):
        super(NasRouteSegmentTypeSub, self).__init__(airway, routePoint, reEntryCount, reEntrySpecial,  **kwargs_)
supermod.NasRouteSegmentType.subclass = NasRouteSegmentTypeSub
# end class NasRouteSegmentTypeSub


class RouteImpactListTypeSub(supermod.RouteImpactListType):
    def __init__(self, predictedAirway=None, predictedFix=None, predictedSector=None, predictedUnit=None, predictedWaypoint=None, **kwargs_):
        super(RouteImpactListTypeSub, self).__init__(predictedAirway, predictedFix, predictedSector, predictedUnit, predictedWaypoint,  **kwargs_)
supermod.RouteImpactListType.subclass = RouteImpactListTypeSub
# end class RouteImpactListTypeSub


class NasFlightStatusTypeSub(supermod.NasFlightStatusType):
    def __init__(self, centre=None, source=None, system=None, timestamp=None, accepted=None, airborneHold=None, airfile=None, flightCycle=None, missedApproach=None, suspended=None, fdpsFlightStatus=None, tfmsStatus=None, **kwargs_):
        super(NasFlightStatusTypeSub, self).__init__(centre, source, system, timestamp, accepted, airborneHold, airfile, flightCycle, missedApproach, suspended, fdpsFlightStatus, tfmsStatus,  **kwargs_)
supermod.NasFlightStatusType.subclass = NasFlightStatusTypeSub
# end class NasFlightStatusTypeSub


class ConstrainedAirspaceEntryTypeSub(supermod.ConstrainedAirspaceEntryType):
    def __init__(self, earliestAirspaceEntryTime=None, impactFca=None, **kwargs_):
        super(ConstrainedAirspaceEntryTypeSub, self).__init__(earliestAirspaceEntryTime, impactFca,  **kwargs_)
supermod.ConstrainedAirspaceEntryType.subclass = ConstrainedAirspaceEntryTypeSub
# end class ConstrainedAirspaceEntryTypeSub


class NasTrajectoryOptionTypeSub(supermod.NasTrajectoryOptionType):
    def __init__(self, assignedIndicator=None, identifier=None, maximumAcceptableDelay=None, routeTrajectoryPair=None, ctopIdentifier=None, ctopName=None, manualOverride=None, minimumNotificationMinutes=None, relativeCost=None, totalCost=None, validEndTime=None, validStartTime=None, constrainedAirspaceEntry=None, **kwargs_):
        super(NasTrajectoryOptionTypeSub, self).__init__(assignedIndicator, identifier, maximumAcceptableDelay, routeTrajectoryPair, ctopIdentifier, ctopName, manualOverride, minimumNotificationMinutes, relativeCost, totalCost, validEndTime, validStartTime, constrainedAirspaceEntry,  **kwargs_)
supermod.NasTrajectoryOptionType.subclass = NasTrajectoryOptionTypeSub
# end class NasTrajectoryOptionTypeSub


class NasAdaptedArrivalRouteTypeSub(supermod.NasAdaptedArrivalRouteType):
    def __init__(self, nasRouteAlphanumeric=None, nasRouteIdentifier=None, nasFavNumber=None, **kwargs_):
        super(NasAdaptedArrivalRouteTypeSub, self).__init__(nasRouteAlphanumeric, nasRouteIdentifier, nasFavNumber,  **kwargs_)
supermod.NasAdaptedArrivalRouteType.subclass = NasAdaptedArrivalRouteTypeSub
# end class NasAdaptedArrivalRouteTypeSub


class LevelConstraintTypeSub(supermod.LevelConstraintType):
    def __init__(self, constraintType=None, positionQualification=None, level=None, timeConstraint=None, **kwargs_):
        super(LevelConstraintTypeSub, self).__init__(constraintType, positionQualification, level, timeConstraint,  **kwargs_)
supermod.LevelConstraintType.subclass = LevelConstraintTypeSub
# end class LevelConstraintTypeSub


class ClimbToLevelConstraintTypeSub(supermod.ClimbToLevelConstraintType):
    def __init__(self, constraintType=None, altitudeQualification=None, climbToLevel=None, **kwargs_):
        super(ClimbToLevelConstraintTypeSub, self).__init__(constraintType, altitudeQualification, climbToLevel,  **kwargs_)
supermod.ClimbToLevelConstraintType.subclass = ClimbToLevelConstraintTypeSub
# end class ClimbToLevelConstraintTypeSub


class ExtendedMultiTimeTypeSub(supermod.ExtendedMultiTimeType):
    def __init__(self, actual=None, estimated=None, target=None, controlled=None, initial=None, **kwargs_):
        super(ExtendedMultiTimeTypeSub, self).__init__(actual, estimated, target, controlled, initial,  **kwargs_)
supermod.ExtendedMultiTimeType.subclass = ExtendedMultiTimeTypeSub
# end class ExtendedMultiTimeTypeSub


class LocationPointTypeSub(supermod.LocationPointType):
    def __init__(self, location=None, **kwargs_):
        super(LocationPointTypeSub, self).__init__(location,  **kwargs_)
supermod.LocationPointType.subclass = LocationPointTypeSub
# end class LocationPointTypeSub


class FixPointTypeSub(supermod.FixPointType):
    def __init__(self, fix=None, extensiontype_=None, **kwargs_):
        super(FixPointTypeSub, self).__init__(fix, extensiontype_,  **kwargs_)
supermod.FixPointType.subclass = FixPointTypeSub
# end class FixPointTypeSub


class DirectionTypeSub(supermod.DirectionType):
    def __init__(self, uom=None, ref=None, valueOf_=None, **kwargs_):
        super(DirectionTypeSub, self).__init__(uom, ref, valueOf_,  **kwargs_)
supermod.DirectionType.subclass = DirectionTypeSub
# end class DirectionTypeSub


class RelativePointTypeSub(supermod.RelativePointType):
    def __init__(self, fix=None, distance=None, radial=None, **kwargs_):
        super(RelativePointTypeSub, self).__init__(fix, distance, radial,  **kwargs_)
supermod.RelativePointType.subclass = RelativePointTypeSub
# end class RelativePointTypeSub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'AerodromeReferenceType'
        rootClass = supermod.AerodromeReferenceType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='',
            pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'AerodromeReferenceType'
        rootClass = supermod.AerodromeReferenceType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(content)
        sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    if sys.version_info.major == 2:
        from StringIO import StringIO
    else:
        from io import BytesIO as StringIO
    parser = None
    rootNode= parsexmlstring_(inString, parser)
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'AerodromeReferenceType'
        rootClass = supermod.AerodromeReferenceType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='')
    return rootObj


def parseLiteral(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'AerodromeReferenceType'
        rootClass = supermod.AerodromeReferenceType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from ??? import *\n\n')
        sys.stdout.write('import ??? as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
