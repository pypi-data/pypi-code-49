import itertools

from cej_utils.is_close_pairing import is_close_pairing_on_arc


def get_closest_enamel_bone_pairs(curr_enamel_pts,
                                  curr_bone_pts,
                                  tooth_centroid=None,
                                  tooth_shapely_poly=None,
                                  bone_mask=None):
    """
    Return the best matching pairs of bone and enamel pts
    """

    if not curr_bone_pts or not curr_enamel_pts:
        return curr_enamel_pts, curr_bone_pts

    curr_enamel_pts += [None for k in range(len(curr_enamel_pts), len(curr_bone_pts))]

    p = list(itertools.product(curr_enamel_pts, curr_bone_pts))

    def dist_fn(be):
        if be[0] and be[1]:
            return (be[0]['x'] - be[1]['x']) ** 2 + (be[0]['y'] - be[1]['y']) ** 2
        else:
            return 1000000

    p = sorted(p, key=dist_fn)

    enamel_pts = [p[0][0]]
    bone_pts = [p[0][1]]
    for pt_pair in p[1:]:
        if pt_pair[0] is not None and pt_pair[0] in enamel_pts:
            continue
        if pt_pair[1] is not None and pt_pair[1] in bone_pts:
            continue
        enamel_pts += [pt_pair[0]]
        bone_pts += [pt_pair[1]]
        if len(enamel_pts) == 2:
            break

    # Check validity of enamel and point point pairing based on arc and as-the-crow-flies distances
    if len(enamel_pts) == 2 and len(bone_pts) == 2 and tooth_shapely_poly:
        if enamel_pts[0] and bone_pts[0] and not is_close_pairing_on_arc(
                enamel_pts[0:1], bone_pts[0:1], tooth_shapely_poly):
            bone_pts = [None, bone_pts[1]]
        if enamel_pts[1] and bone_pts[1] and not is_close_pairing_on_arc(
                enamel_pts[1:2], bone_pts[1:2], tooth_shapely_poly):
            bone_pts = [bone_pts[0], None]

    if len(enamel_pts) == 1:
        assert (len(bone_pts) == 1)
        if tooth_shapely_poly and is_close_pairing_on_arc(enamel_pts, bone_pts,
                                                          tooth_shapely_poly):
            enamel_pts.append(None)
            bone_pts.append(None)
        else:
            enamel_pts = [None, enamel_pts[0]]
            bone_pts = [bone_pts[0], None]

    # if bone mask is supplied, make sure enamel point is not within bone area
    if bone_mask is not None:
        for i, enamel_pt in enumerate(enamel_pts):
            if enamel_pt and bone_mask[enamel_pt['y'], enamel_pt['x']]:
                enamel_pts[i] = None

    return enamel_pts, bone_pts
