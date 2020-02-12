import numpy as np
from pint import UnitRegistry

ureg = UnitRegistry()
ureg.autoconvert_offset_to_baseunit = True
#Q_ = ureg.Quantity

class Params:
  def __init__(self, **kwargs):
    self._units = None
    self.validator = None
    self._current = None
    self._default = None
    self.label = kwargs.get('label', None)
    self.description = kwargs.get('description', None)
    self.id = kwargs.get('id', None)
    self.units = kwargs.get('units', None)
    self.default = kwargs.get('default', None)
    self.current = kwargs.get('current', None)

  def fixUnits(self, newval):
    if isinstance(newval, str):
      newval = newval.replace('C', 'c')      
      newval = newval.replace('cm3', 'cm^3')
      newval = newval.replace('/cm', 'cm^-1')
    else:
      newval = str(newval)
    return newval

  def validate_current(self, newval):
    if (newval != None):
      if (self._units != None):
        newval = self.fixUnits(newval)
        val = ureg.parse_expression(newval)
        if isinstance(val, ureg.Quantity):
          newval = val.to(self.validator).magnitude
        else: 
          newval = val
    return newval;

  @property
  def value(self):
    value = self._current
    if (value==None):
      value = self._default
    if (self._units):
      return str(value) + str(self._units)
    else:
      return str(value)    
    
  @property
  def default(self):
    return self._default

  @default.setter
  def default(self, newval):    
    self._default = Params.validate_current(self, newval)

  @property
  def current(self):
    return self._current

  @current.setter
  def current(self, newval):    
    self._current = self.validate_current(newval)
    
  def validate_units(self, newval):
    if (newval == ""):
      newval = None
    if (newval != None):
      self.validator = None
      newvalidation = self.fixUnits(newval)
      self.validator = ureg.parse_expression(newvalidation)
    return newval;
    
  @property
  def units(self):  
    return self._units

  @units.setter
  def units(self, newval):    
    self._units = self.validate_units(newval)

  def to_dict(self):
    res = { 'type' : 'Param' }    
    res['id'] = self.id
    if (self._current is not None):
      res['current'] = self.current
    if (self.description is not None):
      res['description'] = self.description
    if (self.label is not None):
      res['label'] = self.label
    if (self.units is not None):
      res['units'] = self.units
    if (self._default is not None):
      res['default'] = self.default
    return res

  def __repr__(self):
    res = "{"
    repr = self.to_dict()
    for k,v in repr.items():
      res += k.__repr__() + " : " + v.__repr__() + ", "
    res += "}"
    return res
    
class ParamsFactory:   
  def builder(descriptor):
    if 'type' in descriptor:
      if (descriptor['type'] == "integer"):
        return Integer(**descriptor)
      elif (descriptor['type'] == "number"):
        return Number(**descriptor)
      elif (descriptor['type'] == "choice"):
        return Choice(**descriptor)
      elif (descriptor['type'] == "string"):
        return String(**descriptor)
      elif (descriptor['type'] == "boolean"):
        return Boolean(**descriptor)
      else:
        #print (descriptor)
        return Params(**descriptor)
  
    else:
      return Params()


class Integer(Params):
  def __init__(self, **kwargs):
    self._min = None    
    self._max = None    
    self._units = None
    self.validator = None
    self._current = None
    self._default = None
    self.label = kwargs.get('label', None)
    self.description = kwargs.get('description', None)
    self.id = kwargs.get('id', None)
    self.units = kwargs.get('units', None)
    self.default = kwargs.get('default', None)
    self.current = kwargs.get('current', None)    
    self.min = kwargs.get('min', None)
    self.max = kwargs.get('max', None)

  @property
  def min(self):  
    return self._min

  @min.setter
  def min(self, newval):    
    if newval != None:
      self._min = int(Params.validate_current(self, newval))
    else:
      self._min = None

  @property
  def max(self):  
    return self._max

  @max.setter
  def max(self, newval):    
    if newval != None:
      self._max = int(Params.validate_current(self, newval))
    else :
      self._max = None
      
  @property
  def current(self):
    return self._current

  @current.setter
  def current(self, newval):
    if newval !=  None:
      self._current = int(self.validate_current(newval))
    else:
      self._current = None
    
  def validate_current(self, newval):
    if (newval != None):
      newval = Params.validate_current(self, newval)
      if self._units is not None:
        units = self._units
      if self._min is not None and newval < self._min:
        raise ValueError(str(newval) + units + ", Minimum value is " + str(self._min) + units)
      if self._max is not None and newval > self._max:
        raise ValueError(str(newval) + units + ", Maximum value is " + str(self._max) +  units)
    return newval

  def to_dict(self):
    res = Params.to_dict(self);
    if (self._min is not None):
      res['min'] = self._min
    if (self._max is not None):
      res['max'] = self._max
    res['type'] = "Integer"
    return res

class Number(Params):
  def __init__(self, **kwargs):
    self._units = None
    self.validator = None
    self._current = None
    self._default = None
    self._min = None    
    self._max = None    
    self.label = kwargs.get('label', None)
    self.description = kwargs.get('description', None)
    self.id = kwargs.get('id', None)
    self.units = kwargs.get('units', None)
    self.default = kwargs.get('default', None)
    self.current = kwargs.get('current', None)
    self.min = kwargs.get('min', None)
    self.max = kwargs.get('max', None)

  @property
  def min(self):  
    return self._min

  @min.setter
  def min(self, newval):    
    if newval != None:
      self._min = float(Params.validate_current(self, newval))
    else :
      self._min = None

  @property
  def max(self):  
    return self._max

  @max.setter
  def max(self, newval):    
    if newval != None:
      self._max = float(Params.validate_current(self, newval))
    else :
      self._max = None
      
  @property
  def current(self):
    return self._current

  @current.setter
  def current(self, newval):    
    if newval !=  None:
      self._current = float(self.validate_current(newval))
    else:
      self._current = None    
    
  def validate_current(self, newval):
    if (newval != None):
      newval = Params.validate_current(self, newval)
      units = ""
      if self._units is not None:
        units = self._units
      if self._min is not None and newval < self._min:
        raise ValueError(str(newval) + units + ", Minimum value is " + str(self._min) + units)
      if self._max is not None and newval > self._max:
        raise ValueError(str(newval) + units + ", Maximum value is " + str(self._max) +  units)
    return newval

  def to_dict(self):
    res = Params.to_dict(self);
    if (self._min is not None):
      res['min'] = self._min
    if (self._max is not None):
      res['max'] = self._max
    res['type'] = "Number"
    return res
    
class Choice(Params):
  def __init__(self, **kwargs):
    # always set these first
    self.options = kwargs.get('options', [])
    Params.__init__(self, **kwargs)
    
  def validate_current(self, newval):
    if (newval != None):
      newval = Params.validate_current(self, newval)    
      if newval not in [p[0] for p in self.options]:
        if newval not in [p[1] for p in self.options]:
          raise ValueError("values should be one of the posible options")
      return newval;
    return newval;

  def to_dict(self):
    res = Params.to_dict(self);
    if (self.options is not None):
      res['options'] = self.options
    res['type'] = "Choice"
    return res
    
class String(Params):
  def __init__(self, **kwargs):
    Params.__init__(self, **kwargs)
    
  def validate_current(self, newval):
    if (newval != None):
      newval = Params.validate_current(self, newval)    
      return str(newval);
    return newval;

  def to_dict(self):
    res = Params.to_dict(self);
    res['type'] = "String"
    return res    
    
class Boolean(Params):
  def __init__(self, **kwargs):
    Params.__init__(self, **kwargs)
    
  def validate_current(self, newval):
    if (newval != None):
      newval = Params.validate_current(self, newval)    
      if (newval in ["yes", 1, "si", True, "true", "on"]):
        return "yes"
      elif (newval in ["no", 0, "no", False, "false", "off"]):
        return "no"
      else:
        raise ValueError("values should be a valid boolean")
    return newval;

  def to_dict(self):
    res = Params.to_dict(self);
    res['type'] = "Boolean"
    return res
    
'''class Text(Params):
    def __init__(self, **kwargs):
        self.value = None
        super(Text, self).__init__(**kwargs)

    def __repr__(self):
        # print all attributes with value last
        res = ''
        for i in self:
            if i != 'value':
                res += '    %s: %s\n' % (i, self[i])
        if self.value is not None:
            res += '    value: %s\n' % self.value
        return res

class List(Params):
    def __init__(self, **kwargs):
        self.value = None
        super(List, self).__init__(**kwargs)

    def __repr__(self):
        # print all attributes with value last
        res = ''
        for i in self:
            if i != 'value':
                res += '    %s: %s\n' % (i, self[i])
        if self.value is not None:
            res += '    value: %s\n' % self.value
        return res


class Dict(Params):
    def __init__(self, **kwargs):
        self.value = None
        super(Dict, self).__init__(**kwargs)

    def __repr__(self):
        # print all attributes with value last
        res = ''
        for i in self:
            if i != 'value':
                res += '    %s: %s\n' % (i, self[i])
        if self.value is not None:
            res += '    value: %s\n' % self.value
        return res



class Number(Params):
    def __init__(self, **kwargs):
        # always set these first
        self.min = kwargs.get('min')
        self.max = kwargs.get('max')
        self.units = kwargs.get('units')
        self._value = None
        super(Number, self).__init__(**kwargs)
        if self.units:
            try:
                self.units = ureg.parse_units(self.units)
            except:
                raise ValueError('Unrecognized units: %s' % self.units)

    @property
    def value(self):
        return self._value

    def convert(self, newval):
        "unit conversion with special temperature conversion"
        units = self.units
        if units == ureg.degC or units == ureg.kelvin or units == ureg.degF or units == ureg.degR:
            if newval.units == ureg.coulomb:
                # we want temp, so 'C' is degC, not coulombs
                newval = newval.magnitude * ureg.degC
            elif newval.units == ureg.farad:
               # we want temp, so 'F' is degF, not farads
                newval = newval.magnitude * ureg.degF
        elif units == ureg.delta_degC or units == ureg.delta_degF:
            # detect when user means delta temps
            if newval.units == ureg.degC or newval.units == ureg.coulomb:
                newval = newval.magnitude * ureg.delta_degC
            elif newval.units == ureg.degF or units == ureg.farad:
                newval = newval.magnitude * ureg.delta_degF
        return newval.to(units).magnitude

    @value.setter
    def value(self, newval):
        if self.units and type(newval) == str:
            newval = ureg.parse_expression(newval)
            if hasattr(newval, 'units'):
                newval = self.convert(newval)
            else:
                newval = float(newval)
        if self.min is not None and newval < self.min:
            raise ValueError("Minimum value is %d" % self.min)
        if self.max is not None and newval > self.max:
            raise ValueError("Maximum value is %d" % self.max)
        self._value = newval

    def __repr__(self):
        # print all attributes with value last
        res = ''
        for i in self:
            if i != 'value':
                res += '    %s: %s\n' % (i, self[i])
        if self.value is not None:
            res += '    value: %s\n' % self.value
        return res





# register param types
# Dictionary that maps strings to class names.
Params.types = {
    'Integer': Integer,
    'List': List,
    'Dict': Dict,
    'Text': Text,
    'Number': Number,
}'''