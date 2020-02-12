#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Library Imports
import argparse
# Required
import os
import shutil
import sys
import time
from datetime import datetime
from mkpreview.config import *
from mkpreview.version import __version__
from mkpreview.database import Database
# Program Specific library imports
import ffmpeg
from wand.color import Color
from wand.drawing import Drawing
from wand.image import Image
from wand.display import display as Display
import hashlib
import random
import string

# Add this module's location to syspath
sys.path.insert(0, os.getcwd())

__author__ = 'Colin Bitterfield'
__email__ = 'colin@bitterfield.com'
__prog_name__ = os.path.basename(__file__)
__short_name__ = os.path.splitext(__prog_name__)[0]
__console_size_ = shutil.get_terminal_size((80, 20))[0]
__timestamp__ = time.time()
__run_datetime__ = datetime.fromtimestamp(__timestamp__)  # Today's Date

# Global Variables for Testing
# Test and Debugging Variables
# These are applied to all functions and classes
# These settings override the command line if set to TRUE
# Set to NONE to have no effect
# If set to True or False, it will override the CLI

DEBUG = None
DRYRUN = None
VERBOSE = False
QUIET = None
myDB = None
VIDEOS = None
HWACCEL = None
DOCKER = False

# Global Variables # set defaults here.
if DEBUG:
    tmp = globals().copy()
    [print(k, '  :  ', v, ' type:', type(v)) for k, v in tmp.items() if
     not k.startswith('_') and k != 'tmp' and k != 'In' and k != 'Out' and not hasattr(v, '__call__')]

FFMPEG = ""
FFPROBE = ""


# ---- Functions ----
def getenviron(prefix, **kwargs):
    """
    Get a list of environment variables and return a list for ARG Parsing overrides



    """
    return_list = list()

    # KWARGS is a translation table KEY=Envionment Variable, Value is return key
    # If set scan for this list, if not use a prefix. If prefix is set, variables are limited to the prefix
    for evar in os.environ:
        key = str()
        value = str()
        if prefix in evar or evar in kwargs.keys():
            if DEBUG:
                print('EVAL ENV: {0} {1}'.format(evar, os.environ.get(evar)))
            value = os.environ.get(evar)
            # Something we can work with
            if kwargs and not prefix:
                print('Kargs Only', evar)
                key = kwargs.get(evar, None)
                print(key, value)

            elif evar.startswith(prefix) and not kwargs:
                key = "--" + evar.replace(prefix, '').replace('_', '-').lower()

            elif evar.startswith(prefix) and kwargs:
                key = kwargs[evar.replace(prefix, '')]

            if key:
                return_list.append(key)
                if value != 'True' and value != 'False' and value != 'None':
                    return_list.append(value)

        else:
            # ENV var we don't need
            pass

    return return_list


def isdocker():
    if not os.path.isfile('/proc/self/cgroup'):
        return False
    with open('/proc/self/cgroup', 'r') as procfile:
        for line in procfile:
            fields = line.strip().split('/')
            if 'docker' in fields:
                return True

    return False


def random_string(stringlength=10):
    """Generate a random string of fixed length """
    letters = string.hexdigits
    letters = letters.lower()
    numbers = string.digits
    return ''.join(random.choice(letters + numbers) for i in range(stringlength))


def md5(filename):
    with open(filename, 'rb') as fh:
        m = hashlib.md5()
        while True:
            data = fh.read(8192)
            if not data:
                break
            m.update(data)

        return m.hexdigest()


def video_info(**kwargs):
    """ Retrieve Video Information and return a dictionary with all variables


        Settings:
        ---------
        REQUIRED = filename


        Parameters:
        ----------
        filename = filename

        Raises:
        ------
        Exception
            If filename does not exist or is not a file

        Returns:
        --------
            SUCCESS, file_info(dict)

        Example:
        --------
        SUCCESS, info = video_info(filename=file)

    """
    global DEBUG
    global FFPROBE

    required = list(['filename'])
    max_params = 1
    success = True

    filename = kwargs.get('filename', None)
    local_info = dict()

    # Check for requirement parameters
    if DEBUG:
        print(required, len(required))
    if DEBUG:
        print(kwargs, len(kwargs))
    if len(required) <= len(kwargs) <= max_params:
        for required in required:
            if required not in kwargs:
                success = False
                raise Exception("The parameter {0} is required".format(required))

    else:
        success = False
        raise Exception('parameters required {0} parameters received {1}'.format(len(required), len(kwargs)))

    if DEBUG:
        print('Success Flag, {0}, arguments {1}'.format(success, kwargs))
    # Code to execute here
    # Test Filename
    if not os.path.isfile(filename):
        success = False
    if success:
        # Get Video Information
        probe_args = {'pretty': None,
                      'select_streams': 'v:0',
                      'show_entries': "stream=bit_rate,height,width,codec_long_name,display_aspect_ratio, avg_frame_rate,bit_rate,max_bit_rate,nb_frames : stream_tags= : stream_disposition= :format=duration,size :format_tags= "

                      }
        if DEBUG:
            print("Get Info FFPROBE={0} arguments {1}".format(FFPROBE, probe_args))
        info = ffmpeg.probe(filename, cmd=FFPROBE, **probe_args)
        if DEBUG:
            print(info)
        local_info['codec_long_name'] = info['streams'][0]['codec_long_name']
        local_info['video_width'] = info['streams'][0]['width']
        local_info['video_height'] = info['streams'][0]['height']
        local_info['video_aspect'] = info['streams'][0]['display_aspect_ratio'] if "display_aspect_ratio" in \
                                                                                   info['streams'][0] else None
        v1, v2 = info['streams'][0]['avg_frame_rate'].split('/')
        local_info['video_frame_rate'] = str(int(int(v1) / int(v2)))
        local_info['video_bit_rate'] = info['streams'][0]['bit_rate']
        local_info['video_frames'] = info['streams'][0]['nb_frames']
        local_info['video_duration'] = info['format']['duration']
        local_info['video_size'] = info['format']['size']

        return success, local_info

    else:

        return success, {'status', 'fail'}

    # End Program Functions and Classes


# Setup Function for the application


def setup(configuration):
    global DEBUG
    global VERBOSE
    global DRYRUN
    global QUIET
    global myDB
    global COLORS
    global TABLE
    global VIDEOS
    global DRYRUN
    global HWACCEL
    global FFLOCATIONS
    global FFPROBE
    global FFMPEG

    # Set Globals if needed
    DEBUG = configuration.debug if configuration.debug else DEBUG
    VERBOSE = configuration.verbose if configuration.verbose else VERBOSE
    DRYRUN = configuration.dryrun if configuration.dryrun else DRYRUN
    QUIET = configuration.quiet if configuration.quiet else QUIET

    # Do some quick testing on colors.

    if configuration.colors:
        print('Available Colors are:')
        print('{}'.format("=" * 40))
        for color in COLORS:
            print(color)
        sys.exit(0)

    if not configuration.in_file:
        print('Missing Video File')
        print('Configuration: {}'.format(configuration))
        sys.exit(1)

    if not configuration.dbfile or configuration.create_newdb:
        if configuration.dbfile:
            myDB = Database(configuration.dbfile, quiet=configuration.quiet, debug=configuration.debug)
        else:
            myDB = Database(os.getcwd() + "/mkpreview.db")

        if DEBUG:
            print('Database {} created'.format(configuration.dbfile))
        # Create New database file
        myDB.create(overwrite=False, backup=configuration.backup_db)
        myDB.connect()
        if configuration.md5:
            myDB.create_table(table='preview', overwrite=False, fields=TABLE['preview'], unique=(['filename', 'md5']))
        else:
            myDB.create_table(table='preview', overwrite=False, fields=TABLE['preview'], unique=(['filename']))
        myDB.close()
    else:
        # Make sure we have a table
        myDB = Database(configuration.dbfile)
        myDB.connect()
        if not myDB.istable(table='preview'):
            if configuration.md5:
                myDB.create_table(table='preview', overwrite=False, fields=TABLE['preview'],
                                  unique=(['filename', 'md5']))
            else:
                myDB.create_table(table='preview', overwrite=False, fields=TABLE['preview'], unique=(['filename']))
        # Enable Multiuser and performance setting
        myDB.sql_exec("""PRAGMA journal_mode=WAL;""")
        myDB.close()

    VIDEOS = list()
    if os.path.isfile(configuration.in_file):
        VIDEOS.append(configuration.in_file)

    elif os.path.isdir(configuration.in_file):
        with os.scandir(configuration.in_file) as entries:
            for entry in entries:
                if entry.is_file() and entry.name.split('.', 1)[1] in VIDEO_EXTENSIONS:
                    full_name = os.path.join(configuration.in_file, entry.name)
                    VIDEOS.append(full_name)

        VIDEOS.sort()
    else:
        print('No Valid Input presented {}'.format(configuration.in_file))

    if DEBUG:
        print(VIDEOS)

    # Find and define FFMPEG Tools.
    if not FFLOCATIONS:
        FFLOCATIONS = ['/usr/local/bin']
    for FF in FFLOCATIONS:
        FFMPEG = os.path.join(FF, 'ffmpeg')
        FFPROBE = os.path.join(FF, 'ffprobe')
        if os.path.isfile(FFMPEG) and os.path.isfile(FFPROBE):
            return

    if DEBUG:
        print('FFMPEG Binaries located: {0} {1}'.format(FFPROBE, FFMPEG))

    # Set HWAccels
    if configuration.hwaccel == 'cuda':
        HWACCEL = {'hwaccel': 'cuda'}
    elif configuration.hwaccel == 'videotoolbox':
        HWACCEL = {'hwaccel': 'videotoolbox'}
    else:
        HWACCEL = None
    return

    # Set Hardware Acceleration

    # Program Functions and Classes
    #
    # Apply the following to all when possible
    #
    # def function(**kwargs)


def cli(**kwargs):
    """Cli function expects at least version= to create the argparser
     parameters:
     ------------
     debug
     quiet
     verbose
     dryrun
     docker
     program
     version
     description
     epilog

     returns:
     -------------
     Name space for cli arguments similar to:
     backup_db=None, colors=False, create_newdb=None, dbfile=None, debug=True, dryrun=False, font_size=20, hwaccel=None, in_file='/tmp', md5file=False, out_dir='/tmp', override=None, part_id=None, quiet=False, studio_id=None, tile_bk_color='Black', tile_cols=5, tile_fg_color='White', tile_rows=6, tile_width=320, verbose=True

     """
    # Get any Environment variables and use them if present
    # Define variables being looked for, and their default values if not found
    program_variables = {
        'MKP_DEBUG': False,
        'MKP_VERBOSE': False,
        'MKP_QUIET': False,
        'MKP_DRYRUN': False,
        'MKP_TILE_WIDTH': 320,
        'MKP_TILE_ROWS': 6,
        'MKP_TILE_COLS': 5,
        'MKP_BACKGROUND': 'Black',
        'MKP_FOREGROUND': 'White',
        'MKP_FONT_SIZE': 20,
        'MKP_INPUT': None,
        'MKP_OUTPUT_DIR': None,
        'MKP_DATABASE': None,
        'MKP_CREATEDB': None,
        'MKP_BACKUPDB': None,
        'MKP_MD5': False,
        'MKP_STUDIOID': None,
        'MKP_PARTID': None,
        'MKP_HWACCEL': None
    }

    environment_variables = ", ".join(program_variables.keys())

    # Read the Environment and update program variables accordingly

    for myvar in os.environ:
        if myvar in program_variables.keys():
            program_variables[myvar] = os.environ.get(myvar, program_variables[myvar])

    # Set a default parse description and epilog. Can be overwritten by program if this is called as a function
    default_epilog = """The filename of the output will be the part_id-md5-originalBaseName.png.
    If the part_id and md5 are unset the filename will be the original base name.png
    The following environment variables are recognized.
    [
    {ENVVARS} ]
    """.format(ENVVARS=environment_variables)

    default_description = """
    This program creates preview cards from movie files and creates a database of the video metadata.
    It can also create an MD5 fingerprint for each file.
    """

    # Receive variables from main program
    # Environment Variables trump program variables.

    debug = kwargs.get('debug', program_variables['MKP_DEBUG'])
    verbose = kwargs.get('verbose', program_variables['MKP_VERBOSE'])
    quiet = kwargs.get('quiet', program_variables['MKP_QUIET'])
    dryrun = kwargs.get('dryrun', program_variables['MKP_DRYRUN'])
    docker = kwargs.get('docker', False)

    program = kwargs.get('program', 'cli function')
    version = kwargs.get('version', 'unknown')
    description = kwargs.get('description', default_description)
    epilog = kwargs.get('epilog', default_epilog)

    if program_variables['MKP_DEBUG']:
        print('Program Variables')
        for k, v in program_variables.items():
            print('{0} -> {1}'.format(k, v))

    parser = argparse.ArgumentParser()
    parser.prog = program
    parser.description = description
    parser.epilog = epilog

    # Defaults for all programs
    parser.add_argument('--version',
                        action='version',
                        version='%(prog)s ' + version)

    # For different kinds of output, provide a choice

    parser.add_argument('-v', '--verbose',
                        help='Turn on verbose output',
                        action='store_true',
                        required=False,
                        dest='verbose',
                        default=program_variables['MKP_VERBOSE']
                        )

    parser.add_argument('-dr', '--dryrun',
                        help='Dryrun enabled no changes will occur',
                        action='store_true',
                        required=False,
                        dest='dryrun',
                        default=program_variables['MKP_DRYRUN']
                        )

    parser.add_argument('-d', '--debug',
                        help='Turn on Debugging Mode',
                        action='store_true',
                        required=False,
                        dest='debug',
                        default=program_variables['MKP_DEBUG']
                        )

    parser.add_argument('-q', '--quiet',
                        help='No output is produced',
                        action='store_true',
                        required=False,
                        dest='quiet',
                        default=program_variables['MKP_QUIET']
                        )

    parser.add_argument('-w', '--tile-width',
                        help='Tile width - Tiles are sqaure',
                        type=int,
                        action='store',
                        required=False,
                        dest='tile_width',
                        default=program_variables['MKP_TILE_WIDTH']
                        )

    parser.add_argument('-r', '--tile-rows',
                        help='Number of rows for a preview',
                        action='store',
                        type=int,
                        required=False,
                        dest='tile_rows',
                        default=program_variables['MKP_TILE_ROWS']
                        )

    parser.add_argument('-c', '--tile-cols',
                        help='Number of columns for a preview',
                        action='store',
                        type=int,
                        required=False,
                        dest='tile_cols',
                        default=program_variables['MKP_TILE_COLS']
                        )

    parser.add_argument('-b', '--background',
                        help='Tile Background Color',
                        action='store',
                        required=False,
                        dest='tile_bk_color',
                        default=program_variables['MKP_BACKGROUND']
                        )

    parser.add_argument('-p', '--foreground',
                        help='Tile Pen Color',
                        action='store',
                        required=False,
                        dest='tile_fg_color',
                        default=program_variables['MKP_FOREGROUND']
                        )

    parser.add_argument('-fs', '--font-size',
                        help='Font size for text default is 24pt',
                        action='store',
                        required=False,
                        dest='font_size',
                        default=program_variables['MKP_FONT_SIZE']
                        )

    parser.add_argument('-i', '--input',
                        help='Video input, can by a file or directory. If directory, it will not be recursive',
                        type=str,
                        action='store',
                        required=False,
                        dest='in_file',
                        default=program_variables['MKP_INPUT']
                        )

    parser.add_argument('-o', '--output-dir',
                        help='Where to put the finished files',
                        type=str,
                        action='store',
                        required=False,
                        dest='out_dir',
                        default=program_variables['MKP_OUTPUT_DIR']
                        )

    parser.add_argument('-m', '--md5',
                        help='Add the MD5 of the file to the filename',
                        action='store_true',
                        required=False,
                        dest='md5',
                        default=program_variables['MKP_MD5']
                        )

    parser.add_argument('-s', '--db-file',
                        help='Store the video information in  SQLI3te file',
                        type=str,
                        action='store',
                        required=False,
                        dest='dbfile',
                        default=program_variables['MKP_DATABASE']
                        )

    parser.add_argument('-create-new-db',
                        help='Create a new database file',
                        action='store_true',
                        required=False,
                        dest='create_newdb',
                        default=program_variables['MKP_CREATEDB']
                        )
    parser.add_argument('-backup-db',
                        help='Create a new database file',
                        action='store_true',
                        required=False,
                        dest='backup_db',
                        default=program_variables['MKP_BACKUPDB']
                        )

    parser.add_argument('-override',
                        help='save image with this filename override all other possible choices',
                        type=str,
                        action='store',
                        required=False,
                        dest='override'
                        )

    parser.add_argument('-colors',
                        help='Display List of Available Colors',
                        action='store_true',
                        required=False,
                        dest='colors',
                        default=False
                        )

    parser.add_argument('-studio-id',
                        help='Replace the this id, first part of filename for a part-id use in conjunction with -part-id',
                        action='store',
                        required=False,
                        dest='studio_id',
                        default=program_variables['MKP_STUDIOID']
                        )

    parser.add_argument('-part-id',
                        help='Change first alpha part of filename for the part-id',
                        type=str,
                        action='store',
                        required=False,
                        dest=program_variables['MKP_STUDIOID']
                        )

    parser.add_argument('-hwaccel',
                        help='Enable Hardware acceleration for videotoolbox or cuda',
                        action='store',
                        choices=['cuda', 'videotoolbox'],
                        required=False,
                        dest='hwaccel',
                        default=program_variables['MKP_HWACCEL']
                        )

    parse_out = parser.parse_args()

    # Minimum requirements to return are INPUT/OUTPUT Dir or --Colors to display colors.

    # Make sure we have the minimum number of arguments to process:
    if (not parse_out.in_file and not parse_out.out_dir) and not parse_out.colors:
        print('At a minimum please provide an input file or directory and and output directory')
        if parse_out.debug:
            print('Parser Variables {}'.format(parse_out))
        parser.print_help(sys.stderr)
        sys.exit(1)

    return parse_out


def main():
    config = cli(version=__version__, program=__prog_name__)
    setup(config)

    myDB.connect()
    for video in VIDEOS:
        banner_info = dict()

        if not QUIET:
            print('Processing File {file}'.format(file=video))
        if not QUIET:
            print('Preview is {rows} rows x {cols} cols @ {width} width px'.format(rows=config.tile_rows,
                                                                                   cols=config.tile_cols,
                                                                                   width=config.tile_width))
        if not QUIET:
            print('Background Color is set to {color}'.format(color=config.tile_bk_color))
        print('Video Information for {}'.format(video))
        success, banner_info = video_info(filename=video)

        if not success:
            return 1

        if config.md5 and not DRYRUN:
            md5value = md5(video)
            banner_info['md5'] = md5value
            if not QUIET:
                print('MD5 calculated as {}'.format(md5value))
        elif config.md5:
            banner_info['md5'] = "13227ada4af540092b7c5821c9ff321a"
            md5value = random_string(stringlength=32)
            banner_info['md5'] = md5value

        banner_info['filename'] = video
        banner_info['basename'] = os.path.basename(video)
        banner_info['dirname'] = os.path.dirname(video)

        if config.part_id and config.studio_id:
            # Change the filename for display
            num_id = [str(i) for i in list(os.path.basename(banner_info['basename'].rsplit('.', 1)[0])) if i.isdigit()]
            banner_info['part_id'] = config.part_id + "".join(num_id)
        else:
            banner_info['part_id'] = None

        output_filename = config.out_dir + "/"

        if config.md5:
            output_filename += str(md5) + "_"

        output_filename += os.path.basename(video).split('.')[0]

        if config.override:
            output_filename = config.out_dir + "/" + config.override

        if banner_info['part_id']:
            output_filename = config.out_dir + "/" + banner_info['part_id']

        if not QUIET and success:
            print('Video Information: {info}'.format(info=banner_info))
        if not QUIET and success:
            print('Output Filename = {output}'.format(output=output_filename))

        # calculate iables
        tile_rows = config.tile_rows
        tile_cols = config.tile_cols
        num_tiles = tile_rows * tile_cols
        tile_width = config.tile_width
        tile_bk_color = config.tile_bk_color
        video_frames = banner_info['video_frames']
        tile_mod = int(int(video_frames) / num_tiles)
        tile_expr = "not(mod(n," + str(tile_mod) + "))"
        tile_layout = str(tile_rows) + "x" + str(tile_cols)

        # Setup Preview Filters
        filter_select = {
            'filter_name': 'select',
            'expr': tile_expr
        }
        filter_scale = {
            'filter_name': 'scale',
            'w': tile_width,
            'h': '-1'

        }
        filter_tile = {'filter_name': 'tile',
                       'layout': tile_layout,
                       'padding': '4',
                       'margin': '4',
                       'color': tile_bk_color
                       }

        input_args = {
            'loglevel': 'panic',
            'hide_banner': None,
            'r': '10'
        }

        if config.hwaccel:
            input_args.update({'hwaccel': HWACCEL[config.hwaccel]})

        # Create first image
        if not DRYRUN:
            try:
                out, err = (
                    ffmpeg
                        .input(video, **input_args)
                        .filter(**filter_select)
                        .filter(**filter_scale)
                        .filter(**filter_tile)
                        .output(output_filename + '.jpg', vframes=1, format='image2', vcodec='mjpeg', threads=1)
                        .overwrite_output()
                        .run(cmd=FFMPEG, capture_stdout=True)
                )
            except Exception as error:
                banner_info['comments'] = error

        else:
            with Image() as blank_img:
                blank_img.blank(2045, 1155, background=config.tile_bk_color)
                blank_img.save(filename=output_filename + '.jpg')

        # Get the size of the image
        with Image(filename=output_filename + '.jpg') as img:
            if DEBUG:
                print(img.size)
            image_width, image_height = img.size
            resize_width = int(round(image_width * 1.05))
            border_width = int((resize_width - image_width) / 2 * - 1)
            resize_height = int(round(image_height * 1.25)) + (3 * int(config.font_size))
            border_height = ((resize_height - image_height) * -1) - border_width

            img.background_color = tile_bk_color
            img.gravity = 'north'
            img.extent(
                width=resize_width,
                height=resize_height,
                x=border_width, y=border_height
            )

            img.save(filename=output_filename + '.tmp.jpg')

        if DEBUG:
            print('Image Border width {0} and height {1}'.format(border_width, border_height))

        # Create Banner Image
        if config.part_id:
            message = "Part Number: {EDGEID}\n".format(EDGEID=banner_info['part_id'])
        else:
            message = ""
        message += """{MP4NAME}
        {video_width} x {video_height} format {ASPECT}
        codec {codec_long_name}
        size {video_size}
        runtime {runtime} framerate {video_frame_rate}
        """.format(MP4NAME=banner_info['basename'],
                   video_height=banner_info['video_height'],
                   video_width=banner_info['video_width'],
                   ASPECT=banner_info['video_aspect'],
                   codec_long_name=banner_info['codec_long_name'],
                   video_size=banner_info['video_size'],
                   runtime=banner_info['video_duration'],
                   video_frame_rate=banner_info['video_frame_rate']

                   )
        if VERBOSE and not QUIET:
            print(message)

        with Drawing() as draw:
            draw.stroke_color = Color(config.tile_fg_color)
            draw.stroke_width = 1
            draw.font = 'helvetica'
            draw.font_size = int(config.font_size)
            draw.text_kerning = 2
            draw.fill_color = Color(config.tile_fg_color)
            with Image(filename=output_filename + '.tmp.jpg') as img:
                draw.draw(img)
                img.annotate(message, draw, 30, int(config.font_size) + 10)
                img.save(filename=output_filename + '.jpg')

        os.remove(output_filename + '.tmp.jpg')

        if VERBOSE and not QUIET:
            im = Display(output_filename + '.jpg')
            im.show()

        myDB.insertORupdate(table='preview', key_field='filename', key_value=video, data=banner_info)
        myDB.commit()
    myDB.close()

    print('End of Program')

    return 0


if __name__ == "__main__":

    if DEBUG:
        myglobals = globals().copy()
        for k, v in myglobals.items():
            print('Key {0} Value {1}'.format(k, v))
    main()
