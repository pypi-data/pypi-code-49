# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lime_comb',
 'lime_comb.auth',
 'lime_comb.commands',
 'lime_comb.firestore',
 'lime_comb.gpg',
 'lime_comb.logger']

package_data = \
{'': ['*']}

install_requires = \
['appdirs>=1.4.3,<2.0.0',
 'black>=19.10b0,<20.0',
 'email-validator>=1.0.5,<2.0.0',
 'email_validator>=1.0.5,<2.0.0',
 'google-auth-oauthlib>=0.4.1,<0.5.0',
 'google-auth>=1.10.0,<2.0.0',
 'google-cloud-datastore>=1.10.0,<2.0.0',
 'google-cloud-firestore>=1.6.1,<2.0.0',
 'grpcio-gcp>=0.2.2,<0.3.0',
 'mock-firestore>=0.6.0,<0.7.0',
 'mock>=4.0.1,<5.0.0',
 'password_generator>=0.1.0,<0.2.0',
 'pyperclip>=1.7.0,<2.0.0',
 'python-gnupg>=0.4.5,<0.5.0',
 'requests>=2.23.0,<3.0.0',
 'requests_mock>=1.7.0,<2.0.0',
 'requests_oauthlib>=1.3.0,<2.0.0',
 'semver>=2.9.1,<3.0.0',
 'tabulate>=0.8.6,<0.9.0',
 'tqdm>=4.41.1,<5.0.0']

entry_points = \
{'console_scripts': ['lime-comb = lime_comb.main:run']}

setup_kwargs = {
    'name': 'lime-comb',
    'version': '0.0.7',
    'description': 'lime-comb cli',
    'long_description': '# Lime-comb\n\nThis tool allows:\n-   Encrypt messages directly from your terminal.\n-   Upload keys to central registry\n\n## encrypt\n\nExample usage:\n\n```bash\n$lime-comb enc -t ${SOMEONES_EMAIL} -m "db_qa_password: SUPERSECRET1" -m "dq_preprod_password:SUPERSECRET2"\n-----BEGIN PGP MESSAGE-----\n\nhQIMA3u/FP5aHZnFARAAiSoK/MThwKlKd1BCfPYSeU4E8NwtFjZ6wa9cVxmlcApl\nx+SKvoYoRQIA1melOuYO6tjZSJYDLrQL1Q4kI34eTerT1rtIvlmmn14tBaGy5g4F\nQ2F/sRxmFeVrMmaGaNN39S7YpQRExhi+lJkX8Tj7MvNvbQ26IH7++KnTJPKQmSHH\nuCSnl75IzaapPy14YiOPPrHVN52ODowxcESKQ4A1eu2aUr9dZ9HOyx3MhpCXwXo9\ns1OJqD7gVjeX/z98KCjEorLHZoi/j7Zli07W1jcw3l+OZhHizM3FvVDq3ZeKi97Q\nVTQEF2rkPTyuYoxcj3fRzW/4rwAaSsW2kUGBN2AMLNaAQZEA0BenYy+qi00rO29b\nHPCOCOU/iG4Nojiy/jKVdETEzW048lQsUofYuJbxEuESRP6NuMDEucsOHI6c7T7h\nX4hpROO6R8KZyoJ3nLl+5ItVBOvEApka8q7KzSxE9bXtt7MYTu+EmbyEA4PlL1w1\nsItctobsTcJk0UoTkY2kYy7JdGKd0f1vWUCsQcqVDEywQoXJqF4bnFJCZrKnBQEj\ndAN3rZ4U/Oq9rwLyvf3tZGSuJdQUlfu+VFkdH3/dXA3p+QQj6SeukUwxSymo+gPA\n3i2jWRStKRzyy5odsFxGFTQzEbEotX5n5ATaD/znOFZ/3tV1oRbi4sTSCc2IpanS\nawEEfzCR34YgOMwPzqllvTGPAuyef78BGen4DCTTTTt+YEsTUCrmB9ELaSbaGK7d\nwcPIMoILxtlDaSNiU1/EH7cVQSZtJU/wVmw/QKqtQw2nFzLh2e6XY6JWe6jge8/4\nlkWAGydd3NSG3W9E\n=+MK9\n-----END PGP MESSAGE-----\n\n```\n',
    'author': 'Marcin Niemira',
    'author_email': 'marcin.niemira@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
