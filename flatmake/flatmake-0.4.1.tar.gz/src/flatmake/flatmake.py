import sys
import numpy as np
import flatbuffers
from flatmake.idl.python.Dim import UByteArray
from flatmake.idl.python.Dim import FloatArray
from flatmake.idl.python.Dim import Coordinates2D
from flatmake.idl.python.Dim import RGBTripleArray


def add_ubyte_array(builder, np_arr):
    arr = builder.CreateNumpyVector(np_arr)
    UByteArray.UByteArrayStart(builder)
    UByteArray.UByteArrayAddData(builder=builder, data=arr)
    return UByteArray.UByteArrayEnd(builder)


def add_float_array(builder, np_arr):
    arr = builder.CreateNumpyVector(np_arr)
    FloatArray.FloatArrayStart(builder)
    FloatArray.FloatArrayAddData(builder=builder, data=arr)
    return FloatArray.FloatArrayEnd(builder)


def build_coordinates_2d(np_x, np_y):
    builder = flatbuffers.Builder(0)
    fb_x = add_float_array(
        builder=builder,
        np_arr=np_x
    )
    fb_y = add_float_array(
        builder=builder,
        np_arr=np_y
    )
    Coordinates2D.Coordinates2DStart(builder)
    Coordinates2D.Coordinates2DAddX(builder=builder, x=fb_x)
    Coordinates2D.Coordinates2DAddY(builder=builder, y=fb_y)
    coordinates_2d = Coordinates2D.Coordinates2DEnd(builder)
    builder.Finish(coordinates_2d)
    return builder


def serialize_coordinates_2d(np_x, np_y, verbose=False):
    try:
        builder = build_coordinates_2d(
            np_x=np_x,
            np_y=np_y
        )
        buf = bytes(builder.Output())
    except Exception as e:
        print(e)

    if verbose is True:
        print(f"Size: {str(sys.getsizeof(buf))} bytes")

    return buf


def normalize_to_rgb(np_arr):
    return np.interp(
        np_arr,
        (np_arr.min(), np_arr.max()),
        (0, 255)
    ).astype(int)


def build_rgb_triple_array(np_r, np_g, np_b):
    try:
        builder = flatbuffers.Builder(0)
        fb_r = add_ubyte_array(
            builder=builder,
            np_arr=normalize_to_rgb(
                np_arr=np_r
            )
        )
        fb_g = add_ubyte_array(
            builder=builder,
            np_arr=normalize_to_rgb(
                np_arr=np_r
            )
        )
        fb_b = add_ubyte_array(
            builder=builder,
            np_arr=normalize_to_rgb(
                np_arr=np_r
            )
        )
        RGBTripleArray.RGBTripleArrayStart(builder)
        RGBTripleArray.RGBTripleArrayAddR(builder=builder, r=fb_r)
        RGBTripleArray.RGBTripleArrayAddG(builder=builder, g=fb_g)
        RGBTripleArray.RGBTripleArrayAddB(builder=builder, b=fb_b)
        rgb_triple_array = RGBTripleArray.RGBTripleArrayEnd(builder)
        builder.Finish(rgb_triple_array)
        return builder
    except Exception as e:
        raise Exception(e)


def serialize_rgb_triple_array(np_red, np_green, np_blue, verbose=False):
    try:
        builder = build_rgb_triple_array(
            np_r=np_red,
            np_g=np_green,
            np_b=np_blue
        )
        buf = bytes(builder.Output())
    except Exception as e:
        raise Exception(e)

    if verbose is True:
        print(f"Size: {str(sys.getsizeof(buf))} bytes")

    return buf
