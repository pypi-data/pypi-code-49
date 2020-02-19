import logging
import pytest


from openfisca_ceq.tools.data import year_by_country
from openfisca_ceq.tools.survey_scenario import build_ceq_survey_scenario


log = logging.getLogger(__name__)


@pytest.mark.parametrize("country, year", list(year_by_country.items()))
def test(country, year):
    survey_scenario = build_ceq_survey_scenario(legislation_country = country, year = year)
    assert survey_scenario is not None


if __name__ == '__main__':
    import sys
    logging.basicConfig(level = logging.INFO, stream = sys.stdout)
    country = "senegal"

    year = year_by_country[country]
    survey_scenario = build_ceq_survey_scenario(legislation_country = country, year = year)

    assert not survey_scenario.tax_benefit_system.variables['eleve_enseignement_niveau'].is_neutralized
    log.info("Counts (in millions)")
    log.info((survey_scenario.compute_pivot_table(columns = 'eleve_enseignement_niveau', aggfunc = 'count', period = survey_scenario.year) / 1e6).round(1))
    variables = [
        'pre_school_person',
        'pre_school',
        'primary_education_person',
        'primary_education',
        'secondary_education_person',
        'secondary_education',
        'tertiary_education_person',
        'tertiary_education',
        'education_net_transfers',
        ]
    for variable in variables:
        log.info(
            "{variable}: {aggregate} billions FCFA".format(
                variable = variable,
                aggregate = int(round(survey_scenario.compute_aggregate(variable, period = survey_scenario.year) / 1e9))
                )
            )
