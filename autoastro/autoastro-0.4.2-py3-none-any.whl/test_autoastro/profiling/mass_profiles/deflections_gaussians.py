import autoarray as aa
import autoastro as aast

import time


# Although we could test_autoarray the deflection angles without using an image (e.aast.mp. by just making a grid), we have chosen to
# set this test_autoarray up using an image and mask. This gives run-time numbers that can be easily related to an actual lens
# analysis

shape_2d = (301, 301)
pixel_scales = 0.05
sub_size = 2
radius = 4.0

print("sub grid size = " + str(sub_size))
print("circular mask radius = " + str(radius) + "\n")


mask = aa.mask.circular(
    shape_2d=shape_2d, pixel_scales=pixel_scales, sub_size=sub_size, radius=radius
)

grid = aa.grid.from_mask(mask=mask)

print("Number of points = " + str(grid.sub_shape_1d) + "\n")

### EllipticalGaussian (Integrate) ###

mass_profile = aast.mp.EllipticalGaussian(
    centre=(0.0, 0.0),
    axis_ratio=0.6,
    phi=0.0,
    intensity=1.0,
    sigma=10.0,
    mass_to_light_ratio=1.0,
)

start = time.time()
mass_profile.deflections_from_grid(grid=grid)
diff = time.time() - start
print("EllipticalGaussian time = {}".format(diff))
