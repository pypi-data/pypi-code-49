def struc_generator(bulk, miller_index, layers, vacuum, supercell, adsorbates, sites, locations):

    # explanation of the parameters
    # --- bulk: (bulk object) the bulk that we want to cut surface from, e.g. Rh_bulk
    # --- miller_index: (tuple) what surfaces that we want to cut, e.g. (1, 1, 1)
    # --- layers: (integer) how many layers that we want, e.g. 8 (for pymatgen)
    # --- vacuum: (real) the length of vacuum slab that you want to add, e.g. 18.0
    # --- supercell: (tuple) how large the supercell is, e.g. (3, 3, 1)
    # --- adsorbates: (list of strings) different adsorbate that we want to add, e,g, (['OH'], ['H'], ['O'])
    # --- sites: (list of strings) differnet sites that we want to use, e.g. (['ontop', 'bridge', 'hollow'])
    # --- locations: (dictionary) the locations & offsets that we want to put the adosrbates on,
        #     e.g.
        # locations = {
        #              'OH': {
        #                     'ontop':{
        #                              'height': 2.0
        #                              'offsets': [(1, 1), (1, 2)]
        #                     }
        #                     'bridge':{
        #
        #                     }
        #              }
        #              'O': {
        #
        #              }
        # }

        #-- transfer the Atoms object bulk to pymatgen object and change it to conventional cell
    bulk_pmg = AseAtomsAdaptor.get_structure(bulk)
    bulk_pmg = SpacegroupAnalyzer(bulk_pmg).get_conventional_standard_structure()

    #-- create miller_index surfaces (return a list of surfaces)
    slab_gen = SlabGenerator(bulk_pmg,
                             miller_index,
                             min_slab_size = layers,
                             min_vacuum_size = vacuum,
                             center_slab = False)

    #-- get the slab that we created
    slab = slab_gen.get_slabs()[0]

    #-- change the pymatgen object to ase Atoms object in order to get the basis vector for adding adsorbate
    slab_ase = AseAtomsAdaptor.get_atoms(slab)
    v1 = slab_ase.get_cell()[0] # get first basis vector
    v2 = slab_ase.get_cell()[1] # get second basis vector

    height = np.max(slab_ase.get_positions()[:, 2])

    #-- create supercell
    slab_sc = slab * supercell
    slab_pure_sc = slab_sc # pure surface without any adsorbates

    # unit cell vector of slab_pure_sc
    slab_pure_sc_ase = AseAtomsAdaptor.get_atoms(slab_pure_sc)
    v1_sc = slab_pure_sc_ase.get_cell()[0]
    v2_sc = slab_pure_sc_ase.get_cell()[1]

    #-- find adsorption site
    asf_slab_sc = AdsorbateSiteFinder(slab_sc)
    adsSites_slab_sc = asf_slab_sc.find_adsorption_sites() # return to a dictionary, e.g. adsSites_slab_sc['ontop']

    slab_sc_ase = AseAtomsAdaptor.get_atoms(slab_sc)

    # if there are more than one site in keyword "hollow", then we should return several structures
    slab_sc_ase_assemble = []

    # add adsorbates
    for adsorbate in adsorbates:
        # create ase Atoms object
        mol_ads_ase = molecule(adsorbate)

        # add it to the slab_sc
        for site in sites:

            adsSite_assemble = adsSites_slab_sc[site]

            for item, adsorption_site in enumerate(adsSite_assemble):

                # We have to use deepcopy() because slab_sc_ase is an object, not a number
                slab_sc_ase = copy.deepcopy(slab_pure_sc_ase) # return to clean surface

                offsets = locations[adsorbate][site]['offsets'] # find other offsets of adsorbates, useful in constructing water double layer
                for offset in offsets:

                    # get the x, y, z of the adsorbate
                    adsSite_x = adsorption_site[0] + offset[0]*v1[0] + offset[1]*v2[0]
                    adsSite_y = adsorption_site[1] + offset[0]*v1[1] + offset[1]*v2[1]
                    adsSite_z = adsorption_site[2] + locations[adsorbate][site]['height']

                    # check whether adsSite_x, adsSite_y is out of the supercell, if it is out, then translate
                    if adsSite_x > v1_sc[0]:
                        adsSite_x -= v1_sc[0]
                        adsSite_y -= v1_sc[1]
                    if adsSite_y > v1_sc[1]:
                        adsSite_x -= v1_sc[0]
                        adsSite_y -= v1_sc[1]
                    if adsSite_x > v2_sc[0]:
                        adsSite_x -= v2_sc[0]
                        adsSite_y -= v2_sc[1]
                    if adsSite_y > v2_sc[1]:
                        adsSite_x -= v2_sc[0]
                        adsSite_y -= v2_sc[1]

                    if adsSite_x < 0:
                        adsSite_x += v1_sc[0]
                        adsSite_y += v1_sc[1]
                    if adsSite_y < 0:
                        adsSite_x += v1_sc[0]
                        adsSite_y += v1_sc[1]
                    if adsSite_x < 0:
                        adsSite_x += v2_sc[0]
                        adsSite_y += v2_sc[1]
                    if adsSite_y < 0:
                        adsSite_x += v2_sc[0]
                        adsSite_y += v2_sc[1]

                    # add adsorbate into the slab
                    add_adsorbate(slab = slab_sc_ase,
                                  adsorbate = mol_ads_ase,
                                  height = adsSite_z - height,
                                  position = (adsSite_x, adsSite_y),
                                  mol_index = 0
                                 )

                slab_sc_ase_assemble.append(slab_sc_ase)

    # change the pymatgen object to ase object

    return slab_pure_sc_ase, slab_sc_ase_assemble

def setconstraint(slab, supercell, fixed_layers):
    # get the highest value of z-component
    number = fixed_layers * supercell[0] * supercell[1] - 1
    height_fix = np.sort(slab.get_positions()[:, 2])[number]

    # set constraints, and fix atoms
    c = FixAtoms([atom.index for atom in slab if atom.position[2] <= height_fix])
    slab.set_constraint(c)

    # return slab
    return slab
