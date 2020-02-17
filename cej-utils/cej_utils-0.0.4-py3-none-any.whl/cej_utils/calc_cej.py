import itertools
import json
import warnings
from typing import List, Optional, Tuple, Dict

import imantics
import numpy as np
from shapely.geometry import Polygon, LineString, Point, MultiPolygon, MultiPoint
from shapely.ops import nearest_points, unary_union

from cej_utils.cej_calculations import CejCalculations
from cej_utils.closest_enamel_bone_pairs import get_closest_enamel_bone_pairs


def get_centroid_pts_from_mask(mask: np.ndarray, bayes_threshold: float = 0.5) -> \
        List[Optional[Tuple[float, float]]]:
    """
    Gets centroids from larger segmentation mask (e.g. CEJ, bone points)
    :param mask: numpy array corresponding to an image channel
    :param bayes_threshold: thresholds if provided a probability map rather than a
        binary image
    :return:
    """
    where_prediction = mask > bayes_threshold

    polygons = imantics.Polygons.from_mask(where_prediction).points
    candidate_pts = []
    multipoly = []
    for polygon in polygons:
        if len(polygon) > 2:
            shapely_poly = Polygon(polygon)
            if CejCalculations.get_valid(shapely_poly):
                multipoly.append(CejCalculations.get_valid(shapely_poly))

    poly_union = unary_union(multipoly)

    if isinstance(poly_union, Polygon) and not poly_union.is_empty:
        coords = poly_union.centroid.coords[0]
        candidate_pts = [(coords[0], coords[1])]
    elif not poly_union.is_empty:
        for poly in poly_union:
            coords = poly.centroid.coords[0]
            candidate_pts.append((coords[0], coords[1]))

    return candidate_pts


def match_centroid_pt_to_tooth(
        centroid_pts_from_mask: List[Optional[Tuple[float, float]]],
        tooth_dict
) -> Dict:
    """
    Take in list of x-y point coordinates and return matched with a tooth number
    """
    label_cej_pts = MultiPoint([(val[0], val[1]) for val in centroid_pts_from_mask])

    tooth2coords = {tooth_num: [] for tooth_num in tooth_dict.keys()}
    if isinstance(label_cej_pts, Point):
        label_cej_pts = [label_cej_pts]

    tooth_poly_list = [(tooth_num, tooth_poly) for tooth_num, tooth_poly in
                       tooth_dict.items()]
    # Reverse sort by area so that in case of a distance tie, the tooth with the
    # largest area wins out
    tooth_poly_list.sort(key=lambda x: x[1].area, reverse=True)

    # Create mapping from label_cej_pts to a list of intersection areas.
    # This mapping is to make sure no two points from the same intersection area get
    # assigned to the same tooth
    # TODO: Use overlap classes for this
    tooth_combos = itertools.combinations(tooth_poly_list, 2)

    tooth_intersections = [
        poly_pair[0][1].intersection(poly_pair[1][1]) for poly_pair in tooth_combos
    ]
    tooth_intersections = [
        intersection.minimum_rotated_rectangle for intersection in tooth_intersections
        if intersection.area > 0
    ]

    # print(f'DEBUG len(tooth_intersection){len(tooth_intersections)}')
    def pt_to_intersection_index(label_cej_pt, tooth_intersections):
        """
        Gets tooth number of largest tooth that has intersection with another tooth and also intersects with a cej point
        """
        val = None
        for ix, tooth_intersection in enumerate(tooth_intersections):
            if tooth_intersection.intersects(label_cej_pt):
                val = ix
                break
            else:
                # print(f'DEBUG tooth_intersection:{tooth_intersection} not_contain_pt:{label_cej_pt}')
                pass
        return val

    # dict of pt: intersection class index
    pt_to_intersection = {
        tuple(map(int, label_cej_pt.coords[0])):
            pt_to_intersection_index(label_cej_pt, tooth_intersections)
        for label_cej_pt in label_cej_pts
    }

    # pt_to_intersection = {t[0]: t[1] for t in sorted(pt_to_intersection.items(), key=lambda x: x[1] if x[1] != None else x[0][0], reverse=True)}

    def is_eligible_tooth(tooth_num, curr_pt):
        val = True
        if len(tooth2coords[tooth_num]) > 0:
            for v in tooth2coords[tooth_num]:
                pt = (v['x'], v['y'])
                ix_1 = pt_to_intersection[pt]
                ix_2 = pt_to_intersection[curr_pt]
                # print(f'DEBUG tooth_num:{tooth_num} pt:{pt} curr_pt:{curr_pt} ix_1:{ix_1} ix_2:{ix_2}')
                if ix_1 == ix_2 and ix_1:
                    val = False
                    break
        return val

    def has_enough_pts(tooth_num):
        if len(tooth2coords[tooth_num]) < 2:
            return False
        return True

    for label_cej_pt in label_cej_pts:
        min_dist = CejCalculations.LARGE_DISTANCE
        min_dist_tooth_num = None

        for tooth_num, tooth_poly in tooth_poly_list:
            # if other pt(s) associated with tooth_poly map to same intersection area as
            # current cej_pt then reject this pt`q

            # if not is_eligible_tooth(tooth_num,tuple(map(int,label_cej_pt.coords[0]))):
            #     continue
            # if has_enough_pts(tooth_num):
            #     continue

            # Find the boundary point on the tooth closest to this CEJ
            if tooth_poly:
                try:
                    nearest_geoms = nearest_points(tooth_poly, label_cej_pt)
                    # See how far this CEJ is from the tooth
                    dist0 = LineString([nearest_geoms[0], label_cej_pt]).length
                    if dist0 < min_dist:
                        min_dist = dist0
                        min_dist_tooth_num = tooth_num
                except Exception as e:
                    print('EXCEPTION tooth_poly:{} label_cej_pt:{}'.format(
                        tooth_poly, label_cej_pt
                    ))
                    print(e)

        coords = label_cej_pt.coords[0]

        if min_dist_tooth_num in tooth2coords:
            tooth2coords[min_dist_tooth_num].append(
                {'x': int(coords[0]), 'y': int(coords[1])}
            )
        elif min_dist_tooth_num:
            tooth2coords[min_dist_tooth_num] = [
                {'x': int(coords[0]), 'y': int(coords[1])}
            ]
    # print(f'DEBUG tooth2coords: {tooth2coords}')
    num_per_tooth = {k: len(v) for k, v in tooth2coords.items()}
    # print(f'DEBUG num pts per tooth: {num_per_tooth}')

    return tooth2coords


def pick_largest_tooth(tooth_polygons):
    if type(tooth_polygons[0]) == dict:
        polygons = [
            CejCalculations.cleanup_geometry(tooth_polygons,
                                             return_as_shapely_object=True)
        ]
    else:
        polygons = [
            CejCalculations.cleanup_geometry(poly, return_as_shapely_object=True)
            for poly in tooth_polygons
        ]

    p = sorted(polygons, key=lambda x: x.area, reverse=True)[0]
    if isinstance(p, MultiPolygon):
        p = list(p)
        p = sorted(p, key=lambda x: x.area, reverse=True)[0]

    return p


def calc_cej_per_tooth(tooth_mask,
                       is_maxillary,
                       bone_enamel_boundaries,
                       predicted_cejs,
                       np_image=None,
                       debug_print=False,
                       tooth_shapely_poly=None):
    """
    Caclulate CEJ calculations per tooth.
    This function should not be called by the user directly.
    """
    cej_calc = CejCalculations(bone_enamel_boundaries, tooth_mask, is_maxillary,
                               np_image=np_image)
    pts_cej, tooth_centroid = cej_calc.cej_alveolor_pts(predicted_cejs,
                                                        debug_print=debug_print)
    on_image_boundary = [False, False]

    if pts_cej['bone']:
        pts_cej['enamel'], pts_cej['bone'] = get_closest_enamel_bone_pairs(
            pts_cej['enamel'], pts_cej['bone'],
            tooth_centroid=tooth_centroid,
            tooth_shapely_poly=tooth_shapely_poly,
            bone_mask=bone_enamel_boundaries['bone_mask'])
        for ix, pt_xy in enumerate(pts_cej['bone']):
            if pt_xy:
                on_image_boundary[ix] = cej_calc.is_near_image_border(
                    [pts_cej['bone'][ix]['y'], pts_cej['bone'][ix]['x']])
    pts_cej['bone_pt_on_image_boundary'] = on_image_boundary

    return pts_cej


def get_cej_abc_pts(input):
    """
    GET CEJ points from masks of enamel, bone, tooth and optionally restoration, used in segmentation model
    Input: {'masks': ndarray of masks, 'label2mask': {'enamel':enamel_index,...}}
    Output: CEJ and Bone points
    """
    label2mask = {label.lower(): ind for label, ind in input['label2mask'].items()}
    masks = input['masks']
    bone_mask = np.squeeze(masks[label2mask['bone']])
    cej_mask = np.squeeze(masks[label2mask['cej_center']])

    bone_enamel_masks = {'bone': bone_mask, 'enamel': None}
    bone_enamel_boundaries = {'bone': None, 'enamel': None, 'bone_mask': None}
    bone_enamel_boundaries['bone'] = CejCalculations.get_segmentations(
        bone_enamel_masks['bone'])
    bone_enamel_boundaries['bone_mask'] = bone_enamel_masks['bone']

    tooth_masks = {key.lower(): np.squeeze(masks[ix]) for key, ix in label2mask.items()
                   if 'tooth#' in key}

    tooth = {tooth_number: CejCalculations.get_tooth_boundaries(tooth_mask)
             for tooth_number, tooth_mask in tooth_masks.items()}

    tooth_shapely_polys = {tooth_num: pick_largest_tooth(tooth_geometry)
                           for tooth_num, tooth_geometry in tooth.items()
                           if tooth_geometry}

    cej_pts_from_mask = get_centroid_pts_from_mask(cej_mask, bayes_threshold=0.5)
    matched_cejs = match_centroid_pt_to_tooth(cej_pts_from_mask, tooth_shapely_polys)

    cej_abc_pts = {}
    for key, ix in label2mask.items():
        if 'tooth#' not in key:
            continue
        tooth_number = key.lower()
        if tooth_number not in matched_cejs:
            continue
        predicted_cejs = matched_cejs[tooth_number]
        is_maxillary = tooth_number.find('u') != -1
        tooth_mask = np.squeeze(masks[ix])

        pts = calc_cej_per_tooth(
            tooth_mask,
            is_maxillary,
            bone_enamel_boundaries,
            predicted_cejs,
            np_image=None,
            debug_print=False,
            tooth_shapely_poly=tooth_shapely_polys[tooth_number]
        )

        cej_abc_pts[tooth_number] = pts

    return cej_abc_pts


def get_cej_abc_pts_e2e(input):
    """
    Get CEJ and bone points from masks of enamel, bone, tooth and optionally restoration, used in segmentation model
    Input: {'masks': ndarray of masks, 'label2mask': {'enamel':enamel_index,...}}
    Output: CEJ and Bone points
    """

    label2mask = {label.lower(): ind for label, ind in input['label2mask'].items()}
    masks = input['masks']
    cej_mask = np.squeeze(masks[label2mask['cej_center']])
    bone_pt_mask = np.squeeze(masks[label2mask['bone_point']])

    tooth_masks = {key.lower(): np.squeeze(masks[ix]) for key, ix in label2mask.items()
                   if 'tooth#' in key}

    tooth = {tooth_number: CejCalculations.get_tooth_boundaries(tooth_mask)
             for tooth_number, tooth_mask in tooth_masks.items()}

    tooth_shapely_polys = {tooth_num: pick_largest_tooth(tooth_geometry)
                           for tooth_num, tooth_geometry in tooth.items()
                           if tooth_geometry}

    cej_pts_from_mask = get_centroid_pts_from_mask(cej_mask, bayes_threshold=0.5)
    matched_cejs = match_centroid_pt_to_tooth(cej_pts_from_mask, tooth_shapely_polys)

    bone_pts_from_mask = get_centroid_pts_from_mask(bone_pt_mask, bayes_threshold=0.5)
    matched_bone_pts = match_centroid_pt_to_tooth(bone_pts_from_mask,
                                                  tooth_shapely_polys)

    cej_abc_pts = {}
    for key, ix in label2mask.items():
        if 'tooth#' not in key:
            continue
        tooth_number = key.lower()
        if tooth_number not in matched_cejs:
            continue
        cej_abc_pts[tooth_number] = {'bone': matched_bone_pts[tooth_number],
                                     'enamel': matched_cejs[tooth_number]}

    return cej_abc_pts


def extract_cej_abc_pts_from_prediction(cej_pts_from_mask, enamel_geometry,
                                        bone_geometry, restoration_geometry,
                                        toothnum_geometries,
                                        orig_size, np_image):
    """
    Extract CEJ points from a json with bone, enamel and tooth boundaries
    Input: Standard Overjet result Json
    Output: List of points
    """
    bone_enamel_boundaries = {}
    ensure_in_bound_fn = lambda l: [
        {'x': min(val['x'], orig_size[0] - 1), 'y': min(val['y'], orig_size[1] - 1)} for
        val
        in l]

    bone_enamel_boundaries['enamel'] = [ensure_in_bound_fn(val) for val in
                                        enamel_geometry]
    bone_enamel_boundaries['bone'] = [ensure_in_bound_fn(val) for val in bone_geometry]

    convert_to_tuple_list_fn = lambda pt_list: [(pt['x'], pt['y']) for pt in pt_list]
    bone_input = [convert_to_tuple_list_fn(val) for val in
                  bone_enamel_boundaries['bone']]

    bone_poly = imantics.Polygons(bone_input)
    bone_enamel_boundaries['bone_mask'] = bone_poly.mask(width=orig_size[0],
                                                         height=orig_size[1]).array

    restoration_boundaries = [ensure_in_bound_fn(val) for val in restoration_geometry]

    cej_abc_pts = {}

    tooth = {val['label']: val['geometry'] for val in toothnum_geometries if
             val['geometry']}

    tooth_shapely_polys = {tooth_num: pick_largest_tooth(tooth_geometry)
                           for tooth_num, tooth_geometry in tooth.items()}
    matched_cejs = match_centroid_pt_to_tooth(
        convert_to_tuple_list_fn(cej_pts_from_mask), tooth_shapely_polys)
    for val in toothnum_geometries:
        if not val['geometry']:
            continue
        tooth_number = val['label']
        predicted_cejs = matched_cejs[tooth_number]
        tooth_palmer_label = val['palmer_label']
        tooth_input = [convert_to_tuple_list_fn(v) for v in val['geometry']]
        tooth_poly = imantics.Polygons(tooth_input)
        tooth_mask = tooth_poly.mask(width=orig_size[0], height=orig_size[1]).array
        is_maxillary = tooth_palmer_label.lower().find('u') != -1
        debug_print = False

        pts = calc_cej_per_tooth(
            tooth_mask,
            is_maxillary,
            bone_enamel_boundaries,
            predicted_cejs,
            np_image=np_image,
            debug_print=debug_print,
            tooth_shapely_poly=tooth_shapely_polys[tooth_number])

        cej_abc_pts[tooth_number] = pts

    return cej_abc_pts


def extract_cej_abc_pts_from_prediction_e2e(cej_pts_from_mask,
                                            bone_pts_from_mask,
                                            toothnum_geometries,
                                            orig_size,
                                            np_image):
    """
    Extract CEJ points from a json with bone, enamel and tooth boundaries
    Input: Standard Overjet result Json
    Output: List of points
    """
    convert_to_tuple_list_fn = lambda pt_list: [(pt['x'], pt['y']) for pt in pt_list]
    cej_abc_pts = {}

    tooth = {val['label']: val['geometry'] for val in toothnum_geometries if
             val['geometry']}

    tooth_shapely_polys = {tooth_num: pick_largest_tooth(tooth_geometry)
                           for tooth_num, tooth_geometry in tooth.items()}

    # TODO: This should be one function that also makes sure each bone point/cej pair makes sense.
    matched_cejs = match_centroid_pt_to_tooth(
        convert_to_tuple_list_fn(cej_pts_from_mask), tooth_shapely_polys)
    matched_bone_points = match_centroid_pt_to_tooth(
        convert_to_tuple_list_fn(bone_pts_from_mask), tooth_shapely_polys)
    for val in toothnum_geometries:
        if not val['geometry']:
            continue
        tooth_number = val['label']
        predicted_cejs = matched_cejs[tooth_number]
        predicted_bone_points = matched_bone_points[tooth_number]

        cej_abc_pts[tooth_number] = {'enamel': predicted_cejs,
                                     'bone': predicted_bone_points}

    return cej_abc_pts


def get_cej_pts_from_labelbox(input, extracted_cejs=None):
    """
    Get labeled CEJ points from Labelbox exported json
    Input: {'labelbox_json':/path/to/labelboxjson}
    :type extracted_cej: dict of extracted cejs used as tiebreaker
    Output: [{'external_id':external_id,'cej_abc':{tooth_number_palmer:{'x':x,'y':y}},'image_url':image_url},...]
    """

    def dist_fn(pt):
        if pt[1]:
            return np.sqrt(
                (pt[0]['x'] - pt[1]['x']) ** 2 + (pt[0]['y'] - pt[1]['y']) ** 2)
        else:
            return CejCalculations.LARGE_DISTANCE

    labels_json_path = input['labelbox_json']
    with open(labels_json_path) as json_file:
        r = json.load(json_file)
    all_cej = {}

    for result in r:
        if 'CEJ' in result['Label']:
            external_id = result['External ID']
            # if external_id == '2012-12-03T10:35:16.000000000-05:00~0B.jpg/704/clinic_1005_converted':
            label_cej = [val['geometry'] for val in result['Label']['CEJ']]
            image_url = result['Labeled Data']
            label_cej_pts = MultiPoint([(val['x'], val['y']) for val in label_cej])

            def warning_missing_tooth_num_fn(val):
                if 'tooth_number_palmer' in val:
                    return True
                else:
                    warnings.warn(f'MISSING TOOTH NUMBER in {external_id}',
                                  stacklevel=0)
                    return False

            tooth = {
                val['tooth_number_palmer']: validateCEJPts.cleanup_geometry(
                    val['geometry'],
                    return_as_shapely_object=True
                )
                for val in result['Label']['Tooth'] if warning_missing_tooth_num_fn(val)
            }

            tooth2coords = {tooth_num: {'enamel': []} for tooth_num in tooth.keys()}
            if isinstance(label_cej_pts, Point):
                label_cej_pts = [label_cej_pts]

            for label_cej_pt in label_cej_pts:
                min_dist = CejCalculations.LARGE_DISTANCE
                min_dist_tooth_num = None
                for tooth_num, tooth_poly in tooth.items():
                    # Find the boundary point on the tooth closest to this CEJ
                    try:
                        nearest_geoms = nearest_points(tooth_poly, label_cej_pt)

                    except Exception as e:
                        warnings.warn(
                            f'Check Labelbox bad geometry for {external_id} and tooth_number:{tooth_num}')
                        print('******')
                        print(tooth_poly)
                        print('******')
                        continue

                    # See how far this CEJ is from the tooth
                    dist0 = LineString([nearest_geoms[0], label_cej_pt]).length

                    if dist0 < min_dist:
                        min_dist = dist0
                        min_dist_tooth_num = tooth_num

                coords = label_cej_pt.coords[0]
                # Even if there is no intersection with enamel we assign this CEJ to this tooth's enamel key

                if min_dist_tooth_num in tooth2coords:
                    tooth2coords[min_dist_tooth_num]['enamel'].append(
                        {'x': int(coords[0]), 'y': int(coords[1])})

                else:
                    if min_dist_tooth_num:
                        tooth2coords[min_dist_tooth_num]['enamel'] = [
                            {'x': int(coords[0]), 'y': int(coords[1])}]

            if extracted_cejs:
                # If there is > 2 assigned CEJ points, relabel using extracted points as reference
                # TODO Need to see if Johnny's distance code works better for this
                if external_id in extracted_cejs:
                    for tooth_num in tooth2coords:
                        if len(tooth2coords[tooth_num]['enamel']) > 2 and tooth_num in \
                                extracted_cejs[external_id][
                                    'cej_abc']:
                            extracted_cej = \
                                extracted_cejs[external_id]['cej_abc'][tooth_num][
                                    'enamel']
                            if extracted_cej:
                                tooth_cejs = tooth2coords[tooth_num]['enamel']
                                c = sorted(
                                    list(itertools.product(tooth_cejs, extracted_cej)),
                                    key=dist_fn)
                                tooth2coords[tooth_num]['enamel'] = [c[0][0], c[0][1]]

            all_cej[external_id] = {'cej_abc': tooth2coords, 'image_url': image_url}
    return all_cej


def get_cej_pts_from_labelbox_e2e(input):
    """
    Get labeled CEJ and bone points from Labelbox exported json
    Input: {'labelbox_json':/path/to/labelboxjson}
    :type extracted_cej: dict of extracted cejs used as tiebreaker
    Output: [{'external_id':external_id,'cej_abc':{tooth_number_palmer:{'x':x,'y':y}},'image_url':image_url},...]
    """

    def dist_fn(pt):
        if pt[1]:
            return np.sqrt(
                (pt[0]['x'] - pt[1]['x']) ** 2 + (pt[0]['y'] - pt[1]['y']) ** 2)
        else:
            return CejCalculations.LARGE_DISTANCE

    labels_json_path = input['labelbox_json']
    with open(labels_json_path) as json_file:
        r = json.load(json_file)
    all_cej = {}

    # pt_labels = ['Bone level point', 'Bone depth point', 'CEJ']
    pt_labels = ['Bone level point', 'CEJ']

    for result in r:
        external_id = result['External ID']
        image_url = result['Labeled Data']

        def warning_missing_tooth_num_fn(val):
            if 'tooth_number_palmer' in val:
                return True
            else:
                warnings.warn(f'MISSING TOOTH NUMBER in {external_id}', stacklevel=0)
                return False

        tooth = {
            val['tooth_number_palmer']: validateCEJPts.cleanup_geometry(val['geometry'],
                                                                        return_as_shapely_object=True)
            for val in result['Label']['Tooth']
            if warning_missing_tooth_num_fn(val)}

        tooth2coords = {tooth_num: {'enamel': [], 'bone': []} for tooth_num in
                        tooth.keys()}

        for pt_label in pt_labels:
            if pt_label in result['Label']:
                label_cej = [val['geometry'] for val in result['Label'][pt_label]]
                label_cej_pts = MultiPoint([(val['x'], val['y']) for val in label_cej])

                if isinstance(label_cej_pts, Point):
                    label_cej_pts = [label_cej_pts]

                for label_cej_pt in label_cej_pts:
                    min_dist = CejCalculations.LARGE_DISTANCE
                    min_dist_tooth_num = None
                    for tooth_num, tooth_poly in tooth.items():
                        # Find the boundary point on the tooth closest to this CEJ
                        try:
                            nearest_geoms = nearest_points(tooth_poly, label_cej_pt)
                        except Exception as e:
                            warnings.warn(
                                f'Check Labelbox bad geometry for {external_id} and tooth_number:{tooth_num}')
                            print('******')
                            print(tooth_poly)
                            print('******')
                            continue

                        # See how far this CEJ is from the tooth
                        dist0 = LineString([nearest_geoms[0], label_cej_pt]).length

                        if dist0 < min_dist:
                            min_dist = dist0
                            min_dist_tooth_num = tooth_num
                    coords = label_cej_pt.coords[0]

                    if min_dist_tooth_num in tooth2coords:
                        if pt_label == 'CEJ':
                            tooth2coords[min_dist_tooth_num]['enamel'].append(
                                {'x': int(coords[0]), 'y': int(coords[1])})
                        elif pt_label == 'Bone level point':
                            tooth2coords[min_dist_tooth_num]['bone'].append(
                                {'x': int(coords[0]), 'y': int(coords[1])})
                    else:
                        if min_dist_tooth_num:
                            if pt_label == 'CEJ':
                                tooth2coords[min_dist_tooth_num]['enamel'] = [
                                    {'x': int(coords[0]), 'y': int(coords[1])}]
                            elif pt_label == 'Bone level point':
                                tooth2coords[min_dist_tooth_num]['bone'] = [
                                    {'x': int(coords[0]), 'y': int(coords[1])}]

                all_cej[external_id] = {'cej_abc': tooth2coords, 'image_url': image_url}
    return all_cej


def calc_dist(cej_label, cej_extract):
    dist = 0
    missing_pts = 0
    extra_pts = 0
    LARGE_DISTANCE = 100000000
    for tooth_number in cej_label['cej_abc']:
        cej_label_pt = sorted(
            [x for x in cej_label['cej_abc'][tooth_number]['enamel'] if x is not None],
            key=lambda v: v['x'])
        #         print(len(cej_label_pt))
        if tooth_number in cej_extract['cej_abc'] and \
                cej_extract['cej_abc'][tooth_number]['enamel']:
            cej_extracted_pt = cej_extract['cej_abc'][tooth_number]['enamel']

            def dist_fn(pt):
                if pt[1]:
                    return np.sqrt(
                        (pt[0]['x'] - pt[1]['x']) ** 2 + (pt[0]['y'] - pt[1]['y']) ** 2)
                else:
                    return LARGE_DISTANCE

            c = sorted(list(itertools.product(cej_label_pt, cej_extracted_pt)),
                       key=dist_fn)

            missing_pts += max(len([i for i in cej_label_pt if i]) - len(
                [i for i in cej_extracted_pt if i]), 0)
            extra_pts += max(len([i for i in cej_extracted_pt if i]) - len(
                [i for i in cej_label_pt if i]), 0)
            for elem in c:
                if elem[0] in cej_label_pt:
                    cej_label_pt.remove(elem[0])
                    if elem[1]:
                        dist_inc = dist_fn(elem)
                        dist += dist_inc
        else:
            missing_pts += len(cej_label_pt)

    return (dist, missing_pts, extra_pts)


def get_average_cej_metrics(labeled_cej, extracted_cej):
    num_images = len([i for i in labeled_cej if i in extracted_cej])
    total_dist = 0
    total_missed = 0
    total_extra = 0
    for external_id in labeled_cej:
        if external_id not in extracted_cej:
            continue
        dist, missing_pts, extra_pts = calc_dist(labeled_cej[external_id],
                                                 extracted_cej[external_id])
        total_dist += dist
        total_missed += missing_pts
        total_extra += extra_pts

    print(
        f'Average dist: {total_dist / num_images}, Total missed: {total_missed}, Total extra: {total_extra}')


def find_annotation_errors(labels_json_path, df_file_path):
    """
    Get labeled CEJ points from Labelbox exported json
    labels_json_path: /path/to/labelboxjson
    df_file_path: /path/to/csv_labelbox
    Output: dataframe with project, problem, externalid and labelpath.
    """
    import pandas as pd

    df = pd.read_csv(df_file_path)
    with open(labels_json_path) as json_file:
        r = json.load(json_file)

    all_cej = {}

    problems = []
    label_box_paths = []
    external_ids = []
    projects = []

    for result in r:
        if 'CEJ' in result['Label']:
            external_id = result['External ID']
            labelbox_url = result['View Label']
            label_cej = [val['geometry'] for val in result['Label']['CEJ']]
            image_url = result['Labeled Data']
            label_cej_pts = MultiPoint([(val['x'], val['y']) for val in label_cej])

            def warning_line_or_pt_enamel_geometry(len_geometry):
                if len_geometry > 2:
                    return True
                else:
                    problems.append('Line or point enamel')
                    label_box_paths.append(
                        df[df['file_name'] == external_id]['View Label'].values[0])
                    external_ids.append(
                        df[df['file_name'] == external_id]['External ID'].values[0])
                    projects.append(
                        df[df['file_name'] == external_id]['Project Name'].values[0])
                    warnings.warn('Line or point enamel labelbox geometry in {}'.format(
                        labelbox_url), stacklevel=0)
                    return False

            if 'Enamel' not in result['Label']:
                problems.append('Missing Enamel')
                label_box_paths.append(
                    df[df['file_name'] == external_id]['View Label'].values[0])
                external_ids.append(
                    df[df['file_name'] == external_id]['External ID'].values[0])
                projects.append(
                    df[df['file_name'] == external_id]['Project Name'].values[0])
                warnings.warn('Missing enamel in {}'.format(labelbox_url))
                continue
            if 'Bone' not in result['Label']:
                problems.append('Missing Bone')
                label_box_paths.append(
                    df[df['file_name'] == external_id]['View Label'].values[0])
                external_ids.append(
                    df[df['file_name'] == external_id]['External ID'].values[0])
                projects.append(
                    df[df['file_name'] == external_id]['Project Name'].values[0])
                warnings.warn('Missing bone in {}'.format(labelbox_url))
                continue
            enamel_poly = MultiPolygon(
                [validateCEJPts.cleanup_geometry(val['geometry'],
                                                 return_as_shapely_object=True) for val
                 in
                 result['Label']['Enamel'] if
                 warning_line_or_pt_enamel_geometry(len(val['geometry']))])

            if not enamel_poly.is_valid:
                enamel_poly = enamel_poly.buffer(0)

            def warning_missing_tooth_num_fn(val):
                if 'tooth_number_palmer' in val:
                    return True
                else:
                    warnings.warn('MISSING TOOTH NUMBER in {}'.format(labelbox_url),
                                  stacklevel=0)
                    problems.append('Missing Tooth Number')
                    label_box_paths.append(
                        df[df['file_name'] == external_id]['View Label'].values[0])
                    external_ids.append(
                        df[df['file_name'] == external_id]['External ID'].values[0])
                    projects.append(
                        df[df['file_name'] == external_id]['Project Name'].values[0])
                    return False

            tooth = {val['tooth_number_palmer']: validateCEJPts.cleanup_geometry(
                val['geometry'],
                return_as_shapely_object=True) for val
                in result['Label']['Tooth'] if warning_missing_tooth_num_fn(val)}

            tooth2coords = {}
            assigned_pts = MultiPoint()
            tooth2enamel = {}
            for tooth_num, tooth_poly in tooth.items():
                enamel_in_tooth_poly = tooth_poly.intersection(enamel_poly)
                tooth2enamel[tooth_num] = enamel_in_tooth_poly
                points_in_poly = label_cej_pts.intersection(enamel_in_tooth_poly)
                tooth2coords[tooth_num] = {'enamel': []}
                if points_in_poly:
                    assigned_pts = assigned_pts.union(points_in_poly)
                    if isinstance(points_in_poly, MultiPoint):
                        tooth2coords[tooth_num]['enamel'] = [
                            {'x': int(point.coords[0][0]), 'y': int(point.coords[0][1])}
                            for point in points_in_poly]
                    else:
                        assert (len(points_in_poly.coords) == 1)
                        coords = points_in_poly.coords[0]
                        tooth2coords[tooth_num]['enamel'] = [
                            {'x': int(coords[0]), 'y': int(coords[1])}]
            unassigned_pts = label_cej_pts.difference(assigned_pts)

            if isinstance(unassigned_pts, Point):
                unassigned_pts = [unassigned_pts]

            for unassigned_pt in unassigned_pts:
                min_dist = CejCalculations.LARGE_DISTANCE
                min_dist_tooth_num = None
                for tooth_num, tooth_poly in tooth.items():
                    if tooth_poly.contains(unassigned_pt):
                        min_dist_tooth_num = tooth_num
                        break
                    try:
                        nearest_geoms = nearest_points(tooth_poly, unassigned_pt)
                    except Exception as e:
                        warnings.warn(
                            'Check Labelbox bad geometry for {} and tooth_number:{}'.format(
                                labelbox_url, tooth_num))
                        problems.append('Labelbox Bad Geometry on Tooth Number')
                        label_box_paths.append(
                            df[df['file_name'] == external_id]['View Label'].values[0])
                        external_ids.append(
                            df[df['file_name'] == external_id]['External ID'].values[0])
                        projects.append(
                            df[df['file_name'] == external_id]['Project Name'].values[
                                0])
                        print('******')
                        print(tooth_poly)
                        print('******')
                        continue
                    dist0 = int(LineString([nearest_geoms[0], unassigned_pt]).length)
                    if dist0 == 0:
                        dist0 = CejCalculations.LARGE_DISTANCE
                    dist1 = int(LineString([nearest_geoms[1], unassigned_pt]).length)
                    if dist1 == 0:
                        dist1 = CejCalculations.LARGE_DISTANCE
                    if min(dist0, dist1) < min_dist:
                        min_dist = min(dist0, dist1)
                        min_dist_tooth_num = tooth_num

                coords = unassigned_pt.coords[0]
                if min_dist_tooth_num in tooth2coords:
                    tooth2coords[min_dist_tooth_num]['enamel'].append(
                        {'x': int(coords[0]), 'y': int(coords[1])})
                else:
                    try:
                        tooth2coords[min_dist_tooth_num]['enamel'] = [
                            {'x': int(coords[0]), 'y': int(coords[1])}]
                    except:
                        print('fucked')
                        problems.append('Something is really fucked up')
                        label_box_paths.append(
                            df[df['file_name'] == external_id]['View Label'].values[0])
                        external_ids.append(
                            df[df['file_name'] == external_id]['External ID'].values[0])
                        projects.append(
                            df[df['file_name'] == external_id]['Project Name'].values[
                                0])
            all_cej[external_id] = {'cej_abc': tooth2coords, 'image_url': image_url}
            df_errors = pd.DataFrame.from_dict(
                {'problem': problems, 'project': projects, 'external_id': external_ids,
                 'label_box_path': label_box_paths})
    return df_errors


if __name__ == '__main__':

    """
    For testing the script.
    Usage: python3 calc_cej.py --labelbox_json=/Users/deepakramaswamy/Downloads/perio.cases1.json
    """
    try:
        json_file = '/Users/deepakramaswamy/Downloads/perio.cases1.json'
        extracted_cej = get_cej_pts_from_labelbox_e2e({'labelbox_json': json_file})
    except FileNotFoundError:
        json_file = '/home/devin_overjet_ai/labelbox/jsons/anatomy/train/processed/anatomy_train_v1.5.json'
        extracted_cej = get_cej_pts_from_labelbox_e2e({'labelbox_json': json_file})

    # labeled_cej = get_cej_pts_from_labelbox({'labelbox_json': json_file}, extracted_cej)
    # get_average_cej_metrics(labeled_cej, extracted_cej)
    #

    #
    # import pickle
    # import os
    # import argparse
    #
    # argparser = argparse.ArgumentParser()
    # argparser.add_argument('--labelbox_json', type=str,
    #                        help='path to labelbox exported json; If specified reports labeled CEJ points')
    # argparser.add_argument('--extract_cej', type=int, default=0)
    # args = argparser.parse_args()
    #
    # if not args.labelbox_json:
    #     mask_stack = []
    #     mask_index = {}
    #     mask_index_counter = 0
    #     bem = {'bone': None, 'enamel': None}
    #     bone = pickle.load(open(os.path.join(os.getcwd(), 'test_calc_cej/bone.p'), 'rb'))
    #     mask_stack.append(bone['mask'])
    #     mask_index['bone'] = mask_index_counter
    #     mask_index_counter += 1
    #
    #     enamel = pickle.load(open(os.path.join(os.getcwd(), 'test_calc_cej/enamel.p'), 'rb'))
    #     mask_stack.append(enamel['mask'])
    #     mask_index['enamel'] = mask_index_counter
    #     mask_index_counter += 1
    #
    #     crown = pickle.load(open(os.path.join(os.getcwd(), 'test_calc_cej/crown.p'), 'rb'))
    #     mask_stack.append(crown['mask'])
    #     mask_index['crown'] = mask_index_counter
    #     mask_index_counter += 1
    #
    #     filling_inlay = pickle.load(open(os.path.join(os.getcwd(), 'test_calc_cej/filling_inlay.p'), 'rb'))
    #     mask_stack.append(filling_inlay['mask'])
    #     mask_index['filling_inlay'] = mask_index_counter
    #     mask_index_counter += 1
    #
    #     for tooth_num in ['u3', 'u4', 'u5', 'u6', 'u7', 'u8', 'l5']:
    #         tooth = pickle.load(open(os.path.join(os.getcwd(), f'test_calc_cej/{tooth_num}.p'), 'rb'))
    #         mask_stack.append(tooth['mask'])
    #         mask_index['tooth#' + tooth_num] = mask_index_counter
    #         mask_index_counter += 1
    #
    #     input = {
    #         'masks': np.dstack(mask_stack),
    #         'label2mask': mask_index
    #     }
    #     pts = get_cej_abc_pts(input)
    # else:
    #     if args.extract_cej == 0:
    #         pts = get_cej_pts_from_labelbox({'labelbox_json': args.labelbox_json})
    #     else:
    #         pts = extract_cej_abc_pts_from_labelbox({'labelbox_json': args.labelbox_json})
    # # print(pts)
