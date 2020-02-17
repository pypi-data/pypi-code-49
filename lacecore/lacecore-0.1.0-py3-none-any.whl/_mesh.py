import vg
from ._common.validation import check_arity, check_indices
from ._selection.selection_mixin import SelectionMixin


class Mesh(SelectionMixin):
    """
    A triangular or quad mesh. Vertices and faces are represented using NumPy
    arrays. Instances are read-only, at least for now. This class is optimized
    for cloud computation.

    Args:
        v (np.ndarray): A `kx3` array of vertices. It will be marked read-only.
        f (np.ndarray): A `kx3` or `kx4` array of vertex indices which make
            up the faces. It will be marked read-only.
        copy_v (bool): When `True`, the input vertices will be copied before
            they are marked read-only.
        copy_f (bool): When `True`, the input faces will be copied before
            they are marked read-only.
    """

    def __init__(self, v, f, copy_v=False, copy_f=False):
        num_vertices = vg.shape.check(locals(), "v", (-1, 3))
        vg.shape.check(locals(), "f", (-1, -1))
        check_arity(f)
        check_indices(f, num_vertices, "f")

        # TODO: Needs coverage.
        # if copy_f:
        #     f = np.copy(f)
        # if copy_v:
        #     v = np.copy(v)
        f.setflags(write=False)
        v.setflags(write=False)
        self.f = f
        self.v = v

    # TODO: Needs coverage.
    # @classmethod
    # def from_lace(cls, mesh):
    #     return cls(v=mesh.v, f=mesh.f)

    # TODO: Needs coverage.
    # @classmethod
    # def from_trimesh(cls, mesh):
    #     return cls(v=mesh.vertices, f=mesh.faces)

    def __repr__(self):
        return f"lacecore.Mesh(num_v={self.num_v}, num_f={self.num_f})"

    @property
    def num_v(self):
        """
        The number of vertices.

        Return:
            int: The number of vertices.
        """
        return len(self.v)

    @property
    def num_f(self):
        """
        The number of faces.

        Return:
            int: The number of faces.
        """
        return len(self.f)
