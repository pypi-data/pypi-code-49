from setuptools import find_packages, setup

setup(
    name='flaskner',
    packages=find_packages(),
    version='1.0.0',
    license='MIT',
    description='Extract entities in given document(doc/pdf) or link with flask and spacy',
    author='Steven CIBAMBO',
    author_email='stevencibambo@gmail.com',
    url='https://github.com/stevencibambo/named-entity-recognition',
    download_url='https://github.com/stevencibambo/named-entity-recognition/archive/v_01.tar.gz',
    keywords=['NER','ENTITY','FLASK','API','SPACY','NLTK','TEXT'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'beautifulsoup4',
        'PyPDF2',
        'textract',
        'werkzeug',
        'spacy',
        'pandas',
        ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers', 
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)