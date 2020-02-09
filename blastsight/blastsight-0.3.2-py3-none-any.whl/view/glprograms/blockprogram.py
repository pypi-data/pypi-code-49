#!/usr/bin/env python

#  Copyright (c) 2019-2020 Gabriel Sanhueza.
#
#  Distributed under the MIT License.
#  See LICENSE for more info.

from .shaderprogram import ShaderProgram


class BlockProgram(ShaderProgram):
    def __init__(self, viewer):
        super().__init__(viewer)
        self.base_name = 'Block'

    def setup(self) -> None:
        super().setup()
        self.add_uniform_loc('block_size')

    def setup_shaders(self) -> None:
        # Placeholders to avoid early garbage collection
        vs = self.enable_vertex_shader()
        fs = self.enable_fragment_shader()
        gs = self.enable_geometry_shader()

        self.shader_program.link()

    def inner_draw(self, drawables: list) -> None:
        for drawable in drawables:
            self.update_uniform('block_size', *drawable.element.block_size)
            drawable.draw()
