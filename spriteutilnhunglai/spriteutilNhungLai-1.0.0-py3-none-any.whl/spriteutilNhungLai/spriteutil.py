import timeit
import random
from PIL import Image, ImageDraw
from pathlib import Path
import numpy as np
import sys


class Sprite:
    """WP2: This class represents an sprite object.

    Raises an exception ValueError if one or more arguments label, x1, y1,
        x2, and y2 is not positive integer, or if the arguments x2 and y2
        is not equal or greater respectively than x1 and y1.
    """
    def __init__(self, label, x1, y1, x2, y2):
        if type(label) != int or type(x1) != int or type(y1) != int \
            or type(x2) != int or type(y2) != int or label < 0 or x1 < 0 \
            or x2 < 0 or y1 < 0 or y2 < 0 or x2 < x1 or y2 < y1:
            raise ValueError('Invalid coordinates')
        else:
            self._label = label
            self._top_left = (x1, y1)
            self._bottom_right = (x2, y2)
            self.width = x2 - x1 + 1
            self.height = y2 - y1 + 1

    @property
    def label(self):
        return self._label

    @property
    def top_left(self):
        return self._top_left

    @property
    def bottom_right(self):
        return self._bottom_right


class SpriteSheet:
    def __init__(self, fd, background_color=(255, 255, 255)):
        self.fd = fd
        self._background_color = background_color
        # self.image = Image.open(self.fd)

    @property
    def background_color(self):
        return self._background_color

    def check_fd(self):
        image = Image.open(self.fd)
        return self.find_most_common_color(image)

    ##################################
    @staticmethod
    def __get_data_pixel(image):
        """This function finds the colors of the pixels in the image,
        and the number of pixels of that color.

        @param image: A Image object.

        @return: A dictionary with key is color of pixel in image,
            value is the number of pixels of that color.
        """
        img_size = image.size # (30, 38)
        # get each index of pixel in image
        pixel_img = image.load()
        # key is color of pixel, value is the number of pixels of that color
        dict_number_color = {}
        list_pixel_full = []

        for y in range(img_size[1]):
            for x in range(img_size[0]):
                list_pixel_full.append((x, y))
                # get each color of pixel in image
                pixel_color = pixel_img[x, y]

                if pixel_color in dict_number_color:
                    dict_number_color[pixel_color] += 1
                else:
                    dict_number_color[pixel_color] = 1

        return dict_number_color, list_pixel_full

    @staticmethod
    def find_most_common_color(image):
        """WP1: Find the Most Common Color in an Image.

        @param image: a Image object.

        @return: the pixel color that is the most used in this image.
            - An integer if the mode is grayscale (L);
            - A tuple (red, green, blue) of integers (0 to 255)
                if the mode is RGB;
            - A tuple (red, green, blue, alpha) of integers (0 to 255)
                if the mode is RGBA.
        """
        if image.getcolors() == None:
            dict_number_color = SpriteSheet.__get_data_pixel(image)[0]
            # get key have value biggest in dict dict_pixel
            return max(dict_number_color, key=lambda key: dict_number_color[key])
        return max(image.getcolors())[1]

    ###################################
    def find_sprites(self):
        """WP3: Find sprites in an image.

        Identify all the sprites packed in a single picture.

        @image: Image object.
        @background_color: The function ignores any pixels of the image
            with this color.

        @return sprites: key is label, value: Sprite object.
                label_map: A 2D array of integers of equal dimension
                (width and height) as the original image where the sprites
                are packed in.
        """
        image = Image.open(self.fd)

        list_mode = ["RGB", "RGBA", "L"]
        if image.mode not in list_mode:
            raise ValueError(
                ('The image mode "{}" is not supported').format(image.mode)
            )

        color_ignore = self.find_most_common_color(image)
        list_pixel_full = SpriteSheet.__get_data_pixel(image)[1]

        # pixels have color different color_ignore
        list_pixel_pass = SpriteSheet.__get_list_pixel_pass(image, color_ignore)

        # key : coordinates of pixel, value : label pixel
        dict_pixel_label = {}

        auto = 0
        for coordinates  in list_pixel_full:
            if coordinates in list_pixel_pass \
                and coordinates not in dict_pixel_label:

                auto += 1
                pixel_label = SpriteSheet.__check_neighbor_pixel(
                    coordinates[0], coordinates[1], dict_pixel_label,
                    list_pixel_pass,
                )
                if not pixel_label:
                    dict_pixel_label[coordinates] = auto
                else:
                    dict_pixel_label[coordinates] = pixel_label

        # dictionary of label: key is label, value: coordinates of sprite
        dict_label, list_label = SpriteSheet.__get_number_label(dict_pixel_label)

        SpriteSheet.__check_2_times(dict_pixel_label, dict_label, list_label, list_pixel_pass)

        new_dict_label, new_list_label = SpriteSheet.__get_number_label(dict_pixel_label)

        sprites = SpriteSheet.__get_sprites(list_label, new_dict_label, list_pixel_full)
        label_map = SpriteSheet.__get_label_map(
            image, sprites, new_dict_label, color_ignore, list_pixel_pass
        )
        return sprites, label_map

    @staticmethod
    def __get_list_pixel_pass(image, color):
        """tra ve nhung toa do co mau khac vs color
        """
        list_pixel = []
        img_size = image.size # (30, 38)
        pixel_img = image.load()
        for y in range(img_size[1]):
            for x in range(img_size[0]):
                # get each color of pixel in image
                pixel_color = pixel_img[x, y]
                if pixel_color != color:
                    list_pixel.append((x, y))

        return list_pixel

    @staticmethod
    def __get_sprites(list_label, new_dict_label, list_pixel_full):
        """A collection of key-value pairs (a dictionary)
        where each key-value pair maps the key (the label of a sprite)
        to its associated value (a Sprite object).
        """
        sprites = {}
        for label, pixel in new_dict_label.items():
            x1, x2 = min(pixel)[0], max(pixel)[0]
            y1, y2 = pixel[0][1], pixel[-1][1]

            sprite = Sprite(label, x1, y1, x2, y2)
            sprites[label] = sprite

        return sprites

    @staticmethod
    def __get_label_map(image, sprites, new_dict_label, color_ignore, list_pixel_pass):
        """Create label_map by numpy.

        @image: Image object.
        @sprites: key is label, value: Sprite object.
        @new_dict_label: key is label, value: coordinates of sprite.

        @return : list of a 2D array of integers of equal dimension.
        """
        # toa do trong array , truy xuất bằng numpy là [y, x] , array[37, 29] = 1
        width, height = image.size
        np.set_printoptions(threshold=sys.maxsize)
        label_map = np.full([height, width], 0, dtype = int)

        for label, sprite in sprites.items():
            for pixel in new_dict_label[label]:
                if pixel in list_pixel_pass:
                    x, y = pixel
                    label_map[(y, x)] = label
        return label_map.tolist() # change matrix to list

    @staticmethod
    def __check_neighbor_pixel(x, y, dict_pixel_label, list_pixel_pass):
        """Check directions of current pixel.

        if color of direction different background color and have label
        label of (x, y) = min(directions)

        @return: label of current pixel (int)
        """
        list_direction = [
            (x -1, y + 1), (x, y + 1), (x + 1, y + 1), (x - 1, y),
            (x + 1, y), (x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
        ]
        pixel_label = []
        # key label, value toa do
        dict_check = {}

        for direction in list_direction:
            if direction in list_pixel_pass and direction in dict_pixel_label:
                pixel_label.append(dict_pixel_label[direction])
                if dict_pixel_label[direction] not in dict_check:
                    dict_check[dict_pixel_label[direction]] = [direction]
                else:
                    if direction not in dict_check[dict_pixel_label[direction]]:

                        dict_check[dict_pixel_label[direction]].append(direction)

        if len(dict_check) > 1:
            SpriteSheet.__change_label(pixel_label, dict_check, dict_pixel_label)

        if len(pixel_label) > 0:
            return min(pixel_label)

        return pixel_label

    @staticmethod
    def __change_label(pixel_label, dict_check, dict_pixel_label):
        """Reduce the label obtained if the neighbor has another label.

        Change label of pixel if the neighbor has another label.
        """
        for key, value in dict_check.items():
            if key != min(pixel_label):
                for pixel in value:
                    dict_pixel_label[pixel] = min(pixel_label)

    @staticmethod
    def __get_number_label(dict_pixel_label):
        """Get sum of label in image

        @return dict_label:  with key is label, value: coordinates of sprite
        @return list_label: sum of label in image
        """
        dict_label = {}
        list_label = []
        for key, value in dict_pixel_label.items():
            if value not in list_label:
                list_label.append(value)
            if value not in dict_label:
                dict_label[value] = [key]
            else:
                if key not in dict_label[value]:
                    dict_label[value].append(key)
        return dict_label, list_label

    @staticmethod
    def __check_2_times(dict_pixel_label, dict_label, list_label, list_pixel_pass):
        """Check dict_pixel_label (key: coordinates of pixel, value: label pixel)
        """
        for key, value in dict_label.items():
            if key != min(list_label):
                for pixel in value:
                    pixel_label = SpriteSheet.__check_neighbor_pixel(
                        pixel[0], pixel[1], dict_pixel_label, list_pixel_pass
                    )
                    dict_pixel_label[pixel] = pixel_label
    #################################################################

    def create_sprite_labels_image(self):
        """
        @return: an image of equal dimension (width and height) as
            the original image that was passed to the function find_sprites.
        """
        if type(self.background_color) == int:
            mode = "L"

        elif len(self.background_color) == 3:
            mode = "RGB"
        elif len(self.background_color) == 4:
            mode = "RGBA"

        sprites, label_map = self.find_sprites()

        label_map = np.array(label_map) # change list to matrix
        height, width = label_map.shape
        # create new image
        new_image = Image.new(mode, (width, height), self.background_color)
        draw = ImageDraw.Draw(new_image) # create Draw object

        for label, sprite in sprites.items():
            # create random color for each label
            color = tuple(np.random.choice(range(256), size=3))

            x1, y1 = sprite.top_left
            x2, y2 = sprite.bottom_right

            draw.line(
                [(x1, y1), (x1, y2), (x2, y2), (x2, y1), (x1, y1)],
                fill=color,
            )
            # find coordinates of value = label in matrix label_map
            list_color = np.argwhere(label_map==label).tolist()

            for pixel in list_color:
                y, x = pixel
                new_image.load()[(x, y)] = color
        new_image.show()


def main():

    # ----------------------- Waypoint 1 -------------------------
    # # JPEG image - RBG
    # image = Image.open('image/2d_video_game_cannon_fodder.jpg')

    # # PNG image - RBGA
    # # image = Image.open('image/metal_slug_sprite_standing_stance_large.png')
    # # image = Image.open('image/islands.png')

    # # Grayscale image
    # # image = image.convert('L')

    # print("Mode:", image.mode)
    # print("Most common color:", find_most_common_color(image))
    # print("--------------------------------------------------------------")
    ##############################################################

    # -------------------------- Waypoint 2 -----------------------
    # sprite = Sprite(1, 12, 23, 145, 208)
    # # sprite = Sprite(1, -1, 0, 0, 0)
    # # sprite = Sprite(1, 0, 0, "Hello", 0)
    # # sprite = Sprite(1, 1, 0, 0, 0)
    # print(sprite.label)
    # print(sprite.top_left)
    # print(sprite.bottom_right)
    # print(sprite.width)
    # print(sprite.height)
    ################################################################

    # -------------------------- Waypoint 3 -------------------------
    # image = Image.open('image/optimized_sprite_sheet.png') # 22 sprite
    # image = Image.open('image/sprite_sheet_ken_02.png') # 40 sprite

    # sprites, label_map = find_sprites(image)

    # image = Image.open('image/metal_slug_sprite_large.png') # nhieu manh nho
    # image = Image.open('image/islands_sprites.png') # 2 sprite lồng nhau

    # image = Image.open('image/metal_slug_sprite_standing_stance.png') # 3 sprite
    # image = Image.open('image/ken_sprite_sheet_with_transparent_background.png') # 4 sprite


    # image = Image.open('image/sprite_sheet_ken_01.png') # 7 sprite have background
    # image = Image.open('image/metal_slug_sprites_running_with_gun.png') # 9 sprite

    # image = Image.open('image/metal_slug_single_sprite.png')
    # image = Image.open(Path('image/metal_slug_single_sprite.png'))
    # sprites, label_map = find_sprites(image, background_color=(255, 255, 255))

    # left,upper,right,lower = image.getbbox()
    # print("----------------------------------------------------------")

    # print("Mode:", image.mode)
    # print(image.size, "----- :size")
    # print(len(image.getcolors()))
    # print(image.getdata())


    # print("Most common color:", find_most_common_color(image))

    # print(image.getbbox())
    # print(image.split())
    # image.split()[-1].show()


    # print("----------------------------------------------------------")
    # print(len(sprites))
    # for label, sprite in sprites.items():
    #     print(f"Sprite ({label}): [{sprite.top_left}, {sprite.bottom_right}] {sprite.width}x{sprite.height}")

    # print(label_map)
    # pprint.pprint(label_map, width=120)

    # file_name = (image.filename).split('/')[1].split('.')[0]
    # np.savetxt('test/' + file_name + '.txt', label_map, fmt='%d')
    ###################################################################

    # -----------------------------Waypoint 4 --------------------------
    # sprite_label_image = create_sprite_labels_image(sprites, label_map)
    # sprite_label_image = create_sprite_labels_image(sprites, label_map, background_color=(0, 0, 0, 0))
    # sprite_label_image.save('hello.png')
    # image.show()
    ###################################################################

    # -----------------------------Waypoint 5 --------------------------
    # image = Image.open('image/Barbarian.gif').convert('RGB')
    # sprite_sheet = SpriteSheet(image)

    # sprite_sheet = SpriteSheet('image/Barbarian.gif')

    sprite_sheet = SpriteSheet('image/metal_slug_single_sprite.png') # 1 sprite
    # sprite_sheet = SpriteSheet('image/metal_slug_sprite_standing_stance.png') # 3 sprite

    # image = Image.open(sprite_sheet.fd)
    # print(image)

    # print(sprite_sheet.check_fd())
    sprites, labels = sprite_sheet.find_sprites()
    print(len(sprites))
    for label, sprite in sprites.items():
        print(f"Sprite ({label}): [{sprite.top_left}, {sprite.bottom_right}] {sprite.width}x{sprite.height}")

    # Create the mask image with bounding boxes.
    image = sprite_sheet.create_sprite_labels_image()

    # image.save('barbarian_bounding_boxes.png')
    # image.save('metal_slug_single_sprite.png')
    ####################################################################

    # -----------------------TIME ------------------------
    # Measure the execution time
    # print(
    #     "Measure the execution time:",
    #     timeit.timeit(stmt=lambda: find_sprites(image, background_color=(255, 255, 255)), number=1)
    # )


if __name__ == '__main__':
    main()
