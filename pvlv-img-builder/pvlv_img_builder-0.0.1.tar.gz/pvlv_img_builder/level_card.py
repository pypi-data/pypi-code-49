from pvlv_img_builder.configurations.configuration import (
    TEXT_COLOR,
    TITLE_COLOR,
)
from PIL import ImageFont
from math import ceil
from pvlv_img_builder.modules.level_utils import LevelUtils
from pvlv_img_builder.utils.positions import Position
from pvlv_img_builder.draw_support import (
    SPAN_BORDER,
    SPAN_TITLE,
    SPAN_TEXT,
)

"""                   
    +-----------------------------------------+  
    |              SPAN_BORDER(border)        | span             
    +-----------------------------------------+                                 
    |              SPAN_TITLE(title)          | span     
    |                                         | span 
    +-----------------------------------------+ 
    |              SPAN_DATA                  | span  
    |                                         | span                               
    +--+-----------------------------------+--+   
    |  |                                   |  | span        
    |  |           SPAN_XP_BAR             |  | span
    |  |                                   |  | span           
    +--+-----------------------------------+--+
    |              SPAN_TEXT(text)            | span                         
    +-----------------------------------------+  
    |              SPAN_BORDER(border)        | span     at the end of all                        
    +-----------------------------------------+        
"""

SPAN_DATA = 1
SPAN_XP_BAR = 2


class DrawLevelCard(LevelUtils):

    def __init__(self, data):
        """
        :param data: is a dictionary look the documentation on the top of this file:
        """
        super().__init__(data)
        self.update_bar_data(data)  # the class will read all the data to build the xp bar

        self.height += SPAN_BORDER * self.resolution  # first border at the top

        self.username, h, self.username_color = self.get_section('username', data, SPAN_TITLE, TITLE_COLOR)
        self.height += h

        self.data_section = data.get('data')
        if self.data_section:
            # reserve the space
            self.height += SPAN_DATA * self.resolution
            # get values
            self.rank = self.data_section.get('rank', 'ND')
            self.rank_label = self.data_section.get('rank_label', 'RANK')
            self.rank_color = self.data_section.get('rank_color', TEXT_COLOR)
            self.level = self.data_section.get('level', 'ND')
            self.level_label = self.data_section.get('level_label', 'LEVEL')
            self.level_color = self.data_section.get('level_color', TEXT_COLOR)

        """
        Add space for SPAN_BAR
        The bar is handled in another class.
        """
        self.bar_section = data.get('bar')
        if self.bar_section:
            self.height += SPAN_XP_BAR * self.resolution

        self.text, h, self.text_lines, self.text_color = self.get_text('text', data, SPAN_TEXT, TEXT_COLOR)
        self.height += h

        self.height += SPAN_BORDER * self.resolution  # last border at the end
        self.height = ceil(self.height)

        self.build_canvas()

        self.font_data_value = ImageFont.truetype(self.font_dir, int(self.resolution * SPAN_DATA / 1.2))

    def draw_level_card(self):

        self.debug_section_line()

        self.draw_text(
            self.width / 2,
            self.username,
            span=SPAN_TITLE,
            font=self.font_title,
            fill=self.level_color,
        )

        self.debug_section_line()

        y = self.update_y_cursor(SPAN_DATA, align=Position.DOWN)

        self.draw_text(
            self.X_BORDER_OFFSET,
            self.rank_label,
            y=y,
            font=self.font_text,
            fill=self.rank_color,
            origin_x=Position.RIGHT,
            origin_y=Position.UP
        )
        w, h = self.draw.textsize(str(self.rank_label), font=self.font_text)

        self.draw_text(
            self.X_BORDER_OFFSET + w,
            ' #{}'.format(self.rank),
            y=y,
            font=self.font_data_value,
            fill=self.rank_color,
            origin_x=Position.RIGHT,
            origin_y=Position.UP
        )

        self.draw_text(
            self.width - self.X_BORDER_OFFSET,
            str(self.level),
            y=y,
            font=self.font_data_value,
            fill=self.level_color,
            origin_x=Position.LEFT,
            origin_y=Position.UP
        )
        w, h = self.draw.textsize(str(self.level), font=self.font_data_value)
        self.draw_text(
            self.width - (self.X_BORDER_OFFSET + w),
            '{} '.format(self.level_label),
            y=y,
            font=self.font_text,
            fill=self.level_color,
            origin_x=Position.LEFT,
            origin_y=Position.UP,
        )

        self.debug_section_line()

        y_frame = self.update_y_cursor(SPAN_XP_BAR, frame=True)
        xy_box = [(self.X_BORDER_OFFSET, y_frame[0]), (self.width - self.X_BORDER_OFFSET, y_frame[1])]
        self.draw_xp_bar(xy_box)

        self.debug_section_line()

        self.draw_multiline_text(
            self.width / 2,
            self.text,
            lines=self.text_lines,
            span=SPAN_TEXT,
            font=self.font_text,
            fill=self.text_color,
            align=Position.CENTER
        )

        self.debug_section_line()
