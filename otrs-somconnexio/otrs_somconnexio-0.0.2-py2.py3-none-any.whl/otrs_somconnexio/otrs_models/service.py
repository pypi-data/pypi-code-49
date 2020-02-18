ADSL_SERVICES = ['ADSL', 'ADSL+100min', 'ADSL+1000min']
FIBRE_SERVICES = ['Fibra']
NO_COVERAGE_VALUES = ['NoServei', 'NoFibra', 'fibraIndirecta', 'NoFibraVdf']


class Service():

    def __init__(self, otrs_response):
        self.response = otrs_response

    def _is_adsl(self):
        return self.response.dynamic_field_get('TecDelServei').value in ADSL_SERVICES

    def _is_fibre(self):
        return self.response.dynamic_field_get('TecDelServei').value in FIBRE_SERVICES

    def _has_adsl_coverage(self):
        return self._is_adsl() and self.response.dynamic_field_get('coberturaADSL').value \
            and self.response.dynamic_field_get('coberturaADSL').value not in NO_COVERAGE_VALUES

    def _has_fibre_coverage(self):
        return self._is_fibre() and (self._fibre_MM_coverage() or self._fibre_Vdf_coverage())

    def _fibre_MM_coverage(self):
        return self.response.dynamic_field_get('coberturaFibraMM').value \
            and self.response.dynamic_field_get('coberturaFibraMM').value not in NO_COVERAGE_VALUES

    def _fibre_Vdf_coverage(self):
        return self.response.dynamic_field_get('coberturaFibraVdf').value \
            and self.response.dynamic_field_get('coberturaFibraVdf').value not in NO_COVERAGE_VALUES

    def has_coverage(self):
        return self._has_adsl_coverage() or self._has_fibre_coverage()
