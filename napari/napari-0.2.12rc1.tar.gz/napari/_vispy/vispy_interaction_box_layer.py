from vispy.scene.visuals import Line, Compound, Markers
from .vispy_base_layer import VispyBaseLayer
import numpy as np


class VispyInteractionBoxLayer(VispyBaseLayer):
    def __init__(self, layer):
        # Create a compound visual with the following two subvisuals:
        # Markers: corresponding to the vertices of the interaction box
        # Lines: The lines of the interaction box used for highlights.
        node = Compound([Line(), Markers()])

        super().__init__(layer, node)

        self.layer.events.highlight.connect(self._on_highlight_change)

        self._reset_base()
        self._on_highlight_change()

    def _on_highlight_change(self, event=None):
        # Compute the location and properties of the vertices and box that
        # need to get rendered
        (
            vertices,
            face_color,
            edge_color,
            pos,
            width,
        ) = self.layer._compute_vertices_and_box()

        if vertices is None or len(vertices) == 0:
            vertices = np.zeros((1, self.layer.dims.ndisplay))
            size = 0
        else:
            vertices = vertices + 0.5
            size = self.layer._vertex_size

        self.node._subvisuals[1].set_data(
            vertices,
            size=size,
            face_color=face_color,
            edge_color=edge_color,
            edge_width=1.5,
            symbol='square',
            scaling=False,
        )

        if pos is None or len(pos) == 0:
            pos = np.zeros((1, self.layer.dims.ndisplay))
            width = 0
        else:
            pos = pos + 0.5

        self.node._subvisuals[0].set_data(
            pos=pos, color=edge_color, width=width
        )
