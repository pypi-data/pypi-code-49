import setuptools

with open("CustomAuth/README.md", "r") as fh:
    README = fh.read()

setuptools.setup(
    name="django-custom-user-models",
    version="0.2.01",
    author="mohammad hosein shamsaei",
    author_email="mh.shamsaei.ms@gmail.com",
    description="A custom user model for django authentication",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/MHolger77/django-auth",
    include_package_data=True,
    install_requires=['jdatetime',
                      'PyJWT',
                      'django_tables2',
                      'django-phonenumber-field',
                      'phonenumbers',
                      'kavenegar',
                      'django-cryptography'],
    packages=setuptools.find_packages(),
    classifiers=[
        'Environment :: Web Environment',
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
    ],
    python_requires='>=3.6',
)

# py setup.py sdist bdist_wheel
# twine upload dist/*
