""" Module to compute the directed projection 
of a point to a surface along a direction

::

        ___
            \
             \
        x---->\
               \

OST : Seven nation Army (Westworld), R. Djawadi
"""

from scipy import spatial
import numpy as np


BIG = 1e6


def projection_kdtree(
        points,
        directions,
        point_surface,
        normal_surface,
        **kwargs
        ):
    """
    Project the n points folowing the direction on the m suface.

:param points: "p"  nparray of shape (n,3),
:param directions: nparray of shape (n,3),
:param point_surface: "s" nparray of shape (m,3),
:param normal_surface: nparray of shape (m,3),
:param neigbors: nb of neigbors to take into account
:param tol: maximum distance beyond cyl dist witl bi set to BIG

:returns:
    - **points** - "t"  nparray of shape (n,3), moved on the surface
    - **indexes** - neigborhood of the points (n,k)
    - **cyl_dist** - cylindrical distance of p with each neighbor (n,k)    
        
::

           < shp_dist >
    ______s___________t__________________
          |' .                       A
          |     '  .< cyl_dist >     .
          v                          .< surface_dist>
                 4                   .
                /                    .
               /                     .
              p                      V

          align : alignment (pscal of two unit vectors, in [-1,1])

- compute a kdtree, and reduce the surfacepoints to a neighborhood indexes  [n,k]
- iterate over all points [n]:
- compute the distance surface_dist to the surface, for each neighbor [k]
- compute the alignment align, scal. product of normal and direction [k]
- compute all points all_pts moved on the surface [k,3]
- compute shperical distance  for each point to its moved point [k]
- get the closest point idx closest_pt
- recompute the cylindrical distance cyl_dist for all the neigborhood
    """

    opts = {'neighbors':1000, 'tol':1000.0}
    for keyword in opts:
        if keyword in kwargs:
            opts[keyword] = kwargs[keyword]

    opts['neighbors'] = min(point_surface.shape[0], opts['neighbors'])
    print("KDTree with  "
          + "\n-   Surface points | "
          + str(point_surface.shape[0])
          + "\n- Projected points | "
          + str(points.shape[0])
          + "\n-        Neighbors | "
          + str(opts['neighbors'])
          )

    kdtree = spatial.cKDTree(point_surface)

    # first projection, one neigbor
    _, indexes = kdtree.query(points,
                              k=1)
    moved_pts = []
    for point, direction, i in zip(points, directions, indexes):
        pt_surf = point_surface[i, :]
        nml_surf = normal_surface[i, :]
        surface_dist = np.sum(np.multiply((pt_surf - point),
                                          nml_surf))
        align = np.sum(np.multiply(nml_surf, direction))
        mv_pt = point[:] + (surface_dist / align) * direction[:]
        moved_pts.append(mv_pt)
    moved_pts = np.asarray(moved_pts)

    # second projection, all neigbors
    _, indexes = kdtree.query(moved_pts, k=opts['neighbors'])

    cyl_dists = []
    moved_pts = []
    for point, direction, indx in zip(points,
                                      directions,
                                      indexes):
        part_pts_surf = point_surface[indx, :]
        part_nml_surf = normal_surface[indx, :]

        surface_dist = np.sum(np.multiply((part_pts_surf - point),
                                          part_nml_surf),
                              axis=1)

        # scalar product of normals
        align = np.sum(np.multiply(part_nml_surf,
                                   direction),
                       axis=1)

        # all points projected
        all_pts = (point[np.newaxis, :]
                   + (surface_dist / align)[:, np.newaxis]
                   * direction[np.newaxis, :])

        sphere_dists = np.linalg.norm(part_pts_surf - all_pts, axis=1)

        closest_pt = all_pts[np.argmin(sphere_dists, axis=0), :]

        axis_dist = np.sum(np.multiply((part_pts_surf - closest_pt),
                                       direction),
                           axis=1)

        tmp_pts_surf = part_pts_surf - \
            axis_dist[:, np.newaxis]*direction[np.newaxis, :]
        cyl_dist = np.linalg.norm(tmp_pts_surf - closest_pt, axis=1)

        cyl_dist = np.where(align < 0.0, cyl_dist, BIG*np.ones(cyl_dist.shape))
        cyl_dist = np.where(sphere_dists < opts['tol'], cyl_dist,
                            BIG*np.ones(cyl_dist.shape))

        moved_pts.append(closest_pt)
        cyl_dists.append(cyl_dist)

    moved_pts = np.asarray(moved_pts)
    cyl_dists = np.asarray(cyl_dists)

    return (moved_pts,
            indexes,
            cyl_dists)
