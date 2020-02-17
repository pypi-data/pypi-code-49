import setuptools

setuptools.setup(
      name="d-snek-cogs-perm",
      version="0.0.3",
      author="Jonathan de Jong",
      author_email="jonathan@automatia.nl",
      description="Discord SNEK Cog; Perm",
      url="https://git.jboi.dev/ShadowJonathan/snek-perm",
      packages=['cogs.perm'],
      classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
      ],
      python_requires=">=3.6",
      install_requires=["d-snek>=1.2.6", "discord.py>=1.2.5", "ruamel.yaml"],
      setup_requires=["wheel"],
      extras_require={
            "dev": ["ipython", "twine", "bump2version"],
      }
)
