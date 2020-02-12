from ..utils import PropertiesFromEnumValue
from . import metrics_pb2
EMPTY_MONITORING_INFO_LABEL_PROPS = metrics_pb2.MonitoringInfoLabelProps()
EMPTY_MONITORING_INFO_SPEC = metrics_pb2.MonitoringInfoSpec()

class MonitoringInfo(object):

  class MonitoringInfoLabels(object):
    TRANSFORM = PropertiesFromEnumValue(u'', u'', EMPTY_MONITORING_INFO_SPEC, metrics_pb2.MonitoringInfoLabelProps(name=u'PTRANSFORM'))
    PCOLLECTION = PropertiesFromEnumValue(u'', u'', EMPTY_MONITORING_INFO_SPEC, metrics_pb2.MonitoringInfoLabelProps(name=u'PCOLLECTION'))
    WINDOWING_STRATEGY = PropertiesFromEnumValue(u'', u'', EMPTY_MONITORING_INFO_SPEC, metrics_pb2.MonitoringInfoLabelProps(name=u'WINDOWING_STRATEGY'))
    CODER = PropertiesFromEnumValue(u'', u'', EMPTY_MONITORING_INFO_SPEC, metrics_pb2.MonitoringInfoLabelProps(name=u'CODER'))
    ENVIRONMENT = PropertiesFromEnumValue(u'', u'', EMPTY_MONITORING_INFO_SPEC, metrics_pb2.MonitoringInfoLabelProps(name=u'ENVIRONMENT'))
    NAMESPACE = PropertiesFromEnumValue(u'', u'', EMPTY_MONITORING_INFO_SPEC, metrics_pb2.MonitoringInfoLabelProps(name=u'NAMESPACE'))
    NAME = PropertiesFromEnumValue(u'', u'', EMPTY_MONITORING_INFO_SPEC, metrics_pb2.MonitoringInfoLabelProps(name=u'NAME'))


class MonitoringInfoSpecs(object):

  class Enum(object):
    USER_COUNTER = PropertiesFromEnumValue(u'', u'', metrics_pb2.MonitoringInfoSpec(urn=u'beam:metric:user', type_urn=u'beam:metrics:sum_int_64', required_labels=[u'PTRANSFORM', u'NAMESPACE', u'NAME'], annotations=[metrics_pb2.Annotation(key=u'description', value=u'URN utilized to report user numeric counters.')]), EMPTY_MONITORING_INFO_LABEL_PROPS)
    ELEMENT_COUNT = PropertiesFromEnumValue(u'', u'', metrics_pb2.MonitoringInfoSpec(urn=u'beam:metric:element_count:v1', type_urn=u'beam:metrics:sum_int_64', required_labels=[u'PCOLLECTION'], annotations=[metrics_pb2.Annotation(key=u'description', value=u'The total elements output to a Pcollection by a PTransform.')]), EMPTY_MONITORING_INFO_LABEL_PROPS)
    SAMPLED_BYTE_SIZE = PropertiesFromEnumValue(u'', u'', metrics_pb2.MonitoringInfoSpec(urn=u'beam:metric:sampled_byte_size:v1', type_urn=u'beam:metrics:distribution_int_64', required_labels=[u'PCOLLECTION'], annotations=[metrics_pb2.Annotation(key=u'description', value=u'The total byte size and count of a sampled  set (or all) of elements in the pcollection. Sampling is used  because calculating the byte count involves serializing the  elements which is CPU intensive.')]), EMPTY_MONITORING_INFO_LABEL_PROPS)
    START_BUNDLE_MSECS = PropertiesFromEnumValue(u'', u'', metrics_pb2.MonitoringInfoSpec(urn=u'beam:metric:pardo_execution_time:start_bundle_msecs:v1', type_urn=u'beam:metrics:sum_int_64', required_labels=[u'PTRANSFORM'], annotations=[metrics_pb2.Annotation(key=u'description', value=u'The total estimated execution time of the start bundlefunction in a pardo')]), EMPTY_MONITORING_INFO_LABEL_PROPS)
    PROCESS_BUNDLE_MSECS = PropertiesFromEnumValue(u'', u'', metrics_pb2.MonitoringInfoSpec(urn=u'beam:metric:pardo_execution_time:process_bundle_msecs:v1', type_urn=u'beam:metrics:sum_int_64', required_labels=[u'PTRANSFORM'], annotations=[metrics_pb2.Annotation(key=u'description', value=u'The total estimated execution time of the process bundlefunction in a pardo')]), EMPTY_MONITORING_INFO_LABEL_PROPS)
    FINISH_BUNDLE_MSECS = PropertiesFromEnumValue(u'', u'', metrics_pb2.MonitoringInfoSpec(urn=u'beam:metric:pardo_execution_time:finish_bundle_msecs:v1', type_urn=u'beam:metrics:sum_int_64', required_labels=[u'PTRANSFORM'], annotations=[metrics_pb2.Annotation(key=u'description', value=u'The total estimated execution time of the finish bundle function in a pardo')]), EMPTY_MONITORING_INFO_LABEL_PROPS)
    TOTAL_MSECS = PropertiesFromEnumValue(u'', u'', metrics_pb2.MonitoringInfoSpec(urn=u'beam:metric:ptransform_execution_time:total_msecs:v1', type_urn=u'beam:metrics:sum_int_64', required_labels=[u'PTRANSFORM'], annotations=[metrics_pb2.Annotation(key=u'description', value=u'The total estimated execution time of the ptransform')]), EMPTY_MONITORING_INFO_LABEL_PROPS)
    USER_DISTRIBUTION_COUNTER = PropertiesFromEnumValue(u'', u'', metrics_pb2.MonitoringInfoSpec(urn=u'beam:metric:user_distribution', type_urn=u'beam:metrics:distribution_int_64', required_labels=[u'PTRANSFORM', u'NAMESPACE', u'NAME'], annotations=[metrics_pb2.Annotation(key=u'description', value=u'URN utilized to report user distribution counters.')]), EMPTY_MONITORING_INFO_LABEL_PROPS)


class MonitoringInfoTypeUrns(object):

  class Enum(object):
    SUM_INT64_TYPE = PropertiesFromEnumValue(u'beam:metrics:sum_int_64', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    DISTRIBUTION_INT64_TYPE = PropertiesFromEnumValue(u'beam:metrics:distribution_int_64', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    LATEST_INT64_TYPE = PropertiesFromEnumValue(u'beam:metrics:latest_int_64', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)

