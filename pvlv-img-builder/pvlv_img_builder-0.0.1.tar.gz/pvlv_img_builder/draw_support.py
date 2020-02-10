from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from pvlv_img_builder.utils.positions import Position
from pvlv_img_builder.configurations.configuration import (
    DEBUG,
    BACKGROUND_COLOR,
    DIR_DEFAULT_FONT,
)

SPAN_BORDER = 0.3
SPAN_TITLE = 1.8
SPAN_TEXT = 1


class DrawSupport(object):

    X_BORDER_OFFSET = 25

    def __init__(self, data):

        self.data = data

        self.resolution = 30

        self.width = 350
        self.height = 0

        self.x_cursor = 0
        self.y_cursor = SPAN_BORDER*self.resolution

        self.background_color = self.data.get('background_color', BACKGROUND_COLOR)
        self.image: Image
        self.draw: ImageDraw

        # set the absolute path dir for the font.
        self.font_dir = self.data.get('font', DIR_DEFAULT_FONT)
        # Standard fonts Global for all the canvas
        self.font_title = ImageFont.truetype(self.font_dir, int(self.resolution * SPAN_TEXT / 1.3))
        self.font_text = ImageFont.truetype(self.font_dir, int(self.resolution * SPAN_TEXT / 1.8))

    def build_canvas(self):
        # img = Image.open("img.png")
        self.image = Image.new("RGB", (self.width, self.height), self.background_color)
        # self.image.paste(img)
        self.draw = ImageDraw.Draw(self.image)

    def get_section(self, section_name, data, span, default_color):
        height = 0
        section_value = str(data.get(section_name))
        if section_value:
            height += span * self.resolution
        section_color = data.get('{}_color'.format(section_name), default_color)

        return section_value, height, section_color

    def get_text(self, section_name, data, span, default_color):
        height = 0
        section_lines = 0
        section_value = str(data.get(section_name))
        if section_value:
            section_lines = section_value.count('\n') + 1
            height += span * section_lines * self.resolution
        section_color = data.get('{}_color'.format(section_name), default_color)

        return section_value, height, section_lines, section_color

    # if there is no y it means that the draw is y automated and should follow the y_cursor
    def update_y_cursor(self, span, align=Position.CENTER, frame=False, lines=1):

        y_cursor_increment = (span * lines / 2) * self.resolution
        self.y_cursor += y_cursor_increment
        y = self.y_cursor

        if align == Position.UP:
            y = self.y_cursor - 2/3*y_cursor_increment
        elif align == Position.DOWN:
            y = self.y_cursor + 2/3*y_cursor_increment

        self.debug_section_line(width=1)
        self.y_cursor += y_cursor_increment

        if frame:
            return self.y_cursor - y_cursor_increment*2, self.y_cursor
        return y

    def draw_text(self, x, text, y=None, span=1, fill=None, font=None, anchor=None, origin_x=None, origin_y=None):
        """
        :param x: value of x entry point
        :param y: value of y entry point
        :param text: string of the name that you want to print
        :param span: the di dimension of the section
        :param fill: fill
        :param font: font
        :param anchor: value_printed
        :param origin_x: where the text must start in reference of the origin (center, right or left)
        :param origin_y: same of x but up, down and center
        """
        if not text:
            return

        if not y:
            y = self.update_y_cursor(span)

        w, h = self.draw.textsize(text, font=font)

        if origin_y == Position.UP:
            _y = y - h
        elif origin_y == Position.DOWN:
            _y = y
        else:
            _y = y - (h/2)

        if origin_x == Position.RIGHT:
            _x = x
        elif origin_x == Position.LEFT:
            _x = x - w
        else:
            _x = x - (w / 2)

        if DEBUG:
            self.draw.rectangle([(_x, _y), (_x + w, _y + h)])  # text box

        self.draw.text([_x, _y], text, fill=fill, font=font, anchor=anchor)

    def draw_multiline_text(self, x, text, y=None, lines=1, span=1, fill=None, font=None, anchor=None, align=None):
        """
        :param x: value of x entry point
        :param y: value of y entry point, if none it will handle it automatically
        :param lines: the number of lines in the text
        :param text: string of the name that you want to print
        :param span: the di dimension of the section
        :param fill: fill
        :param font: font
        :param anchor: anchor
        :param align: align
        """
        if not text:
            return

        if not y:
            y = self.update_y_cursor(span, lines=lines)

        w, h = self.draw.multiline_textsize(text, font=font)

        if DEBUG:
            self.draw.rectangle([(x, y), (x + w / 2, y + h / 2)])  # text box

        self.draw.multiline_text([(x - w / 2), (y - h / 2)], text, fill=fill, font=font, anchor=anchor, align=align)

    @staticmethod
    def draw_rectangle(draw_obj, x, y, x_2, y_2, fill=None):
        draw_obj.rectangle([(x, y), (x_2, y_2)], fill=fill)

    def get_image(self):
        """
        :return: image converted as byte array
        """
        # convert the image in bytes to send it
        img_bytes = BytesIO()
        img_bytes.name = 'level_up.png'
        self.image.save(img_bytes, format='PNG')
        img_bytes.seek(0)

        return img_bytes

    def save_image(self, file_dir):
        self.image.save(file_dir, format='PNG')

    def debug_section_line(self, width=2):
        if DEBUG:
            self.draw.line([(0, self.y_cursor), (self.width, self.y_cursor)], width=width)
