import imantics
import numpy as np
from shapely.geometry import Polygon, LineString, Point, MultiPolygon
from shapely.ops import nearest_points


class CejCalculations:
    """
    Helper class for calculating CEJ. This class should NOT be used directly.
    """

    AREA_REMOVAL_PERC = 0.01  # Remove areas below AREA_REMOVAL_PERC of image size
    LARGE_DISTANCE = 10000000  # Large distance used in minimum calculations

    def __init__(self, bone_enamel_boundaries, tooth_mask, is_maxillary, np_image=None,
                 print_flag=False):
        """
        bone_enamel_boundaries is a dict corresponding to boundary points for Bone and Enamel
        tooth_mask is mask for a tooth
        is_maxillary is where the tooth is maxillary
        """
        # Boundaries of bone and enamel polygons
        self.bone_enamel_boundaries = bone_enamel_boundaries
        self.tooth_mask = tooth_mask
        self.is_maxillary = is_maxillary
        self.np_image = np_image
        self.print_flag = print_flag
        self.pixel_buffer = int(
            0.015 * np.sqrt(
                self.tooth_mask.size))  # Ignore boundary points within pixel_buffer from image edge
        self.pixel_buffer_vertical = int(0.01 * self.tooth_mask.shape[0])
        self.pixel_buffer_horizontal = int(0.01 * self.tooth_mask.shape[1])
        self.collinear_threshold = int(0.005 * np.sqrt(
            self.tooth_mask.size))  # pt considered collinear <= this threshold
        self.snapping_threshold = CejCalculations.compute_snapping_value(
            self.tooth_mask.size)  # snap <= this threshold

    def is_near_image_border(self, pt, debug_print=False):
        # Black curved border
        if self.np_image is None:
            val = False
        else:
            sum_top = np.sum(np.squeeze(self.np_image[:pt[0], pt[1]]).astype(bool))
            if debug_print:
                print(
                    f'DEBUG sum_top:{sum_top} pt:{pt} pixel_buffer:{self.pixel_buffer_vertical}')
            if sum_top < self.pixel_buffer_vertical:
                val = True
            else:
                sum_bottom = np.sum(
                    np.squeeze(self.np_image[pt[0]:, pt[1]]).astype(bool))
                if debug_print:
                    print(
                        f'DEBUG sum_bottom:{sum_bottom} pt:{pt} pixel_buffer:{self.pixel_buffer_vertical}')
                if sum_bottom < self.pixel_buffer_vertical:
                    val = True
                else:
                    sum_left = np.sum(
                        np.squeeze(self.np_image[pt[0], :pt[1]]).astype(bool))
                    if debug_print:
                        print(
                            f'DEBUG sum_sum_left:{sum_left} pt:{pt} pixel_buffer:{self.pixel_buffer_horizontal}')
                    if sum_left < self.pixel_buffer_horizontal:
                        val = True
                    else:
                        sum_right = np.sum(
                            np.squeeze(self.np_image[pt[0], pt[1]:]).astype(bool))
                        if debug_print:
                            print(
                                f'DEBUG sum_right:{sum_right} pt:{pt} pixel_buffer:{self.pixel_buffer_horizontal}')
                        if sum_right < self.pixel_buffer_horizontal:
                            val = True
                        else:
                            val = False
        return val

    def is_interior(self, pt):
        """
        Is the boundary point in the interior of the tooth_mask?
        Sanity check if our CEJ is super far from the bone
        """
        pt = (int(pt[0]), int(pt[1]))
        is_interior_pt = False
        border_width = int(self.pixel_buffer / 3) + 1
        if pt[0] > border_width and pt[0] < (
                self.tooth_mask.shape[0] - border_width) and pt[1] > border_width and \
                pt[1] < (
                self.tooth_mask.shape[1] - border_width) and (
        not self.is_near_image_border(pt)):
            top_sum = np.sum([1 for i in range(1, self.pixel_buffer) if
                              self.bone_enamel_boundaries['bone_mask'][
                                  max(pt[0] - i, 0), pt[1]]])
            bottom_sum = np.sum([1 for i in range(1, self.pixel_buffer) if
                                 self.bone_enamel_boundaries['bone_mask'][
                                     min(pt[0] + i, self.tooth_mask.shape[0] - 1), pt[
                                         1]]])
            if not self.is_maxillary:
                if top_sum <= bottom_sum:
                    is_interior_pt = True
            else:
                if bottom_sum <= top_sum:
                    is_interior_pt = True
        return is_interior_pt

    def reject_pt(self, row, col):
        """
        Check if point should be rejected
        """
        # Reject if point is in the border area of image
        return col < self.pixel_buffer or col > (
                    self.tooth_mask.shape[1] - self.pixel_buffer)

    def cej_alveolor_pts(self, predicted_cejs, debug_print=False):
        """
        Calculate bone points given CEJ points for this tooth
        """
        from imantics import Polygons
        from shapely.geometry import MultiLineString, MultiPolygon, Polygon, LinearRing
        bone_enamel_boundaries = self.bone_enamel_boundaries
        dict_keys = set(bone_enamel_boundaries.keys())
        # assert only two keys exist
        assert (len(dict_keys) == 3)

        # Find out the name of the other label
        other_label = list(dict_keys.difference(set(['bone', 'bone_mask'])))[0]
        # other_label = list(dict_keys.difference(set(['bone', 'bone_mask'])))[0]
        # This can be bone-enamel or bone-restoration
        boundary_bone_enamel_pts = {'bone': None, other_label: predicted_cejs}

        tooth_mask = self.tooth_mask
        tooth_centroid = None
        if bone_enamel_boundaries is not None:
            # Get polygons for tooth mask and height and width of the enclosing rectangle
            tooth_poly = Polygons.from_mask(tooth_mask)
            tooth_mask_points = [ptarray for ptarray in tooth_poly.points if
                                 len(ptarray) > 2]
            if not tooth_mask_points:
                return boundary_bone_enamel_pts
            tooth_mask_linear_rings = []
            tooth_mask_polys = []
            max_area = -1
            for mask_single in tooth_mask_points:
                if len(mask_single) > 2:
                    mask_single_poly = Polygon(mask_single)
                    if not mask_single_poly.is_valid:
                        mask_single_poly = mask_single_poly.buffer(0)
                        if isinstance(mask_single_poly, MultiPolygon):
                            mask_single_poly = list(mask_single_poly)[0]
                    if mask_single_poly.area > max_area:
                        tooth_mask_linear_rings = [
                            LinearRing([(pt[0], pt[1]) for pt in mask_single])]
                        max_area = mask_single_poly.area
                    tooth_mask_polys.append(mask_single_poly)

            tooth_mask_multipoly = MultiPolygon(tooth_mask_polys)
            tooth_mask_lines = MultiLineString(tooth_mask_linear_rings)
            # Get rectangle around tooth (if tooth is in pieces get the rectangle enclosing both)
            tooth_box = tooth_mask_multipoly.minimum_rotated_rectangle
            # Calculate centroid of tooth mask. The value is not used in this function.
            if tooth_mask_multipoly.centroid.coords and list(
                    tooth_mask_multipoly.centroid.coords[0]):
                tooth_centroid = {'x': tooth_mask_multipoly.centroid.coords[0][0],
                                  'y': tooth_mask_multipoly.centroid.coords[0][1]}
            # Heuristic to determine if patchy teeth are outliers and should be rejected
            if tooth_box:
                enclosing_coords = list(tooth_box.exterior.coords)
                W_H = [max(abs(enclosing_coords[0][0] - enclosing_coords[1][0]),
                           abs(enclosing_coords[0][1] - enclosing_coords[1][1])),
                       max(abs(enclosing_coords[1][0] - enclosing_coords[2][0]),
                           abs(enclosing_coords[1][1] - enclosing_coords[2][1]))]
                W = min(W_H)
                H = max(W_H)
            else:
                W = tooth_mask.shape[1]  # double check that image width is shape[1]
                H = tooth_mask.shape[0]

            # Find intersection points between bone and tooth boundary
            candidate_bone_pts, *_ = self.find_intersection_pts(
                bone_enamel_boundaries['bone'],
                tooth_mask_lines)

            if debug_print:
                print(f'DEBUG pixel_buffer:{self.pixel_buffer}')
                print(f'DEBUG pre filter candidate_bone_pts: {candidate_bone_pts}')
                print(f'DEBUG bone_lines:{bone_enamel_boundaries["bone"]}')
                print(f'DEBUG tooth_poly:{[tooth_poly]}')
                # print(f'DEBUG tooth_mask_points:{tooth_mask_points}')
            candidate_bone_pts = list(filter(self.is_interior, candidate_bone_pts))
            if debug_print:
                print(f'DEBUG post filter candidate_bone_pts: {candidate_bone_pts}')
            import itertools
            if len(candidate_bone_pts) == 1:
                candidate_bone_pts += candidate_bone_pts
            # get all possible combinations of points
            combos = list(itertools.combinations(candidate_bone_pts, 2))
            # compute square distance of all possible combos
            dist_fn = lambda pt: (pt[0][0] - pt[1][0]) ** 2 + (pt[0][1] - pt[1][1]) ** 2
            dist_values = list(map(dist_fn, combos))
            if dist_values:
                val = combos[np.argmax(dist_values)]
                boundary_bone_enamel_pts['bone'] = sorted(
                    [{'x': val[0][1], 'y': val[0][0]},
                     {'x': val[1][1], 'y': val[1][0]}], key=lambda v: v['x'])
            else:
                top_border_box = [
                    {'x': self.pixel_buffer_horizontal,
                     'y': self.pixel_buffer_vertical},
                    {'x': bone_enamel_boundaries['bone_mask'].shape[
                              1] - self.pixel_buffer_horizontal,
                     'y': self.pixel_buffer_vertical},
                    {'x': bone_enamel_boundaries['bone_mask'].shape[
                              1] - self.pixel_buffer_horizontal,
                     'y': int(self.pixel_buffer_vertical / 2)},
                    {'x': self.pixel_buffer, 'y': int(self.pixel_buffer / 2)}
                ]
                bottom_border_box = [
                    {'x': self.pixel_buffer_horizontal,
                     'y': bone_enamel_boundaries['bone_mask'].shape[
                              0] - self.pixel_buffer_vertical},
                    {'x': bone_enamel_boundaries['bone_mask'].shape[
                              1] - self.pixel_buffer_horizontal,
                     'y': bone_enamel_boundaries['bone_mask'].shape[
                              0] - self.pixel_buffer_vertical},
                    {'x': bone_enamel_boundaries['bone_mask'].shape[
                              1] - self.pixel_buffer_horizontal,
                     'y': bone_enamel_boundaries['bone_mask'].shape[0] - int(
                         self.pixel_buffer_vertical / 2)},
                    {'x': self.pixel_buffer_horizontal,
                     'y': bone_enamel_boundaries['bone_mask'].shape[0] - int(
                         self.pixel_buffer_vertical / 2)}
                ]
                border_box = [top_border_box, bottom_border_box]
                candidate_border_pts, *_ = self.find_intersection_pts(border_box,
                                                                      tooth_mask_lines)
                if debug_print:
                    print(f'DEBUG candidate_border_pts: {candidate_border_pts}')
                if len(candidate_border_pts) == 1:
                    candidate_border_pts += candidate_border_pts
                # get all possible combinations of points
                combos = list(itertools.combinations(candidate_border_pts, 2))
                dist_values = list(map(dist_fn, combos))
                if dist_values:
                    val = combos[np.argmax(dist_values)]
                    boundary_bone_enamel_pts['bone'] = sorted(
                        [{'x': val[0][1], 'y': val[0][0]},
                         {'x': val[1][1], 'y': val[1][0]}], key=lambda v: v['x'])

        return boundary_bone_enamel_pts, tooth_centroid

    def get_two_closest_pts(self, candidate_pts, ref_pts, debug_print=False):
        assert (len(ref_pts) == 2)
        two_closest_pts = []

        # Go through all the points and find the two closest points
        if candidate_pts:
            # Go through all the points and find the two closest points
            if len(candidate_pts) == 1:
                if ref_pts[0]:
                    dist0 = np.sqrt((candidate_pts[0]['x'] - ref_pts[0]['x']) ** 2 + (
                                candidate_pts[0]['y'] - ref_pts[0]['y']) ** 2)
                else:
                    dist0 = CejCalculations.LARGE_DISTANCE
                if ref_pts[1]:
                    dist1 = np.sqrt((candidate_pts[0]['x'] - ref_pts[1]['x']) ** 2 + (
                                candidate_pts[0]['y'] - ref_pts[1]['y']) ** 2)
                else:
                    dist1 = CejCalculations.LARGE_DISTANCE
                if dist0 < dist1:
                    two_closest_pts = [candidate_pts[0], None]
                else:
                    two_closest_pts = [None, candidate_pts[0]]
                return two_closest_pts

            ref_pts_list = list(dict.fromkeys([(v['x'], v['y']) for v in ref_pts]))
            for ref_pt in ref_pts_list:
                def dist_fn(pt1):
                    if pt1 and ref_pt:
                        return np.sqrt(
                            (pt1['x'] - ref_pt[0]) ** 2 + (pt1['y'] - ref_pt[1]) ** 2)
                    else:
                        return CejCalculations.LARGE_DISTANCE

                pts_sorted = sorted(candidate_pts, key=dist_fn)

                candidate_pts.remove(pts_sorted[0])
                two_closest_pts.append(pts_sorted[0])

                # Remove the next points also if they are very close
                for ix in range(1, len(pts_sorted)):
                    if pts_sorted[ix]:
                        delta_x = pts_sorted[0]['x'] - pts_sorted[ix]['x']
                        delta_y = pts_sorted[0]['y'] - pts_sorted[ix]['y']
                        dist_compare = np.sqrt(delta_x ** 2 + delta_y ** 2)
                        dist_ref = dist_fn(pts_sorted[ix])

                        # Greater than 75deg or small distance
                        if dist_compare < 0.4 * dist_ref or (
                                abs(delta_y) > 3.732 * abs(delta_x)):
                            candidate_pts.remove(pts_sorted[ix])
                        else:
                            # Check for near collinear pts
                            g1 = LineString(
                                [ref_pt, (pts_sorted[ix]['x'], pts_sorted[ix]['y'])])
                            p = Point((pts_sorted[0]['x'], pts_sorted[0]['y']))
                            p1, p2 = nearest_points(p, g1)  # find the nearest point on the second line
                            if p1.distance(p2) <= self.collinear_threshold:
                                candidate_pts.remove(pts_sorted[ix])
                            else:
                                break
                    else:
                        break
                if not candidate_pts:
                    break

        assert (len(two_closest_pts) < 3)
        # make two closest points
        for _ in range(len(two_closest_pts), len(ref_pts)):
            two_closest_pts.append(None)

        return two_closest_pts

    @staticmethod
    def snap_lines(g1, g2, threshold):
        from shapely.ops import nearest_points

        coordinates = []
        for x, y in g1.coords:  # for each vertex in the first line
            point = Point(x, y)
            p1, p2 = nearest_points(point,
                                    g2)  # find the nearest point on the second line
            if p1.distance(p2) <= threshold:
                # it's within the snapping tolerance, use the snapped vertex
                coordinates.append((x, y))
                coordinates.append((p2.coords[0][0], p2.coords[0][1]))
            else:
                # it's too far, use the original vertex
                coordinates.append((x, y))
        # convert coordinates back to a LineString and return
        return LineString(coordinates)

    def find_intersection_pts(self, segs, mask_lines, snap=False, swap_xy=True):
        """
        Find intersection points between segments and mask boundaries.
        This class should NOT be used directly.
        """
        from shapely.geometry import MultiLineString, LineString, Point, LinearRing
        if not isinstance(mask_lines, MultiLineString) and not isinstance(mask_lines,
                                                                          LineString):
            polys_mask = []
            for boundary_segment in mask_lines:
                line_element = [(value['x'], value['y']) for value in boundary_segment]
                if len(line_element) > 1:
                    polys_mask.append(LineString(line_element))

            if len(mask_lines) == 1:
                mask_lines = Polygon(
                    [(value['x'], value['y']) for value in mask_lines[0]])
                if not mask_lines.is_valid:
                    mask_lines = mask_lines.buffer(0)
                if isinstance(mask_lines, Polygon):
                    if mask_lines and mask_lines.exterior:
                        mask_lines = LinearRing(mask_lines.exterior.coords)
                    else:
                        mask_lines = MultiLineString([])
                elif isinstance(mask_lines, MultiPolygon):
                    mask_lines = list(mask_lines)
                    mask_lines = MultiLineString(
                        [LinearRing(mask_line.exterior.coords) for mask_line in
                         mask_lines if
                         mask_line and mask_line.exterior])

            else:
                mask_lines = MultiLineString(polys_mask)
        else:
            polys_mask = []
        polys_bone = []
        for boundary_segment in segs:
            line_element = [(value['x'], value['y']) for value in boundary_segment]
            if len(line_element) > 1:
                bone_line = LinearRing(line_element)
                if snap and polys_mask:
                    for mask_line in polys_mask:
                        bone_line = CejCalculations.snap_lines(bone_line, mask_line,
                                                               self.snapping_threshold)
                polys_bone.append(bone_line)
        bone_lines = MultiLineString(polys_bone)

        try:
            intersection = bone_lines.intersection(mask_lines)
        except Exception as e:
            print(e)
            print('intersection error')
            print(f'bone_lines: {bone_lines}')
            print(f'mask_lines: {mask_lines}')
            intersection = []

        candidate_boundary_pts = []
        if intersection:
            if not isinstance(intersection, Point) and not isinstance(intersection,
                                                                      LineString):
                for obj in intersection.geoms:
                    if swap_xy:
                        candidate_boundary_pts += [(int(val[1]), int(val[0])) for val in
                                                   obj.coords]
                    else:
                        candidate_boundary_pts += [(int(val[0]), int(val[1])) for val in
                                                   obj.coords]
            else:
                if swap_xy:
                    candidate_boundary_pts += [(int(val[1]), int(val[0])) for val in
                                               intersection.coords]
                else:
                    candidate_boundary_pts += [(int(val[0]), int(val[1])) for val in
                                               intersection.coords]
        return candidate_boundary_pts, intersection, bone_lines, mask_lines

    @staticmethod
    def compute_snapping_value(img_size):
        return max(1, int(0.005 * np.sqrt(img_size)))

    @staticmethod
    def get_segmentations(mask, return_as_shapely_poly=False):
        """
        Get segmentations of a mask removing tiny areas
        """
        boundary = []
        area_remove_threshold = int(mask.size * CejCalculations.AREA_REMOVAL_PERC / 100)
        polygons = imantics.Polygons.from_mask(mask).points
        for polygon in polygons:
            if len(polygon) > 2:
                shapely_poly = Polygon(polygon)
                if shapely_poly.area > area_remove_threshold:
                    if return_as_shapely_poly:
                        boundary.append(shapely_poly)
                    else:
                        boundary.append(
                            [{'x': int(coord[0]), 'y': int(coord[1])} for coord in
                             shapely_poly.exterior.coords])
        return boundary

    @staticmethod
    def smooth_mask(mask: np.ndarray, print_flag=False) -> np.ndarray:
        """
        Smooth prediction mask boundaries by blurring and then thresholding back to a binary image
        :param mask: binary or boolean numpy array (e.g. Tooth l#4 channel)
        :return: boolean numpy array
        """
        import cv2
        vesselImage = mask.astype(float)
        blurredImage = cv2.blur(mask.astype(float), (1, 1))
        pyrUp = cv2.pyrUp(vesselImage, blurredImage)
        median_blur = cv2.medianBlur(pyrUp, 1)
        pyrDown = cv2.pyrDown(median_blur, median_blur)
        new_image = cv2.threshold(pyrDown, .9, 1, cv2.THRESH_BINARY)[1]
        mask = new_image.astype(bool)
        if print_flag:
            print(
                f'Image smoothed, area reduced from {int(np.sum(vesselImage))} to {int(np.sum(new_image))} pixels')
            import pickle
            pickle.dump(mask, open('debugPoly.p', 'wb'))

        return mask

    @staticmethod
    def get_valid(geom):
        if not geom.is_valid or not geom.buffer(0):
            tol = 0.01
            for i in range(0, 60):
                if geom.simplify(tol).is_valid:
                    geom = geom.simplify(tol)
                    break
                else:
                    tol *= 1.1
        elif not geom.is_valid:
            geom = geom.buffer(0)

        if geom.is_valid:
            return geom
        return False

    @staticmethod
    def get_tooth_boundaries(mask):
        area_remove_threshold = int(mask.shape[0] * mask.shape[1] * 0.01 / 100)
        mask = CejCalculations.smooth_mask(mask)
        boundary = []
        multipoly = []
        from shapely.ops import unary_union
        polygons = imantics.Polygons.from_mask(mask).points
        for polygon in polygons:
            if len(polygon) > 2:
                shapely_poly = Polygon(polygon)
                if shapely_poly.area > area_remove_threshold:
                    if CejCalculations.get_valid(shapely_poly):
                        multipoly.append(CejCalculations.get_valid(shapely_poly))

        poly_union = unary_union(multipoly)

        if isinstance(poly_union, Polygon) and not poly_union.is_empty:
            boundary = [[{'x': int(coord[0]), 'y': int(coord[1])} for coord in
                         poly_union.exterior.coords]]

        elif not poly_union.is_empty:
            for poly in poly_union:
                boundary.append([{'x': int(coord[0]), 'y': int(coord[1])} for coord in
                                 poly.exterior.coords])

        return boundary

    @staticmethod
    def create_polygon(geometry):
        """
        create shapely poly
        """
        p = []
        for xy in geometry:
            p.append((xy['x'], xy['y']))
        return Polygon(p)

    @staticmethod
    def get_geometry_area(geometry):
        """
        return geometry area
        """
        if len(geometry) == 0:
            return 0
        else:
            return CejCalculations.create_polygon(geometry).area

    @staticmethod
    def cleanup_geometry(geometry, return_as_shapely_object=False):
        """
        Remove points that don't result in closed polygons
        """
        if len(geometry) < 3:
            return []
        ref_poly = CejCalculations.create_polygon(geometry)
        # Remove line segments and points making this an invalid Polygon
        if not ref_poly.is_valid:
            ref_poly = ref_poly.buffer(0)
        if return_as_shapely_object:
            return ref_poly
        else:
            new_poly = []
            if isinstance(ref_poly, Polygon) and not ref_poly.is_empty:
                new_poly = [
                    {'x': int(coord[0]), 'y': int(coord[1])}
                    for coord in ref_poly.exterior.coords
                ]
            return new_poly
