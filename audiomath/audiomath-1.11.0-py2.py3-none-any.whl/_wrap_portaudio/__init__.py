# $BEGIN_AUDIOMATH_LICENSE$
# 
# This file is part of the audiomath project, a Python package for
# recording, manipulating and playing sound files.
# 
# Copyright (c) 2008-2020 Jeremy Hill
# 
# audiomath is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program. If not, see http://www.gnu.org/licenses/ .
# 
# The audiomath distribution includes binaries from the third-party
# AVbin and PortAudio projects, released under their own licenses.
# See the respective copyright, licensing and disclaimer information
# for these projects in the subdirectories `audiomath/_wrap_avbin`
# and `audiomath/_wrap_portaudio` . It also includes a fork of the
# third-party Python package `pycaw`, released under its original
# license (see `audiomath/pycaw_fork.py`).
# 
# $END_AUDIOMATH_LICENSE$
"""
Wrap the PortAudio library using high-level functions and classes
to make it easy to use from Python (at a higher level than the
enclosed `_dll_wrapper` submodule, which aims to provide Python
wrappers/replicas of the functions and constants in portaudio.h).
"""
__all__ = [
	'SetDefaultVerbosity',
	'GetHostApiInfo', 'GetDeviceInfo', 'FindDevice', 'FindDevices', 'Tabulate',
	'Stream', 'PORTAUDIO', 'LowLatencyMode',
]

####### portaudio-specific implementation

import os
import re
import sys
import ast
import ctypes
import pstats
import weakref
import cProfile

if sys.version < '3': bytes = str
else: unicode = str; basestring = ( unicode, bytes )
def IfStringThenRawString( x ):
	from . import _dll_wrapper
	if isinstance( x, _dll_wrapper.String ): x = x.data
	if isinstance( x, unicode ): x = x.encode( 'utf-8' )
	return x
def IfStringThenNormalString( x ):
	from . import _dll_wrapper
	if isinstance( x, _dll_wrapper.String ): x = x.data
	if str is not bytes and isinstance( x, bytes ): x = x.decode( 'utf-8' )
	return x

def tryprint( s ):
	try: print( s )
	except: pass

class ErrorCheckingDllWrapper( object ):
	def __init__( self, dll, raiseExceptions=False, printWarnings=False ):
		self.__dll = dll
		self.raiseExceptions = raiseExceptions
		self.printWarnings = printWarnings
	def __getattr__( self, name ):
		func = getattr( self.__dll, name )
		def wrapped( *pargs ):
			error = func( *pargs )
			if error == self.__dll.paUnanticipatedHostError:
				info = self.__dll.Pa_GetLastHostErrorInfo()
				error = info.contents.errorCode
				errorName = 'paUnanticipatedHostError: ' + IfStringThenNormalString( info.contents.errorText )
			elif error:
				lookup = [ x for x in dir( self.__dll ) if getattr( self.__dll, x ) == error ]
				errorName = lookup[ 0 ] if lookup else '???'
			if error:
				msg = '%s() call failed with error code %r (%s)' % ( name, error, errorName )
				if self.raiseExceptions: raise RuntimeError( msg )
				elif self.printWarnings: print( 'WARNING: %s' % msg )
			return error
		wrapped.__name__ = name
		setattr( self, name, wrapped )
		return wrapped

class thing( object ):
	_classNamePrefix = ''
	def __str__( self ):  return self._report( with_repr='short', indent='' )
	def __repr__( self ): return self._report( with_repr='short', indent='' )
	def _short_repr( self, *p ): return '<%s%s 0x%0*X>' % ( self._classNamePrefix, self.__class__.__name__, ( 16 if sys.maxsize > 2 ** 32 else 8 ), id( self ) )
	def _super_repr( self, *p ): return object.__repr__( self )
	def _report( self, with_repr='short', indent='' ):
		s = ''
		if with_repr:
			if   with_repr in [ True, 'short' ]:   f = self._short_repr
			elif with_repr in [ 'super', 'long' ]: f = self._super_repr
			elif callable( with_repr ): f = with_repr
			else: f = object.__repr__
			s = indent + f( self ) + '\n'
			indent += '    '
		indent = ''.join( c if c.isspace() else ' ' for c in indent )
		if getattr( self, 'inputDevice', None ):  s +=  '%sinput device %d: %s <- %s\n' % ( indent, self.inputDevice.index,  self.inputDevice.hostApi.name,  self.inputDevice.name  )
		if getattr( self, 'outputDevice', None ): s += '%soutput device %d: %s -> %s\n' % ( indent, self.outputDevice.index, self.outputDevice.hostApi.name, self.outputDevice.name )
		conditions = ', '.join( '%s=%s' % ( k, v ) for k in 'fs bufferLengthMsec minLatencyMsec'.split() for v in [ getattr( self, k, None ) ] if v not in [ None, '' ] )
		if conditions: s += '%s%s\n' % ( indent, conditions )
		return s.rstrip( '\n' )

	
class Library( thing ):
	"""
	A representation of the PortAudio library itself.
	This will be automatically initialized and
	terminated as appropriate.
	"""
		
	def __init__( self, verbose=False ):
		self.verbose = verbose
		self.__initialized = False
		self.__dll = None
		self.__dll_errorcheck = None
		
	def Initialize( self, minLatencyMsec='auto' ):
		"""
		This doesn't need to be called explicitly unless you
		want to be explicit about the `minLatencyMsec` setting.
		Then it has to be called before any other PortAudio
		operations.
		
		Calling it with `minLatencyMsec=None` will temporarily
		unset the `PA_MIN_LATENCY_MSEC` variable during
		initialization and fall back on the PortAudio library
		default behavior.  If you want to fall back on this
		Python session's environment variable setting (or if
		that hasn't been set, audiomath's own default logic)
		then simply do not call this, or call it with `'auto'`
		"""
		if self.__initialized: return False
		auto = False
		if isinstance( minLatencyMsec, str ):
			minLatencyMsec = minLatencyMsec.lower()
			if minLatencyMsec in [ 'none', '' ]: minLatencyMsec = None
			auto = minLatencyMsec in [ 'auto' ]
		if auto: env = TemporaryEnvironment( PA_MIN_LATENCY_MSEC_AUTO=1 )
		else:    env = TemporaryEnvironment( PA_MIN_LATENCY_MSEC_AUTO=0, PA_MIN_LATENCY_MSEC=minLatencyMsec )
		with env: self.__Open()
		return True
		
	def __Open( self ):
		if not self.__dll: from . import _dll_wrapper; self.__dll = _dll_wrapper
		if not self.__dll_errorcheck: self.__dll_errorcheck = ErrorCheckingDllWrapper( self.__dll, printWarnings=self.verbose )
		if not self.__initialized:
			#import traceback; print(', '.join( '%s=%r' % ( k, os.environ.get( k, '' ) ) for k in 'PA_MIN_LATENCY_MSEC_AUTO PA_MIN_LATENCY_MSEC'.split() ) ); traceback.print_stack(file=sys.stdout)
			if int( os.environ.get( 'PA_MIN_LATENCY_MSEC_AUTO', '1' ) ): # if we haven't come here from Initialize(), where we definitively specify the behavior we want, even if that's to remove the variable...
				if 'PA_MIN_LATENCY_MSEC' not in os.environ:  # ...and if the environment has nothing to say about this preference (not even an explicit blank):
					minLatencyMsec = self.DEFAULT_MIN_LATENCY_MSEC # ...and if the library has no explicit default
					if minLatencyMsec == 'auto': # ... then let's set an "intelligent" default
						minLatencyMsec = None
						if sys.platform.lower().startswith( 'win' ):
							minLatencyMsec = 20
					if minLatencyMsec is None: os.environ.pop( 'PA_MIN_LATENCY_MSEC', '' )
					else: os.environ[ 'PA_MIN_LATENCY_MSEC' ] = str( minLatencyMsec )
					# In the PortAudio v19_20161030 C code it's clear that this setting only affects the DirectSound host API
					# Our tests around 20200115 with Windows 10 showed that it consistently reduced the DirectSound latencies
					# without obvious side-effects when set to '20' so we'll use '20' as the default setting *provided*
					# the user has not specified this setting either in the environment or by calling `PORTAUDIO.Initialize()`.
					# If they have manipulated it (even set the environment variable to blank, or explicitly removed it by
					# calling `PORTAUDIO.Initialize(minLatencyMsec=None)` ) then we'll respect that preference instead.
			env = os.environ.get( 'PA_MIN_LATENCY_MSEC', '' )
			self.__minLatencyMsec = None if env.lower() in [ 'none', '' ] else float( env )
			self.__initialized = ( self.__dll_errorcheck.Pa_Initialize() == 0 )
			if self.verbose: print( ( '%s has been initialized' if self.__initialized else '%s failed to initialize' ) % self._short_repr() )
			self.__Pa_Terminate = self.__dll_errorcheck.Pa_Terminate # this may seem stupid...
		return self
	
	def _Close( self ):
		if self.__initialized:
			if self.verbose > 1: tryprint( '%s is terminating (stage 0)' % self._short_repr() )
			elif self.verbose:   tryprint( '%s is terminating' % self._short_repr() )
			self.__Pa_Terminate() # ...but it works around an exception that would otherwise happen (and be verbosely ignored) during garbage collection in Python 2
			if self.verbose > 1: tryprint( '%s is terminating (stage 1)' % self._short_repr() )
		self.__initialized = False
		
	def __del__( self ):
		self._Close()
	
	@property
	def initialized( self ):
		return self.__initialized
	@property
	def minLatencyMsec( self ):
		return self.__minLatencyMsec
	@property
	def dll( self ):
		return self.__Open().__dll
	@property
	def dll_errorcheck( self ):
		return self.__Open().__dll_errorcheck


	@classmethod
	def ConfigProperty( cls, name, defaultValue, doc='' ):
		dunderName = '_' + cls.__name__ + '__' + name
		setattr( cls, dunderName, defaultValue )
		def fget( self ): return getattr( self, dunderName )
		def fset( self, value ): setattr( self, dunderName, value )
		prop = property( fget=fget, fset=fset, doc=doc.strip() )
		setattr( cls, name, prop )
		
Library.ConfigProperty( 'DEFAULT_INPUT_API_PREFERENCE_ORDER', 'WDM-KS, WASAPI, DirectSound, MME, *',
"""
Comma-separated order in which the host APIs are preferred for input
(recording) streams. `*` indicates any host API name (important for
non-Windows platforms, because the explicitly-ordered host APIs here
are all Windows).
""" )

Library.ConfigProperty( 'DEFAULT_OUTPUT_API_PREFERENCE_ORDER', 'DirectSound, WDM-KS, ASIO, WASAPI, *',
"""
Comma-separated order in which the host APIs are preferred for output
(playback) streams. `*` indicates any host API name (important for
non-Windows platforms, because the explicitly-ordered host APIs here
are all Windows).

In our tests, ASIO had the shortest latency, followed by WDM-KS.
WDM-KS would probably be the most sensible default. However, both have
been demoted in this ordering, because they take over the sound device
in exclusive mode, meaning that sounds from other applications cannot
be heard (NB: in some situations that may be desirable...)

You can call `LowLatencyMode(True)` to rearrange the default
preference order in favor of WDM-KS, and hence in favor exclusive mode
on Windows (it will also separately configure the
`DEFAULT_BUFFER_LENGTH_MSEC` option, which will affect macOS).
""" )

Library.ConfigProperty( 'DEFAULT_BUFFER_LENGTH_MSEC', 'auto',
"""
Specifies the default value for the `bufferLengthMsec` contructor
parameter for the `Stream` class. A value of `'auto'` causes a
value of 8.5ms to be used under the macOS Core Audio host API,
and the PortAudio-defined default on other hosts/platforms. We
do this because the PortAudio default settings on macOS Core Audio
yield an impressive 7.5ms overall output latency, which is often
*too* low and leaves the sound vulnerable to stuttering when Python
does anything else concurrently. In our tests, `bufferLengthMsec=8.5`
put the overall output latency up to around 20ms (comparable to
WDM-KS on Windows) while providing reasonable protection against
crackles and stutters.

You can call `LowLatencyMode(True)` to shoot for lower latency
at the cost of stutter-vulnerability (and also, on Windows, at the
cost of monopolizing the sound output device).
""" )

Library.ConfigProperty( 'DEFAULT_MIN_LATENCY_MSEC', 'auto',
"""
Specifies the default value for the `PA_MIN_LATENCY_MSEC` environment
variable if it is not already set in the environment. (In other words,
if the environment variable has been set, even to a blank string, then
this property will be ignored.) The default value of `'auto'` means
that the variable will be set to 20 for the DirectSound host API, and
left blank otherwise.

In the PortAudio v19_20161030 C code it's clear that this setting
only affects the DirectSound host API. Our tests around 20200115
with Windows 10 showed that it consistently reduced the DirectSound
latencies without obvious side-effects when set to '20'.
""" )
			
PORTAUDIO = Library()
def LowLatencyMode( turnOn, preferASIO=False ):
	"""
	Call this function before you create your first `Stream` or
	`Player` instance.
	
	On Windows, `LowLatencyMode(True)` will manipulate
	`PORTAUDIO.DEFAULT_OUTPUT_API_PREFERENCE_ORDER` to cause the
	WDM-KS host API (or the ASIO host API, if `preferASIO` is `True`)
	to be preferred over DirectSound when constructing output streams.
	This will allow considerably lower output latencies, but will have
	the side-effect of taking exclusive control of the sound driver,
	meaning that sounds from other applications will no longer be
	audible (this may or may not be desirable, depending on your
	application).
	
	`LowLatencyMode(True)` also sets
	`PORTAUDIO.DEFAULT_BUFFER_LENGTH_MSEC = None`, which will have the
	effect of lowering latencies on the Core Audio host API under macOS.
	This will have the side effect of making sounds vulnerable to
	stuttering if Python performs any significant work during playback.
	
	`LowLatencyMode(False)` reverts to factory settings (DirectSound
	preferred on Windows, and a small extra buffer on macOS Core Audio)
	for future `Stream` instances.
	"""
	if turnOn:
		PORTAUDIO.DEFAULT_BUFFER_LENGTH_MSEC = None
		if preferASIO:
			PORTAUDIO.DEFAULT_OUTPUT_API_PREFERENCE_ORDER = 'ASIO, WDM-KS, WASAPI, DirectSound, *'
		else:
			PORTAUDIO.DEFAULT_OUTPUT_API_PREFERENCE_ORDER = 'WDM-KS, ASIO, WASAPI, DirectSound, *'
	else:
		PORTAUDIO.DEFAULT_BUFFER_LENGTH_MSEC = 'auto'
		PORTAUDIO.DEFAULT_OUTPUT_API_PREFERENCE_ORDER = Library.DEFAULT_OUTPUT_API_PREFERENCE_ORDER.__get__( Library )

def struct2dict( s, fieldOrder='' ):
	b = Bunch( { k : IfStringThenNormalString( getattr( s.contents, k ) ) for k in s.contents.__slots__ } )
	b._fieldOrder = fieldOrder
	return b

def GetHostApiInfo():
	"""
	Returns a list of records corresponding to PortAudio's
	`Pa_GetHostApiInfo()` output for every available host
	API.  You can `print()` the result, or otherwise convert
	it to `str()`, to see a pretty tabulated summary.
	"""
	fieldOrder = "index name isDefault type deviceCount defaultInputDevice defaultOutputDevice structVersion"
	hostApis = [ struct2dict( PORTAUDIO.dll.Pa_GetHostApiInfo( i ), fieldOrder ) for i in range( PORTAUDIO.dll.Pa_GetHostApiCount() ) ]
	default = PORTAUDIO.dll.Pa_GetDefaultHostApi()
	for index, hostApi in enumerate( hostApis ):
		hostApi[ 'index' ] = index
		hostApi[ 'isDefault' ] = ( index == default )
	return ListOfHostApiRecords( hostApis )
	
def GetDeviceInfo():
	"""
	Returns a list of records corresponding to PortAudio's
	`Pa_GetDeviceInfo()` output for every available
	combination of host API and device.   You can `print()`
	the result, or otherwise convert it to `str()`, to see
	a pretty tabulated summary.
	"""
	hostApis = GetHostApiInfo()
	fieldOrder = "index name defaultSampleRate //maxInputChannels defaultLowInputLatency defaultHighInputLatency isDefaultInput //maxOutputChannels defaultLowOutputLatency defaultHighOutputLatency isDefaultOutput //structVersion hostApi"
	devices = [ struct2dict( PORTAUDIO.dll.Pa_GetDeviceInfo( i ), fieldOrder ) for i in range( PORTAUDIO.dll.Pa_GetDeviceCount() ) ]
	for index, device in enumerate( devices ):
		device[ 'index' ] = index
		device[ 'hostApi' ] = api = hostApis[ device[ 'hostApi' ] ]
		device[ 'isDefaultInput'  ] = ( index == api[ 'defaultInputDevice'  ] )
		device[ 'isDefaultOutput' ] = ( index == api[ 'defaultOutputDevice' ] )
	return ListOfDeviceRecords( devices )

SANITIZER = re.compile( r'[^a-zA-Z0-9_]+' )
def _Sanitize( x ):
	if not x: return ''
	return re.sub( SANITIZER, ' ', x.lower() )

class _DeviceSpecification( object ):
	PATTERN = re.compile( r'''
		\s*
		(
			(?P<apiPreferences>.*)
			\s*
			(?P<delimiter>\<\-|\-\>|//+)
		)?
		\s*
		(?P<mode>[oi]+\b)?
		\s*\:?\s*
		(?P<id>\S.*)?
		\s*
	''', re.VERBOSE + re.IGNORECASE )
	def __init__( self, id=None, mode=None, apiPreferences=None ):
		if isinstance( id, type( self ) ):
			other = id
			self.id             = other.id
			self.mode           = list( other.mode )
			self.apiPreferences = list( other.apiPreferences )
			self.allCandidates  = other.allCandidates
		else:
			try: id = int( id )
			except: pass
			if isinstance( id, str ):
				id = id.lower().strip()
				m = re.match( self.PATTERN, id )
				if m:
					m = m.groupdict()
					id = _Sanitize( m[ 'id' ] )
					if id in [ '', '*' ]: id = None
					if not mode: mode = m[ 'mode' ]
					if not apiPreferences: apiPreferences = m[ 'apiPreferences' ]
			elif isinstance( id, dict ): id = id[ 'index' ]
			elif isinstance( id, int ) or id is None: pass
			else: raise TypeError( 'invalid `id` argument (use name, index or dict)' )
			self.id = id
			self.mode = None
			self.apiPreferences = None
			self.allCandidates = None
		
		if mode or not self.mode:
			if not mode: mode = ''
			if hasattr( mode, 'NumberOfChannels' ): self.mode = [ 0, mode.NumberOfChannels() ]
			elif isinstance( mode, ( tuple, list ) ) and len( mode ) == 2: self.mode = list( mode )
			else: self.mode = [ mode.lower().count( 'i' ), mode.lower().count( 'o' ) ]
		
		if apiPreferences or not self.apiPreferences:
			if not apiPreferences:
				apiPreferences = PORTAUDIO.DEFAULT_INPUT_API_PREFERENCE_ORDER if self.mode[ 0 ] else PORTAUDIO.DEFAULT_OUTPUT_API_PREFERENCE_ORDER
			if isinstance( apiPreferences, str ):
				apiPreferences = [ preferred.strip() for preferred in apiPreferences.split( ',' ) ]
			# if there's a '*' in the apiPreferences sequence, insert the default host API just before it to ensure that the default is considered first
			self.apiPreferences = [ _Sanitize( preferred ) for item in apiPreferences for preferred in ( [ GetHostApiInfo()[ PORTAUDIO.dll.Pa_GetDefaultHostApi() ][ 'name' ], item ] if item == '*' else [ item ] ) ]
	def __repr__( self ):
		d = dict( self.__dict__ )
		d.pop( 'allCandidates', None )
		return repr( d )
	@property
	def minInputChannels( self ): return self.mode[ 0 ]
	@minInputChannels.setter
	def minInputChannels( self, value ): self.mode[ 0 ] = value
	@property
	def minOutputChannels( self ): return self.mode[ 1 ]
	@minOutputChannels.setter
	def minOutputChannels( self, value ): self.mode[ 1 ] = value
	@property
	def nonspecific( self ): return self.minInputChannels == 0 and self.minOutputChannels == 0
	
def _IsSubphrase( phrase, sentence ):
	return ( ' ' + phrase + ' ' ) in ( ' ' + sentence + ' ' )
	
def FindDevices( id=None, mode=None, apiPreferences=None, _candidates=None ):
	"""
	Calls `GetDeviceInfo()`, filtering and reordering the
	outputs according to the specified criteria. You can
	`print()` the result, or otherwise convert it to `str()`,
	to see a pretty tabulated summary.
	
	You can use `FindDevice()` (singular) to return just the
	top-ranking result (and to assert that at least one
	result can be found).
	
	Args:
		id (int, dict, str, None):
			- `None`: matches all devices;
			- `str`: matches any device with the specified
			  word or phrase in its `name` field;
			- `int`: matches only the device whose `index`
			  field matches `id`;
			- `dict` (including the objects returned by
			  this function, which are `dict` subclassses):
			  matches only the device whose `index` field
			  matches `id['index']`
			
		mode (str, tuple, None):
			May be either a two-element tuple such as
			`mode=(minInputChannels,minOutputChannels)`,
			or a string containing a number of `'o'`
			and/or `'i'` characters.  In either case,
			devices are only matched if they provide
			at least the specified number of input
			and output channels. For example,
			`FindDevices(mode='oo')` matches all devices
			that provide two or more output channels. 
			
		apiPreferences (str, None):
			If this is left at `None`, it defaults to the
			current value of
			`PORTAUDIO.DEFAULT_INPUT_API_PREFERENCE_ORDER`
			(if the `mode` argument requests any inputs) or
			`PORTAUDIO.DEFAULT_OUTPUT_API_PREFERENCE_ORDER`
			otherwise.  The string `'*'` matches all
			host APIs.  Host APIs may be comma-delimited.
			For example, `apiPreferences='DirectSound,*'`
			means "give first priority to devices hosted 
			by the DirectSound API, and then, failing that,
			match all other APIs".  If `'*'` is not included
			in the specification, this argument may limit
			the number of records returned. In any case it
			will affect the ordering of the returned records.
	"""
	if isinstance( id, ( tuple, list ) ):
		return ListOfDeviceRecords( FindDevice( each_id, _candidates=_candidates ) for each_id in id )
	devspec = _DeviceSpecification( id=id, mode=mode, apiPreferences=apiPreferences )
	if devspec.allCandidates is None: devspec.allCandidates = _candidates() if callable( _candidates ) else _candidates
	if devspec.allCandidates is None: devspec.allCandidates = GetDeviceInfo()
	rank = {}
	reordered = []
	for preferenceIndex, preferred in enumerate( devspec.apiPreferences ):
		if not preferred: continue
		for device in devspec.allCandidates:
			if device in reordered: continue
			if isinstance( devspec.id, int  ) and devspec.id != device[ 'index' ]: continue
			if device[ 'maxInputChannels'  ] < devspec.minInputChannels:  continue
			if device[ 'maxOutputChannels' ] < devspec.minOutputChannels: continue
			if preferred != '*' and not _IsSubphrase( preferred, _Sanitize( device[ 'hostApi' ][ 'name' ] ) ): continue
			if isinstance( devspec.id, str  ) and not _IsSubphrase( devspec.id, _Sanitize( device[ 'name' ] ) ): continue
			rank[ device[ 'index' ] ] = preferenceIndex
			reordered.append( device )
	reordered.sort( key=lambda device: (
		rank[ device[ 'index' ] ],
		1 if device.get( 'isDefaultInput', False ) or device.get( 'isDefaultOutput', False ) else 2,
	) )
	return ListOfDeviceRecords( reordered )
	
def FindDevice( id=None, mode=None, apiPreferences=None, _candidates=None ):
	"""
	Returns the first device matched by `FindDevices()`
	(plural) according to the specified criteria. Raises
	an exception if there are no matches.
	"""
	devices = FindDevices( id=id, mode=mode, apiPreferences=apiPreferences, _candidates=_candidates )
	if not devices: raise ValueError( 'could not find a device that matched the criteria' )
	return devices[ 0 ]

class TemporaryEnvironment( object ):
	def __init__( self, **kwargs ):
		self.desired = kwargs
		self.previous = []
	def __enter__( self ):
		previous = {}
		for k, v in self.desired.items():
			# If you uncomment the following line (marked #XXX), values of None will mean "keep whatever value is already set in the environment (which will not necessarily be '')"
			# If you leave the #XXX line commented out, values of None will mean "temporarily unset this environment variable completely"
			#if v is None: continue  #XXX
			exists = k in os.environ
			previous[ k ] = os.environ[ k ] if exists else None
			if v is None: os.environ.pop( k, '' )
			else: os.environ[ k ] = '%g' % v if isinstance( v, float ) else str( v )
		self.previous.append( previous )
	def __exit__( self, *blx ):
		previous = self.previous.pop( -1 )
		for k, v in previous.items():
			if v is None: os.environ.pop( k, '' )
			else: os.environ[ k ] = v

class Stream( thing ):
	"""
	A persistent connection to an audio driver. Multiple
	output callbacks (player objects) and/or multiple 
	input callbacks (recorder objects) may share the
	same `Stream`,  or under some conditions it may be
	possible for each callback (or object) to have its
	own `Stream`.
	
	Typically, objects that play or record will
	automatically create a `Stream` or add themselves to
	an existing `Stream`, so you will not usually need to
	construct a `Stream` instance yourself.  The exception
	is when you need to ensure that the construction of
	such objects is itself fast: then, creating a `Stream`
	in advance, and keeping a reference to it to use in
	initializing the other objects, will speed things up.
	"""
	def __init__( self, device=None, mode=None, apiPreferences=None, outputCallbacks=None, sampleRate=None, sampleFormat=None, verbose=None, bufferLengthMsec=None, minLatencyMsec='auto' ):
		"""
		The `device`, `mode` and `apiPreferences` arguments are the
		same as `id`, `mode` and `apiPreferences` in `FindDevice()`.
		"""
		# TODO: make this more efficient if the device index is already known (no fussing with repeated FindDevice() calls)
		self._library = PORTAUDIO
		self.__verbose = verbose
		if self.verbose: print( '%s is being initialized' % self._short_repr() )
		self.opened = False
		self.started = False
		devspec = _DeviceSpecification( id=device, mode=mode, apiPreferences=apiPreferences )
		self._library.Initialize( minLatencyMsec=minLatencyMsec )
		possibleSampleFormats = [
			dict( ctypes=ctypes.c_float, portaudio=self._library.dll.paFloat32, numpy='float32', bytes=4 ),
		]
		if device is not None:
			device = FindDevice( devspec )
			nInputChannels  = device[ 'maxInputChannels'  ]
			nOutputChannels = device[ 'maxOutputChannels' ]
			if devspec.nonspecific:
				if nOutputChannels: devspec.minOutputChannels = nOutputChannels
				else: devspec.minInputChannels = nInputChannels
		
		if devspec.nonspecific: devspec.minOutputChannels = 2
		nInputChannels, nOutputChannels = devspec.mode
		satisfiesAll = FindDevices( devspec )
		if satisfiesAll and nInputChannels and nOutputChannels:
			self.inputDevice = self.outputDevice = satisfiesAll[ 0 ]
		else:
			self.inputDevice  = satisfiesAll[ 0 ] if satisfiesAll and nInputChannels  else FindDevice( devspec, mode=( nInputChannels,  0 ) ) if nInputChannels  else None
			self.outputDevice = satisfiesAll[ 0 ] if satisfiesAll and nOutputChannels else FindDevice( devspec, mode=( 0, nOutputChannels ) ) if nOutputChannels else None
		if nInputChannels <= 1 and nOutputChannels <= 1:
			if nInputChannels:  nInputChannels  = self.inputDevice[  'maxInputChannels'  ]
			if nOutputChannels: nOutputChannels = self.outputDevice[ 'maxOutputChannels' ]
		if not nInputChannels  or not self.inputDevice[  'maxInputChannels'  ]: self.inputDevice  = None
		if not nOutputChannels or not self.outputDevice[ 'maxOutputChannels' ]: self.outputDevice = None
		
		defaultSampleFormat = self._library.dll.paFloat32
		defaultSampleRate = min( [ device[ 'defaultSampleRate' ] for device in [ self.inputDevice, self.outputDevice ] if device is not None ] )
		if not sampleFormat: sampleFormat = defaultSampleFormat
		if not sampleRate: sampleRate = defaultSampleRate
		inParams = outParams = ctypes.POINTER( self._library.dll.struct_PaStreamParameters )()
		sampleFormat = [ d for d in possibleSampleFormats if sampleFormat in d.values() ][ 0 ]
		if nInputChannels:
			inParams  = self._library.dll.PaStreamParameters( channelCount=nInputChannels,  device=self.inputDevice[  'index' ], sampleFormat=sampleFormat[ 'portaudio' ], suggestedLatency=self.inputDevice[  'defaultLowInputLatency'  ], hostApiSpecificStreamInfo=self._library.dll.NULL ) # NB: None used as NULL
		if nOutputChannels:
			outParams = self._library.dll.PaStreamParameters( channelCount=nOutputChannels, device=self.outputDevice[ 'index' ], sampleFormat=sampleFormat[ 'portaudio' ], suggestedLatency=self.outputDevice[ 'defaultLowOutputLatency' ], hostApiSpecificStreamInfo=self._library.dll.NULL )
		
		self.__nInputChannels  = nInputChannels
		self.__nOutputChannels = nOutputChannels
		self.__sampleFormat    = sampleFormat
		self.__sampleRate      = sampleRate
		
		dtype = sampleFormat[ 'numpy' ]
		
		self._streamPtr = ctypes.c_void_p()
		
		paContinue = self._library.dll.paContinue  # paContinue, paComplete and paAbort are the possible return values from a stream callback
		paComplete = self._library.dll.paComplete
		paAbort    = self._library.dll.paAbort
		
		self._inputCallbacks = {}
		self._outputCallbacks = {}
		self._AddOutputCallback( outputCallbacks )
		
		profile = self.profile = {}
		class ProfileCM( object ):
			__enter__ = lambda self:     [ p.enable()  for p in profile.values() ]
			__exit__  = lambda self, *p: [ p.disable() for p in profile.values() ]
		profileCM = ProfileCM()
		
		inputBytesPerFrame  = nInputChannels  * sampleFormat[ 'bytes' ]
		outputBytesPerFrame = nOutputChannels * sampleFormat[ 'bytes' ]
		wrself = weakref.ref( self )
		def CallbackWrapper( inputData, outputData, frameCount, timeInfo, statusFlags, userData ):
			with profileCM:
				self = wrself()
				if not self: return paAbort
				t = timeInfo.contents.outputBufferDacTime   # fields are currentTime, inputBufferAdcTime, outputBufferDacTime
				if not t: t = timeInfo.contents.currentTime         # workaround for bug under ALSA-on-Linux
				if not t: t = timeInfo.contents.inputBufferAdcTime  # workaround for bug under ALSA-on-Linux
				# statusFlags may be a bitwise-OR combination of: paInputUnderflow, paInputOverflow, paOutputUnderflow, paOutputOverflow, paPrimingOutput
				if inputData:
					for inputCallback in list( self._inputCallbacks.values() ):
						result = inputCallback( t, inputData, frameCount, nInputChannels )
						if result is not None: inputData = result # currently, `GenericInterface.GenericRecorder._InputCallback` always returns `None`, but it could be streamlined by adding a cacheing mechanism similar to `GenericInterface.GenericPlayer._OutputCallback`
				if outputData:
					ctypes.memset( outputData, 0, frameCount * outputBytesPerFrame )
					for outputCallback in list( self._outputCallbacks.values() ):
						result = outputCallback( t, outputData, frameCount, nOutputChannels, dtype )
						if result is not None: outputData = result # the callback itself should never return `None`, but `result` can end up being `None` anyway due to `weakmethod` wrapping, below
			
				return paContinue # possible values are paContinue, paComplete, paAbort
		self._wrappedCallback = self._library.dll.PaStreamCallback( CallbackWrapper )
		
		handle = ctypes.cast( ctypes.addressof( self._streamPtr ), ctypes.POINTER( ctypes.c_void_p ) )
		
		error = self._library.dll_errorcheck.Pa_IsFormatSupported( inParams, outParams, self.__sampleRate )
		if error == self._library.dll.paInvalidSampleRate:
			self.__sampleRate = defaultSampleRate
			if self.verbose: print( '%s is changing the sample rate to %r' % ( self._short_repr(), self.__sampleRate ) )
			error = self._library.dll_errorcheck.Pa_IsFormatSupported( inParams, outParams, self.__sampleRate )
			
		if self.verbose:
			if self.inputDevice:  print( '%s will request input  device %d: %s <- %s' % ( self._short_repr(), self.inputDevice[  'index' ], self.inputDevice[  'hostApi' ][ 'name' ], self.inputDevice[  'name' ] ) )
			if self.outputDevice: print( '%s will request output device %d: %s -> %s' % ( self._short_repr(), self.outputDevice[ 'index' ], self.outputDevice[ 'hostApi' ][ 'name' ], self.outputDevice[ 'name' ] ) )
		
		if bufferLengthMsec is None:
			bufferLengthMsec = self._library.DEFAULT_BUFFER_LENGTH_MSEC
		if bufferLengthMsec == 'default':
			bufferLengthMsec = None # library default (0 will also do it)
		if bufferLengthMsec == 'auto':
			bufferLengthMsec = None
			if sys.platform.lower().startswith( 'darwin' ) and self.outputDevice and self.outputDevice[ 'hostApi' ][ 'name' ].lower().startswith( 'core audio' ):
				bufferLengthMsec = 8.5 # because the impressive latency on macOS, of around 7.5ms, is *too* low and leaves the sound vulnerable to stuttering when Python does anything else concurrently; bufferLengthMsec=8.5 puts the latency up to around 20ms
		self.__bufferLengthMsec = bufferLengthMsec

		bufferLengthSamples = int( round( self.__sampleRate * bufferLengthMsec / 1000.0 ) ) if bufferLengthMsec else self._library.dll.paFramesPerBufferUnspecified
		for attempt in range( 2 ): # TODO: this fails on Mac (hostApi = 'Core Audio') with error -9996 (paInvalidDevice) for some reason...
			error = self._library.dll_errorcheck.Pa_OpenStream( handle, inParams, outParams, self.__sampleRate, bufferLengthSamples, self._library.dll.paNoFlag, self._wrappedCallback, self._library.dll.NULL )
			if self.verbose and ( error or attempt ): print( 'error on Pa_OpenStream attempt #%d: %r' % ( attempt + 1, error ) )
			if not error: break
			if error != -997: break
		if error: # TODO: ...so we have to fall back on this, which ideally we would prefer not to use
			error = self._library.dll_errorcheck.Pa_OpenDefaultStream( handle, nInputChannels, nOutputChannels, sampleFormat[ 'portaudio' ], self.__sampleRate, bufferLengthSamples, self._wrappedCallback, self._library.dll.NULL )
			if not error:
				if self.verbose: print( 'Pa_OpenStream failed, but Pa_OpenDefaultStream succeeded.' )
				defaultApi = GetHostApiInfo()[ self._library.dll.Pa_GetDefaultHostApi() ]
				devices = GetDeviceInfo()
				if nInputChannels:  self.inputDevice  = devices[ defaultApi[ 'defaultInputDevice'  ] ]
				if nOutputChannels: self.outputDevice = devices[ defaultApi[ 'defaultOutputDevice' ] ]
				# TODO: check whether these represent a change relative to what was requested, and issue a warning if so
			
		self.opened = not error
		self.started = self.opened and self._library.dll_errorcheck.Pa_StartStream( self._streamPtr ) == 0
		
	def StartProfiling( self, **types ):
		self.profile.clear()
		if not types: types = { 'cProfile' : True }
		for type, value in types.items():
			if not value: continue
			if type in [ 'profile', 'cProfile' ]:
				self.profile[ type ] =cProfile.Profile()
			elif type == 'line_profiler':
				import line_profiler
				if not callable( value ): raise ValueError( 'line_profiler option expects a callable, e.g. line_profiler=playerInstance._OutputCallback' )
				self.profile[ type ] = line_profiler.LineProfiler( value )
			else:
				raise TypeError( 'unknown profiler module %r' % type )
		
	def StopProfiling( self ):
		for key, profiler in self.profile.items():
			if key == 'cProfile': pstats.Stats( profiler ).sort_stats( 'cumtime' ).print_stats( 25 )
			if key == 'line_profiler': profiler.print_stats()
			print( '' )
		self.profile.clear()
		
	@property
	def bufferLengthMsec( self ):
		return self.__bufferLengthMsec
	@property
	def minLatencyMsec( self ):
		"""
		The value of the `PA_MIN_LATENCY_MSEC` environment
		variable at the time the PortAudio library was loaded
		"""
		return self._library.minLatencyMsec
	@property
	def verbose( self ):
		if self.__verbose is not None: return self.__verbose
		return self._library.verbose if self._library else False
	@verbose.setter
	def verbose( self, value ):
		self.__verbose = value
			
	def _AddOutputCallback( self, *callbacks ):
		AddCallbacks( self._outputCallbacks, *callbacks )
		return self
		
	def _RemoveOutputCallback( self, *keyObjects ):
		return RemoveCallbacks( self._outputCallbacks, *keyObjects )
		
	def _AddInputCallback( self, *callbacks ):
		AddCallbacks( self._inputCallbacks, *callbacks )
		return self
		
	def _RemoveInputCallback( self, *keyObjects ):
		return RemoveCallbacks( self._inputCallbacks, *keyObjects )

	def __del__( self ):
		verbose = self.verbose
		if verbose > 1: print( '%s is being deleted (stage 0)' % self._short_repr() )
		elif verbose: print( '%s is being deleted' % self._short_repr() )
		if self.started:
			try: stop = self._library.dll.Pa_StopStream
			except: pass
			else: callable( stop ) and stop( self._streamPtr )
		self.started = False
		if verbose > 1: print( '%s is being deleted (stage 1)' % self._short_repr() )
		if self.opened:
			try: close = self._library.dll.Pa_CloseStream
			except: pass
			else: callable( close) and close( self._streamPtr )
		self.opened = False
		if verbose > 1: print( '%s is being deleted (stage 2)' % self._short_repr() )
		self._library = None
	
	@property
	def sampleRate( self ): return self.__sampleRate
	fs = sampleRate
	
	@property
	def sampleFormat( self ): return self.__sampleFormat
	
	@property
	def nInputChannels( self ): return self.__nInputChannels
	
	@property
	def nOutputChannels( self ): return self.__nOutputChannels
	
def AddCallbacks( container, *callbacks ):
	callbacks = [ callback for item in callbacks for callback in ( item if isinstance( item, ( tuple, list ) ) else [ item ] if item else [] ) ]
	for callback in callbacks:
		if hasattr( callback, '__self__' ):
			key = id( callback.__self__ )
			wrself = weakref.ref( callback.__self__ )
			func = callback.__func__
			# NB: do not decorate with functools.wraps( callback ) because that will increment the reference count
			def weakmethod( *pargs, **kwargs ):
				self = wrself()
				if self is not None:
					return func( self, *pargs, **kwargs )
			callback = weakmethod
		else:
			key = id( callback )
		container[ key ] = callback
		
def RemoveCallbacks( container, *keyObjects ):
	keyObjects = [ keyObject for item in keyObjects for keyObject in ( item if isinstance( item, ( tuple, list ) ) else [ item ] if item else [] ) ]
	for keyObject in keyObjects: container.pop( id( keyObject ), None )
	return len( container )

def SetDefaultVerbosity( value ):
	"""
	Useful for debugging when the PortAudio library is
	initialized or terminated, when streams are opened,
	started, stopped or closed, and when other objects
	such as players or recorders are initialized or
	garbage-collected.   Objects may be individually
	marked as `.verbose=True` or `.verbose=False`, but
	by default they inherit their verbosity from the
	setting you specify here.
	"""
	PORTAUDIO.verbose = value

class Bunch( dict ):
	def __getattr__( self, name ):
		b = self
		for name in name.split( '.' ): b = b[ name ] if name in b else getattr( super( b.__class__, b ), name ) if isinstance( b, Bunch ) else getattr( b, name )
		return b
	def __setattr__( self, name, value ):
		if name.startswith( '_' ): return dict.__setattr__( self, name, value )
		container = self
		parts = name.split( '.' )
		for name in parts[ :-1 ]:
			try: container = getattr( container, name )
			except: sub = container[ name ] = self.__class__(); container = sub
		container.__setitem__( parts[ -1 ], value )
	def __dir__( self ): return self.keys()
	_getAttributeNames = __dir__
	def __repr__( self ): return self._report()
	_display_sorted = tuple( sys.version_info ) < ( 3, 0 )
	def _report( self, indent=0, minColonPosition=0, sortUnknownKeys=None ):
		s = ' ' * indent + '{\n'
		keys = list( self.keys() )
		order = getattr( self, '_fieldOrder', '' )
		known = order.replace( '/', '' ).split()
		order = order.split()
		unknown = [ key for key in keys if key not in known ]
		if sortUnknownKeys or ( sortUnknownKeys is None and self._display_sorted ): unknown.sort()
		keys = [ key for key in order if key.strip( '/' ) in keys ] + unknown
		maxLen = max( len( repr( key ) ) for key in keys ) if keys else 0
		indentIncrement = 4
		minColonPosition = max( minColonPosition - indentIncrement, maxLen + indent + indentIncrement + 1 )
		#minColonPosition = max( minColonPosition, maxLen + indent + indentIncrement + 1 )
		#minColonPosition = maxLen + indent + indentIncrement + 1
		for key in keys:
			if key.startswith( '//' ): s += '\n'
			key = key.strip( '/' )
			krepr = repr( key )
			spaces = minColonPosition - len( krepr ) - 1
			spacesBefore = indent + indentIncrement
			#spacesBefore = spaces
			spacesAfter = spaces - spacesBefore
			s += ' ' * spacesBefore + krepr + ' ' * spacesAfter + ' : '
			value = self[ key ]
			if hasattr( value, '_report' ): s += '\n' + value._report( indent=indent + indentIncrement, minColonPosition=minColonPosition + indentIncrement, sortUnknownKeys=sortUnknownKeys ).rstrip()
			else: s += repr( value ).strip()
			s += ',\n'
		s += ' ' * ( indent ) + '}'
		return s		
	def _write( self, filename ):
		open( filename, 'wt' ).write( self._report() )
	@classmethod
	def _read( cls, filename ):
		return cls._convert( ast.literal_eval( open( filename, 'rt' ).read() ) )
	@classmethod
	def _convert( cls, d ):
		return cls( { k : cls._convert( v ) for k, v in d.items() } ) if isinstance( d, dict ) and not isinstance( d, cls ) else d

def Tabulate( records, *fields ):
	"""
	Returns a pretty-printed table of the specified `fields`
	(i.e. dictionary entries or attributes) of a list of
	records.  This is called automatically, with certain
	default combinations of field names, when you `print()`
	the results of `GetHostApiInfo()`, `GetDeviceInfo()`
	or `FindDevices()`.
	"""
	fields = [ field for item in fields for field in ( item if isinstance( item, ( tuple, list ) ) else item.split() if isinstance( item, str ) else [] if item is None else [ item ] ) ]
	if not fields:
		if not records: return '(no entries)'
		fields = getattr( records, '_fieldsToTabulate', None )
		if isinstance( fields, str ): fields = fields.split()
		if not fields: raise ValueError( 'no fields specified' )
	sep = '  '
	if not records: return sep.join( fields )
	def render( x, format=None ):
		if not format and isinstance( x, float ): format = '%g'
		if format: return ( format % x ) if '%' in format else format
		return '-' if x is None else str( x )
	def getfield( record, field ):
		try: return record[ field ]
		except: pass
		try: return getattr( record, field )
		except: pass
	fields = [ field.strip() for field in fields ]
	headings, fields = zip( *[ field.split( '=', 1 ) if '=' in field else [ field, field ] for field in fields ] )
	fields,  formats = zip( *[ field.split( ':', 1 ) if ':' in field else [ field, None  ] for field in fields ] )
	table = [ headings ] + [ [ render( getfield( record, field ), format ) for field, format in zip( fields, formats ) ] for record in records ]
	lengths = [ [ len( cell ) for cell in row ] for row in table ]
	lengths = [ max( column ) for column in zip( *lengths ) ]
	return '\n'.join( sep.join( '%-*s' % pair for pair in zip( lengths, row ) ) for row in table )
	
class ListOfHostApiRecords( list ):
	_fieldsToTabulate = 'index name isDefault defaultInputDevice defaultOutputDevice'.split()
	__str__ = Tabulate
class ListOfDeviceRecords( list ):
	_fieldsToTabulate = 'hostApi.name index name maxInputChannels maxOutputChannels defaultSampleRate'.split()
	__str__ = Tabulate
