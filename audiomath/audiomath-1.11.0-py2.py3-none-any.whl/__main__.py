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
If no options are supplied, `-s` is assumed---i.e., an IPython
shell will be opened on the console, with `audiomath` and `numpy`
already imported (both under their full names and under their
respective abbreviated names, `am` and `np`).

If options are supplied, the shell will not be opened unless the
`-s` option is explicitly present among them.
"""
import time
import argparse

import audiomath, audiomath as am
		
parser = argparse.ArgumentParser( prog='python -m ' + __package__, description=__doc__ )
parser.add_argument( "-v", "--version", action='store_true', default=False, help='print the version number' )
parser.add_argument( "-V", "--versions", action='store_true', default=False, help='print package and dependency version information' )
parser.add_argument( "-a", "--apis", "--host-apis", action='store_true', default=False, help='print a list of host APIs' )
parser.add_argument( "-l", "--list-devices", "--devices", action='store_true', default=False, help='print a list of devices' )
parser.add_argument( "-2", "--twoChannelTest", action='store_true', default=False, help='same as -t2, i.e. play a 2-channel test stimulus on an endless loop' )
parser.add_argument( "-8", "--eightChannelTest", action='store_true', default=False, help='same as -t8, i.e. play an 8-channel test stimulus on an endless loop' )
parser.add_argument( "-t", "--test",  metavar='NUMBER_OF_CHANNELS', action='store', default=0, type=int, help='play a test stimulus with the specified number of channels (up to 8) on an endless loop' )
parser.add_argument( "-s", "--shell", action='store_true', default=False, help='open an IPython shell, even if other flags are supplied' )
parser.add_argument( "-d", "--device",  metavar='DEVICE_INDEX',  action='store', default=None, help='specify which device should be used for playback in the --eightChannelTest' )
parser.add_argument(       "--install-ffmpeg",  metavar='PATH_TO_FFMPEG_BINARY',  action='store', default=None, type=str, help='call `ffmpeg.Install()` on the specified path' )
parser.add_argument(       "--install-sox",  metavar='PATH_TO_SOX_BINARY', action='store', default=None, type=str, help='call `sox.Install()` on the specified path' )
parser.add_argument( "-g", "--glitch-test",  "--tone-test", metavar='PARAMS', action='store', default='', help='generate and play a seamlessly looped tone. PARAMS can be `SAMPLING_FREQUENCY:BUFFER_LENGTH_MSEC`, or just `SAMPLING_FREQUENCY` or `:BUFFER_LENGTH_MSEC`, or  even just `:` to use default values' )
parser.add_argument(       "--ptb", "--psychtoolbox", metavar='DEFAULT_LATENCY_CLASS',  action='store', default=None, help='if omitted, use the default back-end. If supplied, use the "PsychToolboxInterface" back-end, and set its default latency class to the specified value.' )
args = parser.parse_args()

openShell = True
player = None
playerName = 'p'
tone = None
toneName = 't'

if args.ptb:
	latencyClass = args.ptb
	if latencyClass.lower() in [ 'psychopy', '-3' ]:
		am.BackEnd.Load( 'PsychoPyInterface' )
		am.LATENCY_CLASS.DEFAULT = -3
	else:
		am.BackEnd.Load( 'PsychToolboxInterface' )
		if latencyClass == '': latencyClass = 'DEFAULT'
		try: latencyClass = int( latencyClass )
		except: latencyClass = getattr( am.LATENCY_CLASS, latencyClass.upper() )
		am.LATENCY_CLASS.DEFAULT = latencyClass

if args.version:
	openShell = args.shell
	print( am.__version__ )

if args.versions:
	openShell = args.shell
	print( '' )
	am.ReportVersions()

if args.apis:
	openShell = args.shell
	print( '' )
	print( am.GetHostApiInfo() )

if args.list_devices:
	openShell = args.shell
	print( '' )
	print( am.GetDeviceInfo() )

if args.eightChannelTest and not args.test: args.test = 8
if args.twoChannelTest   and not args.test: args.test = 2

if args.glitch_test:
	openShell = args.shell
	parameters = args.glitch_test.replace( ':', '+' ).split( '+' )
	fs = bufferLengthMsec = ''
	if len( parameters ) >= 1: fs = parameters[ 0 ]
	if len( parameters ) >= 2: bufferLengthMsec = parameters[ 1 ]
	fs = None if fs.lower() == 'none' else None if not fs else float( fs )
	bufferLengthMsec = None if bufferLengthMsec.lower() == 'none' or args.ptb else 'auto' if not bufferLengthMsec else float( bufferLengthMsec )
	tone = am.ToneTest( fs=fs, bufferLengthMsec=bufferLengthMsec, verbose=False, playing=True, device=args.device )
	print( tone._report( with_repr='short', indent=toneName + ' = ' ) )
	if not openShell and not args.test:
		tone.WaitFor( am.Prompt( 'press return to stop/exit: ' ), False )
		del tone; time.sleep( 0.25 )
	
if args.test:
	openShell = args.shell
	player = am.Player( am.TestSound( list( range( args.test ) ) ), device=args.device )
	print( player._report( with_repr='short', indent=playerName + ' = ' ) )
	if openShell:
		player.Play( loop=True, wait=False )
	else:
		player.Play( loop=True, wait=False )
		player.WaitFor( am.Prompt( 'press return to stop/exit: ' ), False )
		if tone: del tone
		del player; time.sleep( 0.25 )

if args.install_ffmpeg:
	openShell = args.shell
	try: am.ffmpeg.Install( args.install_ffmpeg )
	except Exception as err: sys.sterr.write( '%s\n' % err )

if args.install_sox:
	openShell = args.shell
	try: am.sox.Install( args.install_sox )
	except Exception as err: sys.sterr.write( '%s\n' % err )

if openShell:
	def Shell():
		if player: locals()[ playerName ] = player
		if tone: locals()[ toneName ] = tone
		import os, sys, time, IPython, numpy, numpy as np, audiomath, audiomath as am
		del sys.argv[ 1: ]
		print( '' )
		IPython.start_ipython( user_ns=locals() )	
	Shell()
