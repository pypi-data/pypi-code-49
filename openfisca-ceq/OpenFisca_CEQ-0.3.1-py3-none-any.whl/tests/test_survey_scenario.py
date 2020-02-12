import logging
import pytest


from openfisca_ceq.tools.data import year_by_country
from openfisca_ceq.tools.survey_scenario import build_ceq_survey_scenario


log = logging.getLogger(__name__)


@pytest.mark.parametrize("country, year", list(year_by_country.items()))
def test(country, year):
    survey_scenario = build_ceq_survey_scenario(legislation_country = country, year = year)
    assert survey_scenario is not None
