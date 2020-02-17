import numpy as np


def indices_of_original_elements_after_applying_mask(mask):
    """
    Given a mask that represents which of the original elements should be kept,
    produce an array containing the new indices of the original elements. Returns
    -1 as the index of the removed elements.
    """
    result = np.repeat(np.int(-1), len(mask))
    result[mask] = np.arange(np.count_nonzero(mask))
    return result


def create_submesh(
    mesh, vertex_mask, face_mask, ret_indices_of_original_faces_and_vertices=False
):
    """
    Apply the requested mask to the vertices and faces to create a submesh.
    """
    from .._mesh import Mesh

    new_v = mesh.v[vertex_mask]
    indices_of_original_vertices = indices_of_original_elements_after_applying_mask(
        vertex_mask
    )
    new_f = indices_of_original_vertices[mesh.f[face_mask]]
    submesh = Mesh(v=new_v, f=new_f)

    if ret_indices_of_original_faces_and_vertices:
        indices_of_original_faces = indices_of_original_elements_after_applying_mask(
            face_mask
        )
        return submesh, indices_of_original_faces, indices_of_original_vertices
    else:
        return submesh
