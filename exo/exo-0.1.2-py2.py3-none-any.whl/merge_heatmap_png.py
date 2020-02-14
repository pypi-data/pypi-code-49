#!/usr/bin/python
from PIL import Image

import click

# https://stackoverflow.com/a/35586618
# https://github.com/python-pillow/Pillow/issues/3755

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
@click.command(options_metavar='<options>', context_settings=CONTEXT_SETTINGS)
@click.argument('fig1', type=click.Path(exists=True, resolve_path=True, file_okay=True, dir_okay=False,))
@click.argument('fig2', type=click.Path(exists=True, resolve_path=True, file_okay=True, dir_okay=False,))
@click.option('-o', '--out', metavar="<string>", default='merge.png', prompt=True, show_default='merge.png', help='output filename')
def cli(fig1, fig2, out):
    """
    Combines two PNG files into a single PNG by averaging the pixel RGB values from input PNGs.
    PNGs need to be of same dimensions.

    """
    click.echo('\n' + '.' * 50)

    # open first image
    image1 = Image.open(fig1)

    # open second image
    image2 = Image.open(fig2)

    # retrieve the image dimensions.
    width, height = image1.size
    width2, height2 = image2.size

    if [width, height] != [width2, height2]:
        print("Image dimensions do not match! The Two inputs must have equal dimensions")
        exit(1)
    else:
        print("Fig1 dimensions: ", image1.size)
        print("Fig2 dimensions: ", image2.size)
        # Create a new image object.
        merged = Image.new('RGB', image1.size)

        for i in range(0, width):
            for j in range(0, height):
                ima1 = list(image1.getpixel((i, j)))
                ima2 = list(image2.getpixel((i, j)))
                if ima1 == ima2:
                    r, g, b, a = ima1
                elif [ima1[0], ima1[1], ima1[2]] == [0, 0, 0] and [ima2[0], ima2[1], ima2[2]] != [0, 0, 0]:
                    r, g, b, a = ima2
                elif [ima1[0], ima1[1], ima1[2]] != [0, 0, 0] and [ima2[0], ima2[1], ima2[2]] == [0, 0, 0]:
                    r, g, b, a = ima1
                elif [ima1[0], ima1[1], ima1[2]] != [0, 0, 0] and ima2 == [255, 255, 255, 255]:
                    r, g, b, a = ima1
                elif [ima2[0], ima2[1], ima2[2]] != [0, 0, 0] and ima1 == [255, 255, 255, 255]:
                    r, g, b, a = ima2
                else:
                    # print ima1,ima2
                    r = (ima1[0] + ima2[0]) // 2
                    g = (ima1[1] + ima2[1]) // 2
                    b = (ima1[2] + ima2[2]) // 2
                    a = 255
                    # print [r,g,b,a]

                merged.putpixel((i, j), (r, g, b, a))
        merged.save(out)
    click.echo('\n' + '.' * 50)
