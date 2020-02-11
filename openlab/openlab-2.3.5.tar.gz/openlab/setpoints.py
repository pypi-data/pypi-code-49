def all_setpoints():
    """
    Returns a list of all available/possible setpoints
    Subject to change in the future
    """
    empty_setpoints = [
        "ChokeOpening", "FlowRateIn", "TopOfStringVelocity",
        "DesiredROP", "SurfaceRPM", "ChokePumpFlowRateIn", "BopChokeOpening",
        "MainPitActive", "MainPitReturn", "ControlActivePit",
        "ControlActivePitDensity", "ControlActivePitTemperature"
    ]
    return empty_setpoints

class Setpoints():
    """
    A class property for the setpoints
    """
    def __init__(self):
        self.ChokeOpening = 1 # 0=closed 1=Open
        self.FlowRateIn = None
        self.TopOfStringVelocity = None
        self.DesiredROP  = None
        self.SurfaceRPM = None
        self.ChokePumpFlowRateIn = None
        self.BOPChokeOpening = 1 # 0=closed 1=Open
        self.MainPitActive = None # bool
        self.MainPitReturn = None # bool
        self.ControlActivePit = None #bool
        self.ControlActivePitDensity = None # float
        self.ControlActivePitTemperature = None # float
    
    @property
    def ChokeOpening(self): return self.__ChokeOpening
    @ChokeOpening.setter
    def ChokeOpening(self, value): self.__ChokeOpening = value

    @property
    def FlowRateIn(self): return self.__FlowRateIn
    @FlowRateIn.setter
    def FlowRateIn(self, value): self.__FlowRateIn = value

    @property
    def TopOfStringVelocity(self): return self.__TopOfStringVelocity
    @TopOfStringVelocity.setter
    def TopOfStringVelocity(self, value): self.__TopOfStringVelocity = value

    @property
    def DesiredROP(self): return self.__DesiredROP
    @DesiredROP.setter
    def DesiredROP(self, value): self.__DesiredROP = value            

    @property
    def SurfaceRPM(self): return self.__SurfaceRPM
    @SurfaceRPM.setter
    def SurfaceRPM(self, value): self.__SurfaceRPM = value

    @property
    def ChokePumpFlowRateIn(self): return self.__ChokePumpFlowRateIn
    @ChokePumpFlowRateIn.setter
    def ChokePumpFlowRateIn(self, value): self.__ChokePumpFlowRateIn = value

    @property
    def BOPChokeOpening(self): return self.__BOPChokeOpening
    @BOPChokeOpening.setter
    def BOPChokeOpening(self, value): self.__BOPChokeOpening = value

    @property
    def MainPitActive(self): return self.__MainPitActive
    @MainPitActive.setter
    def MainPitActive(self, value): self.__MainPitActive = value

    @property
    def MainPitReturn(self): return self.__MainPitReturn
    @MainPitReturn.setter
    def MainPitReturn(self, value): self.__MainPitReturn = value

    @property
    def ControlActivePit(self): return self.__ControlActivePit
    @ControlActivePit.setter
    def ControlActivePit(self, value): self.__ControlActivePit = value

    @property
    def ControlActivePitDensity(self): return self.__ControlActivePitDensity
    @ControlActivePitDensity.setter
    def ControlActivePitDensity(self, value): self.__ControlActivePitDensity = value

    @property
    def ControlActivePitTemperature(self): return self.__ControlActivePitTemperature
    @ControlActivePitTemperature.setter
    def ControlActivePitTemperature(self, value): self.__ControlActivePitTemperature = value
