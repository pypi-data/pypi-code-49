"""Parse through a list of all CONUS HV tiles and generate tiled NLCD TIFF files"""

import os
import sys
import subprocess
from collections import namedtuple
import argparse
import datetime as dt

WKT = 'PROJCS["Albers",GEOGCS["WGS 84",DATUM["WGS_1984",SPHEROID["WGS 84",6378140,298.2569999999957,AUTHORITY["EPSG",' \
      '"7030"]],AUTHORITY["EPSG","6326"]],PRIMEM["Greenwich",0],UNIT["degree",0.0174532925199433],AUTHORITY["EPSG",' \
      '"4326"]],PROJECTION["Albers_Conic_Equal_Area"],PARAMETER["standard_parallel_1",29.5],PARAMETER[' \
      '"standard_parallel_2",45.5],PARAMETER["latitude_of_center",23],PARAMETER["longitude_of_center",-96],' \
      'PARAMETER["false_easting",0],PARAMETER["false_northing",0],UNIT["metre",1,AUTHORITY["EPSG","9001"]]] '

all_hv = [('%03d' % h, '%03d' % v) for h in range(33) for v in range(22)]

GeoExtent = namedtuple('GeoExtent', ['x_min', 'y_max', 'x_max', 'y_min'])

CONUS_EXTENT = GeoExtent(x_min=-2565585,
                         y_min=14805,
                         x_max=2384415,
                         y_max=3314805)


def geospatial_hv(h, v, loc=CONUS_EXTENT):
    """
    Geospatial extent for an H-V tile

    Args:
        h (int): Tile H-value
        v (int): Tile V-value
        loc (GeoExtent): The geographic extent that contains the HV tile grid (default=CONUS_EXTENT)

    Returns:
        GeoExtent: The geographic extent of an individual HV tile

    """

    xmin = loc.x_min + h * 5000 * 30
    xmax = loc.x_min + h * 5000 * 30 + 5000 * 30
    ymax = loc.y_max - v * 5000 * 30
    ymin = loc.y_max - v * 5000 * 30 - 5000 * 30

    return GeoExtent(x_min=xmin, x_max=xmax, y_max=ymax, y_min=ymin)


def run_subset(in_file, out_file, ext):
    """
    Call gdal_translate to clip the input file

    Args:
        in_file (str): The source file that will be clipped
        out_file (str): The destination file
        ext (GeoExtent): The geographic extent of the clipping region

    Returns:
        None

    """
    ulx = ext.x_min
    uly = ext.y_max
    lrx = ext.x_max
    lry = ext.y_min
    wkt = WKT
    src = in_file
    dst = out_file

    run_trans = f"gdal_translate -projwin {ulx} {uly} {lrx} {lry} -of GTiff -eco -a_srs {wkt} " \
                f"-co COMPRESS=DEFLATE {src} {dst}"

    subprocess.call(run_trans, shell=True)

    return None


def main_work(infile, output, overwrite, acquired, prod):
    """
    Parse through a list of HV tiles and generate clipped outputs using gdal_translate

    Args:
        infile (str): Full path to a source raster file
        output (str): Full path to a root output destination
        overwrite (bool): Decide whether or not to overwrite existing files (default is False)
        acquired (str): The acquisition date used in the output filenames
        prod (str): Specify the product type (either NLCD or NLCD_TRAINING)

    Returns:
        None

    """
    if not os.path.exists(output):
        try:
            os.makedirs(output)

        except PermissionError as e:
            print("Error: %s, cannot create output directory %s" % (e, output))

            sys.exit(1)

    for h, v in all_hv:
        print('Working on Tile %s' % h + v)

        tile_extent = geospatial_hv(int(h), int(v))

        tile_id = h + v

        generated = dt.datetime.now().strftime('%Y%m%d')

        out_file = os.path.join(output, f'AUX_CU_{tile_id}_{acquired}_{generated}_V01_{prod}.tif')

        if overwrite is True:
            run_subset(infile, out_file, tile_extent)

        else:
            if not os.path.exists(out_file):
                run_subset(infile, out_file, tile_extent)


def main():
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument("-i", "--infile", type=str, required=True,
                        help="Input file to tile")

    parser.add_argument("-o", "--output", type=str, required=True,
                        help="Full path to a root output directory")

    parser.add_argument("--overwrite", action="store_true",
                        help="Overwrite pre-existing files, default is False (do not overwrite)")

    parser.add_argument("--acquired", metavar="YYYYMMDD", default="20010101",
                        help="The acquisition date used in the output filename")

    parser.add_argument("--prod", choices=['NLCD', 'NLCD_TRAINING'], default='NLCD',
                        help='Specify the product type')

    args = parser.parse_args()

    main_work(**vars(args))


if __name__ == '__main__':
    main()
