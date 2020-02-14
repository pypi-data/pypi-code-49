import abc
import enum

from rivm.helpers import DictionaryHelper, Mapping

from .constants import (
    RoadManager,
    MonitorSubstance,
    SpeedProfile,
    RoadProfile,
    TreeProfile,
    RejectionGround,
    VehicleType,
    Category,
    CorrectionCode,
    Generic,
)


class Transformation(abc.ABC):
    """
    Transformation base.
    """

    MAPPING = {}

    @classmethod
    def apply(cls, column, input_):
        """
        Apply the current transformation to the current column.
        :param column: the `pandas.DataFrame` column.
        """

        def parse(enum_or_string):
            if isinstance(enum_or_string, enum.Enum):
                return enum_or_string.value
            return enum_or_string

        mapping = Mapping({
            parse(key): parse(value) for key, value in cls.MAPPING.items()
        })
        return column.map(mapping)


class MergeTransformation(Transformation):
    """
    The merge transformation combines columns together.
    :param *headers: source headers to merge.
    """

    def __init__(self, *headers):
        self._headers = headers

    def apply(self, column, input_):
        """
        Combine any amount of columns into a single one.
        :param column: the `pandas.DataFrame` column.
        :param input_: the `pandas.DataFrame` object to merge from.
        """
        input_columns = input_[[header.value for header in self._headers]]
        return input_columns.apply(
            lambda x: ' '.join(x.dropna().astype(str)),
            axis=1
        )


class UppercaseTransformation(Transformation):
    """
    Uppercase the entire column.
    """

    @classmethod
    def apply(self, column, input_):
        return column.str.upper()


class RoadManagerTransformation(Transformation):
    MAPPING = {
        'G': RoadManager.MUNICIPALITY,
        'P': RoadManager.PROVINCE,
        'R': RoadManager.STATE,
        'W': RoadManager.WATER_AUTHORITY,
        'T': RoadManager.PRIVATE,
    }


class MonitorSubstanceTransformation(Transformation):
    MAPPING = {
        'f': MonitorSubstance.NONE,  # CSV
        't': MonitorSubstance.ALL,  # CSV
        '': MonitorSubstance.PM10_ONLY,  # CSV
        '0': MonitorSubstance.NONE,  # Shape
        '1': MonitorSubstance.ALL,  # Shape
    }


class SpeedProfileTransformation(Transformation):
    MAPPING = {
        'b': SpeedProfile.NON_URBAN_TRAFFIC,
        'c': SpeedProfile.URBAN_TRAFFIC_NORMAL,
        'd': SpeedProfile.URBAN_TRAFFIC_STAGNATING,
        'e': SpeedProfile.URBAN_TRAFFIC_FREE_FLOW,
    }


class RoadProfileTransformation(Transformation):
    MAPPING = {
        '1': RoadProfile.WIDE_STREET_CANYON,
        '2': RoadProfile.NARROW_STREET_CANYON,
        '3': RoadProfile.ONE_SIDE_BUILDINGS,
        '4': RoadProfile.OTHER,
    }


class TreeProfileTransformation(Transformation):
    MAPPING = {
        '1': TreeProfile.NONE_OR_FEW,
        '1.25': TreeProfile.SEPARATED,
        '1.5': TreeProfile.PACKED,
    }


class RejectionGroundTransformation(Transformation):
    MAPPING = {
        '0': RejectionGround.NONE,
        '1': RejectionGround.COMPLIANCE_CRITERION,
        '2': RejectionGround.EXPOSURE_CRITERION,
        '3': RejectionGround.OTHER,
    }


class VehicleTypeTransformation(Transformation):
    MAPPING = {
        'l': VehicleType.LIGHT_TRAFFIC,
        'm': VehicleType.NORMAL_FREIGHT,
        'z': VehicleType.HEAVY_FREIGHT,
        'b': VehicleType.AUTO_BUS,
    }


class CategoryTransformation(Transformation):
    MAPPING = {
        '92': Category.NATIONAL_ROAD,
        '93': Category.FREEWAY,
        '94': Category.FREEWAY_STRICT_ENFORCEMENT,
    }


class CorrectionCodeTransformation(Transformation):
    MAPPING = {
        '1': CorrectionCode.CORRECTION_FIELD,
        '2': CorrectionCode.POINT_SPECIFIC,
    }


class GenericTransformation(Transformation):
    MAPPING = {
        'f': Generic.USER_SPECIFIC,  # CSV
        't': Generic.GENERIC,  # CSV
        '0': Generic.USER_SPECIFIC,  # Shape
        '1': Generic.GENERIC,  # Shape
    }


class NSLTransformation(Transformation):
    """
    Transform back from `MonitorSubstance`.
    """

    MAPPING = DictionaryHelper.inverse(MonitorSubstanceTransformation.MAPPING)


class GrondTransformation(Transformation):
    """
    Transform back from `RejectionGround`.
    """

    MAPPING = DictionaryHelper.inverse(RejectionGroundTransformation.MAPPING)


class WegbeheerderTransformation(Transformation):
    """
    Transform back from `RoadManager`.
    """

    MAPPING = DictionaryHelper.inverse(RoadManagerTransformation.MAPPING)


class WegtypeTransformation(Transformation):
    """
    Transform back from `Category`.
    """

    MAPPING = DictionaryHelper.inverse(CategoryTransformation.MAPPING)
