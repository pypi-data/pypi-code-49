# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['thunagen']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=7.0.0,<8.0.0',
 'google-cloud-pubsub>=1.1.0,<2.0.0',
 'google-cloud-storage>=1.24.1,<2.0.0',
 'importlib_metadata>=1.3.0,<2.0.0',
 'lazy_object_proxy>=1.4.3,<2.0.0',
 'logbook>=1.5.3,<2.0.0',
 'python-dotenv>=0.10.3,<0.11.0',
 'single-version>=1.1,<2.0']

setup_kwargs = {
    'name': 'thunagen',
    'version': '0.3.6',
    'description': 'Google Cloud function to generate thumbnail for images in Google Storage.',
    'long_description': '========\nThunagen\n========\n\n\n.. image:: https://madewithlove.now.sh/vn?heart=true&colorA=%23ffcd00&colorB=%23da251d\n.. image:: https://badge.fury.io/py/thunagen.svg\n   :target: https://pypi.org/project/thunagen/\n\n\nGoogle Cloud function to generate thumbnail for images in Google Storage.\n\nConvention\n----------\n\nThe thumbnails are placed in a folder "thumbnails" at the same place as original file.\n\nThe thumbnail size is appended to filename, right before the extention part. For example:\n\n\n.. code-block::\n\n    bucket/\n    └── folder/\n        ├── photo.jpg\n        └── thumbnails/\n            ├── photo_128x128.jpg\n            └── photo_512x512.jpg\n        ├── photo-missing-extension\n        └── thumbnails/\n            ├── photo-missing-extension_128x128\n            └── photo-missing-extension_512x512\n\n\nThe function expects these environment variables to be set:\n\n- ``THUMB_SIZES``: Size of thumbnails to be generated. Example: ``512x512,128x128``.\n\n- ``MONITORED_PATHS``: Folders (and theirs children) where the function will process the uploaded images. Muliple paths are separated by ":", like ``user-docs:user-profiles``. If you want to monitor all over the bucket, set it as ``/``.\n\n- ``NOTIFY_THUMBNAIL_GENERATED`` (optional): Tell Thunagen to notify after thumbnails are created.\n\nThe variables can be passed via *.env* file in the working directory.\n\nGet notified when thumbnails are generated\n------------------------------------------\n\nOther applications may want to be informed when the thumbnails are created. We support this by leveraging Google Cloud Pub/Sub service.\n\nAfter finishing generating thumbnail, if the ``NOTIFY_THUMBNAIL_GENERATED`` environment variable is set (with non-empty value), the function will publish a message to Pub/Sub. The message is sent to topic ``thumbnail-generated/{bucket_name}/{image_path}``, with the content being JSON string of thumbnail info (size and path). Example:\n\n- Topic: ``thumbnail-generated%2Fbucket%2Ffolder%2Fphoto.jpg`` (URL-encoded of "thumbnail-generated/bucket/folder/photo.jpg")\n\n- Message:\n\n    .. code-block:: json\n\n        {\n            "128x128": "folder/thumbnails/photo_128x128.jpg",\n            "512x512": "folder/thumbnails/photo_512x512.jpg"\n        }\n\nOther applications can subscribe to that topic to get notified. Google doesnot allow slash ("/") in topic name, so subscribed applications have to take care of URL-encode, decode the topic.\n\n\nWhy Thunagen\n------------\n\nI\'m aware that there is already a `Firebase extension <https://firebase.google.com/products/extensions/storage-resize-images>`_ for the same purpose.\nBut that extension, when doing its job, need to create a temporary file and in many cases, falling into race condition when the temporary file is deleted by another execution of the same cloud function. Thunagen, on the other hand, generates the file and uploads (back to Storage) on-the-fly (in memory), so it doesn\'t get into that issue.\n\n\nInstallation\n------------\n\nThunagen is distributed via PyPI. You can install it with ``pip``::\n\n    pip install thunagen\n\n\nInclude to your project\n-----------------------\n\nThunagen is provided without a *main.py* file, for you to incorporate more easily to your project, where you may have your own way to configure deployment environment (different bucket for "staging" and "production", for example).\n\nTo include Thunagen, from your *main.py*, do:\n\n.. code-block:: py\n\n    from thunagen.functions import generate_gs_thumbnail\n\n\nCredit\n------\n\nThunagen is brought to you by `Nguyễn Hồng Quân <https://github.com/hongquan>`_, from SunshineTech (Việt Nam).\n',
    'author': 'Nguyễn Hồng Quân',
    'author_email': 'ng.hong.quan@gmail.com',
    'maintainer': 'Nguyễn Hồng Quân',
    'maintainer_email': 'ng.hong.quan@gmail.com',
    'url': 'https://github.com/sunshine-tech/thunagen.git',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
