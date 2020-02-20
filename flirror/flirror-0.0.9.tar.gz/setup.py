# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['flirror', 'flirror.crawler']

package_data = \
{'': ['*'],
 'flirror': ['static/*',
             'static/css/*',
             'static/font/*',
             'static/scss/*',
             'templates/*',
             'templates/modules/*']}

install_requires = \
['Flask-Assets>=2.0,<3.0',
 'Pillow>=7.0.0,<8.0.0',
 'alpha_vantage>=2.1.3,<3.0.0',
 'arrow>=0.15.5,<0.16.0',
 'click>=7.0,<8.0',
 'feedparser>=5.2.1,<6.0.0',
 'flask>=1.1.1,<2.0.0',
 'google-api-python-client>=1.7.11,<2.0.0',
 'google-auth-httplib2>=0.0.3,<0.0.4',
 'google-auth-oauthlib>=0.4.1,<0.5.0',
 'pony>=0.7.11,<0.8.0',
 'pyScss>=1.3.5,<2.0.0',
 'pyowm>=2.10.0,<3.0.0',
 'qrcode>=6.1,<7.0',
 'schedule>=0.6.0,<0.7.0']

entry_points = \
{'console_scripts': ['flirror-crawler = flirror.crawler.main:main']}

setup_kwargs = {
    'name': 'flirror',
    'version': '0.0.9',
    'description': 'A smartmirror based on Flask',
    'long_description': "# Flirror - A smartmirror based on Flask\n\n\n# Deploy flirror on a Raspberry Pi\n\n## Requirements\n- [Docker](https://www.docker.com/)\n- [docker-compose](https://docs.docker.com/compose/)\n\n### Install docker\nTo install docker on raspbian OS, you can simply run the following command:\n\n```\n$ curl -sSL https://get.docker.com | sh\n```\n\nThis will download the installation script and directly execute it via shell.\nRunning the script may take some time. Afterwards, you might want to add your\nuser (pi) to the docker group, so you can run docker without sudo:\n\n```\n$ sudo usermod -aG docker pi\n```\n\nAfterwards log out and back or reboot the Raspberry Pi via\n\n```\n$ sudo reboot -h\n```\n\n### Install docker-compose\nThere are various ways to install docker-compose. Please see the\n[docker-compose installation guide](https://docs.docker.com/compose/install/)\nfor more detailed information.\n\nI personally installed docker-compose via\n[pipx](https://pipxproject.github.io/pipx/). Using this variant requires\nthe `python-dev` and `libffi-dev` packages to be installed on the system.\n\n```\n$ sudo apt install python-dev libffi-dev\n$ python3 -m pip install --user pipx\n$ python3 -m pipx ensurepath\n$ pipx install docker-compose\n```\n\n## Start flirror\n\nBoth components, `flirror-web` and `flirror-crawler` can be started via the\n`docker-compose.yaml` file within this repository. Thus, you can simply start\nboth services by running.\n\n```\n$ docker-compose up web crawler\n```\n\nwithin the root of this repository.\n\nWith both services running we still need to open some kind of browser to\nsee the actual flirror UI. This can be done by executing the `helpers/start_gui.sh`\nscript. Apart from starting chromium in full screen mode targeting the running\nflirror-web instance inside the docker container, the script also ensures that\nsome environment variables like `DISPLAY` are set and deactivates screen saver\nand energy saving mode of the X server - so the display doesn't go into sleep\nmode after a few minutes.\n\n## Optional configuration\n\nTo hide the mouse cursor, install unclutter via\n\n```\nsudo apt install unclutter\n```\n\nand add the following line to `/home/pi/.config/lxsession/LXDE-pi/autostart`\n\n```\n@unclutter -display :0 -noevents -grab\n```\n",
    'author': 'Felix Edel',
    'author_email': 'felixfelix.schmidt@googlemail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/felixedel/flirror',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
