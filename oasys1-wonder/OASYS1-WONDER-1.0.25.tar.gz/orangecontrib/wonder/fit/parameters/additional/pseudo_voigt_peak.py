import numpy

from orangecontrib.wonder.fit.parameters.fit_parameter import ParametersList, FitParameter, Boundary, PARAM_HWMAX, PARAM_HWMIN
from oasys.widgets import congruence


class SpuriousPeaks(ParametersList):
    def __init__(self, number_of_peaks=1):
        self.pseudo_voigt_peaks = [] * number_of_peaks

    def parse_peaks(self, text, diffraction_pattern_index=0):
        try:
            congruence.checkEmptyString(text, "Reflections")
            empty = False
        except:
            empty = True

        pseudo_voigt_peaks = []

        if not empty:
            lines = text.splitlines()

            for line_index in range(len(lines)):
                pseudo_voigt_peak = PseudoVoigtPeak.parse_peak(line=lines[line_index],
                                                               line_index=line_index,
                                                               diffraction_pattern_index=diffraction_pattern_index)

                if not pseudo_voigt_peak is None: pseudo_voigt_peaks.append(pseudo_voigt_peak)

        self.pseudo_voigt_peaks = pseudo_voigt_peaks

    def get_pseudo_voigt_peaks_number(self):
        return len(self.pseudo_voigt_peaks)

    def get_pseudo_voigt_peak(self, peak_index):
        return self.pseudo_voigt_peaks[peak_index]

    def get_pseudo_voigt_peaks(self):
        return numpy.array(self.pseudo_voigt_peaks)

class PseudoVoigtPeak():
    @classmethod
    def get_parameters_prefix(cls):
        return "pv_"

    def __init__(self, twotheta_0=None, eta=None, fwhm=None, intensity=None):
        self.twotheta_0 = twotheta_0
        self.eta = eta
        self.fwhm = fwhm
        self.intensity = intensity

    def __str__(self):
        return "--" if self.twotheta_0 is None else str(self.twotheta_0.value) + ", " + \
               "--" if self.eta is None else str(self.eta.value) + ", " + \
               "--" if self.fwhm is None else str(self.fwhm.value) + ", " + \
               "--" if self.intensity is None else str(self.intensity.value)

    def get_pseudo_voigt_peak(self, twotheta):
        tths = (2 * (twotheta - self.twotheta_0.value) / self.fwhm.value) ** 2
        pis = numpy.pi * self.fwhm.value / 2

        lorentzian = 1 / (pis * (1 + tths))
        gaussian = numpy.sqrt(numpy.pi * numpy.log(2)) * numpy.exp(-numpy.log(2) * tths) / pis

        return self.intensity.value * (((1 - self.eta.value) * gaussian) + (self.eta.value * lorentzian))

    @classmethod
    def parse_peak(cls, line, line_index=0, diffraction_pattern_index=0):
        try:
            congruence.checkEmptyString(line, "Pseudo-Voigt Peak")
        except:
            return None

        if line.strip().startswith("#"):
            return None
        else:
            parameter_prefix = PseudoVoigtPeak.get_parameters_prefix() + str(diffraction_pattern_index + 1) + "_"

            line_id = "(d.p. " + str(diffraction_pattern_index+1) +", line " + str(line_index+1) + ")"

            psuedo_voigt_peak = PseudoVoigtPeak()

            data = line.strip().split(",")

            if len(data) < 4: raise ValueError("Pseudo-Voigt Peak, malformed line: " + str(line_index+1))

            twotheta_0 = float(data[0].strip())
            eta = float(data[1].strip())
            fwhm = float(data[2].strip())
            intensity = float(data[3].strip())

            congruence.checkStrictlyPositiveAngle(twotheta_0, "2\u03b80 " + line_id)
            if not 0.0 < eta < 1.0: raise ValueError("\u03b7 " + line_id + " must be between 0 and 1")
            congruence.checkStrictlyPositiveNumber(fwhm, "fwhm " + line_id)
            congruence.checkStrictlyPositiveNumber(intensity, "intensity " + line_id)

            psuedo_voigt_peak.twotheta_0 = FitParameter(value=twotheta_0, parameter_name=parameter_prefix + "twotheta0", boundary=Boundary(min_value=0.0))
            psuedo_voigt_peak.eta        = FitParameter(value=eta,        parameter_name=parameter_prefix + "eta", boundary=Boundary(min_value=0.0, max_value=1.0))
            psuedo_voigt_peak.fwhm       = FitParameter(value=fwhm,       parameter_name=parameter_prefix + "fwhm", boundary=Boundary(min_value=0.0))
            psuedo_voigt_peak.intensity  = FitParameter(value=intensity,  parameter_name=parameter_prefix + "intensity", boundary=Boundary(min_value=0.0))

            return psuedo_voigt_peak
