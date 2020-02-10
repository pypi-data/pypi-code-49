from pvlv_img_builder.configurations.configuration import (
    BACKGROUND_COLOR, DEFAULT_TOP_TITLE_COLOR, TEXT_COLOR, DEFAULT_TOWER_2_COLOR,
    DIR_DEFAULT_FONT
)
from pvlv_img_builder.utils.formatting import remap_range
from PIL import ImageFont
from io import BytesIO
from math import ceil
from pvlv_img_builder.modules.support import DrawSupport

draw_support = DrawSupport()


"""
    +-----------------------------------------+
    |             SPAN_BORDER                 | span    |
    +-----------------------------------------+         |
    |                                         | span    |
    |             SPAN_TOP_TITLE              | span    |SPAN_TOP_TITLE_SECTION
    |                                         | span    |
    +-----------------------------------------+         |
    |             SPAN_BORDER                 | span    |
    +-----------------------------------------+                
    |             SPAN_SECTION_TITLE          | span                            |
    |                                         | span                            |
    +-----------------------------------------+                                 |
    |             SPAN_SUBTITLE               | span                            |
    +--+-----------------------------------+--+                                 |
    |  |          SPAN_GRAPH_BORDER        |  | span    |                       |
    |--+-----------------------------------+--|         |                       |
    |  |                                   |  | span    |                       |
    |  |          SPAN_GRAPH               |  | span    |SPAN_GRAPH_SECTION     |
    |  |                                   |  | span    |                       |
    |  |                                   |  | span    |                       |
    |--+-----------------------------------+--|         |                       |
    |  |          SPAN_GRAPH_BORDER        |  | span    |                       |
    +--+-----------------------------------+--+                                 |              
    |                                         | span                            |
    |             SPAN_DESCRIPTION            | span                            |
    |                                         | span                            |
    |                                         | span                            |
    +-----------------------------------------+                                 |
    |             SPAN_BORDER                 | span                            |
    +-----------------------------------------+            
    |             SPAN_BORDER                 | span     at the end of all                        
    +-----------------------------------------+           
"""
SPAN_BORDER = 1
SPAN_TOP_TITLE = 2.5
SPAN_SECTION_TITLE = 2
SPAN_SUBTITLE = 1
SPAN_GRAPH_BORDER = 1
SPAN_GRAPH = 4
SPAN_DESCRIPTION = 1  # It will automatically reserve one span per line

SPAN_TOP_TITLE_SECTION = SPAN_BORDER + SPAN_TOP_TITLE + SPAN_BORDER
SPAN_GRAPH_SECTION = SPAN_GRAPH_BORDER + SPAN_GRAPH + SPAN_GRAPH_BORDER


"""
      B     T  TS T  T                                 
      O     O  OP O  O                                
      R     W  WA W  W
      D     E  EC E  E
      E     R  RE R  R
      R     A  B  A  B                                              
    +------+----------------------------------+------+
    |      |                                  |      |
    |------+----------------------------------+------|
    |      |   -                       -      |      | 
    |      |----     -                 -     -|      |
    |      |----  ----     -        ----  ----|      |
    |      |----  ----  ----  ----  ----  ----|      |
    |------+----------------------------------+------|
    |      |                                  |      | 
    +------+----------------------------------+------+
          

"""
BORDER_DIM = 2
TOWER_DIM = 1
SPACE_DIM = 0.25


class DrawGraph(object):

    def __init__(self, data):

        """
        :param data: is a dictionary look the documentation on the top of this file:
        """

        self.data = data

        self.y_resolution = 45
        self.width = 1800
        self.height = 0

        self.top_title = self.data.get('top_title', False)
        if self.top_title is not False:
            self.height += SPAN_TOP_TITLE_SECTION * self.y_resolution
        self.top_title_color = self.data.get('top_title_color', DEFAULT_TOP_TITLE_COLOR)

        self.data_sections = []

        for data_section in self.data.keys():
            if data_section.startswith('section'):

                ds = self.data.get(data_section)

                # add space for SPAN_SECTION_TITLE
                if ds.get('section_title', False) is not False:
                    self.height += SPAN_SECTION_TITLE * self.y_resolution

                n_subsections = 0
                for graph in ds.keys():
                    if graph.startswith('graph'):
                        n_subsections += 1

                        # add space for SPAN_GRAPH_SUBTITLE
                        if ds[graph].get('subtitle', False) is not False:
                            self.height += SPAN_SUBTITLE * self.y_resolution

                        self.height += SPAN_GRAPH_SECTION * self.y_resolution

                # add space for SPAN_GRAPH_TEXT
                description = ds.get('description', False)
                if description is not False:
                    description_lines = description.count('\n') + 1
                    self.height += SPAN_DESCRIPTION * description_lines * self.y_resolution
                    ds['description_lines'] = description_lines

                self.height += SPAN_BORDER * self.y_resolution
                ds['n_subsections'] = n_subsections
                self.data_sections.append(ds)

        self.height += SPAN_BORDER * self.y_resolution

        self.height = ceil(self.height)
        background_color = self.data.get('background_color', BACKGROUND_COLOR)
        self.image = draw_support.create_image("RGB", self.width, self.height, background_color)
        self.draw = draw_support.create_draw(self.image)

        self.y_cursor = 0

        self.font_dir = self.data.get('font', DIR_DEFAULT_FONT)
        self.font_top_title = ImageFont.truetype(self.font_dir, int(self.y_resolution * SPAN_TOP_TITLE))
        self.font_section_title = ImageFont.truetype(self.font_dir, int(self.y_resolution * SPAN_SECTION_TITLE / 1.2))
        self.font_subtitle = ImageFont.truetype(self.font_dir, int(self.y_resolution * SPAN_SUBTITLE / 1.2))
        self.font_text = ImageFont.truetype(self.font_dir, int(self.y_resolution * SPAN_GRAPH_BORDER / 2))
        self.font_description = ImageFont.truetype(self.font_dir, int(self.y_resolution * SPAN_BORDER / 1.4))

        self.title_color = self.data.get('text_color', TEXT_COLOR)
        self.text_color = self.data.get('title_color', TEXT_COLOR)

    def __remap_values(self, data, max_value):
        value_array = []
        for el in data:
            value_array.append(remap_range(el, 0, max_value, 0, SPAN_GRAPH * self.y_resolution))
        return value_array

    def __draw_towers_names(self, x, x_resolution, data):
        """
        :param x: value of x entry point
        :param x_resolution: value of one x_span in pixels
        :param data: string of the name that you want to print
        """
        for el in data:
            entry_x = x + x_resolution * TOWER_DIM / 2
            entry_y = self.y_cursor + SPAN_GRAPH_BORDER / 2 * self.y_resolution
            draw_support.draw_multiline_text_in_center(
                self.draw, entry_x, entry_y, str(el), fill=self.text_color, font=self.font_text, align='center'
            )

            x += x_resolution * TOWER_DIM + x_resolution * SPACE_DIM

    def __draw_towers_value_vertical(self, x, y, x_resolution, tower_dim, tower_height_pixels, value_printed):

        entry_x = x + tower_dim * x_resolution / 2
        entry_y = y - tower_height_pixels - SPAN_GRAPH_BORDER * self.y_resolution / 2

        draw_support.draw_text(
            self.draw, entry_x, entry_y, str(value_printed), fill=self.text_color, font=self.font_text
        )

    def __draw_towers_value_horizontal(self, x, y, x_resolution, tower_dim, tower_height_pixels, value_printed):

        w, h = draw_support.get_text_dimension(self.draw, str(value_printed), font=self.font_text)

        entry_x = x + tower_dim * x_resolution / 2

        span_text_pixels = SPAN_GRAPH_BORDER * self.y_resolution / 2
        if tower_height_pixels > (h+span_text_pixels):
            entry_y = y - tower_height_pixels + span_text_pixels*0.65
            _fill = self.text_color
        else:
            entry_y = y - tower_height_pixels - span_text_pixels
            _fill = self.text_color

        draw_support.draw_text(
            self.draw, entry_x, entry_y, str(value_printed), fill=_fill, font=self.font_text
        )

    def __draw_towers(self,
                      x, y,
                      x_resolution,
                      tower_structure,
                      tower_index,
                      tower_color,
                      value,
                      value_printed,
                      draw_value_function
                      ):

        tower_structure_sum = sum(tower_structure)

        _pre = abs(tower_structure_sum - sum(tower_structure, tower_index))
        pre_dim = TOWER_DIM * _pre / tower_structure_sum
        _post = abs(tower_structure_sum - _pre - tower_structure[tower_index])
        post_dim = TOWER_DIM * _post / tower_structure_sum
        tower_dim = TOWER_DIM * tower_structure[tower_index] / tower_structure_sum

        vl = iter(value_printed)
        for el in value:
            x += pre_dim * x_resolution
            x_2 = x + tower_dim * x_resolution
            y_2 = y - el

            draw_support.draw_rectangle(self.draw, x, y, x_2, y_2, fill=tower_color)
            try:
                label = next(vl)
            except StopIteration:
                label = 'N/D'

            if el is not 0:
                draw_value_function(x, y, x_resolution, tower_dim, el, label)

            x += (post_dim + tower_dim) * x_resolution + SPACE_DIM * x_resolution

    def __draw_graph(self, graph_data):

        subtitle = graph_data.get('subtitle', False)

        if subtitle is not False:

            subtitle_color = graph_data.get('subtitle_color', self.title_color)

            self.y_cursor += SPAN_SUBTITLE / 2 * self.y_resolution
            draw_support.draw_text(
                self.draw,
                self.width / 2,
                self.y_cursor,
                subtitle,
                font=self.font_subtitle,
                fill=subtitle_color)
            self.y_cursor += SPAN_SUBTITLE / 2 * self.y_resolution

        self.y_cursor += (SPAN_GRAPH_BORDER + SPAN_GRAPH) * self.y_resolution

        x_names = graph_data.get('x_names', False)
        # y_names = graph_data.get('y_names', False)

        towers = []
        n_towers = 0
        tower_structure = []
        max_value = 0

        for key in graph_data.keys():
            if key.startswith('tower'):

                tower_data = graph_data.get(key)
                towers.append(tower_data)

                data = tower_data.get('data')

                this_max = max(data)
                if this_max > max_value:
                    max_value = this_max

                data_len = len(data)
                if data_len > n_towers:
                    n_towers = data_len
                tower_structure.append(tower_data.get('tower_dim', TOWER_DIM))

        border_subdivision = BORDER_DIM * 2
        tower_subdivision = n_towers * TOWER_DIM
        space_subdivision = (n_towers * SPACE_DIM - SPACE_DIM) if n_towers > 1 else 0
        x_resolution = self.width / (border_subdivision + tower_subdivision + space_subdivision)

        x = x_resolution * BORDER_DIM
        y = self.y_cursor

        self.__draw_towers_names(x, x_resolution, x_names)

        for i in range(len(towers)):

            data = towers[i].get('data')
            value_printed = towers[i].get('value_printed')
            color = towers[i].get('color', DEFAULT_TOWER_2_COLOR)
            printed_position = towers[i].get('printed_position')

            if printed_position == 'horizontal':
                draw_value_function = self.__draw_towers_value_horizontal
            elif printed_position == 'vertical':
                draw_value_function = self.__draw_towers_value_vertical
            else:
                draw_value_function = self.__draw_towers_value_horizontal

            value = self.__remap_values(data, max_value)
            self.__draw_towers(
                x, y, x_resolution, tower_structure, i, color, value, value_printed, draw_value_function
            )

        self.y_cursor += SPAN_GRAPH_BORDER * self.y_resolution

    def __draw_section(self, section_data):

        graph_title = section_data.get('section_title', False)

        if graph_title is not False:

            graph_title_color = section_data.get('section_title_color', self.title_color)

            self.y_cursor += SPAN_SECTION_TITLE / 2 * self.y_resolution
            draw_support.draw_text(
                self.draw,
                self.width / 2,
                self.y_cursor,
                graph_title,
                font=self.font_section_title,
                fill=graph_title_color)
            self.y_cursor += SPAN_SECTION_TITLE / 2 * self.y_resolution

        n_subsections = section_data.get('n_subsections', 0)
        for i in range(n_subsections):
            self.__draw_graph(section_data.get('graph_{}'.format(i + 1)))

        description = section_data.get('description', False)

        if description is not False:

            description_color = section_data.get('description_color', self.text_color)
            description_lines = section_data.get('description_lines', 1)

            self.y_cursor += description_lines / 2 * self.y_resolution
            draw_support.draw_multiline_text_in_center(
                self.draw,
                self.width / 2,
                self.y_cursor,
                description,
                font=self.font_description,
                fill=description_color,
                align='center')
            self.y_cursor += description_lines / 2 * self.y_resolution

            # add border at the end of this section
            self.y_cursor += SPAN_BORDER * self.y_resolution

    def draw_graph(self):

        if self.top_title is not False:
            self.y_cursor += (SPAN_BORDER + SPAN_TOP_TITLE/2) * self.y_resolution
            draw_support.draw_text(
                self.draw,
                self.width / 2,
                self.y_cursor,
                self.top_title,
                font=self.font_top_title,
                fill=self.top_title_color
            )
            self.y_cursor += (SPAN_BORDER + SPAN_TOP_TITLE / 2) * self.y_resolution

        for el in self.data_sections:
            self.__draw_section(el)

    def get_image(self):

        """
        :return: image converted as byte array
        """
        # convert the image in bytes to send it
        img_bytes = BytesIO()
        img_bytes.name = 'image.png'
        self.image.save(img_bytes, format='PNG')
        img_bytes.seek(0)

        return img_bytes

    def save_image(self, file_dir):
        self.image.save(file_dir, format='PNG')
