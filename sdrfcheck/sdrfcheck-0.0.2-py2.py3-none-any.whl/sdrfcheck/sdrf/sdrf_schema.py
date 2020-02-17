import logging
import pandas as pd
import typing
from typing import Any

from ebi.ols.api.client import OlsClient
from pandas_schema import Column, Schema, ValidationWarning
from pandas_schema.validation import LeadingWhitespaceValidation, TrailingWhitespaceValidation, _SeriesValidation

from sdrfcheck.sdrf import sdrf
from sdrfcheck.sdrf.exceptions import LogicError

client = OlsClient()


def check_minimum_columns(panda_sdrf=None, minimun_columns: int = 0):
    return len(panda_sdrf.get_sdrf_columns()) < minimun_columns


class SDRFColumn(Column):

    def __init__(self, name: str, validations: typing.Iterable['validation._BaseValidation'] = [], allow_empty=False,
                 optional_type=True):
        super().__init__(name, validations, allow_empty)
        self._optional = optional_type


class OntologyTerm(_SeriesValidation):
    """
    Checks that there is no leading whitespace in this column
    """

    def __init__(self, ontology_name: str = None, **kwargs):
        super().__init__(**kwargs)
        self._ontology_name = ontology_name

    @property
    def default_message(self):
        return "the term name or title can't be found in the ontology -- {}".format(self._ontology_name)

    def validate(self, series: pd.Series) -> pd.Series:
        terms = series.unique()
        labels = []
        for term in terms:
            ontology_terms = client.search(ontology=self._ontology_name, query=term, exact="true")
            if ontology_terms is not None:
                query_labels = [o._data['label'].lower() for o in ontology_terms.data._data]
                for label in query_labels:
                    labels.append(label)
        return series.isin(labels)


class SDRFSchema(Schema):

    def __init__(self, columns: typing.Iterable[SDRFColumn], ordered: bool = False, min_columns: int = 0):
        super().__init__(columns, ordered)
        self._min_columns = min_columns

    def __new__(cls, ordered: bool = False, min_columns: int = 0) -> Any:
        obj = super().__new__(cls)
        obj._min_columns = min_columns
        return obj

    def validate(self, panda_sdrf: sdrf = None) -> typing.List[LogicError]:
        errors = []

        # Check minimum number of columns
        if check_minimum_columns(panda_sdrf, self._min_columns):
            error_message = 'The number of columns in the SDRF ({}) is smaller than the number of mandatory fields ({})'.format(
                len(panda_sdrf.get_sdrf_columns()), self._min_columns)
            errors.append(LogicError(error_message, error_type=logging.WARN))

        # Check the mandatory fields
        error_mandatory = self.validate_mandatory_columns(panda_sdrf)
        if error_mandatory is not None:
            errors.append(error_mandatory)

        # Check that the term is present in ontology
        error_ontology_terms = self.validate_columns(panda_sdrf)
        if error_ontology_terms is not None:
            for error in error_ontology_terms:
                errors.append(error)

        return errors

    def validate_mandatory_columns(self, panda_sdrf):
        error_mandatory = []
        for column in self.columns:
            if column._optional == False and column.name not in panda_sdrf.get_sdrf_columns():
                error_mandatory.append(column.name)
        if len(error_mandatory):
            error_message = 'The following columns are mandatory and not present in the SDRF: {}'.format(
                ",".join(error_mandatory))
            return LogicError(error_message, error_type=logging.ERROR)
        return None

    def validate_columns(self, panda_sdrf):
        # Iterate over each pair of schema columns and data frame series and run validations
        column_pairs = []
        columns_to_pair = self.columns
        errors = []

        for column in columns_to_pair:
            column_pairs.append((panda_sdrf[column.name], column))

        for series, column in column_pairs:
            errors += column.validate(series)
        return sorted(errors, key=lambda e: e.row)


minimum_schema = SDRFSchema([
    SDRFColumn('source name', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()],
               allow_empty=True,
               optional_type=False),
    SDRFColumn('characteristics[organism part]', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()],
               allow_empty=True,
               optional_type=False),
    SDRFColumn('characteristics[disease]', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()],
               allow_empty=True,
               optional_type=False),
    SDRFColumn('characteristics[organism]',
               [LeadingWhitespaceValidation(), TrailingWhitespaceValidation(), OntologyTerm("ncbitaxon")],
               allow_empty=True,
               optional_type=False),
    # SDRFColumn('characteristics[cell type]', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()],
    #            allow_empty=True,
    #            optional_type=False),
    # SDRFColumn('comment[fraction identifier]', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()],
    #            allow_empty=True,
    #            optional_type=False),
    SDRFColumn('comment[data file]', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()],
               allow_empty=True,
               optional_type=False)

],
    min_columns=7)

human_schema = SDRFSchema([
    Column('source name', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()]),
    Column('characteristics[organism part]', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()]),
    Column('characteristics[disease]', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()])
])
