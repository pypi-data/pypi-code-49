import os

from setuptools import setup, find_packages
import versioneer

readme = os.path.normpath(os.path.join(__file__, "..", "README.md"))
with open(readme, "r") as fh:
    long_description = fh.read()

# long_description += '\n\n'
# changelog = os.path.normpath(os.path.join(__file__, '..', 'CHANGELOG.md'))
# with open(changelog, 'r') as fh:
#     long_description += fh.read()


setup(
    cmdclass=versioneer.get_cmdclass(),
    name="kabaret.blender_session",
    version=versioneer.get_version(),
    description=(
        "A Kabaret session usable in blender " "to have a Flow view in 3D view tools."
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/kabaretstudio/kabaret.blender_session",
    author='Damien "dee" Coureau',
    author_email="kabaret-dev@googlegroups.com",
    license="LGPLv3+",
    classifiers=[
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        "Development Status :: 3 - Alpha",
        # "Development Status :: 4 - Beta",
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        # 'Topic :: System :: Shells',
        "Intended Audience :: Developers",
        # 'Intended Audience :: End Users/Desktop',
        "Operating System :: OS Independent",
        # "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: "
        "GNU Lesser General Public License v3 or later (LGPLv3+)",
    ],
    keywords="kabaret blender b3d pipeline dataflow workflow",
    install_requires=["kabaret>=2.1.5",],
    python_requires=">=3.7",
    packages=find_packages("src"),
    package_dir={"": "src"},
    package_data={
        "": ["*.css", "*.png", "*.svg", "*.gif"],
        "kabaret.blender_session": ["user_scripts/startup/*.py"],
    },
)
