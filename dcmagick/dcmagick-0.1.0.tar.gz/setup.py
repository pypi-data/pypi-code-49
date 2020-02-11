# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['dcmagick',
 'dcmagick.common',
 'dcmagick.convert',
 'dcmagick.dump',
 'dcmagick.find']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0',
 'joblib>=0.14.1,<0.15.0',
 'numpy>=1.18.1,<2.0.0',
 'pydicom>=1.4.1,<2.0.0',
 'scikit-image>=0.16.2,<0.17.0',
 'teimpy>=0.1.1,<0.2.0']

entry_points = \
{'console_scripts': ['dcmagick = dcmagick.cli:main']}

setup_kwargs = {
    'name': 'dcmagick',
    'version': '0.1.0',
    'description': 'Python libray for displaying images on terminal',
    'long_description': '# dcmagick\n[![PyPI version](https://badge.fury.io/py/dcmagick.svg)](https://badge.fury.io/py/dcmagick)\n[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/amplify-education/serverless-domain-manager/master/LICENSE)\n[![Build Status](https://travis-ci.org/ar90n/dcmagick.svg?branch=master)](https://travis-ci.org/ar90n/dcmagick)\n\ndcmagick is a cli tool for finding, dumping and converting DICOM images.\nThis is insipired by [DCMTK](https://dicom.offis.de/dcmtk.php.en), [GDCM](https://sourceforge.net/projects/gdcm/) and [imagemagick](https://www.imagemagick.org/).\n\n## Installation\n\n```bash\n$ pypi install dcmagick\n```\n\n## Feature\n\n### Dump\n\nDump DICOM tags and images on terminal via various format.\n\n#### Dump by PRETTYE\n```bash\n$ dcmagick dump --format PRETTY ~/dcms/CT_small.dcm 2> /dev/null\n(0008, 0005) Specific Character Set              CS: \'ISO_IR 100\'\n(0008, 0008) Image Type                          CS: [\'ORIGINAL\', \'PRIMARY\', \'AXIAL\']\n(0008, 0012) Instance Creation Date              DA: \'20040119\'\n(0008, 0013) Instance Creation Time              TM: \'072731\'\n(0008, 0014) Instance Creator UID                UI: 1.3.6.1.4.1.5962.3\n(0008, 0016) SOP Class UID                       UI: CT Image Storage\n(0008, 0018) SOP Instance UID                    UI: 1.3.6.1.4.1.5962.1.1.1.1.1.20040119072730.12322\n(0008, 0020) Study Date                          DA: \'20040119\'\n(0008, 0021) Series Date                         DA: \'19970430\'\n(0008, 0022) Acquisition Date                    DA: \'19970430\'\n(0008, 0023) Content Date                        DA: \'19970430\'\n(0008, 0030) Study Time                          TM: \'072730\'\n(0008, 0031) Series Time                         TM: \'112749\'\n(0008, 0032) Acquisition Time                    TM: \'112936\'\n(0008, 0033) Content Time                        TM: \'113008\'\n(0008, 0050) Accession Number                    SH: \'\'\n(0008, 0060) Modality                            CS: \'CT\'\n...\n```\n\n#### Dump by JSON\n```bash\n$ dcmagick dump --format JSON ~/dcms/CT_small.dcm 2> /dev/null | jq .\n{\n  "0008, 0005": {\n    "vr": "CS",\n    "description": "Specific Character Set",\n    "value": [\n      "ISO_IR 100"\n    ]\n  },\n  "0008, 0008": {\n    "vr": "CS",\n    "description": "Image Type",\n    "value": [\n      "ORIGINAL",\n      "PRIMARY",\n      "AXIAL"\n    ]\n  },\n  "0008, 0012": {\n    "vr": "DA",\n    "description": "Instance Creation Date",\n    "value": "20040119"\n  },\n  "0008, 0013": {\n    "vr": "TM",\n    "description": "Instance Creation Time",\n    "value": "072731"\n  },\n  "0008, 0014": {\n    "vr": "UI",\n    "description": "Instance Creator UID",\n    "value": "1.3.6.1.4.1.5962.3"\n  },\n...\n```\n\n#### Dump by BRAILLE\n```bash\n$ dcmagick dump --format BRAILLE ~/dcms/CT_small.dcm 2> /dev/null\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠌⢆⠕⡌⡢⡑⡐⢌⠢⠑⢌⠪⡪⡪⡪⡪⡪⣪⢪⡪⡪⡪⡪⡪⡪⡪⡪⣪⢪⢪⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡌⡊⢆⢕⢜⡬⣪⣎⣎⢜⢌⠢⡑⢕⢕⢝⢜⢎⢎⢎⢎⢎⢇⢏⢎⢮⢪⢣⡣⡣⡣⡣⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢪⢨⢪⣞⡾⣫⢻⢜⡎⡟⡾⣆⢇⠪⡪⡪⡪⡪⡪⡪⡪⡪⡣⡳⡱⡣⡣⡳⡱⡕⡝⡜⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠢⡱⣸⡽⡳⡹⣜⢜⡕⡕⡝⡎⡯⣳⡕⡌⡪⡪⡪⡣⡫⡪⡣⡣⡇⣇⢗⢕⢝⡜⡜⡜⠌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡢⡑⡵⣝⢎⢧⢫⢎⢮⢺⢸⡪⡺⡸⡪⡻⣆⠪⡘⢜⢜⢜⢼⢸⢜⢎⢎⢮⢪⢣⠣⢃⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢐⠌⡎⣞⢜⢎⡎⡮⡪⡳⡹⣜⢜⢕⢝⢜⢭⡳⡕⢌⠢⡑⡱⡑⡕⢕⢕⢕⢕⢑⠁⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢆⢣⢳⢝⢜⢕⢕⢕⢵⢹⡪⡺⡜⣕⡳⡹⡸⡸⣽⢰⠐⢔⠢⡑⠜⠌⠂⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠢⠢⡃⣗⢝⢕⢝⢎⡇⣏⢮⡺⣪⢳⡱⣕⢽⢸⢜⠼⡕⡅⠕⡨⠨⢈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⡎⡪⡑⣕⢽⡪⡇⡗⣗⢽⡸⡱⡕⡕⣳⢹⢜⢮⢳⡹⡪⣏⢎⡂⡢⠑⠄⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡐⡕⡝⡜⡌⡎⣯⡺⣝⢞⡼⡪⣎⢮⡪⡪⣪⡫⣝⢵⡳⣝⢝⣮⢣⢃⢪⢘⢌⠪⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡘⡜⡜⡜⡜⢔⢕⡷⣝⢮⣳⣽⢽⢹⠱⡙⢎⠞⣞⢮⡳⣝⢮⡳⣕⢇⠣⡑⠜⢔⢑⠅⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢰⢡⢣⠱⡑⢜⢸⠨⢢⢿⣯⣿⢟⠜⡌⢆⢣⢑⢅⢕⠌⡎⡟⡷⣷⣽⠺⡘⢌⢂⠣⡑⡅⢕⢑⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢰⠸⡘⢜⠌⡪⠨⡊⡔⡅⣗⢽⢝⡧⡣⡱⡘⡌⢆⢣⠱⡰⡑⡌⡪⡪⡺⡸⡨⢂⠕⢌⢊⢢⠡⡑⢔⠨⡠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⡀⡆⡣⡑⢅⠕⡡⢪⢨⡪⡪⣪⣺⣪⢷⣝⣎⢆⢪⠢⡱⡑⢅⢣⠢⡃⢎⠢⡑⡕⢕⢱⢑⠜⢌⢢⢡⠱⡡⡑⢌⠢⡑⢄⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⡠⡰⣑⢑⢔⠰⡨⡢⡪⡺⡼⣕⢗⣽⣺⣾⣿⣿⣿⣿⣾⣌⢊⠆⢕⠡⡅⠕⢌⢢⢱⢼⣼⣷⣷⣷⣯⣎⢢⠡⡱⠰⡘⠄⠕⠨⡂⠥⡑⢄⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⢀⢄⢢⢗⡏⡮⡢⡣⡪⡪⡪⡪⣪⢳⢝⡾⣽⣾⢷⣷⣻⣞⡿⡽⣿⣿⣷⣿⣼⣬⣶⣽⣮⣮⣿⢿⡿⣿⢿⣿⣿⣟⢆⠕⢌⢌⢂⠣⡑⢅⠢⠡⡂⡑⢔⠰⡀⡀⠀⠀⠀⠀⠀⠀\n⠢⡑⡝⡜⡪⡯⡪⡺⣝⢜⢎⢞⢜⡜⡮⡫⢣⢑⠕⡌⢝⢻⢿⣯⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣽⣯⣿⢿⠫⡣⠱⡨⡊⢆⢂⢪⠨⠢⡑⢌⠪⡰⠨⡂⡢⢊⠔⡡⠠⡀⠀⠀⠀\n⡑⡌⡌⢎⠪⡣⡱⡹⡜⡜⡜⣜⢜⢜⠰⡡⡑⡌⡪⡐⡅⢕⠍⡫⡞⣿⣿⣿⣯⢿⢽⢽⣽⣾⢟⡯⡻⡘⢔⢑⢌⠪⡰⡘⢔⢑⠔⡅⡃⡊⡢⢃⠎⡊⢆⠪⠢⡱⠨⡊⠔⠅⢕⠠\n⢌⢆⠕⡅⡣⡱⢸⢸⢸⢸⢮⡺⠜⡔⠕⡌⡢⣑⠢⡑⢌⢢⢱⢐⠕⢜⢜⣷⣿⡽⣽⣿⢯⢏⢇⢣⢑⢌⠆⡕⢔⠱⡨⠪⡘⢌⠜⡐⡑⠌⡢⠡⡑⡑⢕⢑⠕⢜⠸⡨⠪⡑⡅⡪\n⢢⠢⢣⢊⠆⢎⢊⢆⠣⡑⡕⡸⡨⡪⡘⡌⡪⡂⡣⡑⡅⢕⠌⡆⡣⡑⢕⠸⢽⡿⣿⢫⠫⡘⢔⢑⠔⢅⠕⢌⠆⢇⠎⡪⢊⢢⢑⠱⡘⡌⠆⡕⢌⢌⠢⢅⢣⢑⢕⢘⢌⢢⢑⢌\n⡊⢎⠪⡢⢩⢊⢢⢑⢅⢕⢅⠎⡔⢕⠸⡨⠢⡣⡑⡕⢜⢔⢱⢨⠢⡣⡑⢕⢑⢝⢕⢑⢕⢑⢅⢣⢑⢅⢣⢑⠕⢅⠇⢎⠪⡘⡌⡪⢂⢎⠪⣘⢐⢅⢕⢡⢱⢨⠢⡑⡅⡕⢜⢐\n⢜⢌⢪⢨⠢⡣⡑⢅⢣⢊⢆⢣⠱⡑⡑⢕⢑⠕⡌⡪⢢⢑⢢⢑⠕⡌⡊⣊⠢⡑⡐⡱⡘⢌⢊⢢⢑⢅⠇⡕⡱⡡⢣⢑⠅⢇⠪⡌⡆⡕⡱⡐⢕⢌⢆⢣⠱⡨⡊⢆⢊⠔⡡⡡\n⡢⡱⡨⢢⠣⡒⢌⠪⡢⢱⢘⠔⡕⢅⢣⠣⡑⡕⢌⠎⡜⢌⢊⢆⢕⢌⠜⡐⢕⢨⠨⠢⡑⢅⢣⠱⡐⡢⠣⡊⢆⢣⢑⠢⡑⢅⢇⠪⡢⢱⢨⠸⡐⡅⢆⢣⢑⢕⢘⢌⠄⡕⢌⢆\n⢢⢱⠸⡰⡑⡅⡣⡑⢌⠢⡡⡃⡪⡨⡂⡣⢑⠜⢌⠎⢌⠢⢑⠐⢅⢢⠡⢣⢱⢱⡹⡨⢌⠢⡑⡅⡣⡑⡕⡑⡅⡣⠡⡡⠨⠢⡡⡃⡊⡢⡑⡅⢇⢕⠱⡡⠣⡪⠸⡐⢅⠊⢆⠕\n⢅⢣⠱⡸⡐⢕⢑⠌⡆⢕⠰⡨⢂⠢⡂⡊⢔⠨⠢⡡⡱⢨⢂⢇⢣⠢⡣⡑⢌⠢⡊⢔⢅⠕⡌⡢⡡⡑⡌⡌⢌⠢⢑⠌⢌⢊⠢⡪⠨⡂⢎⢌⠢⢢⢃⢎⠪⡘⢌⠢⡢⡡⡑⡌\n⡊⢆⢣⠱⡸⡘⢜⠸⡨⢢⠣⡪⢪⢘⢌⢪⠢⡣⢣⠣⡪⠪⡂⢇⠪⡊⢆⢊⠢⡑⢌⢒⠢⡣⡱⢨⠪⡨⢢⢊⢢⢑⠔⢌⠢⡂⢕⠨⡌⣊⢢⠡⡣⠱⡘⢔⢕⠱⡑⡕⢜⠔⢕⠱\n⢸⢨⢢⠣⡪⡨⡢⢣⠪⡢⡣⡑⡅⡣⢪⢂⢇⠕⢅⠣⡪⢊⠪⡨⠊⠌⡂⠅⢅⢊⠐⢌⢊⠢⡑⢅⠣⡊⢎⠜⡌⢆⢍⠎⡊⣊⠪⠪⡘⢔⠅⡇⡣⢍⢎⠪⡢⢣⢱⠸⡰⡩⡊⢎\n⡑⡅⡣⡱⠸⡐⠕⢅⠣⣊⢢⢑⠕⢜⢔⠱⡐⠅⡃⡑⠌⡂⡑⠄⠅⠕⡨⠨⢂⠢⠡⡑⡐⡐⠄⢅⠣⡑⡑⢕⠸⡐⢕⢸⠨⡢⡹⡘⡌⢆⢣⠱⡘⡔⢅⢣⢑⢱⠨⣊⢢⠱⡘⡌\n⠸⡐⢕⠸⡘⡌⡣⢃⠣⡊⢌⠢⢑⠡⢂⢑⠌⠌⠢⠨⠨⡐⠨⠨⡈⡂⠢⠡⡑⠌⡊⡐⡐⠌⠌⠢⠨⡐⠨⡠⡑⠌⡌⢆⠣⡱⢨⠢⡣⢱⠡⡣⢱⢘⠜⡔⡱⢡⠣⡢⢣⠱⡡⠣\n⠡⢃⠅⠅⢅⢂⢊⠔⡁⡂⠅⢌⢂⠅⡢⢂⠊⠌⠌⢌⠌⡂⡑⡡⠨⠂⠅⠕⡐⠅⡢⢁⠊⠌⢌⠌⠢⠨⠨⠐⢄⠑⢄⠑⢌⢐⠡⠑⠌⡊⢌⠊⢆⠣⠱⡘⢌⢊⠪⡨⠢⡃⠕⡉\n⢈⠢⡈⡊⠔⡐⡐⡨⢐⠨⡈⠢⡐⠨⠐⠄⠅⡃⠅⢅⢂⠢⢂⠢⠡⠡⡡⢑⠨⠨⡐⠄⠕⠡⡁⡊⠌⡊⠌⢌⢂⢑⢐⠡⢂⢂⢊⠌⢌⢂⠢⢑⢐⠡⠑⢄⢑⠄⠕⡠⠑⢄⢑⢐\n⢐⢁⢂⠢⠡⢂⢂⢂⠢⠡⡈⠢⠨⠨⠨⠊⠌⢄⢑⢐⠄⠕⡐⠡⠡⡑⠄⢕⠨⢊⢐⠅⠅⠕⡐⡐⡡⠨⡨⢂⢂⠢⢂⢑⢐⠔⡐⢌⠐⢄⢑⢐⠔⠡⠡⠡⢂⠊⠔⡨⢈⠢⡁⠢\n```\n\n#### Dump by HALFBLOCK\n```bash\n$ dcmagick dump --format HALFBLOCK ~/dcms/CT_small.dcm 2> /dev/null\n```\n![Dump by HALFBLOCK](https://github.com/ar90n/dcmagick/blob/doc/images/sc_halfblock.png)\n\n#### Dump by ITERM2\n```bash\n$ dcmagick dump --format ITERM2 ~/dcms/CT_small.dcm 2> /dev/null\n```\n![Dump by ITERM2](https://github.com/ar90n/dcmagick/blob/doc/images/sc_iterm2.png)\n\n### Find\n\nFind DICOM images by MongpDB like query to its tags.\n\n```bash\n$ dcmagick find --query \'{"Modality": "MR"}\' --name \'*.dcm\' ~/dcms/ 2> /dev/null\n/home/argon/dcms/MR_small_bigendian.dcm\n/home/argon/dcms/emri_small_jpeg_2k_lossless.dcm\n/home/argon/dcms/MR_small_RLE.dcm\n/home/argon/dcms/emri_small.dcm\n/home/argon/dcms/emri_small_big_endian.dcm\n/home/argon/dcms/MR_small_jp2klossless.dcm\n/home/argon/dcms/MR_small_implicit.dcm\n/home/argon/dcms/MR_small_expb.dcm\n/home/argon/dcms/emri_small_jpeg_ls_lossless.dcm\n/home/argon/dcms/MR_small.dcm\n/home/argon/dcms/MR_truncated.dcm\n/home/argon/dcms/emri_small_RLE.dcm\n/home/argon/dcms/MR_small_jpeg_ls_lossless.dcm\n```\n\n### Convert\n\nConvert DICOM images into PNG or JPEG, and vice versa.\n\n#### DICOM to PNG.\n```bash\n$ dcmagick convert ~/dcms/CT_small.dcm ~/out.png 2> /dev/null\n$ file out.png\n/home/argon/out.png: PNG image data, 128 x 128, 8-bit grayscale, non-interlaced\n```\n\n#### PNG to DICOM.\n```bash\n$ dcmagick convert ~/out.png ~/out.dcm 2> /dev/null\n$ file out.dcm\n/home/argon/out.dcm: DICOM medical imaging data\n```\n\n## License\nThis software is released under the MIT License, see [LICENSE](LICENSE).\n',
    'author': 'Masahiro Wada',
    'author_email': 'argon.argon.argon@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ar90n/dcmagick',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
