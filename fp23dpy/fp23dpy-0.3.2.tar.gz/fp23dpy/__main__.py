"""
Main script for 3D reconstruction of Fringe Pattern images
"""
import argparse
import numpy as np
import os
import os.path as osp
from skimage import io
try:
    from tqdm import tqdm
except:
    # If tqdm is not available use for each loops instead
    tqdm = lambda x: x

from . import Calibration
from . import Roi
from . import fp23d 
from . import export3D 
from .export import max_vertices
from . import helpers as h


def main():
    ### Quick fix of calibration ###
    import sys
    if 'calibrate' in sys.argv:
        sys.argv.remove('calibrate')
        from .__calibrate_main__ import calibration_main; calibration_main();
        exit()


    parser = argparse.ArgumentParser(description='3D reconstruct images with Fringe Patterns')
    parser.add_argument('files', type=str, nargs='+',
                        help='Input image files to reconstruct, files with prefix "reconstructed" and "segmented" will not be considered')
    parser.add_argument('--output', '-o', type=str,
                        help='Output file for the reconstructed 3D files, default is the same as the first input file')
    parser.add_argument('--prefix', type=str, default='reconstructed_',
                        help='Prefix of the reconstructed 3D files, default is "reconstructed_"')
    parser.add_argument('--ext', type=str, default='glb',
                        help='Output 3D file format, default is GL transmission format .glb')
    # parser.add_argument('--ransac', action='store_true',
    #                     help='Use ransac to estimate a quadratic background carrier (currently not implemented).')
    parser.add_argument('--negative_theta', action='store_true',
                        help='If the camera is above or to the right of the projector this option should be used or a negative theta should be set in calibration file.')
    parser.add_argument('--same', action='store_true',
                        help='Do not crop the output results.')
    parser.add_argument('--with-texture', action='store_true',
                        help='Search for a texture file for output reconstruction with prefix "texture_" to file name.')
    parser.add_argument('--print-image', action='store_true',
                        help='Print the reconstruction as an image filed scaled for simple visualisation of the result, the pixel values will only correspond to relative reconstruction.')
    parser.add_argument('--print-ascii', action='store_true',
                        help='Print the reconstruction as an ascii csv text file for later import into python, this file might be very large.')
    parser.add_argument('--print-roi', action='store_true',
                        help='Print the rectangle of interest used for the output images.')
    parser.add_argument('--roi-file', type=str, default='roi.txt',
                        help='The name for the roi file, default is "roi.txt"')
    parser.add_argument('--out-3D-size', type=float, default=None,
                        help='If scaling parameter is not used this is used to set half the size of the 3D structure')
    parser.add_argument('--max-vertices', type=int, default=max_vertices,
                        help='If scaling parameter is not used this is used to set half the size of the 3D structure')
    parser.add_argument('--threed-align', action='store_true',
                        help='Attempt to do an aligment of the third dimension for multiple reconstructions')
    args = parser.parse_args()
    method_args = ['negative_theta', 'same']
    d_args = {key: vars(args)[key] for key in method_args}

    output_image_type = np.uint8

    ###### Manipulating input files ######
    to_reconstruct = args.files
    if osp.isdir(to_reconstruct[0]):
        input_dir = to_reconstruct[0]
        to_reconstruct = [f for f in os.listdir(input_dir) if h.is_image_file(f)]
    else:
        input_dir = osp.dirname(to_reconstruct[0])

    if len(to_reconstruct) > 0:
        to_reconstruct = [f for f in to_reconstruct if not 'calibrat' in f and not 'segment' in f and not 'reconstruct' in f]
    if len(to_reconstruct) == 0:
        print("No images found to reconstruct")
        exit()
    to_reconstruct = sorted(to_reconstruct)

    global_calibration = None
    global_calibration_file = osp.join(input_dir, 'calibration.txt')
    if osp.isfile(global_calibration_file):
        global_calibration = Calibration.read(global_calibration_file)

    global_mask = None
    global_roi = Roi()
    global_segmentation_file_png = osp.join(input_dir, 'segmentation.png')
    global_segmentation_file_tif = osp.join(input_dir, 'segmentation.tif')
    if osp.isfile(global_segmentation_file_png):
        segmented = io.imread(global_segmentation_file_png, as_gray=True)
        global_mask = segmented == 0
        global_roi = Roi.find_from_mask(global_mask)
    elif osp.isfile(global_segmentation_file_tif):
        segmented = io.imread(global_segmentation_file_tif, as_gray=True)
        global_mask = segmented == 0
        global_roi = Roi.find_from_mask(global_mask)

    max_roi = Roi()

    ###### Demodulation of files ######
    reconstructed = []
    for input_file in tqdm(to_reconstruct, disable=len(to_reconstruct) == 1):
        input_dir, input_filename = osp.split(input_file)
        input_filename_base, _ = osp.splitext(input_filename)
        if not osp.isfile(input_file):
            print("Warning: File {} not found".format(input_file))
            continue

        signal = io.imread(input_file, as_gray=True)

        local_calibration_file = osp.join(input_dir, 'calibration_' + input_filename_base + '.txt')
        if osp.isfile(local_calibration_file):
            calibration = Calibration.read(local_calibration_file)
        elif not global_calibration is None:
            calibration = global_calibration
        else:
            print("Warning: No calibration file found, using automatic calibration algorithm") 
            calibration = Calibration.calibrate(signal)
            print(calibration)

        local_segmentation_file = osp.join(input_dir, 'segmented_' + input_filename)
        if osp.isfile(local_segmentation_file):
            segmented = io.imread(local_segmentation_file, as_gray=True)
            mask = segmented == 0
            signal = np.ma.array(signal, mask=mask, fill_value=0)
            roi = Roi.find_from_mask(mask)
        elif not global_mask is None:
            signal = np.ma.array(signal, mask=global_mask, fill_value=0)
            roi = global_roi
        else:
            roi = Roi.full(signal.shape)
        if args.same:
            roi = Roi.full(signal.shape)

        texture_file = osp.join(input_dir, input_filename_base + '_texture.png')
        texture = None
        if args.with_texture and osp.isfile(texture_file):
            texture = io.imread(texture_file)
            texture = roi.apply(texture)


        grid3d = fp23d(signal, calibration, **d_args)
        reconstructed += [{'filename': input_file, 'name': '{}{}'.format(args.prefix, input_filename_base), 'grid': grid3d, 'texture': texture, 'calibration': calibration, 'roi': roi}]

        if max_roi.empty() or list(signal.shape) == max_roi.full_shape():
            max_roi.maximize(roi)

        # plt.subplot(121)
        # plt.imshow(signal)
        # plt.subplot(122)
        # plt.imshow(threeD)
        # plt.show()


    ###### Post processing of 3D files ######
    if len(reconstructed) == 0:
        print("No files were reconstructed")
        exit()
    if len(to_reconstruct) > 1:
        print('Working on 3D files')

    if args.print_roi:
        max_roi.write(osp.join(input_dir, args.roi_file))
    roi = reconstructed[0]['roi'].copy()
    roi.rebase(max_roi)

    base_grid = roi.unapply(reconstructed[0]['grid'])
    for reconstruction in reconstructed:  # (input_file, grid3d, texture, calibration, roi) in tqdm(reconstructed):
        input_dir = osp.dirname(reconstruction['filename'])
        output_dir = input_dir if args.output is None else osp.dirname(args.output)
        # input_filename_base = osp.splitext(reconstruction['name'])[0]

        if args.threed_align and roi.full_shape() == max_roi.full_shape():
            roi.rebase(max_roi)
            reconstruction['grid'] = roi.unapply(reconstruction['grid'])
            diff = reconstruction['grid'][2] - base_grid[2]
            l = np.median(np.ma.compressed(diff))
            reconstruction['grid'] -= l
            base_grid = reconstruction['grid']

        grid3d = reconstruction['grid'].copy()
        np.ma.set_fill_value(grid3d, 0)
        if np.ma.isMaskedArray(grid3d):
            grid3d.data[grid3d.mask] = np.nan

        if args.print_ascii:
            ascii_array = grid3d.reshape((grid3d.shape[1] * 3, grid3d.shape[2]))
            np.savetxt(osp.join(output_dir, '{}.csv'.format(reconstruction['name'])), ascii_array, fmt='%.3e')

        if args.print_image:
            threeD = h.image_scaled(np.ma.filled(grid3d[2]), (0, np.iinfo(output_image_type).max))
            output_file = osp.join(output_dir, '{}.png'.format(reconstruction['name']))
            io.imsave(output_file, threeD.astype(output_image_type))

    if args.output is None:
        input_dir = osp.dirname(reconstructed[0]['filename'])
        output_file = osp.join(input_dir, '{}.{}'.format(reconstructed[0]['name'], args.ext))
    elif osp.isdir(args.output):
        output_file = osp.join(args.output, '{}.{}'.format(reconstructed[0]['name'], args.ext))
    else:
        output_file = args.output

    # Export 3D to a single file
    export3D(output_file, reconstructed, args.out_3D_size, args.max_vertices, args.prefix)

if __name__ == '__main__':
    main()
