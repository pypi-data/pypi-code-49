import setuptools as st
import ohppipeline
packages = st.find_packages()
with open("./requirements.txt","r") as f :
    requirements = f.read().splitlines()


st.setup(
        name     = ohppipeline.__name__,
        version  = ohppipeline.__version__,
        install_requires=requirements,
        packages = packages,
        author   = ohppipeline.__author__,
        )
