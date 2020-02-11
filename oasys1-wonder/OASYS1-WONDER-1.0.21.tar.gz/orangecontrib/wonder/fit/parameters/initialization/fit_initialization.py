from orangecontrib.wonder.fit.parameters.fit_parameter import ParametersList

class FitInitialization(ParametersList):
    fft_parameters = None

    def __init__(self,
                 fft_parameters = None,):
        self.fft_parameters = fft_parameters

    def duplicate(self):
        fft_parameters = None if self.fft_parameters is None else self.fft_parameters.duplicate()

        return FitInitialization(fft_parameters=fft_parameters)
