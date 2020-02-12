from ..utils import PropertiesFromEnumValue
from . import metrics_pb2
EMPTY_MONITORING_INFO_LABEL_PROPS = metrics_pb2.MonitoringInfoLabelProps()
EMPTY_MONITORING_INFO_SPEC = metrics_pb2.MonitoringInfoSpec()

class AccumulationMode(object):

  class Enum(object):
    UNSPECIFIED = PropertiesFromEnumValue(u'', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    DISCARDING = PropertiesFromEnumValue(u'', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    ACCUMULATING = PropertiesFromEnumValue(u'', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    RETRACTING = PropertiesFromEnumValue(u'', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)


class BeamConstants(object):

  class Constants(object):
    MIN_TIMESTAMP_MILLIS = PropertiesFromEnumValue(u'', u'-9223372036854775', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    MAX_TIMESTAMP_MILLIS = PropertiesFromEnumValue(u'', u'9223372036854775', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    GLOBAL_WINDOW_MAX_TIMESTAMP_MILLIS = PropertiesFromEnumValue(u'', u'9223371950454775', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)


class ClosingBehavior(object):

  class Enum(object):
    UNSPECIFIED = PropertiesFromEnumValue(u'', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    EMIT_ALWAYS = PropertiesFromEnumValue(u'', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    EMIT_IF_NONEMPTY = PropertiesFromEnumValue(u'', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)


class DisplayData(object):

  class Type(object):

    class Enum(object):
      UNSPECIFIED = PropertiesFromEnumValue(u'', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
      STRING = PropertiesFromEnumValue(u'', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
      INTEGER = PropertiesFromEnumValue(u'', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
      FLOAT = PropertiesFromEnumValue(u'', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
      BOOLEAN = PropertiesFromEnumValue(u'', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
      TIMESTAMP = PropertiesFromEnumValue(u'', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
      DURATION = PropertiesFromEnumValue(u'', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
      JAVA_CLASS = PropertiesFromEnumValue(u'', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)


class IsBounded(object):

  class Enum(object):
    UNSPECIFIED = PropertiesFromEnumValue(u'', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    UNBOUNDED = PropertiesFromEnumValue(u'', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    BOUNDED = PropertiesFromEnumValue(u'', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)


class MergeStatus(object):

  class Enum(object):
    UNSPECIFIED = PropertiesFromEnumValue(u'', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    NON_MERGING = PropertiesFromEnumValue(u'', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    NEEDS_MERGE = PropertiesFromEnumValue(u'', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    ALREADY_MERGED = PropertiesFromEnumValue(u'', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)


class OnTimeBehavior(object):

  class Enum(object):
    UNSPECIFIED = PropertiesFromEnumValue(u'', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    FIRE_ALWAYS = PropertiesFromEnumValue(u'', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    FIRE_IF_NONEMPTY = PropertiesFromEnumValue(u'', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)


class OutputTime(object):

  class Enum(object):
    UNSPECIFIED = PropertiesFromEnumValue(u'', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    END_OF_WINDOW = PropertiesFromEnumValue(u'', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    LATEST_IN_PANE = PropertiesFromEnumValue(u'', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    EARLIEST_IN_PANE = PropertiesFromEnumValue(u'', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)


class Parameter(object):

  class Type(object):

    class Enum(object):
      UNSPECIFIED = PropertiesFromEnumValue(u'', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
      WINDOW = PropertiesFromEnumValue(u'', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
      PIPELINE_OPTIONS = PropertiesFromEnumValue(u'', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
      RESTRICTION_TRACKER = PropertiesFromEnumValue(u'', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)


class StandardCoders(object):

  class Enum(object):
    BYTES = PropertiesFromEnumValue(u'beam:coder:bytes:v1', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    STRING_UTF8 = PropertiesFromEnumValue(u'beam:coder:string_utf8:v1', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    KV = PropertiesFromEnumValue(u'beam:coder:kv:v1', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    BOOL = PropertiesFromEnumValue(u'beam:coder:bool:v1', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    VARINT = PropertiesFromEnumValue(u'beam:coder:varint:v1', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    DOUBLE = PropertiesFromEnumValue(u'beam:coder:double:v1', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    ITERABLE = PropertiesFromEnumValue(u'beam:coder:iterable:v1', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    TIMER = PropertiesFromEnumValue(u'beam:coder:timer:v1', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    INTERVAL_WINDOW = PropertiesFromEnumValue(u'beam:coder:interval_window:v1', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    LENGTH_PREFIX = PropertiesFromEnumValue(u'beam:coder:length_prefix:v1', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    GLOBAL_WINDOW = PropertiesFromEnumValue(u'beam:coder:global_window:v1', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    WINDOWED_VALUE = PropertiesFromEnumValue(u'beam:coder:windowed_value:v1', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    PARAM_WINDOWED_VALUE = PropertiesFromEnumValue(u'beam:coder:param_windowed_value:v1', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    STATE_BACKED_ITERABLE = PropertiesFromEnumValue(u'beam:coder:state_backed_iterable:v1', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    ROW = PropertiesFromEnumValue(u'beam:coder:row:v1', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)


class StandardEnvironments(object):

  class Environments(object):
    DOCKER = PropertiesFromEnumValue(u'beam:env:docker:v1', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    PROCESS = PropertiesFromEnumValue(u'beam:env:process:v1', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    EXTERNAL = PropertiesFromEnumValue(u'beam:env:external:v1', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)


class StandardPTransforms(object):

  class CombineComponents(object):
    COMBINE_PER_KEY_PRECOMBINE = PropertiesFromEnumValue(u'beam:transform:combine_per_key_precombine:v1', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    COMBINE_PER_KEY_MERGE_ACCUMULATORS = PropertiesFromEnumValue(u'beam:transform:combine_per_key_merge_accumulators:v1', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    COMBINE_PER_KEY_EXTRACT_OUTPUTS = PropertiesFromEnumValue(u'beam:transform:combine_per_key_extract_outputs:v1', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    COMBINE_GROUPED_VALUES = PropertiesFromEnumValue(u'beam:transform:combine_grouped_values:v1', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)


  class Composites(object):
    COMBINE_PER_KEY = PropertiesFromEnumValue(u'beam:transform:combine_per_key:v1', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    COMBINE_GLOBALLY = PropertiesFromEnumValue(u'beam:transform:combine_globally:v1', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    RESHUFFLE = PropertiesFromEnumValue(u'beam:transform:reshuffle:v1', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    WRITE_FILES = PropertiesFromEnumValue(u'beam:transform:write_files:v1', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)


  class DeprecatedPrimitives(object):
    READ = PropertiesFromEnumValue(u'beam:transform:read:v1', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    CREATE_VIEW = PropertiesFromEnumValue(u'beam:transform:create_view:v1', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)


  class Primitives(object):
    PAR_DO = PropertiesFromEnumValue(u'beam:transform:pardo:v1', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    FLATTEN = PropertiesFromEnumValue(u'beam:transform:flatten:v1', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    GROUP_BY_KEY = PropertiesFromEnumValue(u'beam:transform:group_by_key:v1', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    IMPULSE = PropertiesFromEnumValue(u'beam:transform:impulse:v1', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    ASSIGN_WINDOWS = PropertiesFromEnumValue(u'beam:transform:window_into:v1', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    TEST_STREAM = PropertiesFromEnumValue(u'beam:transform:teststream:v1', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    MAP_WINDOWS = PropertiesFromEnumValue(u'beam:transform:map_windows:v1', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    MERGE_WINDOWS = PropertiesFromEnumValue(u'beam:transform:merge_windows:v1', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)


  class SplittableParDoComponents(object):
    PAIR_WITH_RESTRICTION = PropertiesFromEnumValue(u'beam:transform:sdf_pair_with_restriction:v1', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    SPLIT_RESTRICTION = PropertiesFromEnumValue(u'beam:transform:sdf_split_restriction:v1', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    PROCESS_KEYED_ELEMENTS = PropertiesFromEnumValue(u'beam:transform:sdf_process_keyed_elements:v1', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    PROCESS_ELEMENTS = PropertiesFromEnumValue(u'beam:transform:sdf_process_elements:v1', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    SPLIT_AND_SIZE_RESTRICTIONS = PropertiesFromEnumValue(u'beam:transform:sdf_split_and_size_restrictions:v1', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    PROCESS_SIZED_ELEMENTS_AND_RESTRICTIONS = PropertiesFromEnumValue(u'beam:transform:sdf_process_sized_element_and_restrictions:v1', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)


class StandardSideInputTypes(object):

  class Enum(object):
    ITERABLE = PropertiesFromEnumValue(u'beam:side_input:iterable:v1', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    MULTIMAP = PropertiesFromEnumValue(u'beam:side_input:multimap:v1', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)


class TimeDomain(object):

  class Enum(object):
    UNSPECIFIED = PropertiesFromEnumValue(u'', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    EVENT_TIME = PropertiesFromEnumValue(u'', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    PROCESSING_TIME = PropertiesFromEnumValue(u'', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)
    SYNCHRONIZED_PROCESSING_TIME = PropertiesFromEnumValue(u'', u'', EMPTY_MONITORING_INFO_SPEC, EMPTY_MONITORING_INFO_LABEL_PROPS)

