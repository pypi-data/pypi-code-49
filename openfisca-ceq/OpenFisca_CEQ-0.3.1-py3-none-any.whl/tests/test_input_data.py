import pandas as pd
import pytest


import logging

from openfisca_ceq.tools.data import get_data_file_paths
from openfisca_ceq.tools.data import year_by_country


log = logging.getLogger(__name__)


@pytest.mark.parametrize("country, year", list(year_by_country.items()))
def test_household_id_coherence(country, year):
    expenditures_data_path, income_data_path = get_data_file_paths(country, year)
    expenditures = pd.read_stata(expenditures_data_path).astype({"prod_id": str})
    income = pd.read_stata(income_data_path)
    log.info(
        len(
            set(expenditures.hh_id).difference(set(income.hh_id))
            )
        )
    log.info(
        len(
            set(income.hh_id).difference(set(expenditures.hh_id))
            )
        )
    # BIM
    # Sénégal: keep only household from income
    # Mali: manque 165 ménages


if __name__ == "__main__":
    import sys
    logging.basicConfig(level = logging.INFO, stream = sys.stdout)
    country = "cote_d_ivoire"
    test_household_id_coherence(country, 2014)
