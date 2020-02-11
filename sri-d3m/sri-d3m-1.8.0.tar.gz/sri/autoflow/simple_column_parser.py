import datetime
import typing

import dateutil.parser
import numpy  # type: ignore
from d3m.primitive_interfaces import unsupervised_learning as pi_unsupervised

from d3m import container, utils as d3m_utils
from d3m.base import utils as base_utils
from d3m.metadata import base as metadata_base, hyperparams as hyperparams_base
from d3m.metadata import params as meta_params
from d3m.primitive_interfaces import base, transformer
from d3m.primitive_interfaces import base as pi_base

from sri.common import config
from sri.common import constants as con

# __all__ = ('SimpleColumnParserPrimitive',)

DEFAULT_DATETIME = datetime.datetime.fromtimestamp(0, datetime.timezone.utc)

Inputs = container.DataFrame
Outputs = container.DataFrame


class Hyperparams(hyperparams_base.Hyperparams):
    parse_semantic_types = hyperparams_base.Set(
        elements=hyperparams_base.Enumeration(
            values=[con.BOOLEAN_TYPE, con.CATEGORICAL_TYPE, con.INTEGER_TYPE, con.FLOAT_TYPE, con.FLOAT_VECTOR_TYPE,
            con.DATE_TIME_TYPE],
            # Default is ignored.
            # TODO: Remove default. See: https://gitlab.com/datadrivendiscovery/d3m/issues/141
            default=con.BOOLEAN_TYPE
        ),
        default=(
            con.BOOLEAN_TYPE, con.CATEGORICAL_TYPE, con.INTEGER_TYPE, con.FLOAT_TYPE, con.FLOAT_VECTOR_TYPE,
            con.DATE_TIME_TYPE
        ),
        semantic_types=['https://metadata.datadrivendiscovery.org/types/ControlParameter'],
        description="A set of semantic types to parse. One can provide a subset of supported semantic types to limit what the primitive parses.",
    )
    use_columns = hyperparams_base.Set(
        elements=hyperparams_base.Hyperparameter[int](-1),
        default=(),
        semantic_types=['https://metadata.datadrivendiscovery.org/types/ControlParameter'],
        description="A set of column indices to force primitive to operate on. If any specified column cannot be parsed, it is skipped.",
    )
    exclude_columns = hyperparams_base.Set(
        elements=hyperparams_base.Hyperparameter[int](-1),
        default=(),
        semantic_types=['https://metadata.datadrivendiscovery.org/types/ControlParameter'],
        description="A set of column indices to not operate on. Applicable only if \"use_columns\" is not provided.",
    )
    return_result = hyperparams_base.Enumeration(
        values=['append', 'replace', 'new'],
        default='replace',
        semantic_types=['https://metadata.datadrivendiscovery.org/types/ControlParameter'],
        description="Should parsed columns be appended, should they replace original columns, or should only parsed columns be returned?",
    )
    add_index_columns = hyperparams_base.UniformBool(
        default=True,
        semantic_types=['https://metadata.datadrivendiscovery.org/types/ControlParameter'],
        description="Also include primary index columns if input data has them. Applicable only if \"return_result\" is set to \"new\".",
    )
    parse_categorical_target_columns = hyperparams_base.UniformBool(
        default=False,
        semantic_types=['https://metadata.datadrivendiscovery.org/types/ControlParameter'],
        description="Should it parse also categorical target columns?",
    )
    replace_index_columns = hyperparams_base.UniformBool(
        default=True,
        semantic_types=['https://metadata.datadrivendiscovery.org/types/ControlParameter'],
        description="Replace primary index columns even if otherwise appending columns. Applicable only if \"return_result\" is set to \"append\".",
    )


class SimpleColumnParserParams(meta_params.Params):
    column_map: typing.Dict[str, int]


class SimpleColumnParser(pi_unsupervised.UnsupervisedLearnerPrimitiveBase[Inputs, Outputs, SimpleColumnParserParams,
                                                                          Hyperparams]):
    """
    A primitive which parses strings into their parsed values. This primitive was adapted
    from Mitars ColumnParserPrimitive in the Common Primitives repo.

    It goes over all columns (by default, controlled by ``use_columns``, ``exclude_columns``)
    and checks those with structural type ``str`` if they have a semantic type suggesting
    that they are a boolean value, categorical, integer, float, or time (by default,
    controlled by ``parse_semantic_types``). Categorical values are converted to integer
    encodings.

    What is returned is controlled by ``return_result`` and ``add_index_columns``.
    """

    metadata = metadata_base.PrimitiveMetadata(
        {
            'id': 'd519cb7a-1782-4f51-b44c-58f0236e47c7',
            'version': config.VERSION,
            'name': "Parses strings into their types",
            'description': 'Adapted from Mitars Column Parser - this implementation turns categorical values into integers instead of hashes',
            'python_path': 'd3m.primitives.data_transformation.simple_column_parser.DataFrameCommon',
            'source': config.SOURCE,
            'installation':  [ config.INSTALLATION ],
            'algorithm_types': [
                metadata_base.PrimitiveAlgorithmType.DATA_CONVERSION,
            ],
            'primitive_family': metadata_base.PrimitiveFamily.DATA_TRANSFORMATION,
        },
    )

    def __init__(self, *, hyperparams: Hyperparams) -> None:
        super().__init__(hyperparams=hyperparams)
        self._fitted = False
        self._column_values_map = None
        self._training_inputs = None

    def get_params(self) -> SimpleColumnParserParams:
        return SimpleColumnParserParams(column_map=self._column_values_map)

    def set_params(self, *, params: SimpleColumnParserParams) -> None:
        self._column_values_map = params.column_map

    def set_training_data(self, *, inputs: Inputs) -> None:
        self._training_inputs = inputs
        self._fitted = False

    def fit(self, *, timeout: float = None, iterations: int = None) -> base.CallResult[None]:
        if not self._fitted:
            if self._training_inputs is None:
                raise ValueError('Missing training(fitting) data.')

            # Create the column parser mapping
            self._generate_values_map(self._training_inputs, self.hyperparams)

            self._fitted = True
        return base.CallResult(None)

    def produce(self, *, inputs: Inputs, timeout: float = None, iterations: int = None) -> base.CallResult[Outputs]:
        columns_to_use, output_columns = self._produce_columns(inputs, self.hyperparams)

        if self.hyperparams['replace_index_columns'] and self.hyperparams['return_result'] == 'append':
            assert len(columns_to_use) == len(output_columns)

            index_columns = inputs.metadata.get_index_columns()

            index_columns_to_use = []
            other_columns_to_use = []
            index_output_columns = []
            other_output_columns = []
            for column_to_use, output_column in zip(columns_to_use, output_columns):
                if column_to_use in index_columns:
                    index_columns_to_use.append(column_to_use)
                    index_output_columns.append(output_column)
                else:
                    other_columns_to_use.append(column_to_use)
                    other_output_columns.append(output_column)

            outputs = base_utils.combine_columns(inputs, index_columns_to_use, index_output_columns,
                                                 return_result='replace',
                                                 add_index_columns=self.hyperparams['add_index_columns'])
            outputs = base_utils.combine_columns(outputs, other_columns_to_use, other_output_columns,
                                                 return_result='append',
                                                 add_index_columns=self.hyperparams['add_index_columns'])
        else:
            outputs = base_utils.combine_columns(inputs, columns_to_use, output_columns,
                                                 return_result=self.hyperparams['return_result'],
                                                 add_index_columns=self.hyperparams['add_index_columns'])

        return base.CallResult(outputs)

    @classmethod
    def _can_use_column(cls, inputs_metadata: metadata_base.DataMetadata, column_index: int,
                        hyperparams: Hyperparams) -> bool:
        column_metadata = inputs_metadata.query((metadata_base.ALL_ELEMENTS, column_index))

        # We produce only on columns which have not yet been parsed (are strings).
        if column_metadata['structural_type'] != str:
            return False

        semantic_types = column_metadata.get('semantic_types', [])

        for semantic_type in hyperparams['parse_semantic_types']:
            if semantic_type not in semantic_types:
                continue

            if semantic_type == con.CATEGORICAL_TYPE:
                # Skip parsing if a column is categorical, but also a target column.
                if not hyperparams['parse_categorical_target_columns'] and con.TARGET_TYPE in semantic_types:
                    continue

            return True

        return False

    def _generate_values_map(self, inputs: Inputs, hyperparams: Hyperparams) -> None:
        # This method looks at all the types of data in the input and creates a map from those values to an integer.
        # This map is then persisted to ensure that future invocations result in the same mapping. The value 0 is
        # held in reserve to map unseen values to.

        # Processing updates this field
        self._column_values_map = {}

        columns_to_use = self._get_columns(inputs.metadata, hyperparams)
        # We check against this list again, because there might be multiple matching semantic types
        # (which is not really valid).
        parse_semantic_types = hyperparams['parse_semantic_types']

        for column_index in columns_to_use:
            mdata = inputs.metadata.query_column(column_index)
            semantic_types = mdata['semantic_types']
            cattype = con.CATEGORICAL_TYPE
            if mdata['structural_type'] == str:
                if con.BOOLEAN_TYPE in parse_semantic_types and con.BOOLEAN_TYPE in semantic_types:
                    self._generate_map_for_boolean_column(inputs, column_index)
                if cattype in parse_semantic_types and cattype in semantic_types:
                    if hyperparams['parse_categorical_target_columns'] or con.TARGET_TYPE not in semantic_types:
                        self._generate_map_for_column(inputs, column_index)

    def _generate_map_for_boolean_column(self, inputs, column_index):
        boolean_values = [
            ("0", "1"),
            ("n", "y"),
            ("no", "yes"),
            ("f", "t"),
            ("false", "true")
        ]
        values = tuple(set(v.strip() for v in inputs.iloc[:, column_index]))
        if len(values) == 2:
            for f, t in boolean_values:
                if values[0].lower() == f and values[1].lower() == t:
                    self._column_values_map[column_index] = {values[0]: 0, values[1]: 1}
                    return
                if values[0].lower() == t and values[1].lower() == f:
                    self._column_values_map[column_index] = {values[0]: 1, values[1]: 0}
                    return
        self._generate_map_for_column(inputs, column_index)

    def _generate_map_for_column(self, inputs: Inputs, column_index: int) -> None:
        values_map: typing.Dict[str, int] = {}
        for value in inputs.iloc[:, column_index]:
            value = value.strip()
            if value not in values_map:
                value_int = len(values_map) + 1
                values_map[value] = value_int
        self._column_values_map[column_index] = values_map

    def _produce_columns(self, inputs: Inputs,
                         hyperparams: Hyperparams) -> typing.Tuple[typing.List[int], typing.List[Outputs]]:
        # The logic of parsing values tries to mirror also the logic of detecting
        # values in "SimpleProfilerPrimitive". One should keep them in sync.

        columns_to_use = self._get_columns(inputs.metadata, hyperparams)

        # We check against this list again, because there might be multiple matching semantic types
        # (which is not really valid).
        parse_semantic_types = hyperparams['parse_semantic_types']

        output_columns = []

        for column_index in columns_to_use:
            column_metadata = inputs.metadata.query((metadata_base.ALL_ELEMENTS, column_index))
            semantic_types = column_metadata.get('semantic_types', [])

            def type_match(type_):
                return type_ in parse_semantic_types and type_ in semantic_types

            if column_metadata['structural_type'] == str:
                if type_match(con.BOOLEAN_TYPE):
                    output_columns.append(self._parse_boolean_data(inputs, column_index))

                elif type_match(con.CATEGORICAL_TYPE):
                    if hyperparams['parse_categorical_target_columns'] or con.TARGET_TYPE not in semantic_types:
                        output_columns.append(self._parse_categorical_data(inputs, column_index))

                elif type_match(con.INTEGER_TYPE):
                    if con.PRIMARY_KEY_TYPE in semantic_types:
                        integer_required = True
                    else:
                        integer_required = False

                    output_columns.append(self._parse_integer(inputs, column_index, integer_required))

                elif type_match(con.FLOAT_TYPE):
                    output_columns.append(self._parse_float_data(inputs, column_index))

                elif type_match(con.FLOAT_VECTOR_TYPE):
                    output_columns.append(self._parse_float_vector_data(inputs, column_index))

                elif type_match(con.DATE_TIME_TYPE):
                    output_columns.append(self._parse_time_data(inputs, column_index))

                else:
                    assert False, column_index

        assert len(output_columns) == len(columns_to_use)

        return columns_to_use, output_columns

    def _produce_columns_metadata(self, inputs_metadata: metadata_base.DataMetadata,
                                  hyperparams: Hyperparams) -> typing.Tuple[typing.List[int],
                                                                            typing.List[metadata_base.DataMetadata]]:
        columns_to_use = self._get_columns(inputs_metadata, hyperparams)

        # We check against this list again, because there might be multiple matching semantic types
        # (which is not really valid).
        parse_semantic_types = hyperparams['parse_semantic_types']

        output_columns = []

        for column_index in columns_to_use:
            column_metadata = inputs_metadata.query((metadata_base.ALL_ELEMENTS, column_index))
            semantic_types = column_metadata.get('semantic_types', [])

            def type_match(type_):
                return type_ in parse_semantic_types and type_ in semantic_types

            if column_metadata['structural_type'] == str:
                if type_match(con.BOOLEAN_TYPE):
                    output_columns.append(self._parse_boolean_metadata(inputs_metadata, column_index))

                elif type_match(con.CATEGORICAL_TYPE):
                    if hyperparams['parse_categorical_target_columns'] or con.TARGET_TYPE not in semantic_types:
                        output_columns.append(self._parse_categorical_metadata(inputs_metadata, column_index))

                elif type_match(con.INTEGER_TYPE):
                    output_columns.append(self._parse_integer_metadata(inputs_metadata, column_index))

                elif type_match(con.FLOAT_TYPE):
                    output_columns.append(self._parse_float_metadata(inputs_metadata, column_index))

                elif type_match(con.FLOAT_VECTOR_TYPE):
                    output_columns.append(self._parse_float_vector_metadata(inputs_metadata, column_index))

                elif type_match(con.DATE_TIME_TYPE):
                    output_columns.append(self._parse_time_metadata(inputs_metadata, column_index))

                else:
                    assert False, column_index

        assert len(output_columns) == len(columns_to_use)

        return columns_to_use, output_columns

    @classmethod
    def _get_columns(cls, inputs_metadata: metadata_base.DataMetadata, hyperparams: Hyperparams) -> typing.List[int]:

        def can_use_column(column_index: int) -> bool:
            return cls._can_use_column(inputs_metadata, column_index, hyperparams)

        columns_to_use, columns_not_to_use = base_utils.get_columns_to_use(inputs_metadata,
                                                                           hyperparams['use_columns'],
                                                                           hyperparams['exclude_columns'],
                                                                           can_use_column)

        # We are OK if no columns ended up being parsed.
        # "base_utils.combine_columns" will throw an error if it cannot work with this.

        if hyperparams['use_columns'] and columns_not_to_use:
            cls.logger.warning("Not all specified columns can parsed. Skipping columns: %(columns)s", {
                'columns': columns_not_to_use,
            })

        return columns_to_use

    def _parse_boolean_data(self, inputs: Inputs, column_index: metadata_base.SimpleSelectorSegment) -> Outputs:
        return self._parse_categorical_data(inputs, column_index)

    def _parse_boolean_metadata(self, inputs_metadata: metadata_base.DataMetadata,
                                column_index: metadata_base.SimpleSelectorSegment) -> metadata_base.DataMetadata:
        return self._parse_categorical_metadata(inputs_metadata, column_index)

    def _parse_categorical_data(self, inputs: Inputs, column_index: int) -> Outputs:
        # When we hit an unmapped value we can map it to 0 in the _map_values function
        column_values_map = self._column_values_map[column_index]

        def map_value(v):
            try:
                return column_values_map[v]
            except KeyError:
                return 0

        outputs = container.DataFrame({inputs.columns[column_index]:
                                           [map_value(value.strip()) for value in inputs.iloc[:, column_index]]},
                                      generate_metadata=False)
        outputs.metadata = self._parse_categorical_metadata(inputs.metadata, column_index)

        return outputs

    @classmethod
    def _parse_categorical_metadata(cls, inputs_metadata: metadata_base.DataMetadata,
                                    column_index: metadata_base.SimpleSelectorSegment) -> metadata_base.DataMetadata:
        outputs_metadata = inputs_metadata.select_columns([column_index])
        return outputs_metadata.update_column(0, {'structural_type': int})

    @classmethod
    def _str_to_int(cls, value: str) -> typing.Union[float, int]:
        try:
            return int(value.strip())
        except ValueError:
            try:
                # Maybe it is an int represented as a float. Let's try this. This can get rid of non-integer
                # part of the value, but the integer was requested through a semantic type, so this is probably OK.
                return int(float(value.strip()))
            except ValueError:
                # No luck, use NaN to represent a missing value.
                return float('nan')

    @classmethod
    def _parse_integer(cls, inputs: Inputs, column_index: metadata_base.SimpleSelectorSegment,
                       integer_required: bool) -> container.DataFrame:
        outputs = container.DataFrame({inputs.columns[column_index]:
                                           [cls._str_to_int(value) for value in inputs.iloc[:, column_index]]},
                                      generate_metadata=False)

        if outputs.dtypes.iloc[0].kind == 'f':
            structural_type: type = float
        elif outputs.dtypes.iloc[0].kind in ['i', 'u']:
            structural_type = int
        else:
            assert False, outputs.dtypes.iloc[0]

        if structural_type is float and integer_required:
            raise ValueError("Not all values in a column can be parsed into integers, but only integers were expected.")

        outputs.metadata = inputs.metadata.select_columns([column_index])
        outputs.metadata = outputs.metadata.update_column(0, {'structural_type': structural_type})

        return outputs

    @classmethod
    def _parse_integer_metadata(cls, inputs_metadata: metadata_base.DataMetadata,
                                column_index: metadata_base.SimpleSelectorSegment) -> metadata_base.DataMetadata:
        outputs_metadata = inputs_metadata.select_columns([column_index])
        # Without data we assume we can parse everything into integers. This might not be true and
        # we might end up parsing into floats if we have to represent missing (or invalid) values.
        return outputs_metadata.update_column(0, {'structural_type': int})

    @classmethod
    def _str_to_float(cls, value: str) -> float:
        try:
            return float(value.strip())
        except ValueError:
            return float('nan')

    @classmethod
    def _parse_float_data(cls, inputs: Inputs, column_index: metadata_base.SimpleSelectorSegment) -> Outputs:
        outputs = container.DataFrame({inputs.columns[column_index]:
                                           [cls._str_to_float(value) for value in inputs.iloc[:, column_index]]},
                                      generate_metadata=False)
        outputs.metadata = cls._parse_float_metadata(inputs.metadata, column_index)

        return outputs

    @classmethod
    def _parse_float_metadata(cls, inputs_metadata: metadata_base.DataMetadata,
                              column_index: metadata_base.SimpleSelectorSegment) -> metadata_base.DataMetadata:
        outputs_metadata = inputs_metadata.select_columns([column_index])
        return outputs_metadata.update_column(0, {'structural_type': float})

    @classmethod
    def _parse_float_vector_data(cls, inputs: Inputs, column_index: metadata_base.SimpleSelectorSegment) -> Outputs:
        # We are pretty strict here because we are assuming this was generated programmatically.
        outputs = container.DataFrame(
            {
                inputs.columns[column_index]: [
                    container.ndarray([cls._str_to_float(value) for value in values.split(',')])
                    for values in inputs.iloc[:, column_index]
                ],
            },
            generate_metadata=False,
        )
        outputs.metadata = cls._parse_float_metadata(inputs.metadata, column_index)
        # We have to automatically generate metadata to set ndarray dimension(s).
        outputs.metadata = outputs.metadata.generate(outputs)

        return outputs

    @classmethod
    def _parse_float_vector_metadata(cls, inputs_metadata: metadata_base.DataMetadata,
                                     column_index: metadata_base.SimpleSelectorSegment) -> metadata_base.DataMetadata:
        outputs_metadata = inputs_metadata.select_columns([column_index])
        # We cannot know the dimension of the ndarray without data.
        outputs_metadata = outputs_metadata.update_column(0, {'structural_type': container.ndarray})
        outputs_metadata = outputs_metadata.update((metadata_base.ALL_ELEMENTS, 0, metadata_base.ALL_ELEMENTS),
                                                   {'structural_type': numpy.float64})
        return outputs_metadata

    @classmethod
    def _time_to_foat(cls, value: str) -> float:
        try:
            return dateutil.parser.parse(value, default=DEFAULT_DATETIME, fuzzy=True).timestamp()
        except (ValueError, OverflowError):
            return float('nan')

    @classmethod
    def _parse_time_data(cls, inputs: Inputs, column_index: metadata_base.SimpleSelectorSegment) -> Outputs:
        outputs = container.DataFrame({inputs.columns[column_index]:
                                           [cls._time_to_foat(value) for value in inputs.iloc[:, column_index]]},
                                      generate_metadata=False)
        outputs.metadata = cls._parse_time_metadata(inputs.metadata, column_index)

        return outputs

    @classmethod
    def _parse_time_metadata(cls, inputs_metadata: metadata_base.DataMetadata,
                             column_index: metadata_base.SimpleSelectorSegment) -> metadata_base.DataMetadata:
        outputs_metadata = inputs_metadata.select_columns([column_index])
        return outputs_metadata.update_column(0, {'structural_type': float})

    @classmethod
    def can_accept(cls, *, method_name: str, arguments: typing.Dict[str, typing.Union[metadata_base.Metadata, type]],
                   hyperparams: Hyperparams) -> typing.Optional[metadata_base.DataMetadata]:
        output_metadata = super().can_accept(method_name=method_name, arguments=arguments, hyperparams=hyperparams)

        # If structural types didn't match, don't bother.
        if output_metadata is None:
            return None

        if method_name != 'produce':
            return output_metadata

        if 'inputs' not in arguments:
            return output_metadata

        inputs_metadata = typing.cast(metadata_base.DataMetadata, arguments['inputs'])

        columns_to_use, output_columns = cls._produce_columns_metadata(inputs_metadata, hyperparams)

        # We are stricter here than "produce" because we are not really useful.
        if not columns_to_use:
            return None

        if hyperparams['replace_index_columns'] and hyperparams['return_result'] == 'append':
            assert len(columns_to_use) == len(output_columns)

            index_columns = inputs_metadata.get_index_columns()

            index_columns_to_use = []
            other_columns_to_use = []
            index_output_columns = []
            other_output_columns = []
            for column_to_use, output_column in zip(columns_to_use, output_columns):
                if column_to_use in index_columns:
                    index_columns_to_use.append(column_to_use)
                    index_output_columns.append(output_column)
                else:
                    other_columns_to_use.append(column_to_use)
                    other_output_columns.append(output_column)

            outputs_metadata = base_utils.combine_columns_metadata(
                inputs_metadata, index_columns_to_use, index_output_columns,
                return_result='replace', add_index_columns=hyperparams['add_index_columns'],
            )
            return base_utils.combine_columns_metadata(
                outputs_metadata, other_columns_to_use, other_output_columns,
                return_result='append', add_index_columns=hyperparams['add_index_columns'],
            )
        else:
            return base_utils.combine_columns_metadata(
                inputs_metadata, columns_to_use, output_columns,
                return_result=hyperparams['return_result'], add_index_columns=hyperparams['add_index_columns'],
            )
