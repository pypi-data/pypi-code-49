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
This sub-module provides an alternative back-end for high-
precision playback, based on the PsychToolbox project's reworking
of the PortAudio binaries.  It requires the third-party
`psychtoolbox` module to be installed (you must do this yourself,
for example by running `python -m pip install psychtoolbox`,
because `psychtoolbox` is not a hard/automatically-installed
dependency of `audiomath`.

This alternative back-end can be enabled by calling
`audiomath.BackEnd.Load('PsychToolboxInterface')`. This removes
the default `audiomath.PortAudioInterface.*` symbols from the
top-level `audiomath.*` namespace and replaces them with
`audiomath.PsychToolboxInterface.*` symbols, most of which have
names and prototypes that are familiar from the default back-end
(`Player`, `Stream`, `FindDevices`, etc...)

Extra features:
	
	- The `latencyClass` input parameter to `Player` and `Stream`
	  constructors. This is only respected for the first such 
	  construction call, since the same `Stream` will be shared
	  by all `Player` instances). The supported settings are all
	  attributes of the `LATENCY_CLASS` enumerator. The higher
	  the number, the more aggressively (and less cooperatively)
	  the host API will drive the sound device, and the lower
	  the latency is likely to get.
	  
	- The ability to pre-schedule sounds with the `when` argument,
	  e.g. `now = Seconds(); p.Play(when=now + 0.5)`

Limitations, relative the the default `PortAudioInterface`:

	- cannot `.Seek(t)` to any position except the beginning `t=0`
	  (likewise `.Play(t)`, `.Pause(t)` or `.Set(head=t)` will only
	  work with `t=0`)
	
	- no channel-by-channel control of volumes (`.pan` or `.levels`)
	
	- no on-the-fly resampling or `.speed` control
	
	- no dynamic properties
	
	- no `Recorder` implementation

Notes:

	- on Windows, PsychToolbox uses the WASAPI host API by
	  default. For best performance, and especially if you want to
	  use `latencyClass < 2` (such that other processes can access
	  the sound device at the same time) then you should ensure
	  your sounds are sampled at 48000 Hz, not the usual 44100 Hz.
	  
	- some host APIs may be unable to be driven with certain
	  latency classes (for example, in our experience Windows
	  WDM-KS cannot handle a latency class higher than 1)
"""

"""	
TODO:

	- figure out a workaround for `.volume_channels` brokenness, to allow `.levels` and
	  `.pan` to work.
	  
	- figure out a way to `.Seek()` ? PsychoPy seems to have an analogous `.seek()` method
	  but it's unclear from the code whether it does anything.
	  
Compatibility, as at 20200130:

	- On macOS, `pip install psychtoolbox` fails with::

	      clang: error: no such file or directory: 'PsychSourceGL/Cohorts/PortAudio/libportaudio_osx_64.a'

	  (see also https://github.com/Psychtoolbox-3/Psychtoolbox-3/issues/587#issuecomment-566547575 )

	  However, `pip install -e` worked with PsychToolbox-3 repo commit deba01649.

	- On Windows it seems possible to install `psychtoolbox` for Python 3.7 but not 3.8:
	  under 3.8, a normal `pip` install fails complaining about the lack of a `libusb`
	  library, and an editable install succeeds but two out the four resulting `.pyd`
	  files are unimportable, seemingly lacking (the path to?) some DLL dependency that
	  they need to load at import time.

Performance, as at 20200208:

	- On macOS, PTB gave latencies even lower (~3ms) than the already very low (~5ms)
	  macOS Core-Audio latencies under vanilla PortAudio.

	- On Windows 10, there's no advantage in terms of absolute latency, at least
	  from the many onboard cards tested in early 2020.  Using PTB's default host API
	  (WASAPI) at its preferred sampling frequency (48000) with latency class 3, the
	  latency was around 17ms, which is the same as you get from vanilla PortAudio
	  using WDM-KS at 44100Hz. The main advantage to PTB, then, is the ability to
	  pre-schedule.
	  
	- On Ubuntu, `sudo apt install libusb-1.0.0-dev portaudio19-dev libasound-dev`
	  were necessary (over and above the base Shady-development system) to allow
	  `python3 pip install psychtoolbox` to succeed.
"""


__all__ = [
	'PORTAUDIO',
	'GetHostApiInfo', 'GetDeviceInfo',
	'FindDevices', 'FindDevice',
	'LATENCY_CLASS', 'Stream',
	'Player',
	'Recorder', 'Record',
	'Seconds', # the PTB-specific clock that allows pre-scheduling of playback via the `when` option
]

import os

from . import DependencyManagement
ptb_audio =  DependencyManagement.Import( 'psychtoolbox.audio', packageName='psychtoolbox' )
PsychPortAudio = ptb_audio.PsychPortAudio  # triggers exception if dependency import failed

import psychtoolbox as ptb; DependencyManagement.RegisterVersion( ptb )
from psychtoolbox import GetSecs as Seconds
ppa_version = PsychPortAudio( 'Version' )
DependencyManagement.RegisterVersion( name='PsychPortAudio', value=( ppa_version[ 'version' ], ppa_version[ 'date' ], ppa_version[ 'time' ] ) )


from .GenericInterface import GenericPlayer, GenericRecorder
from . import _wrap_portaudio as wpa # we won't use the binary from here - this is imported exclusively for the pure-Python logic that filters device records and/or pretty-prints things

SINGLE_OUTPUT_STREAM = True


def adopt( func ):
	func.__doc__ = getattr( wpa, func.__name__ ).__doc__
	return func
	
@adopt
def FindDevice( id=None, mode=None, apiPreferences=None, _candidates=None ):
	return wpa.FindDevice( id=id, mode=mode, apiPreferences=apiPreferences, _candidates=GetDeviceInfo )

@adopt
def FindDevices( id=None, mode=None, apiPreferences=None, _candidates=None ):
	return wpa.FindDevices( id=id, mode=mode, apiPreferences=apiPreferences, _candidates=GetDeviceInfo )

@adopt
def GetHostApiInfo():
	dd = ptb_audio.get_devices()
	dd = [ wpa.Bunch( # a subset of the wpa.GetHostApiInfo() fields
		index = int( d[ 'HostAudioAPIId' ] ),
		name = d[ 'HostAudioAPIName' ],
		_fieldOrder = 'index name', 
	) for d in dd ]
	dd = { frozenset( d.items() ) : d for d in dd }.values()
	dd = wpa.ListOfHostApiRecords( sorted( dd, key=lambda d: d[ 'index' ] ) )
	return dd
	
@adopt
def GetDeviceInfo():
	dd = ptb_audio.get_devices()
	dd = wpa.ListOfDeviceRecords( wpa.Bunch( # a subset of the wpa.GetDeviceInfo() fields
		index = int( d[ 'DeviceIndex' ] ),
		name = d[ 'DeviceName' ],
		defaultSampleRate = float( d[ 'DefaultSampleRate' ] ),
		maxInputChannels = d[ 'NrInputChannels' ],
		defaultLowInputLatency = d[ 'LowInputLatency' ],
		defaultHighInputLatency = d[ 'HighInputLatency' ],
		maxOutputChannels = d[ 'NrOutputChannels' ],
		defaultLowOutputLatency = d[ 'LowOutputLatency' ],
		defaultHighOutputLatency = d[ 'HighOutputLatency' ],
		hostApi = wpa.Bunch( index = int( d[ 'HostAudioAPIId' ] ), name = d[ 'HostAudioAPIName' ] ),
		_fieldOrder = 'index name defaultSampleRate //maxInputChannels defaultLowInputLatency defaultHighInputLatency //maxOutputChannels defaultLowOutputLatency defaultHighOutputLatency //hostApi',
	) for d in dd )
	return dd

class Library( object ):
	# dummy object, just to duck-type our own wpa.PORTAUDIO object
	# and provide a (crude) Initialize() method
	def Initialize( self, minLatencyMsec='auto' ):
		# Less sophisticated than the original, in that it makes a lasting change to the environment
		# Probably ineffectual anyway---PsychPortAudio may not use this setting at all
		auto = False
		if isinstance( minLatencyMsec, str ):
			minLatencyMsec = minLatencyMsec.lower()
			if minLatencyMsec in [ 'none', '' ]: minLatencyMsec = None
			auto = minLatencyMsec in [ 'auto' ]
		if auto: pass
		elif minLatencyMsec is None: os.environ.pop( 'PA_MIN_LATENCY_MSEC', None )
		else: os.environ[ 'PA_MIN_LATENCY_MSEC' ] = str( minLatencyMsec )
PORTAUDIO = Library()

class LATENCY_CLASS( object ):
	RELAXED = 0
	SHARED = 1
	EXCLUSIVE = 2
	AGGRESSIVE = DEFAULT = 3
	CRITICAL = 4

class Stream( wpa.thing, ptb_audio.Stream ):
	_classNamePrefix = __module__ + '.'
	#_classNamePrefix = __module__.split( '.' )[ -1 ] + '.'
	def __init__( self, device=(), mode=None, sampleRate=None, latencyClass='DEFAULT', verbose=False, bufferLengthMsec=None, minLatencyMsec='auto' ):
		self.verbose = verbose
		if not verbose: ptb_audio.verbosity( 2 ) # warnings & errors
		if not mode: mode = 'oo'
		if isinstance( mode, str ): mode = ( mode.lower().count( 'i' ), mode.lower().count( 'o' ) )
		nInputChannels, nOutputChannels = mode
		nOutputChannels = max( 1, nOutputChannels )
		if nInputChannels or not nOutputChannels: raise ValueError( 'PTB Streams can only be used for output' )
		if isinstance( device, dict ): device = device[ 'index' ]
		if sampleRate is None: sampleRate = 44100
		self.__fs = sampleRate
		
		if isinstance( latencyClass, str ): latencyClass = getattr( LATENCY_CLASS, latencyClass.upper() )
		self.__latencyClass = latencyClass
		
		buffer_size = []
		if bufferLengthMsec is not None:
			raise NotImplementedError( 'bufferLengthMsec must be None (TODO: support for other values is not yet implemented)' )
		self.__bufferLengthMsec = bufferLengthMsec

		previousEnvMinLatencyMsec = os.environ.get( 'PA_MIN_LATENCY_MSEC', None )
		if minLatencyMsec == 'auto': minLatencyMsec = previousEnvMinLatencyMsec # TODO: could try 20 on Windows...
		if isinstance( minLatencyMsec, str ): minLatencyMsec = minLatencyMsec.lower() 
		if minLatencyMsec in [ None, 'none', '' ]: os.environ.pop( 'PA_MIN_LATENCY_MSEC', None )
		else: os.environ[ 'PA_MIN_LATENCY_MSEC' ] = str( minLatencyMsec )
		self.__minLatencyMsec = None if minLatencyMsec is None else float( minLatencyMsec )
			
		# NB: `mode=9` is necessary black magic copied from the PsychoPy wrapper, which adds
		#     8 to the default `mode` value of 1---no idea what 1 means, what the extra 8
		#     means, or what other values might do.
		ptb_audio.Stream.__init__( self, device_id=device, mode=9, latency_class=latencyClass, freq=sampleRate, channels=nOutputChannels, buffer_size=buffer_size, suggested_latency=[], select_channels=[], flags=0)
		self.start( repetitions=0, when=0, wait_for_start=1 ) # this line is also necessary black magic
		
		if previousEnvMinLatencyMsec is None: os.environ.pop( 'PA_MIN_LATENCY_MSEC', None )
		else: os.environ[ 'PA_MIN_LATENCY_MSEC' ] = previousEnvMinLatencyMsec
		
		devices = GetDeviceInfo()
		status = self.status
		inputDeviceIndex  = status[  'InDeviceIndex' ]
		outputDeviceIndex = status[ 'OutDeviceIndex' ]
		self.inputDevice  = None if  inputDeviceIndex < 0 else devices[ int(  inputDeviceIndex ) ]
		self.outputDevice = None if outputDeviceIndex < 0 else devices[ int( outputDeviceIndex ) ]
		self.nInputChannels  = nInputChannels
		self.nOutputChannels = nOutputChannels
		
	@ptb_audio.Stream.volume.getter
	def volume( self ):
		vol = PsychPortAudio( 'Volume', self.handle )
		try: vol = vol[ 0 ]
		except: pass  # bugfix relative to psychtoolbox.audio.Stream from psychtoolbox 3.0.16  (pip-installed 20200128)
		return vol
	
	@property
	def fs( self ): return self.__fs
	@property
	def minLatencyMsec( self ): return self.__minLatencyMsec
	@property
	def bufferLengthMsec( self ): return self.__bufferLengthMsec
	@property
	def latencyClass( self ): return self.__latencyClass

class Player( GenericPlayer ):
	_classNamePrefix = Stream._classNamePrefix
	def __init__( self, sound, device=None, stream=None, latencyClass='DEFAULT', bufferLengthMsec=None, minLatencyMsec='auto', fs=None, resample=True, verbose=None, **kwargs ):
		self.__verbose = verbose
		self.__stream = None
		self.__slave = None
		self.__sound = None
		self.__nextSample = 0
		if self.verbose: print( '%s is being initialized' % self._short_repr() )
		if stream is None and device is not None: stream = device
		if device is None and stream is not None: device = stream
		if device != stream: raise ValueError( 'the `stream` and `device` arguments are synonymous---they cannot take different values unless one is left as `None`' )
		super( Player, self ).__init__( sound=sound, **kwargs )
		global SINGLE_OUTPUT_STREAM
		alreadyInitialized = isinstance( SINGLE_OUTPUT_STREAM if SINGLE_OUTPUT_STREAM else stream, Stream )
		if alreadyInitialized and SINGLE_OUTPUT_STREAM: stream = SINGLE_OUTPUT_STREAM
		if not alreadyInitialized:
			stream = Stream(
				device = device,
				sampleRate = fs if fs else self.sound.fs if self.sound else 44100,
				mode = ( 0, self.sound.nChannels if self.sound else 2),
				latencyClass = latencyClass,
				bufferLengthMsec = bufferLengthMsec,
				minLatencyMsec = minLatencyMsec,
			)
		if SINGLE_OUTPUT_STREAM: SINGLE_OUTPUT_STREAM = stream
		self.__stream = stream
		self.when = None
		self.resume = True
		if self.sound and self.sound.fs != self.stream.fs:
			if resample: self.sound = self.sound.Copy().Resample( self.stream.fs )
			else: raise ValueError( 'sound sampling frequency (%g Hz) does not match stream sampling frequency (%g Hz) - create the Player with resample=True to get around this' )
		else:
			self.sound = self.sound

	@property
	def stream( self ):
		return self.__stream
		
	@property
	def fs( self ):
		return self.__stream.fs
		
	@property
	def verbose( self ):
		if self.__verbose is not None: return self.__verbose
		return self.__stream.verbose if self.__stream else False
	@verbose.setter
	def verbose( self, value ):
		self.__verbose = value

	@property
	def volume( self ): return self.__stream.volume
	@volume.setter
	def volume( self, value ): self.__stream.volume = value
	vol = volume
	
	@property
	def _playing( self ):
		slave = self.__slave
		if not slave: return False
		status = slave.status
		if status.get( 'Active', 0 ): return True
		if status.get( 'State',  0 ): return True
		return False
	@_playing.setter
	def _playing( self, value ): # called by superclass .Play(), .Pause() et al.
		slave = self.__slave
		if not slave: return
		status = slave.status
		alreadyPlaying = status.get( 'Active', 0 ) or status.get( 'State', 0 )
		if bool( value ) == bool( alreadyPlaying ): return
		if value:
			when, self.when = self.when, None
			resume, self.resume = self.resume, False
			slave.start(
				repetitions = 0 if self.loop else 1,
				when = when if when else 0,
				resume = 1 if resume else 0,
			)
		else:
			self.resume = True
			slave.stop()
	
	@property
	def _nextSample( self ): return self.__nextSample
	@_nextSample.setter
	def _nextSample( self, value ): # called by superclass .Play(t), .Pause(t), .Seek(t), .Set(head=t)
		slave = self.__slave
		status = slave.status if slave else {}
		alreadyPlaying = status.get( 'Active', 0 ) or status.get( 'State', 0 )
		self.__nextSample = value
		if value == 0: # can rewind to start with .Play(0) or head=0 or .Seek(0) ...
			self.resume = False
			if alreadyPlaying:
				slave.stop( block_until_stopped=1 )
				self._playing = True
		else: # ...but cannot Seek() to any other position (TODO?)
			self.resume = True
	
	@GenericPlayer.sound.setter
	def sound( self, value ):
		GenericPlayer.sound.fset( self, value )
		# TODO: watch out for sample-rate mismatches
		value = self.sound
		data = None
		if value:
			data = value.y
			if self.__stream:
				nChannelsInStream = self.__stream.nOutputChannels
				nSamples, nChannels = data.shape
				if nChannels > nChannelsInStream: data = data[ :, :nChannelsInStream ]
				elif nChannels == 1 and nChannelsInStream > nChannels: data = data[ :, [ 0 ] * nChannelsInStream ]
		if self.__slave:
			self.__slave.stop()
			if data is not None: self.__slave.fill_buffer( data, start_index=1 ) # why 1? black magic
		elif self.__stream:
			if data is not None: self.__slave = ptb_audio.Slave( self.__stream.handle, data=data, volume=self.volume )

	@property
	def minLatencyMsec( self ): return self.__stream.minLatencyMsec
	@property
	def bufferLengthMsec( self ): return self.__stream.bufferLengthMsec
	@property
	def latencyClass( self ): return self.__stream.latencyClass

class Recorder( GenericRecorder ):
	_classNamePrefix = Stream._classNamePrefix
	def __init__( self, *p, **k ):
		raise NotImplementedError( 'TODO: no Recorder implementation yet in the %s back-end' % self.__module__ )
Record = Recorder.MakeRecording
