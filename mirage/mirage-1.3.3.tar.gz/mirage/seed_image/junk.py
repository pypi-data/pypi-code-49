
yd, xd = self.output_dims
galimage = np.zeros((yd, xd))
segmentation = segmap.SegMap()
        segmentation.xdim = xd
        segmentation.ydim = yd
        segmentation.initialize_map()
for source in blah:
    galdims = stamp.shape
            psf_image = self.create_psf_stamp(entry['pixelx'], entry['pixely'], (galdims[1], galdims[0]), 1)

            xpts, ypts, (i1, i2), (j1, j2), (k1, k2), (l1, l2) = self.create_psf_stamp_coords(entry['pixelx'],
                                                                                              entry['pixely'],
                                                                                              (galdims[1],
                                                                                               galdims[0]))
            stamp = s1.fftconvolve(stamp, psf_image, mode='same')

























        psfimage = np.zeros(self.output_dims)

        for source in point_sources:
        # PTSRC CODE FOR COMPARISON -- REMOVE WHEN DONE
            xpos_aperture = entry['pixelx'] + self.coord_adjust['xoffset']
            ypos_aperture = entry['pixely'] + self.coord_adjust['yoffset']
            xpos_fullframe = entry['pixelx'] + self.subarray_bounds[0]
            ypos_fullframe = entry['pixely'] + self.subarray_bounds[1]
            #nx = math.floor(xpos)
            #ny = math.floor(ypos)

            # Desired counts per second in the point source
            counts = entry['countrate_e/s']  # / self.frametime

            # Load PSF from the appropriate file given the source location
            # Remember that this source location should be in the coordinate
            # system of the aperture being simulated, and not include any padding
            # for WFSS seed images.

            # UPDATED FOR NEW PSF LIBRARY---------------------------------

            # Separate the coordinates of the PSF into rounded integer and fractional pixels.
            # Work in full frame coordinates. Adjust if simulating a subarray.
            #subpix_x, integx = np.modf(entry['pixelx'] + self.subarray_bounds[0])
            #subpix_y, integy = np.modf(entry['pixely'] + self.subarray_bounds[1])

            # Interpolate the oversampled PSF to the nearest whole pixel
            # This creates a 2d interpolated PSF
            print("CLEAN UP HERE")
            #psf_integer_interp = self.psf_library.position_interpolation(integx, integy, method='idw')

            # FOR USE WITH OLD PSF LIBRARY---------------------------------
            # psf_obj = PSF(entry['pixelx'], entry['pixely'], self.psfname,
            #              interval=self.params['simSignals']['psfpixfrac'], oversampling=1)

            # Calculate the coordinate limits of the aperture/PSF stamp overlap
            # psf_ydim, psf_xdim = psf_obj.model.shape
            #psf_xdim, psf_ydim = (self.psf_library_x_dim, self.psf_library_y_dim)
            (i1, i2, j1, j2, k1, k2, l1, l2) = self.cropped_coords(xpos_aperture, ypos_aperture,
                                                                   self.psf_library_x_dim,
                                                                   self.psf_library_y_dim,
                                                                   self.output_dims[1], self.output_dims[0])
            (i1_ff, i2_ff, j1_ff, j2_ff, k1_ff, k2_ff, l1_ff, l2_ff) = self.cropped_coords(xpos_fullframe, ypos_fullframe,
                                                                                           self.psf_library_x_dim,
                                                                                           self.psf_library_y_dim,
                                                                                           self.ffsize, self.ffsize)

            #try:
            if 1>0:
                ypts, xpts = np.mgrid[j1:j2, i1:i2]
                ypts_ff, xpts_ff = np.mgrid[j1_ff:j2_ff, i1_ff:i2_ff]

                # FOR USE WITH OLD PSF LIBRARY
                # scaled_psf = psf_obj.model.evaluate(x=xpts, y=ypts, flux=counts, x_0=nx, y_0=ny)

                # FOR USE WITH NEW PSF LIBRARY
                scaled_psf = self.psf_library.evaluate(x=xpts_ff, y=ypts_ff, flux=counts, x_0=xpos_fullframe,
                                                       y_0=xpos_fullframe)
                #scaled_psf = psf_integer_interp.evaluate(x=xpts, y=ypts, flux=counts, x_0=xpos, y_0=ypos)
                psfimage[ypts, xpts] += scaled_psf
        # PTSRC CODE FOR COMPARISON -- REMOVE WHEN DONE