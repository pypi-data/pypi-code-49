import abc

import pandas
import geopandas
import shapely

from .constants import Aerius, NSLMonitoring, AeriusShape
from .operation import (
    RemoveDuplicateRows,
    RemoveEmptyRows,
    RemoveInvalidRows,
    RemoveValidRows,
    RemoveColumns,
)
from .transformation import (
    MergeTransformation,
    UppercaseTransformation,
    MonitorSubstanceTransformation,
    RejectionGroundTransformation,
    RoadProfileTransformation,
    RoadManagerTransformation,
    TreeProfileTransformation,
    VehicleTypeTransformation,
    SpeedProfileTransformation,
    CategoryTransformation,
    NSLTransformation,
    GrondTransformation,
    WegbeheerderTransformation,
    WegtypeTransformation,
)


class Builder(abc.ABC):
    """
    Builder base.
    :param input_: the input CSV or bundle.
    """

    HEADERS = {}
    TRANSFORMATIONS = {}
    POST_PROCESSING = []

    def __init__(self, input_):
        self._input = input_.data_frame
        self._output = pandas.DataFrame({
            header.value: [] for header in self.HEADERS
        })

    def build(self):
        """
        Convert the headers and transformations in the right format CSV.
        """
        for output_header, input_header in self.HEADERS.items():
            # Keep column empty when input header is unmapped.
            if not input_header:
                continue
            # Copy the raw values for each mapped header.
            if input_header.value in self._input:
                self._output[output_header.value] = \
                    self._input[input_header.value].copy()
        # Apply each mapped transformation.
        for header, transformation in self.TRANSFORMATIONS.items():
            self._output[header.value] = transformation.apply(
                self._output[header.value],
                self._input,
            )
        # Apply post-processing.
        for operation in self.POST_PROCESSING:
            self._output = operation.apply(self._output)
        return self._output


class ShapeBuilder(Builder):
    """
    Shape builder base.
    :param input_: the input CSV or bundle.
    """

    def __init__(self, input_):
        input_.data_frame['geometry'] = \
            input_.data_frame['geometry'].apply(shapely.wkt.loads)
        self._input = input_.data_frame
        self._output = geopandas.GeoDataFrame(
            {
                header.value: [] for header in self.HEADERS
            },
            geometry='geometry'
        )


class AeriusRekenpunten(Builder):
    """
    Builder for the Aerius `Rekenpunten` CSV.
    """

    HEADERS = {
        Aerius.CALCULATION_POINT_ID: NSLMonitoring.RECEPTORID,
        Aerius.JURISDICTION_ID: NSLMonitoring.OVERHEIDID,
        Aerius.LABEL: NSLMonitoring.NAAM,
        Aerius.MONITOR_SUBSTANCE: NSLMonitoring.NSL,
        Aerius.REJECTION_GROUND: NSLMonitoring.GROND,
        Aerius.DESCRIPTION: None,
        Aerius.GEOMETRY: NSLMonitoring.GEOMET_WKT,
    }

    TRANSFORMATIONS = {
        Aerius.MONITOR_SUBSTANCE: MonitorSubstanceTransformation,
        Aerius.REJECTION_GROUND: RejectionGroundTransformation,
        Aerius.DESCRIPTION: MergeTransformation(
            NSLMonitoring.OVERHEID,
            NSLMonitoring.OPMERKING,
        )
    }

    POST_PROCESSING = [
        RemoveDuplicateRows(Aerius.CALCULATION_POINT_ID),
    ]


class AeriusOverdrachtslijnen(Builder):
    """
    Builder for the Aerius `Overdrachtslijnen` CSV.
    """

    HEADERS = {
        Aerius.SRM1_ROAD_ID: NSLMonitoring.SEGMENT_ID,
        Aerius.CALCULATION_POINT_ID: NSLMonitoring.RECEPTORID,
        Aerius.JURISDICTION_ID: NSLMonitoring.OVERHEIDID,
        Aerius.LABEL: NSLMonitoring.NAAM,
        Aerius.ROAD_PROFILE: NSLMonitoring.WEGTYPE,
        Aerius.TREE_PROFILE: NSLMonitoring.BOOM_FACT,
        Aerius.DESCRIPTION: None,
        Aerius.DISTANCE: NSLMonitoring.AFSTAND,
    }

    TRANSFORMATIONS = {
        Aerius.ROAD_PROFILE: RoadProfileTransformation,
        Aerius.TREE_PROFILE: TreeProfileTransformation,
        Aerius.DESCRIPTION: MergeTransformation(
            NSLMonitoring.OVERHEID,
            NSLMonitoring.OPMERKING,
        )
    }

    POST_PROCESSING = [
        RemoveEmptyRows(Aerius.SRM1_ROAD_ID),
    ]


class AeriusWegvakkenSRM1(Builder):
    """
    Builder for the Aerius `Wegvakken-SRM1` CSV.
    """

    HEADERS = {
        Aerius.SRM1_ROAD_ID: NSLMonitoring.SEGMENT_ID,
        Aerius.JURISDICTION_ID: NSLMonitoring.OVERHEIDID,
        Aerius.LABEL: NSLMonitoring.STRAATNAAM,
        Aerius.ROAD_MANAGER: NSLMonitoring.WEGBEHEER,
        Aerius.SPEED_PROFILE: NSLMonitoring.SNELHEID,
        Aerius.TUNNEL_FACTOR: NSLMonitoring.TUN_FACTOR,
        Aerius.LIGHT_TRAFFIC_INTENSITY: NSLMonitoring.INT_LV,
        Aerius.LIGHT_TRAFFIC_STAGNATION_FACTOR: NSLMonitoring.STAGF_LV,
        Aerius.NORMAL_FREIGHT_INTENSITY: NSLMonitoring.INT_MV,
        Aerius.NORMAL_FREIGHT_STAGNATION_FACTOR: NSLMonitoring.STAGF_MV,
        Aerius.HEAVY_FREIGHT_INTENSITY: NSLMonitoring.INT_ZV,
        Aerius.HEAVY_FREIGHT_STAGNATION_FACTOR: NSLMonitoring.STAGF_ZV,
        Aerius.AUTO_BUS_INTENSITY: NSLMonitoring.INT_BV,
        Aerius.AUTO_BUS_STAGNATION_FACTOR: NSLMonitoring.STAGF_BV,
        Aerius.DESCRIPTION: None,
        Aerius.GEOMETRY: NSLMonitoring.GEOMET_WKT,
        Aerius.CATEGORY: NSLMonitoring.WEGTYPE,
    }

    TRANSFORMATIONS = {
        Aerius.ROAD_MANAGER: RoadManagerTransformation,
        Aerius.SPEED_PROFILE: SpeedProfileTransformation,
        Aerius.CATEGORY: CategoryTransformation,
        Aerius.DESCRIPTION: MergeTransformation(
            NSLMonitoring.OVERHEID,
            NSLMonitoring.OPMERKING,
        )
    }

    POST_PROCESSING = [
        RemoveValidRows(Aerius.CATEGORY),
        RemoveColumns(Aerius.CATEGORY),
    ]


class AeriusWegvakkenSRM2(Builder):
    """
    Builder for the Aerius `Wegvakken-SRM2` CSV.
    """

    HEADERS = {
        Aerius.SRM2_ROAD_ID: NSLMonitoring.SEGMENT_ID,
        Aerius.JURISDICTION_ID: NSLMonitoring.OVERHEIDID,
        Aerius.LABEL: NSLMonitoring.STRAATNAAM,
        Aerius.ROAD_MANAGER: NSLMonitoring.WEGBEHEER,
        Aerius.ELEVATION_HEIGHT: NSLMonitoring.HOOGTE,
        Aerius.CATEGORY: NSLMonitoring.WEGTYPE,
        Aerius.TUNNEL_FACTOR: NSLMonitoring.TUN_FACTOR,
        Aerius.MAX_SPEED: NSLMonitoring.MAXSNELH_P,
        Aerius.DYNAMIC_MAX_SPEED: NSLMonitoring.MAXS_P_DYN,
        Aerius.BARRIER_LEFT_DISTANCE: NSLMonitoring.A_SCHERM_L,
        Aerius.BARRIER_LEFT_HEIGHT: NSLMonitoring.S_HOOGTE_L,
        Aerius.BARRIER_RIGHT_DISTANCE: NSLMonitoring.A_SCHERM_R,
        Aerius.BARRIER_RIGHT_HEIGHT: NSLMonitoring.S_HOOGTE_R,
        Aerius.LIGHT_TRAFFIC_INTENSITY: NSLMonitoring.INT_LV,
        Aerius.LIGHT_TRAFFIC_DYNAMIC_INTENSITY: NSLMonitoring.INT_LV_DYN,
        Aerius.LIGHT_TRAFFIC_STAGNATION_FACTOR: NSLMonitoring.STAGF_LV,
        Aerius.NORMAL_FREIGHT_INTENSITY: NSLMonitoring.INT_MV,
        Aerius.NORMAL_FREIGHT_STAGNATION_FACTOR: NSLMonitoring.STAGF_MV,
        Aerius.HEAVY_FREIGHT_INTENSITY: NSLMonitoring.INT_ZV,
        Aerius.HEAVY_FREIGHT_STAGNATION_FACTOR: NSLMonitoring.STAGF_ZV,
        Aerius.AUTO_BUS_INTENSITY: NSLMonitoring.INT_BV,
        Aerius.AUTO_BUS_STAGNATION_FACTOR: NSLMonitoring.STAGF_BV,
        Aerius.DESCRIPTION: None,
        Aerius.GEOMETRY: NSLMonitoring.GEOMET_WKT,
    }

    TRANSFORMATIONS = {
        Aerius.ROAD_MANAGER: RoadManagerTransformation,
        Aerius.CATEGORY: CategoryTransformation,
        Aerius.DESCRIPTION: MergeTransformation(
            NSLMonitoring.OVERHEID,
            NSLMonitoring.OPMERKING,
        ),
    }

    POST_PROCESSING = [
        RemoveInvalidRows(Aerius.CATEGORY),
    ]


class AeriusMaatregelen(Builder):
    """
    Builder for the Aerius `Maatregelen` CSV.
    """

    HEADERS = {
        Aerius.MEASURE_ID: NSLMonitoring.MAATR_ID,
        Aerius.JURISDICTION_ID: NSLMonitoring.OVERHEID,
        Aerius.LABEL: NSLMonitoring.NAAM,
        Aerius.SUBSTANCE: NSLMonitoring.STOF,
        Aerius.FACTOR: NSLMonitoring.FACTOR,
        Aerius.VEHICLE_TYPE: NSLMonitoring.VOERTUIG,
        Aerius.SPEED_PROFILE: NSLMonitoring.SNELHEID,
        Aerius.DESCRIPTION: None,
        Aerius.GEOMETRY: NSLMonitoring.GEOMET_WKT,
    }

    TRANSFORMATIONS = {
        Aerius.SUBSTANCE: UppercaseTransformation,
        Aerius.VEHICLE_TYPE: VehicleTypeTransformation,
        Aerius.SPEED_PROFILE: SpeedProfileTransformation,
        Aerius.DESCRIPTION: MergeTransformation(
            NSLMonitoring.CATEGORIE,
            NSLMonitoring.GENERIEK,
            NSLMonitoring.NAAM,
        )
    }

    POST_PROCESSING = [
        RemoveInvalidRows(Aerius.SPEED_PROFILE)
    ]


class AeriusCorrecties(Builder):
    """
    Builder for the Aerius `Correcties` CSV.
    """

    HEADERS = {
        Aerius.LABEL: NSLMonitoring.NAAM,
        Aerius.JURISDICTION_ID: NSLMonitoring.OVERHEID,
        Aerius.SUBSTANCE: NSLMonitoring.STOF,
        Aerius.VALUE: NSLMonitoring.CORRECTIE,
        Aerius.CALCULATION_POINT_ID: NSLMonitoring.RECEPTOR_ID,
        Aerius.DESCRIPTION: None,
    }

    TRANSFORMATIONS = {
        Aerius.SUBSTANCE: UppercaseTransformation,
        Aerius.DESCRIPTION: MergeTransformation(
            NSLMonitoring.CODE,
            NSLMonitoring.CORRECTIE_ID,
            NSLMonitoring.GEOMET_WKT,
        )
    }


class NSLMonitoringRekenpunten(Builder):
    """
    Builder for the NSL Monitoring `Rekenpunten` CSV.
    """

    HEADERS = {
        NSLMonitoring.SEGMENT_ID: Aerius.SRM1_ROAD_ID,
        NSLMonitoring.RECEPTORID: Aerius.CALCULATION_POINT_ID,
        NSLMonitoring.OVERHEIDID: Aerius.JURISDICTION_ID,
        NSLMonitoring.OVERHEID: None,
        NSLMonitoring.NUMMER: None,
        NSLMonitoring.NAAM: Aerius.LABEL,
        NSLMonitoring.X_POS: None,
        NSLMonitoring.Y_POS: None,
        NSLMonitoring.TYPE: None,
        NSLMonitoring.AANT_PERS: None,
        NSLMonitoring.NSL: Aerius.MONITOR_SUBSTANCE,
        NSLMonitoring.GROND: Aerius.REJECTION_GROUND,
        NSLMonitoring.AFSTAND: Aerius.DISTANCE,
        NSLMonitoring.WEGTYPE: Aerius.ROAD_PROFILE,
        NSLMonitoring.BOOM_FACT: Aerius.TREE_PROFILE,
        NSLMonitoring.OPMERKING: Aerius.DESCRIPTION,
        NSLMonitoring.OPM_OVDR: None,
        NSLMonitoring.GEWIJZIGD: None,
        NSLMonitoring.GEOMET_WKT: Aerius.GEOMETRY,
        NSLMonitoring.ACTIE: None,
    }

    TRANSFORMATIONS = {
        NSLMonitoring.NSL: NSLTransformation,
        NSLMonitoring.GROND: GrondTransformation,
    }


class NSLMonitoringWegvakken(Builder):
    """
    Builder for the NSL Monitoring `Wegvakken` CSV.
    """

    HEADERS = {
        NSLMonitoring.SEGMENT_ID: Aerius.SRM1_ROAD_ID,
        NSLMonitoring.NWB_WEG_ID: None,
        NSLMonitoring.NWB_VERSIE: None,
        NSLMonitoring.BEGIN_POS: None,
        NSLMonitoring.EIND_POS: None,
        NSLMonitoring.OVERHEIDID: Aerius.JURISDICTION_ID,
        NSLMonitoring.OVERHEID: None,
        NSLMonitoring.STRAATNAAM: Aerius.LABEL,
        NSLMonitoring.STRAATNR: None,
        NSLMonitoring.WEGBEHEER: Aerius.ROAD_MANAGER,
        NSLMonitoring.HOOGTE: Aerius.ELEVATION_HEIGHT,
        NSLMonitoring.X_POS: None,
        NSLMonitoring.Y_POS: None,
        NSLMonitoring.WEGTYPE: Aerius.CATEGORY,
        NSLMonitoring.SNELHEID: Aerius.SPEED_PROFILE,
        NSLMonitoring.TUN_FACTOR: Aerius.TUNNEL_FACTOR,
        NSLMonitoring.BOOM_FACT: None,
        NSLMonitoring.MAXSNELH_P: Aerius.MAX_SPEED,
        NSLMonitoring.MAXS_P_DYN: Aerius.DYNAMIC_MAX_SPEED,
        NSLMonitoring.MAXSNELH_V: None,
        NSLMonitoring.A_RAND_L: None,
        NSLMonitoring.A_GEVEL_L: None,
        NSLMonitoring.BEBDICHT_L: None,
        NSLMonitoring.A_TOEPAS_L: None,
        NSLMonitoring.A_SCHERM_L: Aerius.BARRIER_LEFT_DISTANCE,
        NSLMonitoring.S_HOOGTE_L: Aerius.BARRIER_LEFT_HEIGHT,
        NSLMonitoring.A_RAND_R: None,
        NSLMonitoring.A_GEVEL_R: None,
        NSLMonitoring.BEBDICHT_R: None,
        NSLMonitoring.A_TOEPAS_R: None,
        NSLMonitoring.A_SCHERM_R: Aerius.BARRIER_RIGHT_DISTANCE,
        NSLMonitoring.S_HOOGTE_R: Aerius.BARRIER_RIGHT_HEIGHT,
        NSLMonitoring.STAGF_LV: Aerius.LIGHT_TRAFFIC_STAGNATION_FACTOR,
        NSLMonitoring.INT_LV: Aerius.LIGHT_TRAFFIC_INTENSITY,
        NSLMonitoring.INT_LV_DYN: Aerius.LIGHT_TRAFFIC_DYNAMIC_INTENSITY,
        NSLMonitoring.STAGF_MV: Aerius.NORMAL_FREIGHT_STAGNATION_FACTOR,
        NSLMonitoring.INT_MV: Aerius.NORMAL_FREIGHT_INTENSITY,
        NSLMonitoring.STAGF_ZV: Aerius.HEAVY_FREIGHT_STAGNATION_FACTOR,
        NSLMonitoring.INT_ZV: Aerius.HEAVY_FREIGHT_INTENSITY,
        NSLMonitoring.STAGF_BV: Aerius.AUTO_BUS_STAGNATION_FACTOR,
        NSLMonitoring.INT_BV: Aerius.AUTO_BUS_INTENSITY,
        NSLMonitoring.OPMERKING: None,
        NSLMonitoring.GEWIJZIGD: None,
        NSLMonitoring.GEOMET_WKT: Aerius.GEOMETRY,
        NSLMonitoring.ACTIE: None,
    }

    TRANSFORMATIONS = {
        NSLMonitoring.WEGBEHEER: WegbeheerderTransformation,
        NSLMonitoring.WEGTYPE: WegtypeTransformation,
    }


class NSLMonitoringMaatregelen(Builder):
    """
    Builder for the NSL Monitoring `Maatregelen` CSV.
    """

    HEADERS = {
        NSLMonitoring.MAATR_ID: None,
        NSLMonitoring.NAAM: None,
        NSLMonitoring.OVERHEID: None,
        NSLMonitoring.CATEGORIE: None,
        NSLMonitoring.STOF: None,
        NSLMonitoring.FACTOR: None,
        NSLMonitoring.GENERIEK: None,
        NSLMonitoring.VOERTUIG: None,
        NSLMonitoring.SNELHEID: None,
        NSLMonitoring.ACTIE: None,
        NSLMonitoring.GEWIJZIGD: None,
        NSLMonitoring.GEOMET_WKT: None,
    }


class NSLMonitoringCorrecties(Builder):
    """
    Builder for the NSL Monitoring `Correcties` CSV.
    """

    HEADERS = {
        NSLMonitoring.CORRECTIE_ID: None,
        NSLMonitoring.VARIANT_ID: None,
        NSLMonitoring.JAAR: None,
        NSLMonitoring.NAAM: None,
        NSLMonitoring.OVERHEID: None,
        NSLMonitoring.STOF: None,
        NSLMonitoring.CODE: None,
        NSLMonitoring.CORRECTIE: None,
        NSLMonitoring.RECEPTORID: None,
        NSLMonitoring.GEOMET_WKT: None,
        NSLMonitoring.ACTIE: None,
    }


class NSLMonitoringResultaten(Builder):
    """
    Builder for the NSL Monitoring `Resultaten` CSV.
    """

    HEADERS = {
        NSLMonitoring.RECEPTORID: Aerius.CALCULATION_POINT_ID,
        NSLMonitoring.MRONDE: None,
        NSLMonitoring.REKENJAAR: Aerius.CALCULATION_YEAR,
        NSLMonitoring.OVERHEIDID: None,
        NSLMonitoring.OVERHEID: None,
        NSLMonitoring.NUMMER: None,
        NSLMonitoring.NAAM: Aerius.LABEL,
        NSLMonitoring.NSL: Aerius.MONITOR_SUBSTANCE,
        NSLMonitoring.GROND: None,
        NSLMonitoring.OPMERKING: None,
        NSLMonitoring.X_POS: None,
        NSLMonitoring.Y_POS: None,
        NSLMonitoring.CONC_NO2: Aerius.NO2_TOTAL_CONCENTRATION,
        NSLMonitoring.CONC_PM10: Aerius.PM10_TOTAL_CONCENTRATION,
        NSLMonitoring.PM10_OD: Aerius.PM10_EXCEEDANCE_DAYS,
        NSLMonitoring.CONC_PM25: Aerius.PM25_TOTAL_CONCENTRATION,
        NSLMonitoring.CONC_EC: Aerius.EC_TOTAL_CONCENTRATION,
        NSLMonitoring.SRM2_NOX: Aerius.NOX_SRM2_CONCENTRATION,
        NSLMonitoring.SRM2_NO2: None,
        NSLMonitoring.SRM2_FNO2: None,
        NSLMonitoring.SRM2_PM10: Aerius.PM10_SRM2_CONCENTRATION,
        NSLMonitoring.SRM2_PM25: Aerius.PM25_SRM2_CONCENTRATION,
        NSLMonitoring.SRM2_EC: Aerius.EC_SRM2_CONCENTRATION,
        NSLMonitoring.SRM1_NOX: Aerius.NOX_SRM1_CONCENTRATION,
        NSLMonitoring.SRM1_NO2DU: Aerius.NO2_SRM1_CONCENTRATION_DIRECT,
        NSLMonitoring.SRM1_FNO2: None,
        NSLMonitoring.SRM1_PM10: Aerius.PM10_SRM1_CONCENTRATION,
        NSLMonitoring.SRM1_PM25: Aerius.PM25_SRM1_CONCENTRATION,
        NSLMonitoring.SRM1_EC: Aerius.EC_SRM1_CONCENTRATION,
        NSLMonitoring.WIND_SPEED: None,
        NSLMonitoring.GCN_NO2: Aerius.NO2_GCN_BACKGROUND_CONCENTRATION,
        NSLMonitoring.GCN_O3: None,
        NSLMonitoring.GCN_PM10: Aerius.PM10_GCN_BACKGROUND_CONCENTRATION,
        NSLMonitoring.GCN_PM25: Aerius.PM25_GCN_BACKGROUND_CONCENTRATION,
        NSLMonitoring.GCN_EC: Aerius.EC_GCN_BACKGROUND_CONCENTRATION,
        NSLMonitoring.BG_C_NO2: None,
        NSLMonitoring.BG_C_O3: None,
        NSLMonitoring.BG_C_PM10: None,
        NSLMonitoring.BG_C_PM25: None,
        NSLMonitoring.AIR_NO2: None,
        NSLMonitoring.AIR_O3: None,
        NSLMonitoring.C_AIR_NO2: None,
        NSLMonitoring.C_AIR_O3: None,
        NSLMonitoring.C_HWN_NO2: None,
        NSLMonitoring.C_HWN_O3: None,
        NSLMonitoring.C_HWN_PM10: Aerius.NO2_GCN_MAIN_ROADS_CORRECTION,
        NSLMonitoring.C_HWN_PM25: Aerius.PM25_GCN_MAIN_ROADS_CORRECTION,
        NSLMonitoring.C_HWN_EC: Aerius.EC_GCN_MAIN_ROADS_CORRECTION,
        NSLMonitoring.ACHTG_NO2: Aerius.NO2_BACKGROUND_CONCENTRATION,
        NSLMonitoring.ACHTG_O3: Aerius.O3_BACKGROUND_CONCENTRATION,
        NSLMonitoring.ACHTG_PM10: Aerius.PM10_BACKGROUND_CONCENTRATION,
        NSLMonitoring.ACHTG_PM25: Aerius.PM25_BACKGROUND_CONCENTRATION,
        NSLMonitoring.ACHTG_EC: Aerius.EC_BACKGROUND_CONCENTRATION,
        NSLMonitoring.AACHT_NO2: None,
        NSLMonitoring.AACHT_O3: None,
        NSLMonitoring.AACHT_PM10: None,
        NSLMonitoring.AACHT_PM25: None,
        NSLMonitoring.GEOMET_WKT: Aerius.GEOMETRY,
    }


class ResultatenCompact(ShapeBuilder):
    """
    Builder for the `Resultaten Compact` shape.
    """

    HEADERS = {
        AeriusShape.CALC_P_ID: Aerius.CALCULATION_POINT_ID,
        AeriusShape.CALC_YEAR: Aerius.CALCULATION_YEAR,
        AeriusShape.AERIUS_V: Aerius.AERIUS_VERSION,
        AeriusShape.AERIUS_DBV: Aerius.AERIUS_DATABASE_VERSION,
        AeriusShape.GEOMETRY: Aerius.GEOMETRY,
        AeriusShape.NO2_TCON: Aerius.NO2_TOTAL_CONCENTRATION,
        AeriusShape.PM10_TCON: Aerius.PM10_TOTAL_CONCENTRATION,
        AeriusShape.PM25_TCON: Aerius.PM25_TOTAL_CONCENTRATION,
        AeriusShape.EC_TCON: Aerius.EC_TOTAL_CONCENTRATION,
        AeriusShape.NO2_EXC_H: Aerius.NO2_EXCEEDANCE_HOURS,
        AeriusShape.PM10_EXC_D: Aerius.PM10_EXCEEDANCE_DAYS,
        AeriusShape.NO2_BGC: Aerius.NO2_BACKGROUND_CONCENTRATION,
        AeriusShape.PM10_BGC: Aerius.PM10_BACKGROUND_CONCENTRATION,
        AeriusShape.PM25_BGC: Aerius.PM25_BACKGROUND_CONCENTRATION,
        AeriusShape.EC_BGC: Aerius.EC_BACKGROUND_CONCENTRATION,
        AeriusShape.R2_NO2COND: Aerius.NO2_SRM2_CONCENTRATION_DIRECT,
        AeriusShape.R2_PM10CON: Aerius.PM10_SRM2_CONCENTRATION,
        AeriusShape.R2_PM25CON: Aerius.PM25_SRM2_CONCENTRATION,
        AeriusShape.R2_ECCON: Aerius.EC_SRM2_CONCENTRATION,
        AeriusShape.R1_NO2COND: Aerius.NO2_SRM1_CONCENTRATION_DIRECT,
        AeriusShape.R1_PM10CON: Aerius.PM10_SRM1_CONCENTRATION,
        AeriusShape.R1_PM25CON: Aerius.PM25_SRM1_CONCENTRATION,
        AeriusShape.R1_ECCON: Aerius.EC_SRM1_CONCENTRATION,
    }


class ResultatenUitgebreid(ShapeBuilder):
    """
    Builder for the `Resultaten Uitgebreid` shape.
    """

    HEADERS = {
        **ResultatenCompact.HEADERS,  # Include the 'Compact' headers.
        AeriusShape.O3_BGC: Aerius.O3_BACKGROUND_CONCENTRATION,
        AeriusShape.R2_NOXCON: Aerius.NOX_SRM2_CONCENTRATION,
        AeriusShape.R1_NOXCON: Aerius.NOX_SRM1_CONCENTRATION,
        AeriusShape.NO2GCNMRC: Aerius.NO2_GCN_MAIN_ROADS_CORRECTION,
        AeriusShape.PM10GCNMRC: Aerius.PM10_GCN_MAIN_ROADS_CORRECTION,
        AeriusShape.PM25GCNMRC: Aerius.PM25_GCN_MAIN_ROADS_CORRECTION,
        AeriusShape.ECGCNMRC: Aerius.EC_GCN_MAIN_ROADS_CORRECTION,
    }
