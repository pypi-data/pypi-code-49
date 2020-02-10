from math import ceil
from pvlv_img_builder.configurations.configuration import (
    TEXT_COLOR,
    TITLE_COLOR,
    GRAY_BLUE,
)
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
    |                                         | span
    |              SPAN_RANK                  |
    |                                         | span
    +-----------------------------------------+
    |              SPAN_TEXT(text)            | span
    +-----------------------------------------+
    |              SPAN_BORDER(border)        | span     at the end of all
    +-----------------------------------------+

"""

SPAN_RANK = 1.5

"""
        +--------+--------------------+---------------------+-+----------+           
        |        |                    |                     | |          |                      
   +--> |  RANK  |      USERNAME      |    XP_BAR           | | LEVEL    |      
   |    |        |                    |                     | |          |                   
   |    +-+------+--------------------+---------------------+-+----------+ 
OFFSET

"""

DIM_RANK = 1.5
DIM_USERNAME = 7
DIM_XP_BAR = 7
DIM_LEVEL = 3

DIM = DIM_RANK + DIM_USERNAME + DIM_XP_BAR + DIM_LEVEL


class DrawRankingCard(LevelUtils):

    def __init__(self, data):
        """
        :param data: is a dictionary look the documentation on the top of this file:
        """
        super().__init__(data)

        self.height += SPAN_BORDER * self.resolution  # first border at the top

        self.title, h, self.title_color = self.get_section('title', data, SPAN_TITLE, TITLE_COLOR)
        self.height += h

        self.rank_sections = []
        sections = self.data.get('rank', False)
        if sections is not False:
            # extract the sections and put them into an array
            for key in sections.keys():
                self.rank_sections.append(sections.get(key))
                self.height += SPAN_RANK * self.resolution

        # add space for SPAN_TEXT
        self.text, h, self.text_lines, self.text_color = self.get_text('text', data, SPAN_TEXT, TEXT_COLOR)
        self.height += h

        self.height += SPAN_BORDER * self.resolution  # last border in the end

        # ceil the value to from float to decimal value, cause the img creation need int
        self.height = ceil(self.height)
        self.width = ceil(self.resolution * DIM + self.X_BORDER_OFFSET*2)

        self.build_canvas()

    def __draw_rank_section(self, xy_box, data, biggest_rank, biggest_level):

        coords_1 = xy_box[0]
        coords_2 = xy_box[1]

        username = data.get('username', 'Anonymous')
        username_color = data.get('username_color', TEXT_COLOR)
        highlight = data.get('highlight', False)

        data_section = data.get('data')
        rank = data_section.get('rank', 'ND')
        rank_color = data_section.get('rank_color', GRAY_BLUE)
        level = data_section.get('level', 'ND')
        level_label = data_section.get('level_label', 'LEVEL')
        level_color = data_section.get('level_color', GRAY_BLUE)

        y_cursor = coords_1[1] + (coords_2[1] - coords_1[1]) / 2

        self.draw_text(
            self.X_BORDER_OFFSET,
            '#{} '.format(rank),
            y=y_cursor,
            font=self.font_text,
            fill=rank_color,
            origin_x=Position.RIGHT,
            origin_y=Position.CENTER
        )

        # to know the space between rank and username to keep all in line
        biggest_rank_txt = '#{} '.format(biggest_rank)
        w, h = self.draw.textsize(biggest_rank_txt, font=self.font_text)
        self.draw_text(
            self.X_BORDER_OFFSET + w,
            ' '+username,
            y=y_cursor,
            font=self.font_text,
            fill=username_color if not highlight else GRAY_BLUE,
            origin_x=Position.RIGHT,
            origin_y=Position.CENTER,
        )

        x_cursor = (DIM_RANK+DIM_USERNAME) * self.resolution
        next_x_cursor = x_cursor + DIM_XP_BAR * self.resolution

        self.update_bar_data(data)
        xy_box_bar = [(x_cursor, coords_1[1]), (next_x_cursor, coords_2[1])]
        self.draw_xp_bar(xy_box_bar, xp_reference=False)

        # to know the space between rank and username to keep all in line
        biggest_level_txt = '{}'.format(biggest_level)
        w, h = self.draw.textsize(biggest_level_txt, font=self.font_text)

        x_cursor = self.width - (self.X_BORDER_OFFSET + w)
        self.draw_text(
            x_cursor,
            level_label,
            y=y_cursor,
            font=self.font_text,
            fill=self.text_color,
            origin_x=Position.LEFT,
            origin_y=Position.CENTER,
        )

        self.draw_text(
            x_cursor,
            ' {}'.format(level),
            y=y_cursor,
            font=self.font_text,
            fill=level_color,
            origin_x=Position.RIGHT,
            origin_y=Position.CENTER

        )

    def draw_ranking(self):

        self.debug_section_line()

        if self.title is not False:
            self.draw_text(
                self.width / 2,
                self.title,
                font=self.font_title,
                fill=self.title_color
            )

        self.debug_section_line()

        # to know the space between rank/level to keep all in line
        # we need to know the dimensions of the biggest rank and level
        biggest_rank = self.rank_sections[-1].get('data', {}).get('rank', 'ND')  # ordered in crescent mode
        biggest_level = self.rank_sections[0].get('data', {}).get('level', 'ND')  # ordered in descendent mode

        for el in self.rank_sections:
            y_frame = self.update_y_cursor(SPAN_RANK, frame=True)
            xy_box = [(self.X_BORDER_OFFSET, y_frame[0]), (self.width - self.X_BORDER_OFFSET, y_frame[1])]
            self.__draw_rank_section(xy_box, el, biggest_rank, biggest_level)
            self.debug_section_line()

        if self.text is not False:
            self.draw_multiline_text(
                self.width / 2,
                self.text,
                lines=self.text_lines,
                font=self.font_text,
                fill=self.text_color,
                align=Position.CENTER
            )

        self.debug_section_line()
