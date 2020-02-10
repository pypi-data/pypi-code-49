from pvlv_img_builder.configurations.configuration import (
    TITLE_COLOR,
    TEXT_COLOR,
)
from PIL import ImageFont
from math import ceil
from pvlv_img_builder.draw_support import DrawSupport, Position
from pvlv_img_builder.draw_support import (
    SPAN_TITLE,
    SPAN_TEXT,
    SPAN_BORDER,
)


"""                   
    +-----------------------------------------+
    |              SPAN_BORDER(border)        | span
    +-----------------------------------------+
    |                                         | span
    |              SPAN_LEVEL(title)          | span
    |                                         | span
    +-----------------------------------------+
    |              SPAN_BOLD_TEXT             | span
    |                                         | span
    +-----------------------------------------+
    |              SPAN_TEXT(text)            | span
    +-----------------------------------------+
    |              SPAN_BORDER(border)        | span
    +-----------------------------------------+        
"""
SPAN_BOLD_TEXT = 1


class DrawLevelUpCard(DrawSupport):

    def __init__(self, data):
        """
        :param data: is a dictionary look the documentation on the top of this file:
        """
        super().__init__(data)

        self.level, h, self.level_color = self.get_section('level', self.data, SPAN_TITLE, TITLE_COLOR)
        self.height += h

        self.bold_text, h, self.bold_text_color = self.get_section('bold_text', self.data, SPAN_BOLD_TEXT, TITLE_COLOR)
        self.height += h

        self.text, h, self.text_lines, self.text_color = self.get_text('text', self.data, SPAN_TEXT, TEXT_COLOR)
        self.height += h

        self.height += SPAN_BORDER * self.resolution
        self.height = ceil(self.height)

        self.build_canvas()

        self.font_bold_text = ImageFont.truetype(self.font_dir, int(self.resolution * SPAN_BOLD_TEXT / 1.3))

    def draw_level_up(self):

        self.debug_section_line()

        self.draw_text(
            self.width / 2,
            self.level,
            span=SPAN_TITLE,
            font=self.font_title,
            fill=self.level_color,
            anchor=Position.CENTER,
        )

        self.debug_section_line()

        self.draw_text(
            self.width / 2,
            self.bold_text,
            span=SPAN_BOLD_TEXT,
            font=self.font_bold_text,
            fill=self.bold_text_color
        )

        self.debug_section_line()

        self.draw_multiline_text(
            self.width / 2,
            self.text,
            lines=self.text_lines,
            span=SPAN_TEXT,
            font=self.font_text,
            fill=self.text_color,
            align=Position.CENTER,
        )

        self.debug_section_line()
