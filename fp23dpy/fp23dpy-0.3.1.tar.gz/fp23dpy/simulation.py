import numpy as np
import scipy
import trimesh

from . import threeD_to_phase_const
from . import export
from . import helpers as h

def _create_camera_matrix(calibration):  # not fully implemented
    if 'camera_type' in calibration:
        raise ValueError('camera_type not supported yet')
    else:
        return np.eye((3, 4))

def estimate_projection_map(image_shape, X, Y, d, calibration):  # currently not fully implemented
    assert len(image_shape) == 2
    n_pixels = np.prod(image_shape)

    mesh = export.mesh_it(X, Y, d)
    ray_tracer = trimesh.ray.ray_triangle.RayMeshIntersector(mesh)
    ray_origins = None
    ray_directions = None
    try:
        _, rays, locations = ray_tracer.intersects_id(ray_origins, ray_directions, return_locations=True, multiple_hits=False)  # needs installation of dumb not python stuff
    except:
        raise EnvironmentError("Install trimesh[easy] for this method to work")

    mask = np.ones(n_pixels, dtype=bool)
    Xmap = np.zeros(n_pixels)
    Ymap = np.zeros(n_pixels)
    dmap = np.zeros(n_pixels)

    mask[rays] = True
    Xmap[rays] = locations[:, 0]
    Ymap[rays] = locations[:, 1]
    dmap[rays] = locations[:, 2]

    mask.shape = Xmap.shape = Ymap.shape = dmap.shape = image_shape
    Xmap = np.ma.array(Xmap, mask=mask)
    Ymap = np.ma.array(Ymap, mask=mask)
    dmap = np.ma.array(dmap, mask=mask)
    return np.ma.stack(Xmap, Ymap, dmap)


def render_from_map(dmap, calibration, amplitude=1, background=1):
    """
    Method used to simulate an FP image of a 3D structure by mainly using a map of the world third coordinate of the object surface in the camera.
    Assumes that an orthographic camera rotated theta radians round the y-axis. 
    If not the full image is used as for the drop case the dmap parameter should be a masked numpy array and the function will always return a masked array.
    """
    dmap = np.ma.asarray(dmap)
    tpc = threeD_to_phase_const(calibration['T'], calibration['theta'], calibration['scale'])
    if 'phi' in calibration:
        pass # multiply constant slightly
    carrier = h.make_carrier(dmap.shape, calibration['T'], calibration['gamma'])
    phase = dmap * tpc + carrier
    signal = amplitude * np.cos(phase) + background

    mask = dmap.mask
    kernel = 1 / 5 * np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]])
    signal = np.ma.array(scipy.signal.convolve2d(signal, kernel, 'same'), mask=mask)
    signal.data[signal.mask] = 0
    return signal

def render(camera_shape, X, Y, d, calibration):
    """Helper function to render a general 3D structure"""
    _, _, dmap = estimate_projection_map(camera_shape, X, Y, d, calibration)
    return render_from_map(dmap, calibration)
