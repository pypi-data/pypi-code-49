from brainrender.scene import Scene

regions = ['PRT', 'SCm', 'SCs']
for region in regions:
    scene = Scene()
    scene.add_brain_regions([region], colors='white', alpha=0.5)
    scene.render()