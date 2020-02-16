from autolens.plot import plotters

import numpy as np

# Although we could test_autoarray the deflection angles without using an image (e.al. by just making a grid), we have chosen to
# set this test_autoarray up using an image and mask. This gives run-time numbers that can be easily related to an actual lens
# analysis

sub_size = 2
inner_radius = 0.2
outer_radius = 4.0

print("sub grid size = " + str(sub_size))
print("annular inner mask radius = " + str(inner_radius) + "\n")
print("annular outer mask radius = " + str(outer_radius) + "\n")

for data_resolution in ["hst_up"]:

    print()

    imaging = simulate_util.load_test_imaging(
        data_type="lens_sie__source_smooth",
        data_resolution=data_resolution,
        psf_shape_2d=(3, 3),
    )
    mask = al.mask.circular_annular(
        shape=imaging.shape,
        pixel_scales=imaging.pixel_scales,
        inner_radius=inner_radius,
        outer_radius=outer_radius,
    )
    masked_imaging = al.masked.imaging(imaging=imaging, mask=mask, sub_size=sub_size)

    print("Deflection angle run times for image type " + data_resolution + "\n")
    print("Number of points = " + str(masked_imaging.grid.sub_shape_1d) + "\n")

    interpolator = al.Interpolator.from_mask_grid_and_pixel_scale_interpolation_grids(
        mask=masked_imaging.mask,
        grid=masked_imaging.grid,
        pixel_scale_interpolation_grid=0.05,
    )

    print(
        "Number of interpolation points = "
        + str(interpolator.interp_grid.sub_shape_1d)
        + "\n"
    )

    ### EllipticalIsothermal ###

    mass_profile = al.EllipticalIsothermal(
        centre=(0.0, 0.0), axis_ratio=0.8, phi=45.0, einstein_radius=1.0
    )

    interp_deflections = mass_profile.deflections_from_grid(
        grid=interpolator.interp_grid
    )
    deflections = np.zeros((masked_imaging.grid.sub_shape_1d, 2))
    deflections[:, 0] = interpolator.interpolated_values_from_values(
        values=interp_deflections[:, 0]
    )
    deflections[:, 1] = interpolator.interpolated_values_from_values(
        values=interp_deflections[:, 1]
    )

    true_deflections = mass_profile.deflections_from_grid(grid=masked_imaging.grid)

    true_deflections_y_2d = masked_imaging.grid.array_stored_1d_from_sub_array_1d(
        sub_array_1d=true_deflections[:, 0]
    )
    true_deflections_x_2d = masked_imaging.grid.array_stored_1d_from_sub_array_1d(
        sub_array_1d=true_deflections[:, 1]
    )

    difference_y = deflections[:, 0] - true_deflections[:, 0]
    difference_x = deflections[:, 1] - true_deflections[:, 1]

    print("interpolation y error: ", np.mean(difference_y))
    print("interpolation y uncertainty: ", np.std(difference_y))
    print("interpolation y max error: ", np.max(difference_y))
    print("interpolation x error: ", np.mean(difference_x))
    print("interpolation x uncertainty: ", np.std(difference_x))
    print("interpolation x max error: ", np.max(difference_x))

    difference_y_2d = masked_imaging.grid.array_stored_1d_from_sub_array_1d(
        sub_array_1d=difference_y
    )
    difference_x_2d = masked_imaging.grid.array_stored_1d_from_sub_array_1d(
        sub_array_1d=difference_x
    )

    aplt_array.array(array=true_deflections_y_2d)
    aplt_array.array(array=difference_y_2d)

    aplt_array.array(array=true_deflections_x_2d)
    aplt_array.array(array=difference_x_2d)

    # difference_percent_y = (np.abs(difference_y) / np.abs(true_deflections[:,0]))*100.0
    # difference_percent_x = (np.abs(difference_x) / np.abs(true_deflections[:,1]))*100.0
    #
    # print("interpolation y mean percent difference: ", np.mean(difference_percent_y))
    # print("interpolation y std percent difference: ", np.std(difference_percent_y))
    # print("interpolation y max percent difference: ", np.max(difference_percent_y))
    # print("interpolation x mean percent difference: ", np.mean(difference_percent_x))
    # print("interpolation x std percent difference: ", np.std(difference_percent_x))
    # print("interpolation x mean percent difference: ", np.max(difference_percent_x))
    #
    # difference_percent_y_2d = masked_imaging.grid.scaled_array_2d_with_sub_dimensions_from_sub_array_1d(
    #     sub_array_1d=difference_percent_y)
    # difference_percent_x_2d = masked_imaging.grid.scaled_array_2d_with_sub_dimensions_from_sub_array_1d(
    #     sub_array_1d=difference_percent_x)
    #
    # aplt.array(arrays=difference_percent_y_2d)
    # aplt.array(arrays=difference_percent_x_2d)
