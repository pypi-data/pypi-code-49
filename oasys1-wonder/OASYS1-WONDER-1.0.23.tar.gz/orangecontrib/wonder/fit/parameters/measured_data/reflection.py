import numpy

from orangecontrib.wonder.fit.parameters.fit_parameter import PARAM_HWMAX, PARAM_HWMIN

class Reflection():

    h = 0
    k = 0
    l = 0

    d_spacing = 0.0

    intensity = None

    def __init__(self, h, k, l, intensity):
        self.h = h
        self.k = k
        self.l = l

        self.intensity = intensity

    @classmethod
    def get_parameters_prefix(cls):
        return "reflection_"

    def to_text(self):
        return str(self.h) + ", " + str(self.k) + ", " + str(self.l) + ", "  + str(self.intensity)

    def to_row(self):
        text = str(self.h) + ", " + str(self.k) + ", " + str(self.l) + ", " + self.intensity.parameter_name + " "

        if self.intensity.function:
            text += ":= " + str(self.intensity.function_value)
        else:
            text += str(self.intensity.value)

            if self.intensity.fixed:
                text += "fixed"
            elif not self.intensity.boundary is None:
                if not self.intensity.boundary.min_value == PARAM_HWMIN:
                    text += ", min " + str(self.intensity.boundary.min_value)

                if not self.intensity.boundary.max_value == PARAM_HWMAX:
                    text += ", max " + str(self.intensity.boundary.max_value)

        return text

    def get_theta_hkl(self, wavelength):
        return numpy.degrees(numpy.asin(2*self.d_spacing/wavelength))

    def get_q_hkl(self, wavelength):
        return 8*numpy.pi*self.d_spacing/(wavelength**2)

    def get_s_hkl(self, wavelength):
        return self.get_q_hkl(wavelength)/(2*numpy.pi)
