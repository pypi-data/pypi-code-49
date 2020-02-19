# -*- coding: utf-8 -*-

from PIL import Image
import numpy as np


def process(input_path, output_path):
    image = Image.open(input_path)
    image.putalpha(255)

    array_image = np.array(image)
    array_r = np.copy(array_image)
    array_r[:, :, 1:3] = 0
    image_r = Image.fromarray(array_r)

    array_gb = np.copy(array_image)
    array_gb[:, :, 0] = 0
    image_gb = Image.fromarray(array_gb)

    canvas_r = Image.new("RGB", image.size, color=(0, 0, 0))
    canvas_gb = Image.new("RGB", image.size, color=(0, 0, 0))

    canvas_r.paste(image_r, (5, 5), image_r)
    canvas_gb.paste(image_gb, (0, 0), image_gb)

    result_array = np.array(canvas_r) + np.array(canvas_gb)
    result = Image.fromarray(result_array)
    result = result.crop((5, 5, image.size[0], image.size[1]))
    result.save(output_path)
