import autoarray as aa
import autoastro as aast

import time

# Although we could test_autoarray the image without using an image (e.aast.lp. by just making a grid), we have chosen to
# set this test_autoarray up using an image and mask. This gives run-time numbers that can be easily related to an actual lens
# analysis

shape_2d = (301, 301)
pixel_scales = 0.05
sub_size = 4
radius = 3.0

print("sub grid size = " + str(sub_size))
print("circular mask radius = " + str(radius) + "\n")

mask = aa.mask.circular(
    shape_2d=shape_2d, pixel_scales=pixel_scales, sub_size=sub_size, radius=radius
)

grid = aa.grid.from_mask(mask=mask)

print("Number of grid points = " + str(grid.sub_shape_1d) + "\n")

### EllipticalGaussian ###

light_profile = aast.lp.EllipticalGaussian(
    centre=(0.0, 0.0), axis_ratio=0.8, phi=45.0, sigma=1.0
)

start = time.time()
light_profile.profile_image_from_grid(grid=grid)
diff = time.time() - start
print("EllipticalGaussian time = {}".format(diff))

### SphericalGaussian ###

light_profile = aast.lp.SphericalGaussian(centre=(0.0, 0.0), sigma=1.0)

start = time.time()
light_profile.profile_image_from_grid(grid=grid)
diff = time.time() - start
print("SphericalGaussian time = {}".format(diff))

### EllipticalExponential ###

profile = aast.lp.EllipticalExponential(
    centre=(0.0, 0.0), axis_ratio=0.8, phi=45.0, intensity=1.0, effective_radius=1.0
)

start = time.time()
profile.profile_image_from_grid(grid=grid)
diff = time.time() - start
print("EllipticalExponential time = {}".format(diff))

### SphericalExponential ###

profile = aast.lp.SphericalExponential(
    centre=(0.0, 0.0), intensity=1.0, effective_radius=1.0
)

start = time.time()
profile.profile_image_from_grid(grid=grid)
diff = time.time() - start
print("SphericalExponential time = {}".format(diff))

### EllipticalDevVaucouleurs ###

profile = aast.lp.EllipticalDevVaucouleurs(
    centre=(0.0, 0.0), axis_ratio=0.8, phi=45.0, intensity=1.0, effective_radius=1.0
)

start = time.time()
profile.profile_image_from_grid(grid=grid)
diff = time.time() - start
print("EllipticalDevVaucouleurs time = {}".format(diff))

### SphericalDevVaucouleurs ###

profile = aast.lp.SphericalDevVaucouleurs(
    centre=(0.0, 0.0), intensity=1.0, effective_radius=1.0
)

start = time.time()
profile.profile_image_from_grid(grid=grid)
diff = time.time() - start
print("SphericalDevVaucouleurs time = {}".format(diff))

### EllipticalSersic ###

light_profile = aast.lp.EllipticalSersic(
    centre=(0.0, 0.0),
    axis_ratio=0.8,
    phi=45.0,
    intensity=1.0,
    effective_radius=1.0,
    sersic_index=2.5,
)

start = time.time()
light_profile.profile_image_from_grid(grid=grid)
diff = time.time() - start
print("EllipticalSersic time = {}".format(diff))

### SphericalSersic ###

light_profile = aast.lp.SphericalSersic(
    centre=(0.0, 0.0), intensity=1.0, effective_radius=1.0, sersic_index=2.5
)

start = time.time()
light_profile.profile_image_from_grid(grid=grid)
diff = time.time() - start
print("SphericalSersic time = {}".format(diff))

### EllipticalCoreSersic ###

light_profile = aast.lp.EllipticalCoreSersic(
    centre=(0.0, 0.0),
    axis_ratio=0.8,
    phi=45.0,
    intensity=1.0,
    effective_radius=1.0,
    sersic_index=2.5,
    radius_break=0.01,
    intensity_break=0.05,
    gamma=0.25,
    alpha=3.0,
)

start = time.time()
light_profile.profile_image_from_grid(grid=grid)
diff = time.time() - start
print("EllipticalCoreSersic time = {}".format(diff))

### SphericalCoreSersic ###

light_profile = aast.lp.SphericalCoreSersic(
    centre=(0.0, 0.0),
    intensity=1.0,
    effective_radius=1.0,
    sersic_index=2.5,
    radius_break=0.01,
    intensity_break=0.05,
    gamma=0.25,
    alpha=3.0,
)

start = time.time()
light_profile.profile_image_from_grid(grid=grid)
diff = time.time() - start
print("SphericalCoreSersic time = {}".format(diff))

print()
