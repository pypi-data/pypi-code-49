import logging


from openfisca_ceq import CountryTaxBenefitSystem as CEQTaxBenefitSystem
from openfisca_ceq.tools.indirect_taxation.tax_benefit_system_indirect_taxation_completion import (
    add_coicop_item_to_tax_benefit_system
    )


log = logging.getLogger(__name__)


def main():
    country = "senegal"
    tax_benefit_system = CEQTaxBenefitSystem()
    add_coicop_item_to_tax_benefit_system(tax_benefit_system, country)
    for variable_name in sorted(tax_benefit_system.variables.keys()):
        log.info(
            "{} : {}".format(
                variable_name,
                tax_benefit_system.variables[variable_name].label
                )
            )


if __name__ == '__main__':
    import sys
    logging.basicConfig(level = logging.INFO, stream = sys.stdout)
    main()
