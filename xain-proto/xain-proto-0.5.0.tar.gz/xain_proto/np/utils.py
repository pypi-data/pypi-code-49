"""NumPy ndarray to protobuf serialization and deserialization"""

from io import BytesIO

import numpy as np

from xain_proto.np.ndarray_pb2 import NDArray


def ndarray_to_proto(numpy_array: np.ndarray) -> NDArray:
    """Serialize a numpy array into an NDArray protobuf message.

    Args:
        numpy_array (np.ndarray): A numpy array to be serialized.

    Returns:
        A NDArray protobuf message.
    """

    bytes_array: BytesIO = BytesIO()
    np.save(file=bytes_array, arr=numpy_array, allow_pickle=False)
    proto_array: NDArray = NDArray(ndarray=bytes_array.getvalue())

    return proto_array


def proto_to_ndarray(proto_array: NDArray) -> np.ndarray:
    """Deserializes an NDArray protobuf message into a numpy array.

    Args:
        proto_array (NDArray): NDArray protobuf message to be deserialized.

    Returns:
        A numpy ndarray.
    """

    if proto_array.ndarray == b"":
        return np.empty(shape=(0,))

    bytes_array: BytesIO = BytesIO(proto_array.ndarray)
    numpy_array: np.ndarray = np.load(file=bytes_array, allow_pickle=False)

    return numpy_array
