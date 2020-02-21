import brainrender
brainrender.SHADER_STYLE = 'cartoon'

from brainrender.scene import Scene

from vtkplotter.analysis import surfaceIntersection
import pandas as pd

cells = pd.read_hdf('secrets/CC_134_1_ch1_cells.h5', key='hdf')


color = 'salmon'

show = 'schematic'

# ------------------------------ INJECTION SCENE ----------------------------- #
if show == 'inj':
    scene = Scene(add_root=True)

    scene.add_brain_regions(['SCm'], use_original_color=True, wireframe=False, alpha=.6)

    inj = scene.add_from_file('secrets/CC_134_1_ch1inj.obj')
    inj.color(color).alpha(.9)
    inj.lighting(
            style='plastic',
            ambient=0,
            diffuse=.1,
            specular=0,
            enabled=False)   
    scene.edit_actors(inj, smooth=True)

    inters = surfaceIntersection(scene.actors['regions']['SCm'], inj)
    scene.edit_actors(inters, smooth=True)
    scene.edit_actors(inters, line=True, line_kwargs=dict(lw=10))

    scene.add_vtkactor(inters)


# ------------------------- INJECTION SCHEMATIC SCENE ------------------------ #
if show == 'schematic':
    if brainrender.SHADER_STYLE != 'cartoon':
        raise ValueError('Set cartoon style at imports')
    scene = Scene()

    areas = ['MOs', 'ZI', 'VMH', 'SCm']
    scene.add_brain_regions(areas, use_original_color=True, alpha=1)

    # scene.add_brain_regions(['SCm'], use_original_color=True, alpha=1)



# -------------------------------- CELLS SCENE ------------------------------- #
if show == 'cells':
    areas = ['MOs', 'ZI', 'VMH',]

    scene = Scene()

    scene.add_brain_regions(areas, use_original_color=True, alpha=.1)
    scene.add_cells(cells, color=color, regions=areas)


    scene.add_brain_regions(['SCm'], use_original_color=True, alpha=.2, wireframe=True)

scene.render()
