import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="spheres", 
    version="0.2.0.1",
    author="Matthew Weiss",
    author_email="heyredhat@gmail.com",
    description="functorial visualization library with support for quantum mechanics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/heyredhat/spheres",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    setup_requires=["numpy", "scipy", "cython"],\
    install_requires=["flask", "python-socketio", "eventlet",\
        "termcolor", "sympy", "numpy", "scipy", "cython", "qutip"],\
    python_requires=">=3",\
    package_data={
        "": ["templates/*",\
             "static/css/*",\
             "static/fonts/*",\
             "static/img/*",\
             "static/models/*",\
             "static/js/spheres/*",\
             "static/js/*.js",\
             "static/js/jquery-ui/*",\
             "static/js/three.js/build/three.min.js",\
             "static/js/three.js/examples/js/controls/DragControls.js",\
             "static/js/three.js/examples/js/controls/TransformControls.js",\
             "static/js/three.js/examples/js/utils/SceneUtils.js",\
             "static/js/three.js/examples/js/controls/OrbitControls.js",\
             "static/js/three.js/examples/js/controls/TrackballControls.js",\
             "static/js/three.js/examples/js/effects/OutlineEffect.js",\
             "static/js/three.js/examples/js/shaders/CopyShader.js",\
             "static/js/three.js/examples/js/shaders/AfterimageShader.js",\
             "static/js/three.js/examples/js/postprocessing/EffectComposer.js",\
             "static/js/three.js/examples/js/postprocessing/RenderPass.js",\
             "static/js/three.js/examples/js/shaders/HalftoneShader.js",\
             "static/js/three.js/examples/js/postprocessing/ShaderPass.js",\
             "static/js/three.js/examples/js/shaders/PixelShader.js",\
             "static/js/three.js/examples/js/postprocessing/AfterImagePass.js",\
             "static/js/three.js/examples/js/postprocessing/OutlinePass.js",\
             "static/js/three.js/examples/js/postprocessing/HalftonePass.js",\
             "static/js/three.js/examples/js/loaders/GLTFLoader.js"]\
    }
)