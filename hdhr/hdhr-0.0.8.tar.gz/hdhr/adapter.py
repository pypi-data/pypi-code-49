
import logging
import re

from ctypes import *
from sys import exit
from socket import inet_aton
from time import time
from collections import deque
from struct import unpack

from hdhr.adapter_types import *
from hdhr.externals import *
from hdhr.types import *
from hdhr.constants import *

from hdhr.utility import ascii_bytes, ip_ascii_to_int

_LOGGER = logging.getLogger(__name__)

class OperationRejectedError(Exception):
    """Indicates that the current operation was rejected by the remote device."""
    pass

def error_for_result(result, message):
    if result == 0:
        return OperationRejectedError(message)
    elif result == -1:
        return ConnectionError(message)
    else:
        return Exception(message)

class HdhrUtility(object):
    """Calls that don't require a device entity."""

    @staticmethod
    def get_channel_maps():
        return MAP_LIST

    @staticmethod
    def discover_find_devices_custom(ip=None):
        """Discover tuner devices."""

        try:
            ip_int = ip_ascii_to_int(ip) if ip else 0
        except:
            _LOGGER.exception("Could not convert IP [%s] to integer." % (ip))
            raise

        _LOGGER.debug("Discovering devices.  MAX= (%d)  IP= [%s]" % 
                     (MAX_DEVICES, ip if ip_int else 0))

        devices = (TYPE_hdhomerun_discover_device_t * MAX_DEVICES)()

        try:
            num_found = CFUNC_hdhomerun_discover_find_devices_custom(
                            ip_int, 
                            HDHOMERUN_DEVICE_TYPE_TUNER, 
                            HDHOMERUN_DEVICE_ID_WILDCARD, 
                            devices, 
                            MAX_DEVICES
                        )
        except:
            _LOGGER.exception("Library call to discover devices failed.")
            raise

        if num_found == -1:
            message = ("Device discovery failed (%d), but this could be due to" 
                       " lack of connectivity." % (num_found))

            _LOGGER.warn(message)
            return []

        _LOGGER.debug("(%d) devices found." % (num_found))

        return devices[0:num_found]

    @staticmethod
    def device_create_from_str(device_str):
        """Create a device-object to manipulate a specific device with."""

        _LOGGER.debug("Creating device-entity for device [%s]." % (device_str))

        try:
            device = CFUNC_hdhomerun_device_create_from_str(ascii_bytes(device_str), 
                                                            None
                                                           )
        except:
            _LOGGER.exception("Library call to create device entity failed.")
            raise

        if not device:
            message = "Could not build device entity."
            
            _LOGGER.exception(message)
            raise Exception(message)

        return device.contents

    @staticmethod
    def get_channels_in_range(channel_map):
        """Determine the maximum number of channels available."""

        _LOGGER.debug("Calculating channels count.")
    
        try:
            channel_list = CFUNC_hdhomerun_channel_list_create(channel_map)
        except:
            _LOGGER.exception("Could not create channel-list entity for range "
                              "check.")
            raise

        if not channel_list:
            message = "Could not build channel-list."
            
            _LOGGER.error(message)
            raise Exception(message)

        try:
            count = CFUNC_hdhomerun_channel_list_total_count(channel_list)
        except:
            _LOGGER.exception("Could not produce channel count.")
            raise
        else:
            return count
        finally:
            try:
                CFUNC_hdhomerun_channel_list_destroy(channel_list)
            except:
                _LOGGER.exception("Could not destroy channel-list entity.")
                raise

class HdhrDeviceQuery(object):
    """Device-specific queries."""

    hd = None

    def __init__(self, hd):
        self.hd = hd

    def __del__(self):
        try:
            CFUNC_hdhomerun_device_destroy(self.hd)
        except:
            _LOGGER.exception("Could not destroy device-entity object.")
            raise

    def get_hw_model_str(self):
        """Get the hardware model of the device."""

        _LOGGER.debug("Doing device_get_hw_model_str call for device [%s]." % 
                     (self.hd))

        try:
            result = CFUNC_hdhomerun_device_get_hw_model_str(
                            self.hd
                        )
        except:
            _LOGGER.exception("Could not get hardware model string.")
            raise

        return ascii_str(result) if result is not None else None

    def get_model_str(self):
        """Get the model of the device."""

        _LOGGER.debug("Doing device_get_model_str call for device [%s]." % 
                     (self.hd))

        try:
            result = CFUNC_hdhomerun_device_get_model_str(
                            self.hd
                        )
        except:
            _LOGGER.exception("Could not get model string.")
            raise

        return ascii_str(result) if result is not None else None

    def get_tuner_status(self):
        """Get the current state of the tuner."""

        _LOGGER.debug("Doing device_get_tuner_status call for device [%s]." %
                     (self.hd))

        raw_data = c_char_p()
        status = TYPE_hdhomerun_tuner_status_t()

        try:
            result = CFUNC_hdhomerun_device_get_tuner_status(
                            self.hd,
                            raw_data,
                            status
                        )
        except:
            _LOGGER.exception("Tuner status failed.")
            raise

        if result != 1:
            message = ("Could not get tuner status (%d)." % (result))
            
            _LOGGER.error(message)
            raise error_for_result(result, message)

        return (status, raw_data.value)

    def get_tuner_vstatus(self):
        """Get the current state of the tuner using virtual channels (familiar 
        channel number).
        """

        _LOGGER.debug("Doing device_get_tuner_vstatus call for device [%s]." % 
                     (self.hd))

        raw_data = c_char_p()
        vstatus = TYPE_hdhomerun_tuner_vstatus_t()

        try:
            result = CFUNC_hdhomerun_device_get_tuner_vstatus(
                            self.hd, 
                            raw_data, 
                            vstatus
                        )
        except:
            _LOGGER.exception("Tuner vstatus failed.")
            raise

        if result != 1:
            message = ("Could not get tuner vstatus (%d)." % (result))
            
            _LOGGER.error(message)
            raise error_for_result(result, message)

        return (vstatus, raw_data.value)

    def get_tuner_streaminfo(self):
        """Gets the programs (sub-channels) for the current stream."""

        _LOGGER.debug("Doing device_get_tuner_streaminfo call for device [%s]." % 
                     (self.hd))

        raw_str = c_char_p()

        try:
            result = CFUNC_hdhomerun_device_get_tuner_streaminfo(
                            self.hd, 
                            raw_str
                        )
        except:
            _LOGGER.exception("Tuner streaminfo failed.")
            raise

        if result != 1:
            message = ("Could not get tuner streaminfo (%d)." % (result))
            
            _LOGGER.error(message)
            raise error_for_result(result, message)

        unparsed = ascii_str(raw_str.value)

        regex = re.compile(
            r'^(?P<program>\d+): (?P<vchannel>\d+(?:\.\d+)?)(?: (?P<name>\S+))??(?: \((?P<flags>.+)\))?$',
            re.MULTILINE)
        
        return [StreamInfo(**m.groupdict()) for m in regex.finditer(unparsed)]

    def get_tuner_program(self):
        """Gets the current MPEG program filter."""

        _LOGGER.debug("Doing device_get_tuner_program call for device [%s]." % 
                     (self.hd))

        raw_str = c_char_p()

        try:
            result = CFUNC_hdhomerun_device_get_tuner_program(
                            self.hd, 
                            raw_str
                        )
        except:
            _LOGGER.exception("Tuner program failed.")
            raise

        if result != 1:
            message = ("Could not get tuner program (%d)." % (result))
            
            _LOGGER.error(message)
            raise error_for_result(result, message)

        return ascii_str(raw_str.value)

    def set_tuner_vchannel(self, vchannel):
        """Set the current vchannel (familiar channel numbering)."""
        
        vchannel = str(vchannel)
        
        _LOGGER.debug("Doing device_set_tuner_vchannel call for device [%s] with"
                     " vchannel [%s]." % (self.hd, vchannel))
        
        try:
            result = CFUNC_hdhomerun_device_set_tuner_vchannel(self.hd, 
                                                               ascii_bytes(vchannel))
        except:
            _LOGGER.exception("Could not set vchannel.")
            raise

        if result != 1:
            message = "Failed to set vchannel."
            
            _LOGGER.error(message)
            raise error_for_result(result, message)

    def get_version(self):
        """Get firmware version."""

        raw_str = c_char_p()

        _LOGGER.debug("Doing device_get_version call for device [%s]." %
                     (self.hd))

        try:
            result = CFUNC_hdhomerun_device_get_version(
                            self.hd, 
                            raw_str,
                            None
                        )
        except:
            _LOGGER.exception("Could not do get version request.")
            raise

        if result != 1:
            message = ("Could not get firmware version (%d)." % (result))
            
            _LOGGER.error(message)
            raise error_for_result(result, message)

        return ascii_str(raw_str.value)

    def get_supported(self, prefix=None):
        """Get supported features as a dictionary of lists."""
    
        raw_str = c_char_p()

        _LOGGER.debug("Doing device_get_supported call for device [%s]." % 
                     (self.hd))

        try:
            result = CFUNC_hdhomerun_device_get_supported(
                            self.hd, 
                            None, 
                            raw_str
                        )
        except:
            _LOGGER.exception("Could not do get-supported request.")
            raise

        if result != 1:
            message = ("Could not get supported features (%d)." % (result))
            
            _LOGGER.error(message)
            raise error_for_result(result, message)

        raw_rows = ascii_str(raw_str.value).strip().split("\n")
        rows = { }
        for row in raw_rows:
            (key, value) = row.split(': ', 1)
            rows[key] = value.split(' ')

        return rows

    def iterate_channels_start(self, channel_map):
        """Establish the initial state information for a channel-scan. As 
        opposed to the generator function, this allows the caller to stash the
        state value and each, next, successive channel at some unspecified time
        in the future.
        """
    
        _LOGGER.info("Doing channel scan with map [%s]." % (channel_map))

        _LOGGER.debug("Determining range of channel scan.")

        try:
            num_channels = HdhrUtility.get_channels_in_range(channel_map)
        except:
            _LOGGER.exception("Could not calculate the maximum number of "
                              "channels to be scanned.")
            raise

        _LOGGER.debug("Building channel-scan object.")

        try:
            scan = CFUNC_channelscan_create(self.hd, channel_map)
        except:
            _LOGGER.exception("Could not initialize channel-scan object.")
            raise

        if not scan:
            message = "Could not build channel-scan object."
            
            _LOGGER.error(message)
            raise Exception(message)

        return { 'scan':    scan, 
                 'current': 0, 
                 'count':   num_channels,
                 'done':    False,
               }
    
    def iterate_channels_next(self, state):
        """Take the object returned by iterate_channels_start and scan the next
        channel.
        """

        # Scanning has already completed.
        if state['done']:
            _LOGGER.debug("HDHR: Iteration is short-circuiting because we're "
                          "already done.")
            return False

        result = TYPE_hdhomerun_channelscan_result_t()

        # Done scanning?
        if CFUNC_channelscan_advance(state['scan'].contents, result) != 1:
            state['done'] = True
            
            _LOGGER.debug("HDHR: Finished channel-scanning.")
            return False

        state['current'] += 1
            
        if CFUNC_channelscan_detect(state['scan'].contents, result) == 1 and \
             result.program_count > 0:

            _LOGGER.debug("HDHR: Channel (%d) locked." % (state['current']))
            return result
        
        else:
            _LOGGER.debug("HDHR: Channel (%d) skipped." % (state['current']))
            return None

        _LOGGER.debug("Channel scan progress is (%d)/(%d)." % (i + 1, 
                                                               num_channels))

    def scan_channels(self, channel_map):
        """This is a generator that iterates through all potential channels and
        determines what can be locked. It yields at every candidate frequency,
        and indicates whether it could be locked, current progress, . If so, it 
        """

        _LOGGER.info("Doing channel scan with map [%s]." % (channel_map))

        _LOGGER.debug("Determining range of channel scan.")

        try:
            num_channels = HdhrUtility.get_channels_in_range(channel_map)
        except:
            _LOGGER.exception("Could not calculate the maximum number of "
                              "channels to be scanned.")
            raise

        _LOGGER.debug("Building channel-scan object.")

        try:
            scan = CFUNC_channelscan_create(self.hd, channel_map)
        except:
            _LOGGER.exception("Could not initialize channel-scan object.")
            raise

        if not scan:
            message = "Could not build channel-scan object."
            
            _LOGGER.error(message)
            raise Exception(message)

        _LOGGER.debug("Doing actual scan.")

        try:
            found = self.__do_scan(scan, num_channels)
        except:
            _LOGGER.exception("Could not do actual channel scan.")
            raise
        else:
            _LOGGER.info("Found programs on (%d) channels." % (len(found)))
            return found
        finally:
            try:
                CFUNC_channelscan_destroy(scan)
            except:
                _LOGGER.exception("Could not destroy channel-scan entity.")
                raise

    def __do_scan(self, scan, num_channels):
        """Do the actual scan (looping over channel numbers)."""
    
        i = 0
        num_channels = float(num_channels)
        while 1:
            result = TYPE_hdhomerun_channelscan_result_t()

            if CFUNC_channelscan_advance(scan.contents, result) != 1:
                break

            if CFUNC_channelscan_detect(scan.contents, result) == 1 and \
                 result.program_count > 0:
            
                yield (True, i, num_channels, result)
            
            else:
                yield (False, i, num_channels)
            
            i += 1

            _LOGGER.debug("Channel scan progress is (%d)/(%d)." % 
                          (i + 1, num_channels))

        # Yield at 100%.
        yield (False, i, num_channels)

    def set_tuner_target(self, target_uri=None):
        """Start sending video to the given URI."""

        if target_uri is None:
            target_uri = 'none'

        _LOGGER.debug("Setting target to [%s]." % (target_uri))

        try:
            result = CFUNC_hdhomerun_device_set_tuner_target(self.hd, 
                                                             ascii_bytes(target_uri))
        except:
            _LOGGER.exception("There was an exception while setting the tuner "
                              "target.")
            raise

        if result != 1:
            message = ("Could not set tuner target to [%s]." % (target))
            
            _LOGGER.error(message)
            raise error_for_result(result, message)

class HdhrVideoPrimitives(object):
    """Wrappers for low-level functions."""

    hd = None

    def __init__(self, hd):
        self.hd = hd

    def start_video(self):
        """Start receiving video (the library opens a receiver thread)."""
    
        try:
            result = CFUNC_hdhomerun_device_stream_start(self.hd)
        except:
            _LOGGER.exception("There was an exception within the stream-start "
                              "external.")
            raise

        if result != 1:
            message = "Stream-start failed."
            
            _LOGGER.error(message)
            raise error_for_result(result, message)
    
    def stop_video(self):
        """Cease receiving video (the library closes its receiver thread)."""
    
        try:
            result = CFUNC_hdhomerun_device_stream_stop(self.hd)
        except:
            _LOGGER.exception("There was an exception within the stream-stop "
                              "external.")
            raise
    
    def receive_rtp_frame(self):
        """Receive a single communication frame. May be video, audio, etc..
        (however RTP splits its data up).
        """

        actual_count = c_uint()
        
        try:
            byte_array = CFUNC_hdhomerun_device_stream_recv(
                            self.hd, 
                            VIDEO_DATA_BUFFER_SIZE_1S, 
                            byref(actual_count)
                         )
        except:
            _LOGGER.exception("Could not read RTP frame.")
            raise

        return (byte_array, actual_count.value)
    
class HdhrVideo(object):    
    """Provides useful functionality implementing the methods in the primitives
    class, above.
    """

    hd    = None
    vprim = None

    def __init__(self, hd):
        self.hd = hd

        try:
            self.vprim = HdhrVideoPrimitives(hd)
        except:
            _LOGGER.exception("Could not build video-primitives object.")
            raise

    def __receive_loop(self, frame_cb):
        count = 0
        while 1:
            try:        
                frame = self.vprim.receive_rtp_frame()
            except:
                _LOGGER.exception("Could not read frame.")
                raise

            if not frame[1]:
                continue

            try:
                if not frame_cb(frame):
                    break
            except:
                _LOGGER.exception("Uncaught exception in frame callback.")
                raise

            count += 1

        return count

    def stream_video(self, frame_cb):

        _LOGGER.info("Starting video feed: %s" % (self.hd))
        
        try:
            self.vprim.start_video()
        except:
            _LOGGER.exception("Could not start feed.")
            raise

        try:
            self.__receive_loop(frame_cb)
        except Exception as e:
            _LOGGER.exception("There was an error in the feed receive-loop: "
                              "%s" % (e))
            raise
        finally:
            _LOGGER.info("Stopping video feed: %s" % (self.hd))
        
            try:
                self.vprim.stop_video()
            except:
                _LOGGER.exception("Exception while stopping feed.")
                raise

    def stream_to_file(self, file_path):
    
        with file(file_path, 'ab') as f:

            def frame_received(frame):
                if not hasattr(frame_received, 'frame_count'):
                    frame_received.last_second = time()
                    frame_received.frame_count = 0
                    frame_received.bytes_per_second = 0
                    frame_received.rates = deque()
                    frame_received.max_history = 3
                    frame_received.types = {}
            
                current_second = int(time())
            
                if frame_received.frame_count > 0 and current_second != frame_received.last_second:
                    frame_received.rates.append(frame_received.frame_count)
                    if len(frame_received.rates) > frame_received.max_history:
                        frame_received.rates.popleft()

                    types = []
                    for ptype, count in frame_received.types.iteritems():
                        types.append('%d=%d' % (ptype, count))
                    
                    print("Frames/s: %d  Bytes/s: %d [%s]" % 
                          (frame_received.frame_count, 
                           frame_received.bytes_per_second, ' '.join(types)))
                    
                    frame_received.frame_count = 0
                    frame_received.bytes_per_second = 0
                    frame_received.last_second = current_second

                (cbuffer, length) = frame

                frame_received.frame_count += 1
                frame_received.bytes_per_second += length

                buffer = ''.join([chr(cbuffer[i]) for i in xrange(length)])
                f.write(buffer)

#                process_mpegts_packet(buffer)
            
                return True

#            print("Beginning to stream.")

            try:
                return self.stream_video(frame_received)
            except:
                _LOGGER.exception("Error while streaming the video.")
                raise

