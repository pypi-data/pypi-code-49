import shapely
import matplotlib.collections
from matplotlib.path import Path


def render(shapes, **path_patch_options):
    pathpatches = []
    for shape in shapes:
        if type(shape) is shapely.geometry.LineString:
            pathpatches.append(matplotlib.patches.PathPatch(
                matplotlib.path.Path(list(shape.coords), closed=False),
                fill=False, **path_patch_options
            ))
        elif type(shape) is shapely.geometry.LinearRing:
            pathpatches.append(matplotlib.patches.PathPatch(
                matplotlib.path.Path(list(shape.coords), closed=True),
                fill=False, **path_patch_options
            ))
        elif type(shape) is shapely.geometry.Polygon:
            vertices = list(shape.exterior.coords)
            codes = (
                [Path.MOVETO] +
                [Path.LINETO] * (len(vertices) - 2) +
                [Path.CLOSEPOLY]
            )

            for ring in shape.interiors:
                ring_vertices = list(ring.coords)
                ring_codes = (
                    [Path.MOVETO] +
                    [Path.LINETO] * (len(ring_vertices) - 2) +
                    [Path.CLOSEPOLY]
                )
                vertices += ring_vertices
                codes += ring_codes
            pathpatches.append(matplotlib.patches.PathPatch(
                matplotlib.path.Path(vertices, codes, closed=True),
                fill=True, **path_patch_options
            ))
        elif type(shape) is shapely.geometry.MultiPolygon:
            for shape in shape.geoms:
                vertices = list(shape.exterior.coords)
                codes = (
                    [Path.MOVETO] +
                    [Path.LINETO] * (len(vertices) - 2) +
                    [Path.CLOSEPOLY]
                )

                for ring in shape.interiors:
                    ring_vertices = list(ring.coords)
                    ring_codes = (
                        [Path.MOVETO] +
                        [Path.LINETO] * (len(ring_vertices) - 2) +
                        [Path.CLOSEPOLY]
                    )
                    vertices += ring_vertices
                    codes += ring_codes
                pathpatches.append(matplotlib.patches.PathPatch(
                    matplotlib.path.Path(vertices, codes, closed=True),
                    fill=True, **path_patch_options
                ))
        elif type(shape) is shapely.geometry.Point:
            continue
        else:
            raise ValueError('Unsupported shape type {}'.format(shape))

    return pathpatches


def patches(shapes, **path_patch_options):
    return matplotlib.collections.PatchCollection(
        render(shapes, **path_patch_options), match_original=True
    )
