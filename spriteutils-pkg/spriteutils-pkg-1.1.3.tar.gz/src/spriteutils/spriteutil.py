#!/usr/bin/env python 3.7
"""Utilities for finding sprite from spritesheet"""

import random
import numpy as np
from PIL import Image
from PIL import ImageDraw


# Index of return data of method Image.getcolors()
# tuple(frequency, pixel)
FREQUENCY_IDX = 0
PIXEL_IDX = 1

# Color mode
COLOR_MODES_WITH_INTEGER_ELEMENT = ["L", "P", "1"]

# 4 adjacent neighbor (8 connectivity method)
ADJACENT_OFFSETS = [(-1, -1), (-1, 0), (-1, 1), (0, -1)]

# Polar point coordinate index
LEFTMOST_IDX = 0
TOPMOST_IDX = 1
RIGHTMOST_IDX = 2
BOTTOMOST_IDX = 3

# Alpha channel threshold
MIN_ALPHA = 200
MAX_ALPHA = 255

# Datatype
INTEGER = int
TUPLE = tuple


class Sprite:
    """Represent a sprite"""

    def __init__(self, label, x1, y1, x2, y2, total_pixels_count):
        """
        Construtor of the class

        Arguments:
            label (int) -- A whole number represents the label of the
                sprites

            x1, y1, x2, y2 (int) -- Leftmost, Topmost, Rightmost, Bottomost
                coordinates of the sprite in the spritesheet

        Raise:
            TypeError -- If any of the arguments is not an integer
            ValueError:
                If any of the arguments is not a whole number
                    (positive integer including zero)
                If  x2 < x1 or y2 < y1
        """
        # Validate arguments
        args = [label, x1, y1, x2, y2]
        for arg in args:
            if not isinstance(arg, int):
                raise TypeError(f"All arguments MUST be an integer")
            if arg < 0:
                raise ValueError(f"All arguments MUST be a whole number")

        if x2 < x1 or y2 < y1:
            raise ValueError("Invalid coordinates")

        self.__label = label
        self.__top_left_corner = (x1, y1)
        self.__bottom_right_corner = (x2, y2)
        self.__num_of_horizontally_pixels = x2 - x1 + 1
        self.__num_of_vertically_pixels = y2 - y1 + 1
        self.__surface = self.__num_of_horizontally_pixels * self.__num_of_vertically_pixels
        self.__density = total_pixels_count / self.__surface
        self.__centroid = ((x1 + x2) // 2, (y1 + y2) // 2)


    @property
    def label(self):
        """int: Represent label of the sprite"""
        return self.__label

    @property
    def top_left(self):
        """obj:`tuple`: Represent the coordinate of the top-left corner"""
        return self.__top_left_corner

    @property
    def bottom_right(self):
        """obj:`tuple`: Represent the coordinate of the bottom-right corner"""
        return self.__bottom_right_corner

    @property
    def width(self):
        """int: Represent the number of pixels horizontally of this sprite"""
        return self.__num_of_horizontally_pixels

    @property
    def height(self):
        """int: Represent the number of pixels horizontally of this sprite"""
        return self.__num_of_vertically_pixels

    @property
    def surface(self):
        """int: Represent the surface area of the sprite's bounding box"""
        return self.__surface

    @property
    def density(self):
        """int: Represent the number of non-background-pixels of this sprite"""
        return self.__density

    @property
    def centroid(self):
        """tuple: Represent the centroid coordinates of the sprite's bounding box"""
        return self.__centroid


class LabelMap:
    """Represent the label map of an image"""

    def __init__(self, height, width):
        """Construct a new zeros label map"""
        if not isinstance(height, int) or not isinstance(width, int):
            raise TypeError("Label map `height` and `width` MUST be integer")

        self.__height = height
        self.__width = width
        self.__lastest_label = 0
        self.__label_map = np.zeros((height, width), dtype=np.int)
        self.__existing_labels = TableOfEquivalenceLabel()
        self.__label_polar_points = dict()

    def __update_polar_points(self, label, row, col):
        """
        Update the polar points of the provided `label` based on the
        new coordinate (`row`, `col`) of the label in the label map

        Arguments:
            label (int) -- A label in the label map
            row (int) -- The vertical coordinate of the `label`
            col (int) -- The horizontal coordinate of the `label`
        """
        label_polar_point = self.__label_polar_points.get(label)
        if label_polar_point is None:
            # Add new label at current point to the dictionary
            self.__label_polar_points.update({label: [col, row, col, row]})
        else:
            # Update the newest polar points

            if col > label_polar_point[RIGHTMOST_IDX]:
                label_polar_point[RIGHTMOST_IDX] = col
            elif col < label_polar_point[LEFTMOST_IDX]:
                label_polar_point[LEFTMOST_IDX] = col

            if row > label_polar_point[BOTTOMOST_IDX]:
                label_polar_point[BOTTOMOST_IDX] = row
            elif row < label_polar_point[TOPMOST_IDX]:
                label_polar_point[TOPMOST_IDX] = row

    @property
    def label_polar_points(self):
        """dict: Represent all labels in the map and their polar points"""
        return self.__label_polar_points

    @property
    def map(self):
        """list: Represent the label maps"""
        return self.__label_map.tolist()

    def check_neighbor(self, row, col):
        """
        Check the neighbor of a specified position (`row`, `col`) in the
        label map. Assigned the neighbor label to the specified position
        if the is a non-background label. Get the new label otherwise

        Arguments:
            row (int) -- The vertical coordinate
            col (int) -- The horizontal coordinate
        """
        assigned_label = None
        # Check adjacent neighbor using 8-connectivity
        for row_offset, col_offset in ADJACENT_OFFSETS:
            neighbor_row = row + row_offset
            neighbor_col = col + col_offset
            try:
                assert neighbor_row >= 0 and neighbor_col >= 0
                nearby_label = \
                    self.__label_map[neighbor_row][neighbor_col]
            except (IndexError, AssertionError):
                continue

            # Skip the background label
            if nearby_label == 0:
                continue

            # Assigned the nearest neighbor to the current possition
            if assigned_label is None:
                assigned_label = nearby_label

            # Set equivalence relationship if there are other different
            # adjacent label
            elif nearby_label != assigned_label:
                self.__existing_labels.set_eq_label(
                    nearby_label, assigned_label)

        # Get new label if there aren't any adjacent label
        if assigned_label is None:
            self.__lastest_label += 1
            assigned_label = self.__lastest_label
            self.__existing_labels.add_new_label(assigned_label)

        self.__label_map[row][col] = assigned_label

    def reduce_label(self):
        """
        Relabel the labels according to their smallest equivalence label

        Count the total pixels of each label after reduce the label

        Return:
            total_pixels (dict) -- The dictionary where key is the label
                and the value is the total pixels of the label in the
                label map
        """
        total_pixels = {}
        for row in range(self.__height):
            for col in range(self.__width):
                current_label = self.__label_map[row][col]
                # Reduce equivalence label
                if current_label:
                    # Get the smallest equivalence label
                    current_label = \
                        self.__existing_labels.get_eq_label(current_label)
                    # Relabel the labels with their equivalence label
                    self.__label_map[row][col] = current_label
                    # Count the occurence of a label inside map
                    total_pixels[current_label] = \
                        total_pixels.get(current_label, 0) + 1

                    # find min, max coordinate of each label
                    self.__update_polar_points(int(current_label), row, col)
        return total_pixels


class TableOfEquivalenceLabel:
    """Represent the table of equivalence pixels of the spritesheet"""

    def __init__(self):
        self.__eq_map = dict()

    def add_new_label(self, label):
        """
        Add the new `label` to the `eq_map` dictionary

        Arguments:
            label (int) -- The new label which we want to add to the map
        """
        self.__eq_map.setdefault(label, label)

    def set_eq_label(self, first_label, second_label):
        """
        Set equivalence label of two adjacent label(`first_label`,
        `second_label`) base on the smaller equivalence label

        Arguments:
            first_label, second_label (int) -- Labels that are adjacent
                to each other
        """
        # Get equivalence label of each label
        first_eq_label = self.get_eq_label(first_label)
        seccond_eq_label = self.get_eq_label(second_label)

        # Set the equivalence labels of both labels to the smaller
        # equivalence label
        if first_eq_label > seccond_eq_label:
            self.__eq_map[first_eq_label] = seccond_eq_label
        elif seccond_eq_label > first_eq_label:
            self.__eq_map[seccond_eq_label] = first_eq_label

    def get_eq_label(self, label):
        """
        Recursively gets the smaller label in the equivalence sequence.
        Eventually get the smallest equivalence label in the equivalence
        sequence.

        Update each label in the equivalence sequence with the smallest
        equivalence label.

        Arguments:
            label (int) -- A label of the sprite

        Returns:
            eq_label (int) -- The smallest equivalence label of the
                provided label
        """
        possible_eq_label = self.__eq_map[label]

        # Return the smallest equivalence label in the equivalence
        # sequence
        if possible_eq_label == label:
            return label

        # Recursively get the smaller equivalence sequence
        eq_label = self.get_eq_label(possible_eq_label)

        # Update each label in the equivalence sequence with the
        # smallest equivalence label
        self.__eq_map[label] = eq_label
        return eq_label


class SpriteSheet:
    """Represent a spritesheet"""

    def __init__(self, fd, background_color=None):
        """Constructor of the class

        Arguments:
            fd -- A PIL.Image object, a filename (string), pathlib.Path
                object or a file object. The file object must implement
                read(), seek(), and tell() methods, and be opened in
                binary mode.

            background_color(optional) -- The pixel color represents the
                background color of the spritesheet.
                The type of the argument depends on the image's mode:

                An integer -- If the mode is grayscale

                A tuple (red, green, blue) of integers if the mode is RGB

                A tuple (red, green, blue, alpha) of integers if the
                    mode is RGBA. The alpha element is optional.If not
                    defined, while the image mode is RGBA, the
                    constructor considers the alpha element to be 255.

        Raise:
            FileNotFoundError -- If the file cannot be found.

            PIL.UnidentifiedImageError -- If the image cannot be opened
                and identified.

            ValueError -- If the mode is not “r”, or if a StringIO
                instance is used for fp.

            ValueError -- If the arugment `background_color` does not
                compatile with image mode
        """
        if not isinstance(fd, Image.Image):
            image = Image.open(fd)
        else:
            image = fd
        self.__image = image

        # If the argument `background_color` was not specified set the
        # most common color of the image as background color
        if background_color is None:
            background_color = self.find_most_common_color(image)
        else:
            self.__check_background_color(image.mode, background_color)

        self.__background_color = background_color
        self.__label_map = None
        self.__sprites = None
        self.__mask_colors = None
        self.__sprites_masks_image = None

    # Check if the provided `background_color` is compatible with the
    # image mode
    @staticmethod
    def __check_background_color(mode, background_color):
        image_mode = mode

        # Datatype of a pixel (integer or tuple) according to image mode
        if image_mode in COLOR_MODES_WITH_INTEGER_ELEMENT:
            pixel_datatype = INTEGER
        else:
            pixel_datatype = TUPLE

        # Check compatility of background_color and image.mode
        if pixel_datatype != type(background_color):
            raise ValueError(
                "arguments `background_color` does not compatile with image mode")

    # Generate unique mask color for each sprite base on the provided
    # `image_mode`
    def __generate_mask_color(self, image_mode):
        """
        Generate unique mask color for each label in provided `labels`
        (list of label) base on the provided `image_mode`

        Return:
            (dict) -- Each key-value pair maps the label of a sprite
                (int) to its associated unique pixel color (tuple)
        """
        labels = self.__sprites.keys()
        is_rgba = image_mode == "RGBA"
        num_of_labels = len(labels)
        colors = []
        num_of_colors = 0
        while num_of_colors < num_of_labels:
            # Generate a random color

            color = [
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)]

            if is_rgba:
                # The mask color alpha channel shouldn't be to low for
                # clear image
                color.append(random.randint(MIN_ALPHA, MAX_ALPHA))

            color = tuple(color)

            # Check if the color is already picked
            if color not in colors:
                colors.append(color)
                num_of_colors += 1

        self.__mask_colors = dict(zip(labels, colors))

    @property
    def background_color(self):
        """Represents background color of the spritesheet"""
        return self.__background_color

    @staticmethod
    def find_most_common_color(image):
        """
        Find the most used pixel color in the provided `image` (a Image
        object)

        Arguments:
            image (:obj:`PIL.Image.Image`) -- An Image

        Raise:
            TypeError: If the argument `image` is not an Image object

        Return:
            The most used pixel color in the provided image

            The data type of value return depend on the mode of the image
                An integer -- If the image.mode is 'L' or 'P'
                A tuple -- If the image.mode is 'RGB', 'RGBA', 'LA', or
                'PA'
        """
        if not isinstance(image, Image.Image):
            raise TypeError("arguments `image` MUST be an Image object")

        # Size of image in pixels
        image_size = image.width * image.height

        # Get the frequencies of all distinct pixels in the image in
        # form of tuple(frequency, pixel)
        pixel_frequencies = image.getcolors(maxcolors=image_size)

        # Sort the list by descending frequency
        pixel_frequencies = sorted(
            pixel_frequencies,
            key=lambda x: x[FREQUENCY_IDX], reverse=True)

        return pixel_frequencies[0][PIXEL_IDX]

    def find_sprites(self):
        """
        Determine the sprites of the the spritesheet

        Return: A tuple (sprites, label_map) where:
            sprites (dict): Each key-value pair maps the key (the label
                of a sprite) to its associated value (a Sprite object)

            label_map (list):
                A 2D array of integers of equal dimension (width and
                height) as the original image where the sprites are
                packed in.

                The array maps each pixel of the `image` to the label
                of the sprite this pixel corresponds to, or 0 if this
                pixel doesn't belong to a sprite (e.g., background
                color).
        """

        if self.__sprites is not None and self.__label_map is not None:
            return self.__sprites, self.__label_map

        # Size of the image
        height = self.__image.height
        width = self.__image.width

        # Get map of pixel color from the image
        pixel_map = self.__image.load()

        # Initial the label map object
        label_map = LabelMap(height, width)

        for row in range(height):
            for col in range(width):
                # Get current pixel
                current_pixel = pixel_map[col, row]

                # Skip the pixel it is the background pixel
                if current_pixel == self.background_color:
                    continue

                # Check neighbor and assign label accordingly
                label_map.check_neighbor(row, col)

        # Reduce equivalence labels into the smallest equivalence label
        total_pixels = label_map.reduce_label()
        # Create Sprite
        self.__sprites = dict()

        for label, polar_points in label_map.label_polar_points.items():
            total_pixels_count = total_pixels[label]
            self.__sprites[label] = Sprite(
                label,
                polar_points[LEFTMOST_IDX],
                polar_points[TOPMOST_IDX],
                polar_points[RIGHTMOST_IDX],
                polar_points[BOTTOMOST_IDX],
                total_pixels_count)

        self.__label_map = label_map.map
        return self.__sprites, self.__label_map

    def create_sprite_labels_image(self, background_color=(255, 255, 255)):
        """
        Draws the sprite masks for each sprite in the spritesheet

        If the instance method find_sprite() hasn't been called, the
        method initially called it to get the sprites of the spritesheet

        The function draws each sprite mask with a random uniform color
        (one color per sprite mask).

        The function also draws a rectangle (bounding box) around each
        sprite mask, of the same color used for drawing the sprite mask.

        Arguments:
            background_color (tuple, optional) -- The background color
                of the image to create (default: (255, 255, 255))

        Return:
            image (obj:`PIL.Image.Image`) -- The sprite masks image
        """
        if self.__sprites is None or self.__label_map is None:
            self.find_sprites()
        if self.__sprites_masks_image:
            return self.__sprites_masks_image

        # Initial data to create new image
        image_mode = "RGBA" if len(background_color) == 4 else "RGB"
        height = self.__image.height
        width = self.__image.width

        # Generate unique colors for each sprite in the spritesheet
        self.__generate_mask_color(image_mode)

        # Create new image
        image = Image.new(image_mode, (width, height), background_color)
        # Initail draw context
        draw_context = ImageDraw.Draw(image, image_mode)

        # Draw sprite masks
        for row in range(height):
            for col in range(width):
                label = self.__label_map[row][col]
                if label:
                    draw_context.point(
                        (col, row), self.__mask_colors[label])

        # Draw rectangle boundaries
        for label, sprite in self.__sprites.items():
            draw_context.rectangle(
                [sprite.top_left, sprite.bottom_right],
                outline=self.__mask_colors[label])

        # Delete the drawing context
        del draw_context

        self.__sprites_masks_image = image
        return image
