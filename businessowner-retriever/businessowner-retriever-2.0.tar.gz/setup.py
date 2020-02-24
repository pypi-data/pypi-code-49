# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['businessowner_retriever']
install_requires = \
['Logbook>=1.5.2,<2.0.0',
 'click>=7.0,<8.0',
 'colorama>=0.4.1,<0.5.0',
 'named-enum>=1.0.0,<2.0.0',
 'parsel>=1.5.2,<2.0.0',
 'requests[socks]>=2.22.0,<3.0.0',
 'terminaltables>=3.1.0,<4.0.0']

entry_points = \
{'console_scripts': ['businessowner-retriever = businessowner_retriever:cli']}

setup_kwargs = {
    'name': 'businessowner-retriever',
    'version': '2.0',
    'description': 'Tool to retrieve list of Vietnamese registered business owners.',
    'long_description': '# BusinessOwner Retriever\n\nTool to retrieve list of Vietnamese registered business owners.\n\n## Install\n\n```\npip3 install businessowner-retriever\n```\n\nOn Windows, you can download the prebuilt *msi* file, running it to install.\n\nThe software is primarily developed and tested on Ubuntu Linux. Windows 10 64-bit is rougly tested and provided installer. I don\'t have Mac OS X to support.\n\n## Usage\n\nThe command name changes, depending on whether you installed the program.\n\nTypical, it is `businessowner-retriever` on Linux and `businessowner-retriever.exe` on Windows.\nIf you run from the source, it is `businessowner_retriever.py`.\n\nFirst, you can run the command with "--help" option to see summary of usage:\n\n\n```sh\n$ businessowner-retriever --help\nUsage: businessowner-retriever [OPTIONS] COMMAND [ARGS]...\n\nOptions:\n  -V, --version  Show the version and exit.\n  -v, --verbose  Show more log to debug (verbose mode).\n  --help         Show this message and exit.\n\nCommands:\n  businessowners  Get business owners\n  codes           Get province, district codes\n```\n\nThe program provides two subcommands, which you can also find brief usage guide:\n\n```sh\n$ businessowner-retriever codes --help\nUsage: businessowner-retriever codes [OPTIONS] [AREA_CODE]\n\n  Get province, district codes\n\nOptions:\n  -v, --verbose  Show more log to debug (verbose mode).\n  --help         Show this message and exit.\n```\n\n```sh\n$ businessowner-retriever businessowners --help\nUsage: businessowner-retriever businessowners [OPTIONS] AREA_CODE\n\n  Get business owners\n\nOptions:\n  -t, --tax-duty [normal|vat-exempted|suspended|closed|adjusting]\n                                  [default: normal]\n  -o, --out FILENAME              [required]\n  -v, --verbose                   Show more log to debug (verbose mode).\n  --help                          Show this message and exit.\n```\n\nNow are the steps:\n\n### 1. Find province code\n\n```sh\n$ businessowner-retriever codes\n┌───────────────────┬──────┐\n│ Province          │ Code │\n├───────────────────┼──────┤\n│ An Giang          │ 805  │\n│ Bà Rịa - Vũng Tàu │ 717  │\n│ Bình Dương        │ 711  │\n│ Bình Phước        │ 707  │\n│ Bình Thuận        │ 715  │\n│ Bình Định         │ 507  │\n│ Bạc Liêu          │ 821  │\n│ Bắc Cạn           │ 207  │\n│ Bắc Giang         │ 221  │\n│ Bắc Ninh          │ 223  │\n│ Bến Tre           │ 811  │\n│ Cao Bằng          │ 203  │\n│ Cà Mau            │ 823  │\n│ Cần Thơ           │ 815  │\n│ Gia Lai           │ 603  │\n│ Hà Giang          │ 201  │\n│ Hà Nam            │ 111  │\n│ Hà Nội            │ 101  │\n│ Hà Tĩnh           │ 405  │\n│ Hòa Bình          │ 305  │\n│ Hưng Yên          │ 109  │\n│ Hải Dương         │ 107  │\n│ Hải Phòng         │ 103  │\n│ Hậu Giang         │ 816  │\n│ Khánh Hòa         │ 511  │\n│ Kiên Giang        │ 813  │\n│ Kon Tum           │ 601  │\n│ Lai Châu          │ 302  │\n│ Long An           │ 801  │\n│ Lào Cai           │ 205  │\n│ Lâm Đồng          │ 703  │\n│ Lạng Sơn          │ 209  │\n│ Nam Định          │ 113  │\n│ Nghệ An           │ 403  │\n│ Ninh Bình         │ 117  │\n│ Ninh Thuận        │ 705  │\n│ Phú Thọ           │ 217  │\n│ Phú Yên           │ 509  │\n│ Quảng Bình        │ 407  │\n│ Quảng Nam         │ 503  │\n│ Quảng Ngãi        │ 505  │\n│ Quảng Ninh        │ 225  │\n│ Quảng Trị         │ 409  │\n│ Sóc Trăng         │ 819  │\n│ Sơn La            │ 303  │\n│ TP Hồ Chí Minh    │ 701  │\n│ Thanh Hoá         │ 401  │\n│ Thái Bình         │ 115  │\n│ Thái Nguyên       │ 215  │\n│ Thừa Thiên - Huế  │ 411  │\n│ Tiền Giang        │ 807  │\n│ Trà Vinh          │ 817  │\n│ Tuyên Quang       │ 211  │\n│ Tây Ninh          │ 709  │\n│ Vĩnh Long         │ 809  │\n│ Vĩnh Phúc         │ 219  │\n│ Yên Bái           │ 213  │\n│ Điện Biên         │ 301  │\n│ Đà Nẵng           │ 501  │\n│ Đắc Lắc           │ 605  │\n│ Đắk Nông          │ 606  │\n│ Đồng Nai          │ 713  │\n│ Đồng Tháp         │ 803  │\n└───────────────────┴──────┘\n```\n\n### 2. From the chosen province, lookup ward code\n\nFor example, we want to look into Đắk Nông province.\n\n```\n$ businessowner-retriever codes 606\n┌──────────────────┬───────┐\n│ District         │ Code  │\n├──────────────────┼───────┤\n│ Huyện Cư Jút     │ 60603 │\n│ Huyện Krông Nô   │ 60605 │\n│ Huyện Tuy Đức    │ 60617 │\n│ Huyện Đắk Glong  │ 60615 │\n│ Huyện Đắk Mil    │ 60607 │\n│ Huyện Đắk R\'Lấp  │ 60611 │\n│ Huyện Đắk Song   │ 60609 │\n│ Thị xã Gia Nghĩa │ 60613 │\n└──────────────────┴───────┘\n```\n\nTry Cư Jút district, with code `60603`:\n\n```\n$ businessowner-retriever codes 60603\n┌────────────────────┬─────────┐\n│ Ward               │ Code    │\n├────────────────────┼─────────┤\n│ Thị trấn Ea T-Ling │ 6060301 │\n│ Xã Cư Knia         │ 6060305 │\n│ Xã Ea Pô           │ 6060303 │\n│ Xã Nam Dong        │ 6060309 │\n│ Xã Trúc Sơn        │ 6060315 │\n│ Xã Tâm Thắng       │ 6060313 │\n│ Xã Đắk DRông       │ 6060311 │\n│ Xã Đắk Wil         │ 6060307 │\n└────────────────────┴─────────┘\n\n```\n\n### 3. Retrieve list of business owners in that ward\n\n\n```\n$ businessowner-retriever businessowners 6060305 -o xa_cu_kinia.csv\nWrote to file: xa_cu_knia.csv\n```\n\n## Notes\n\n- The server of data source, [www.gdt.gov.vn](http://www.gdt.gov.vn/wps/portal/home/hct), has access throttling. After an amount of data retrieval, it will block us. You should take a rest, before continuing, or finding a proxy to fake your IP address.\n\n- On Windows, please run the program inside [ConEmu](https://conemu.github.io/). It is because *BusinessOwner Retriever* has an issue with character encoding in PowerShell console, which I (Quân) can\'t resolve (I\'m just a Linux programmer).\n',
    'author': 'Nguyễn Hồng Quân',
    'author_email': 'ng.hong.quan@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://hongquan@bitbucket.org/hongquan/businessowner_retriever.git',
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
