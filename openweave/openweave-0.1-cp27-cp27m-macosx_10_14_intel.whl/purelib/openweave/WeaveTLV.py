#!/usr/bin/env python3
# coding=utf-8

#
#   Copyright (c) 2019-2020 Google LLC.
#   All rights reserved.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

#
#   @file
#         This file contains definitions for working with data encoded in Weave TLV format
#


from __future__ import absolute_import
from __future__ import print_function

import sys
import struct
from collections import Mapping, Sequence, OrderedDict


TLVType_SignedInteger                   = 0x00
TLVType_UnsignedInteger                 = 0x04
TLVType_Boolean                         = 0x08
TLVType_FloatingPointNumber             = 0x0A
TLVType_UTF8String                      = 0x0C
TLVType_ByteString                      = 0x10
TLVType_Null                            = 0x14
TLVType_Structure                       = 0x15
TLVType_Array                           = 0x16
TLVType_Path                            = 0x17

TLVTagControl_Anonymous                 = 0x00
TLVTagControl_ContextSpecific           = 0x20
TLVTagControl_CommonProfile_2Bytes      = 0x40
TLVTagControl_CommonProfile_4Bytes      = 0x60
TLVTagControl_ImplicitProfile_2Bytes    = 0x80
TLVTagControl_ImplicitProfile_4Bytes    = 0xA0
TLVTagControl_FullyQualified_6Bytes     = 0xC0
TLVTagControl_FullyQualified_8Bytes     = 0xE0

TLVBoolean_False                        = TLVType_Boolean
TLVBoolean_True                         = TLVType_Boolean + 1

TLVEndOfContainer                       = 0x18                  

INT8_MIN                                = -128
INT16_MIN                               = -32768
INT32_MIN                               = -2147483648
INT64_MIN                               = -9223372036854775808
 
INT8_MAX                                = 127
INT16_MAX                               = 32767
INT32_MAX                               = 2147483647
INT64_MAX                               = 9223372036854775807
 
UINT8_MAX                               = 255
UINT16_MAX                              = 65535
UINT32_MAX                              = 4294967295
UINT64_MAX                              = 18446744073709551615

ElementTypes = {
    0x00:"Signed Integer 1-byte value",
    0x01:"Signed Integer 2-byte value",
    0x02:"Signed Integer 4-byte value",
    0x03:"Signed Integer 8-byte value",
    0x04:"Unsigned Integer 1-byte value",
    0x05:"Unsigned Integer 2-byte value",
    0x06:"Unsigned Integer 4-byte value",
    0x07:"Unsigned Integer 8-byte value",
    0x08:"Boolean False",
    0x09:"Boolean True",
    0x0A:"Floating Point 4-byte value",
    0x0B:"Floating Point 8-byte value",
    0x0C:"UTF-8 String 1-byte length",
    0x0D:"UTF-8 String 2-byte length",
    0x0E:"UTF-8 String 4-byte length",
    0x0F:"UTF-8 String 8-byte length",
    0x10:"Byte String 1-byte length",
    0x11:"Byte String 2-byte length",
    0x12:"Byte String 4-byte length",
    0x13:"Byte String 8-byte length",
    0x14:"Null",
    0x15:"Structure",
    0x16:"Array",
    0x17:"Path",
    0x18:"End of Collection"
}

TagControls = {
    0x00:"Anonymous",
    0x20:"Context 1-byte",
    0x40:"Common Profile 2-byte",
    0x60:"Common Profile 4-byte",
    0x80:"Implicit Profile 2-byte",
    0xA0:"Implicit Profile 4-byte",
    0xC0:"Fully Qualified 6-byte",
    0xE0:"Fully Qualified 8-byte"
}

class TLVWriter(object):

    def __init__(self, encoding=None, implicitProfile=None):
        self._encoding = encoding if encoding is not None else bytearray()
        self._implicitProfile = implicitProfile
        self._containerStack = []

    @property
    def encoding(self):
        '''The object into which encoded TLV data is written.
           
           By default this is a bytearray object. 
        '''
        return self._encoding
    
    @encoding.setter
    def encoding(self, val):
        self._encoding = val

    @property
    def implicitProfile(self):
        '''The Weave profile id used when encoding implicit profile tags.
        
           Setting this value will result in an implicit profile tag being encoded
           whenever the profile of the tag to be encoded matches the specified implicit
           profile id.
           
           Setting this value to None (the default) disabled encoding of implicit
           profile tags.
        '''
        return self._implicitProfile
    
    @implicitProfile.setter
    def implicitProfile(self, val):
        self._implicitProfile = val

    def put(self, tag, val):
        '''Write a value in TLV format with the specified TLV tag.
        
           val can be a Python object which will be encoded as follows: 
           - Python bools, floats and strings are encoded as their respective TLV types.
           - Python ints are encoded as unsigned TLV integers if zero or positive; signed TLV
             integers if negative.
           - None is encoded as a TLV Null.
           - bytes and bytearray objects are encoded as TVL byte strings.
           - Mapping-like objects (e.g. dict) are encoded as TLV structures.  The keys of the
             map object are expected to be tag values, as described below for the tag argument.
             Map values are encoded recursively, using the same rules as defined for the val
             argument. The encoding order of elements depends on the type of the map object. 
             Elements within a dict are automatically encoded tag numerical order. Elements
             within other forms of mapping object (e.g. OrderedDict) are encoded in the
             object's natural iteration order.
           - Sequence-like objects (e.g. arrays) are written as TLV arrays. Elements within
             the array are encoded recursively, using the same rules as defined for the val
             argument.

           tag can be a small int (0-255), a tuple of two integers, or None.
           If tag is an integer, it is encoded as a TLV context-specific tag.
           If tag is a two-integer tuple, it is encoded as a TLV profile-specific tag, with
             the first integer encoded as the profile id and the second as the tag number.
           If tag is None, it is encoded as a TLV anonymous tag.
        '''
        if val == None:
            self.putNull(tag)
        elif isinstance(val, bool):
            self.putBool(tag, val)
        elif isinstance(val, int):
            if val < 0:
                self.putSignedInt(tag, val)
            else:
                self.putUnsignedInt(tag, val)
        elif isinstance(val, float):
            self.putFloat(tag, val)
        elif isinstance(val, str):
            self.putString(tag, val)
        elif isinstance(val, bytes) or isinstance(val, bytearray):
            self.putBytes(tag, val)
        elif isinstance(val, Mapping):
            self.startStructure(tag)
            if type(val) == dict:
                val = OrderedDict(sorted(val.items(), key=lambda item: tlvTagToSortKey(item[0])))
            for containedTag, containedVal in val.items():
                self.put(containedTag, containedVal)
            self.endContainer()
        elif isinstance(val, Sequence):
            self.startArray(tag)
            for containedVal in val:
                self.put(None, containedVal)
            self.endContainer()
        else:
            raise ValueError('Attempt to TLV encode unsupported value')

    def putSignedInt(self, tag, val):
        '''Write a value as a TLV signed integer with the specified TLV tag.'''
        if val >= INT8_MIN and val <= INT8_MAX:
            format = '<b'
        elif val >= INT16_MIN and val <= INT16_MAX:
            format = '<h'
        elif val >= INT32_MIN and val <= INT32_MAX:
            format = '<l'
        elif val >= INT64_MIN and val <= INT64_MAX:
            format = '<q'
        else:
            raise ValueError('Integer value out of range')
        val = struct.pack(format, val)
        controlAndTag = self._encodeControlAndTag(TLVType_SignedInteger, tag, lenOfLenOrVal=len(val))
        self._encoding.extend(controlAndTag)
        self._encoding.extend(val)

    def putUnsignedInt(self, tag, val):
        '''Write a value as a TLV unsigned integer with the specified TLV tag.'''
        val = self._encodeUnsignedInt(val)
        controlAndTag = self._encodeControlAndTag(TLVType_UnsignedInteger, tag, lenOfLenOrVal=len(val))
        self._encoding.extend(controlAndTag)
        self._encoding.extend(val)

    def putFloat(self, tag, val):
        '''Write a value as a TLV float with the specified TLV tag.'''
        val = struct.pack('d', val)
        controlAndTag = self._encodeControlAndTag(TLVType_FloatingPointNumber, tag, lenOfLenOrVal=len(val))
        self._encoding.extend(controlAndTag)
        self._encoding.extend(val)

    def putString(self, tag, val):
        '''Write a value as a TLV string with the specified TLV tag.'''
        val = val.encode('utf-8')
        valLen = self._encodeUnsignedInt(len(val))
        controlAndTag = self._encodeControlAndTag(TLVType_UTF8String, tag, lenOfLenOrVal=len(valLen))
        self._encoding.extend(controlAndTag)
        self._encoding.extend(valLen)
        self._encoding.extend(val)

    def putBytes(self, tag, val):
        '''Write a value as a TLV byte string with the specified TLV tag.'''
        valLen = self._encodeUnsignedInt(len(val))
        controlAndTag = self._encodeControlAndTag(TLVType_ByteString, tag, lenOfLenOrVal=len(valLen))
        self._encoding.extend(controlAndTag)
        self._encoding.extend(valLen)
        self._encoding.extend(val)

    def putBool(self, tag, val):
        '''Write a value as a TLV boolean with the specified TLV tag.'''
        if val:
            type = TLVBoolean_True
        else:
            type = TLVBoolean_False
        controlAndTag = self._encodeControlAndTag(type, tag)
        self._encoding.extend(controlAndTag)

    def putNull(self, tag):
        '''Write a TLV null with the specified TLV tag.'''
        controlAndTag = self._encodeControlAndTag(TLVType_Null, tag)
        self._encoding.extend(controlAndTag)

    def startContainer(self, tag, containerType):
        '''Start writing a TLV container with the specified TLV tag.
        
           containerType can be one of TLVType_Structure, TLVType_Array or
           TLVType_Path.
        '''
        self._verifyValidContainerType(containerType)
        controlAndTag = self._encodeControlAndTag(containerType, tag)
        self._encoding.extend(controlAndTag)
        self._containerStack.insert(0, containerType)

    def startStructure(self, tag):
        '''Start writing a TLV structure with the specified TLV tag.'''
        self.startContainer(tag, containerType=TLVType_Structure)

    def startArray(self, tag):
        '''Start writing a TLV array with the specified TLV tag.'''
        self.startContainer(tag, containerType=TLVType_Array)

    def startPath(self, tag):
        '''Start writing a TLV path with the specified TLV tag.'''
        self.startContainer(tag, containerType=TLVType_Path)

    def endContainer(self):
        '''End writing the current TLV container.'''
        self._containerStack.pop(0)
        controlAndTag = self._encodeControlAndTag(TLVEndOfContainer, None)
        self._encoding.extend(controlAndTag)

    def _encodeControlAndTag(self, type, tag, lenOfLenOrVal=0):
        controlByte = type
        if lenOfLenOrVal == 2:
            controlByte |= 1
        elif lenOfLenOrVal == 4:
            controlByte |= 2
        elif lenOfLenOrVal == 8:
            controlByte |= 3
        if tag == None:
            if type != TLVEndOfContainer and len(self._containerStack) != 0 and self._containerStack[0] == TLVType_Structure:
                raise ValueError('Attempt to encode anonymous tag within TLV structure')
            controlByte |= TLVTagControl_Anonymous
            return struct.pack('<B', controlByte)
        if isinstance(tag, int):
            if tag < 0 or tag > UINT8_MAX:
                ValueError('Context-specific TLV tag number out of range')
            if len(self._containerStack) == 0:
                raise ValueError('Attempt to encode context-specific TLV tag at top level')
            if self._containerStack[0] == TLVType_Array:
                raise ValueError('Attempt to encode context-specific tag within TLV array')
            controlByte |= TLVTagControl_ContextSpecific
            return struct.pack('<BB', controlByte, tag)
        if isinstance(tag, tuple):
            (profile, tagNum) = tag
            if not isinstance(tagNum, int):
                raise ValueError('Invalid object given for TLV tag')
            if tagNum < 0 or tagNum > UINT32_MAX:
                raise ValueError('TLV tag number out of range')
            if profile != None:
                if not isinstance(profile, int):
                    raise ValueError('Invalid object given for TLV profile id')
                if profile < 0 or profile > UINT32_MAX:
                    raise ValueError('TLV profile id value out of range')
            if len(self._containerStack) != 0 and self._containerStack[0] == TLVType_Array:
                raise ValueError('Attempt to encode profile-specific tag within TLV array')
            if profile == None or profile == self._implicitProfile:
                if tagNum <= UINT16_MAX:
                    controlByte |= TLVTagControl_ImplicitProfile_2Bytes
                    return struct.pack('<BH', controlByte, tagNum)
                else:
                    controlByte |= TLVTagControl_ImplicitProfile_4Bytes
                    return struct.pack('<BL', controlByte, tagNum)
            elif profile == 0:
                if tagNum <= UINT16_MAX:
                    controlByte |= TLVTagControl_CommonProfile_2Bytes
                    return struct.pack('<BH', controlByte, tagNum)
                else:
                    controlByte |= TLVTagControl_CommonProfile_4Bytes
                    return struct.pack('<BL', controlByte, tagNum)
            else:
                if tagNum <= UINT16_MAX:
                    controlByte |= TLVTagControl_FullyQualified_6Bytes
                    return struct.pack('<BLH', controlByte, profile, tagNum)
                else:
                    controlByte |= TLVTagControl_FullyQualified_8Bytes
                    return struct.pack('<BLL', controlByte, profile, tagNum)
        raise ValueError('Invalid object given for TLV tag')
    
    @staticmethod
    def _encodeUnsignedInt(val):
        if val < 0:
            raise ValueError('Integer value out of range')
        if val <= UINT8_MAX:
            format = '<B'
        elif val <= UINT16_MAX:
            format = '<H'
        elif val <= UINT32_MAX:
            format = '<L'
        elif val <= UINT64_MAX:
            format = '<Q'
        else:
            raise ValueError('Integer value out of range')
        return struct.pack(format, val)
        
    @staticmethod
    def _verifyValidContainerType(containerType):
        if containerType != TLVType_Structure and containerType != TLVType_Array and containerType != TLVType_Path:
            raise ValueError('Invalid TLV container type')

class TLVReader(object):

    def __init__(self, tlv):
        self._tlv = tlv
        self._bytesRead = 0
        self._decodings = []

    @property
    def decoding(self):
        return self._decodings

    def get(self):
        """Get the dictionary representation of tlv data
        """
        out = {}
        self._get(self._tlv, self._decodings, out)
        return out

    def _decodeControlByte(self, tlv, decoding):
        controlByte, = struct.unpack("<B", tlv[self._bytesRead:self._bytesRead+1])
        controlTypeIndex = controlByte & 0xE0
        decoding["tagControl"] = TagControls[controlTypeIndex]
        elementtypeIndex = controlByte & 0x1f
        decoding["type"] = ElementTypes[elementtypeIndex]
        self._bytesRead += 1

    def _decodeControlAndTag(self, tlv, decoding):
        """The control byte specifies the type of a TLV element and how its tag, length and value fields are encoded.
         The control byte consists of two subfields: an element type field which occupies the lower 5 bits, 
         and a tag control field which occupies the upper 3 bits. The element type field encodes the element’s type 
         as well as how the corresponding length and value fields are encoded.  In the case of Booleans and the 
         null value, the element type field also encodes the value itself."""

        self._decodeControlByte(tlv, decoding)

        if decoding["tagControl"] == "Anonymous":
            decoding["tag"] = None
            decoding["tagLen"] = 0
        elif decoding["tagControl"] == "Context 1-byte":
            decoding["tag"], = struct.unpack("<B", tlv[self._bytesRead:self._bytesRead+1])
            decoding["tagLen"] = 1
            self._bytesRead  += 1
        elif decoding["tagControl"] == "Common Profile 2-byte":
            profile = 0
            tag,  = struct.unpack("<H",  tlv[self._bytesRead:self._bytesRead+2])
            decoding["profileTag"] = (profile, tag)
            decoding["tagLen"] = 2
            self._bytesRead  += 2
        elif decoding["tagControl"] == "Common Profile 4-byte":
            profile = 0
            tag,  = struct.unpack("<L",  tlv[self._bytesRead:self._bytesRead+4])
            decoding["profileTag"] = (profile, tag)
            decoding["tagLen"] = 4
            self._bytesRead  += 4
        elif decoding["tagControl"] == "Implicit Profile 2-byte":
            profile = None
            tag,  = struct.unpack("<H",  tlv[self._bytesRead:self._bytesRead+2])
            decoding["profileTag"] = (profile, tag)
            decoding["tagLen"] = 2
            self._bytesRead  += 2
        elif decoding["tagControl"] == "Implicit Profile 4-byte":
            profile = None
            tag,  = struct.unpack("<L",  tlv[self._bytesRead:self._bytesRead+4])
            decoding["profileTag"] = (profile, tag)
            decoding["tagLen"] = 4
            self._bytesRead += 4
        elif decoding["tagControl"] == "Fully Qualified 6-byte":
            profile, = struct.unpack("<L",  tlv[self._bytesRead:self._bytesRead+4])
            tag, = struct.unpack("<H",  tlv[self._bytesRead+4:self._bytesRead+6])
            decoding["profileTag"] = (profile, tag)
            decoding["tagLen"] = 2
            self._bytesRead += 6
        elif decoding["tagControl"] == "Fully Qualified 8-byte":
            profile, = struct.unpack("<L",  tlv[self._bytesRead:self._bytesRead+4])
            tag, = struct.unpack("<L",  tlv[self._bytesRead+4:self._bytesRead+8])
            decoding["profileTag"] = (profile, tag)
            decoding["tagLen"] = 4
            self._bytesRead += 8

    def _decodeStrLength(self, tlv, decoding):
        """UTF-8 or Byte StringLength fields are encoded in 0, 1, 2 or 4 byte widths, as specified by
         the element type field. If the element type needs a length field grab the next bytes as length"""
        if "length" in decoding["type"]:
            if "1-byte" in decoding["type"]:
                decoding["strDataLen"], = struct.unpack("<B", tlv[self._bytesRead:self._bytesRead+1])
                decoding["strDataLenLen"] = 1
                self._bytesRead += 1
            elif "2-byte" in decoding["type"]:
                decoding["strDataLen"], = struct.unpack("<H", tlv[self._bytesRead:self._bytesRead+2])
                decoding["strDataLenLen"] = 2
                self._bytesRead += 2
            elif "4-byte" in decoding["type"]:
                decoding["strDataLen"], = struct.unpack("<L", tlv[self._bytesRead:self._bytesRead+4])
                decoding["strDataLenLen"] = 4
                self._bytesRead += 4
            elif "8-byte" in decoding["type"]:
                decoding["strDataLen"], = struct.unpack("<Q", tlv[self._bytesRead:self._bytesRead+8])
                decoding["strDataLenLen"] = 8
                self._bytesRead += 8
        else:
            decoding["strDataLen"]= 0
            decoding["strDataLenLen"] = 0

    def _decodeVal(self, tlv, decoding):
        """decode primitive tlv value to the corresponding python value, tlv array and path are decoded as
        python list, tlv structure is decoded as python dictionary"""
        if decoding["type"] == "Structure":
            decoding["value"] = {}
            decoding["Structure"] =  []
            self._get(tlv, decoding["Structure"], decoding["value"])
        elif decoding["type"] == "Array":
            decoding["value"] = []
            decoding["Array"] =  []
            self._get(tlv, decoding["Array"], decoding["value"])
        elif decoding["type"] == "Path":
            decoding["value"] = []
            decoding["Path"] =  []
            self._get(tlv, decoding["Path"], decoding["value"])
        elif decoding["type"] == "Null":
            decoding["value"] = None
        elif decoding["type"] == "End of Collection":
            decoding["value"] = None
        elif decoding["type"] == "Boolean True":
            decoding["value"] = True
        elif decoding["type"] == "Boolean False":
            decoding["value"] = False
        elif decoding["type"] == "Unsigned Integer 1-byte value":
            decoding["value"], = struct.unpack("<B", tlv[self._bytesRead: self._bytesRead + 1])
            self._bytesRead += 1
        elif decoding["type"] == "Signed Integer 1-byte value":
            decoding["value"], = struct.unpack("<b", tlv[self._bytesRead: self._bytesRead + 1])
            self._bytesRead += 1
        elif decoding["type"] == "Unsigned Integer 2-byte value":
            decoding["value"], = struct.unpack("<H", tlv[self._bytesRead: self._bytesRead + 2])
            self._bytesRead += 2
        elif decoding["type"] == "Signed Integer 2-byte value":
            decoding["value"], = struct.unpack("<h", tlv[self._bytesRead: self._bytesRead + 2])
            self._bytesRead += 2
        elif decoding["type"] == "Unsigned Integer 4-byte value":
            decoding["value"], = struct.unpack("<L", tlv[self._bytesRead: self._bytesRead + 4])
            self._bytesRead += 4
        elif decoding["type"] == "Signed Integer 4-byte value":
            decoding["value"], = struct.unpack("<l", tlv[self._bytesRead: self._bytesRead + 4])
            self._bytesRead += 4
        elif decoding["type"] == "Unsigned Integer 8-byte value":
            decoding["value"], = struct.unpack("<Q", tlv[self._bytesRead: self._bytesRead + 8])
            self._bytesRead += 8
        elif decoding["type"] == "Signed Integer 8-byte value":
            decoding["value"], = struct.unpack("<q", tlv[self._bytesRead: self._bytesRead + 8])
            self._bytesRead += 8
        elif decoding["type"] == "Floating Point 4-byte value":
            decoding["value"], = struct.unpack("<f", tlv[self._bytesRead: self._bytesRead + 4])
            self._bytesRead += 4
        elif decoding["type"] == "Floating Point 8-byte value":
            decoding["value"], = struct.unpack("<d", tlv[self._bytesRead: self._bytesRead + 8])
            self._bytesRead += 8
        elif "UTF-8 String" in decoding["type"]:
            val, = struct.unpack("<%ds" % decoding["strDataLen"],
                                               tlv[self._bytesRead: self._bytesRead + decoding["strDataLen"]])
            try:
                decoding["value"] = str(val, 'utf-8')
            except:
                decoding["value"] = val
            self._bytesRead += decoding["strDataLen"]
        elif "Byte String" in decoding["type"]:
            val, = struct.unpack("<%ds" % decoding["strDataLen"],
                                 tlv[self._bytesRead: self._bytesRead + decoding["strDataLen"]])

            decoding["value"] = val
            self._bytesRead += decoding["strDataLen"]
        else:
            raise ValueError('Attempt to decode unsupported TLV type')

    def _get(self, tlv, decodings, out):
        endOfEncoding = False

        while len(tlv[self._bytesRead:]) > 0 and endOfEncoding == False:
            decoding = {}
            self._decodeControlAndTag(tlv, decoding)
            self._decodeStrLength(tlv, decoding)
            self._decodeVal(tlv, decoding)
            decodings.append(decoding)

            if decoding["type"] == "End of Collection":
                endOfEncoding = True
            else:
                if "profileTag" in list(decoding.keys()):
                    out[decoding["profileTag"]] = decoding["value"]
                elif "tag" in list(decoding.keys()):
                    if decoding["tag"] is not None:
                        out[decoding["tag"]] = decoding["value"]
                    else:
                        if isinstance(out, Mapping):
                            out["Any"] = decoding["value"]
                        elif isinstance(out, Sequence):
                            out.append(decoding["value"])
                else:
                    raise ValueError('Attempt to decode unsupported TLV tag')

def tlvTagToSortKey(tag):
    if tag == None:
        return -1
    if isinstance(tag, int):
        majorOrder = 0
    elif isinstance(tag, tuple):
        (profileId, tag) = tag
        if profileId == None:
            majorOrder = 1
        else:
            majorOrder = profileId + 2
    else:
        raise ValueError('Invalid TLV tag')
    return (majorOrder << 32) + tag

if __name__ == '__main__':
    val = dict([
        (1, 0),
        (2, 65536),
        (3, True),
        (4, None),
        (5, "Hello!"),
        (6, bytearray([ 0xDE, 0xAD, 0xBE, 0xEF ])),
        (7, [
            "Goodbye!",
            71024724507,
            False
        ]),
        ((0x235A0000, 42), "FOO"),
        ((None, 42), "BAR"),
    ])

    writer = TLVWriter()
    encodedVal = writer.put(None, val)

    reader = TLVReader(writer.encoding)
    out = reader.get()

    print("TLVReader input: " + str(val))
    print("TLVReader output: " + str(out["Any"]))

    if (val == out["Any"]):
        print('Test Success')
    else:
        print('Test Failure')
