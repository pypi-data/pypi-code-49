from shapely.geometry import Point, MultiPoint, Polygon, LineString
from shapely.ops import split, nearest_points, snap

LARGE_DISTANCE = 10000000


def min_arc_length(tooth_boundary, pts):
    """
    Finds the minimum arc length between two points on a closed boundary.
    """
    # Split tooth_boundary into fragments along pts
    multi_pts = MultiPoint(pts)
    cmp_pts = [Point(pts[0]), Point(pts[1])]
    s = split(tooth_boundary, multi_pts)

    def eq_fn(p1, p2):
        """ Check if two points are essentially the same. """
        return p1.almost_equals(p2, 2)

    select_frag = None
    for s_frag in s:
        frag_pts = [Point(s_frag.coords[0]), Point(s_frag.coords[-1])]
        # If pts match a fragment break
        if (eq_fn(frag_pts[0], cmp_pts[0]) and eq_fn(frag_pts[1], cmp_pts[1])) or (
                eq_fn(frag_pts[0], cmp_pts[1]) and eq_fn(frag_pts[1], cmp_pts[0])):
            select_frag = s_frag
            break

    if select_frag:
        # select the minimum of the fragment length and its complement
        frag_length = select_frag.length
        complement_frag_length = tooth_boundary.length - frag_length
        return min(frag_length, complement_frag_length), select_frag
    else:
        print('no match')
        return LARGE_DISTANCE, LARGE_DISTANCE


def create_shapely_polygon(geometry):
    """
    Creates shapely polygon
    """
    p = []
    for xy in geometry:
        p.append((xy['x'], xy['y']))
    return Polygon(p)


def is_close_pairing_on_arc(pt1, pt2, tooth_poly):
    """
    Checks if pt1 is close to pt2 by comparing straight line distance to distance along
    tooth boundary.
    """

    # Convert to shapely object if needed
    if not isinstance(tooth_poly, Polygon):
        try:
            shapely_poly = create_shapely_polygon(tooth_poly)
        except Exception as e:
            print(f'EXCEPTION_tooth_poly: {tooth_poly}')
            raise e
    else:
        shapely_poly = tooth_poly

    tooth_boundary = shapely_poly.boundary

    # Get nearest points of candidate points on the tooth boundary
    npt0_0, npt0_1 = nearest_points(tooth_boundary, Point(pt1[0]['x'], pt1[0]['y']))
    npt1_0, npt1_1 = nearest_points(tooth_boundary, Point(pt2[0]['x'], pt2[0]['y']))
    new_pts = [npt0_0, npt1_0]

    # Snap with tolerance 0 thus making sure sure nearest points are actually on tooth
    # boundary
    line = LineString(new_pts)
    new_tooth_boundary = snap(tooth_boundary, line, 0.1)

    # Check if min_length_along_arc is not too far away from the straight line length
    min_length_along_arc, s_arc = min_arc_length(new_tooth_boundary, new_pts)
    val = line.length * 1.5 > min_length_along_arc

    return val
