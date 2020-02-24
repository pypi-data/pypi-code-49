from optimeed.core.collection import Collection
from optimeed.core import Option_class
from optimeed.core.tools import getPath_workspace, rsetattr, rgetattr, text_format, indentParagraph
import copy
from multiprocessing import Pool, cpu_count
from abc import abstractmethod
import numpy as np


class Parametric_Collection(Collection):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # def __str__(self):
    #     return super().__str__() +\
    #            text_format.DARKCYAN + '\nSWEEP PARAMETER:\n' + text_format.END +\
    #            indentParagraph(str(self.analysed_attribute), 1) +\
    #            text_format.DARKCYAN + '\nBASE DATA:\n' + text_format.END + indentParagraph(str(self.reference_data), 1)

    @staticmethod
    def get_extension():
        return '.colp'


class Parametric_parameter:
    """Abstract class for a parametric parameter"""

    def __init__(self, analyzed_attribute, reference_device):
        """
        :param analyzed_attribute: Analyzed attribute of the device
        :param reference_device: reference device
        """
        self.analyzed_attribute = analyzed_attribute
        self.reference_device = reference_device

    @abstractmethod
    def get_values(self):
        pass

    def get_reference_device(self):
        return self.reference_device

    def get_analyzed_attribute(self):
        return self.analyzed_attribute


class Parametric_minmax(Parametric_parameter):
    def __init__(self, analyzed_attribute, reference_device, minValue, maxValue, is_adim=False, npoints=10):
        """
        Parametric between boundaries min and max.
        :param minValue: Minimum value to use
        :param maxValue: Maximum value to use
        :param is_adim: if values are adim: multiplication factor based on current reference attribute value
        :param npoints: number of points to evaluate between range
        """
        super().__init__(analyzed_attribute, reference_device)
        self.is_adim = is_adim
        self.values = np.linspace(minValue, maxValue, npoints)

    def get_values(self):
        values = self.values
        if self.is_adim:
            for i in range(len(values)):
                values[i] *= rgetattr(self.get_reference_device(), self.get_analyzed_attribute())
        return self.values


class Parametric_analysis(Option_class):
    NUMBER_OF_CORES = 1

    def __init__(self, theParametricParameter, theCharacterization, filename_collection=None, description_collection=None, autosave=False):
        super().__init__()
        if filename_collection is None:
            self.filename_collection = "Param_{}".format(theParametricParameter.get_analyzed_attribute())
        else:
            self.filename_collection = filename_collection

        self.description_collection = description_collection
        self.theCharacterization = theCharacterization
        self.theParametricParameter = theParametricParameter

        self.autosave = autosave

        self.add_option(self.NUMBER_OF_CORES, "Number of cores used in evaluation", 1)

    def run(self):
        """Instantiates input arguments for analysis"""

        # Set devices to evaluate
        values = self.theParametricParameter.get_values()
        listOfDevices = list()
        for value in values:
            device = copy.deepcopy(self.theParametricParameter.get_reference_device())
            rsetattr(device, self.theParametricParameter.get_analyzed_attribute(), value)
            listOfDevices.append(device)

        # Collections out:
        theCollection_out = self.initialize_output_collection()

        # Simulates
        pool = Pool(min(cpu_count(), self.get_optionValue(self.NUMBER_OF_CORES)))
        for device in pool.imap_unordered(self.evaluate, listOfDevices):
            theCollection_out.add_data(device)

        if self.autosave:
            theCollection_out.stop_autosave()
            theCollection_out.save()
        return theCollection_out

    def evaluate(self, theDevice):
        self.theCharacterization.compute(theDevice)
        return theDevice

    def initialize_output_collection(self):
        filename = "{}/{}".format(getPath_workspace(), self.filename_collection)

        theCollection_out = Parametric_Collection(filename=filename)
        theCollection_out.set_info(self.description_collection)
        if self.autosave:
            theCollection_out.start_autosave(60)
        return theCollection_out
