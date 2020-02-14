"""
Classes to model Mass Spectra and Scans
"""

################################################################################
#                                                                              #
#    PyMassSpec software for processing of mass-spectrometry data              #
#    Copyright (C) 2005-2012 Vladimir Likic                                    #
#    Copyright (C) 2019-2020 Dominic Davis-Foster                              #
#                                                                              #
#    This program is free software; you can redistribute it and/or modify      #
#    it under the terms of the GNU General Public License version 2 as         #
#    published by the Free Software Foundation.                                #
#                                                                              #
#    This program is distributed in the hope that it will be useful,           #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of            #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
#    GNU General Public License for more details.                              #
#                                                                              #
#    You should have received a copy of the GNU General Public License         #
#    along with this program; if not, write to the Free Software               #
#    Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.                 #
#                                                                              #
################################################################################

# 3rd party
import deprecation

# this package
from pyms import __version__
from pyms.Base import pymsBaseClass, _list_types
from pyms.Mixins import MassListMixin


class Scan(pymsBaseClass, MassListMixin):
	"""
	Generic object for a single Scan's raw data

	:param mass_list: mass values
	:type mass_list: list
	:param intensity_list: intensity values
	:type intensity_list: list

	:authors: Andrew Isaac, Qiao Wang, Vladimir Likic, Dominic Davis-Foster (type assertions and properties)
	"""

	def __init__(self, mass_list, intensity_list):
		"""
		Initialise the class
		"""
		
		if not isinstance(mass_list, _list_types) or \
			not isinstance(mass_list[0], (int, float)):
			raise TypeError("'mass_list' must be a list of numbers")
		
		if not isinstance(intensity_list, _list_types) or \
			not isinstance(intensity_list[0], (int, float)):
			raise TypeError("'intensity_list' must be a list of numbers")
		
		if not len(mass_list) == len(intensity_list):
			raise ValueError("'mass_list' is not the same size as 'intensity_list'")
		
		self._mass_list = list(mass_list)
		self._intensity_list = list(intensity_list)
		self._min_mass = min(mass_list)
		self._max_mass = max(mass_list)
	
	def __len__(self):
		"""
		Returns the length of the object

		:rtype: int

		:authors: Andrew Isaac, Qiao Wang, Vladimir Likic
		"""
		
		return len(self._mass_list)
	
	def __eq__(self, other):
		"""
		Return whether this object is equal to another object

		:param other: The other object to test equality with
		:type other: object

		:rtype: bool
		"""
		
		if isinstance(other, self.__class__):
			return self._intensity_list == other.intensity_list \
					and self._mass_list == other.mass_list
		
		return NotImplemented
	
	def __copy__(self):
		"""Returns a copy of the object"""
		
		return self.__class__(self._mass_list[:], self._intensity_list[:])
	
	def __deepcopy__(self, memodict={}):
		return self.__copy__()
		
	def __dict__(self):
		print(f"""
intensity_list: {self.intensity_list},
mass_list: {self.mass_list},
min_mass: {self.min_mass},
max_mass: {self.max_mass},
""")
		return {
				"intensity_list": self.intensity_list,
				"mass_list": self.mass_list,
				}
	
	def __iter__(self):
		for key, value in self.__dict__().items():
			yield key, value
	
	def __getstate__(self):
		return self.__dict__()
	
	def __setstate__(self, state):
		self.__init__(**state)
	
	@property
	def intensity_list(self):
		"""
		Returns a copy of the intensity list

		:rtype: list

		:authors: Qiao Wang, Andrew Isaac, Vladimir Likic
		"""
		
		return self._intensity_list[:]
	
	@property
	def mass_spec(self):
		"""
		Returns the intensity list

		:rtype: list

		:authors: Qiao Wang, Andrew Isaac, Vladimir Likic
		"""
		
		return self._intensity_list

	@deprecation.deprecated(deprecated_in="2.1.2", removed_in="2.2.0",
							current_version=__version__,
							details="Use :attr:`pyms.Spectrum.Scan.intensity_list` instead")
	def get_intensity_list(self):
		"""
		Returns the intensities for the current scan

		:rtype: list

		:authors: Qiao Wang, Andrew Isaac, Vladimir Likic
		"""
		
		return self.intensity_list
	
	@deprecation.deprecated(deprecated_in="2.1.2", removed_in="2.2.0",
							current_version=__version__,
							details="Use :attr:`pyms.Spectrum.Scan.min_mass` instead")
	def get_min_mass(self):
		"""
		Returns the minimum m/z value in the scan

		:rtype: float

		:author: Andrew Isaac
		"""
		
		return self.min_mass
	
	@deprecation.deprecated(deprecated_in="2.1.2", removed_in="2.2.0",
							current_version=__version__,
							details="Use :attr:`pyms.Spectrum.Scan.max_mass` instead")
	def get_max_mass(self):
		"""
		Returns the maximum m/z value in the scan

		:rtype: float

		:author: Andrew Isaac
		"""
		
		return self.max_mass
	
	@classmethod
	def from_dict(cls, dictionary):
		return cls(**dictionary)


class MassSpectrum(Scan):
	"""
	Models a binned mass spectrum

	:param mass_list: mass values
	:type mass_list: list
	:param intensity_list: intensity values
	:type intensity_list: list

	:authors: Andrew Isaac, Qiao Wang, Vladimir Likic, Dominic Davis-Foster (type assertions and properties)
	"""
	
	@Scan.intensity_list.setter
	def intensity_list(self, value):
		"""
		Set the intensity values for the spectrum
		
		:param value: list of intensity value for each mass in `mass_list`
		:type value: list
		"""
		
		if not isinstance(value, _list_types) or not isinstance(value[0], (int, float)):
			raise TypeError("'intensity_list' must be a list of numbers")
		
		# if not len(self.mass_list) == len(value):
		# 	raise ValueError("'mass_list' and 'intensity_list' are not the same size")
		
		self._intensity_list = value
		
	@Scan.mass_spec.setter
	def mass_spec(self, value):
		"""
		Set the intensity values for the spectrum

		:param value: list of intensity value for each mass in `mass_list`
		:type value: list
		"""
		
		if not isinstance(value, _list_types) or not isinstance(value[0], (int, float)):
			raise TypeError("'intensity_list' must be a list of numbers")
		
		# if not len(self.mass_list) == len(value):
		# 	raise ValueError("'mass_list' and 'intensity_list' are not the same size")
		
		self._intensity_list = value
		
	@MassListMixin.mass_list.setter
	def mass_list(self, value):
		"""
		Set the mass values for the spectrum

		:param value: list of mass values for the spectrum
		:type value: list
		"""
		
		if not isinstance(value, _list_types) or not isinstance(value[0], (int, float)):
			raise TypeError("'mass_list' must be a list of numbers")
		
		# if not len(self.mass_list) == len(value):
		# 	raise ValueError("'mass_list' and 'intensity_list' are not the same size")
		
		self._mass_list = value
