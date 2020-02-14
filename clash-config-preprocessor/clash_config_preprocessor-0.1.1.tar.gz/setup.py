# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['clash_config_preprocessor']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=5.3,<6.0', 'requests>=2.22.0,<3.0.0']

entry_points = \
{'console_scripts': ['clash_config_preprocessor = '
                     'clash_config_preprocessor.cli:cli']}

setup_kwargs = {
    'name': 'clash-config-preprocessor',
    'version': '0.1.1',
    'description': '',
    'long_description': '## Clash Config Preprocessor\n\nProcess multiple clash configure files , integrate them to single clash configure file.\n\n### How to use\n\n```bash\npipx install clash_config_preprocessor\nclash_config_preprocessor /path/to/preprocessor.config.yml -o /path/to/config.yml\n```\n\npreprocessor.config.yml **NOT** clash configure\n\n### example\n\npreprocessor configure example v2\n\n```yaml\n# 针对预处理器的配置\npreprocessor:\n  version: 2 # 目标预处理器版本号 目前有 1 和 2\n\n# clash 的 基础配置\n# 将会被放置在 输出文件 的 根节点\n# 内容参见 https://github.com/Dreamacro/clash/blob/dev/README.md\nclash-general:\n  port: 1081\n  socks-port: 1080\n  #redir-port: 1081\n\n  allow-lan: true\n  mode: Rule\n  log-level: info\n\n  external-controller: "0.0.0.0:6170"\n  secret: ""\n\n  dns:\n    enable: true # set true to enable dns (default is false)\n    ipv6: true # default is false\n    listen: 0.0.0.0:1053\n    enhanced-mode: redir-host\n    nameserver:\n      - 127.0.0.1:8053\n\n# 代理数据来源\n# 预处理器 将会从这些来源中读取代理信息 用于下面的 Proxy Group 生成\n# 读取的文件 必须是 一个标准的 clash 配置文件\nproxy-sources:\n  - type: url\n    url: "https://raw.githubusercontent.com/Howard-00/clash-config-preprocessor/master/example/proxies.yml"\n    udp: true # 对订阅中没有 udp 字段的服务器增加 udp，会导致不支持 udp 的服务器出错，请自行测试\n    prefix: "xxcloud - " # 节点名称添加前缀\n    suffix: " - xxcloud" # 节点名称添加后缀\n    plugin: obfs # 为订阅中没有混淆信息的订阅添加混淆（仅ss）\n    plugin-opts:\n      mode: tls\n      host: download.windowsupdate.com\n\n  - type: plain\n    data:\n      name: "ss1"\n      type: ss\n      server: server\n      port: 443\n      cipher: AEAD_CHACHA20_POLY1305\n      password: "password"\n      udp: true\n\n# 代理组(Proxy Group) 生成规则\n# 预处理器将会读取 *所有载入的代理信息*\n# 并将其 分配到 输出文件 的 代理组\n# 把 black-regex\n# 替换为 - - type: black-regex\\n          pattern:\n# 把 white-regex:\n# 替换为   - type: white-regex\\n          pattern:\n# \\n 是换行 可以实现简单的迁移\nproxy-group-dispatch:\n  - name: ✈️ Proxy # 代理组名称\n    proxies-filters: # 分配给代理组 的 过滤器，目前支持 black-regex 和 white-regex，越靠前的优先级越高\n      # 一个节点被重复匹配会去重，保留它第一次匹配的位置\n\n      - - type: white-regex\n          pattern: ".*" # 匹配到的代理 将会分配到 此代理组\n        - type: black-regex\n          pattern: ".*高倍率.*" # 匹配到的代理 将不会分配到 此代理组\n\n      - - type: white-regex # 可以弄多组过滤器，用来控制顺序\n          pattern: ".*高倍率.*"\n\n    flat-proxies: # 强制某个代理组内的代理并加至最前\n      - "vmess"\n    back-flat-proxies: # 强制某个代理组内的代理并加至最后\n      - "socks"\n    type: fallback # 类型 参见 clash 配置\n    url: "https://www.google.com/generate_204" # 测试 url 参见 clash 配置\n    interval: 300 # 超时 参见 clash 配置\n\n  - name: "🌑 Others"\n    type: select\n    flat-proxies: ["✈️ Proxy", "DIRECT"]\n\n# 规则集\n# 从外部载入一个规则集 并将其应用于规则\nrule-sets:\n  - name: ConnersHua_domains # 名称，在 Rule 中使用 RULE-SET,<name> 即可展开\n    type: clash # 类型，目前支持 clash 和 surge-ruleset\n    source: url # 来源，url 和 file\n    url: "https://raw.githubusercontent.com/ConnersHua/Profiles/master/Clash/Pro.yaml" # 如果是 file， 则需要填写 path\n    filters:\n      - operation: remove # 操作，目前支持 pick, remove, target-map, add-no-resolve，匹配成功后将执行\n        type: # 有三种过滤，type 和 target 是对规则类型和目标的完整匹配，采用列表的方式，可以写多条。\n          - IP-CIDR # 而 patter 是对规则模版的匹配，使用正则表达式，没写的类型默认匹配成功\n          - IP-CIDR6 # 这些过滤器按顺序执行，执行过 target-map 后目标会立即被修改并用于下一个过滤器的匹配\n      - operation: remove\n        type:\n          - GEOIP\n        pattern: "CN"\n        target:\n          - "DIRECT"\n\n      - operation: remove\n        type:\n          - MATCH\n\n      - operation: target-map\n        target-map:\n          - "PROXY,✈️ Proxy"\n          - "Apple,🍎 Apple"\n          - "GlobalMedia,📺 GlobalMedia"\n          - "HKMTMedia,🎬 HKMTMedia"\n          - "Hijacking,🚫 Hijacking"\n\n      - operation: add-no-resolve\n  - name: ConnersHua_ips\n    type: clash\n    source: url\n    url: "https://raw.githubusercontent.com/ConnersHua/Profiles/master/Clash/Pro.yaml" # 如果是 file， 则需要填写 path\n    filters:\n      - operation: target-map\n        target-map:\n          - "PROXY,✈️ Proxy"\n          - "Apple,🍎 Apple"\n          - "GlobalMedia,📺 GlobalMedia"\n          - "HKMTMedia,🎬 HKMTMedia"\n          - "Hijacking,🚫 Hijacking"\n      - operation: pick\n        type:\n          - IP-CIDR\n          - IP-CIDR6\n  - name: lhie-AD\n    type: surge-ruleset # 目前仅支持 surge 的 list 规则\n    source: url\n    url: "https://raw.githubusercontent.com/lhie1/Rules/master/Surge3/Reject.list"\n    target: "REJECT"\n\n# 规则\n# 将会 处理后 输出到 目标文件的 Rule\nrule:\n  - "RULE-SET,lhie-AD" # 将会从上述规则集展开\n  - "RULE-SET,ConnersHua_domains" # 将会从上述规则集展开\n  - "DOMAIN-SUFFIX,google.com,✈️ Proxy"\n  - "DOMAIN-KEYWORD,google,✈️ Proxy"\n  - "DOMAIN,google.com,✈️ Proxy"\n  - "DOMAIN-SUFFIX,ad.com,REJECT"\n  - "RULE-SET,ConnersHua_ips" # 将会从上述规则集展开\n  - "IP-CIDR,127.0.0.0/8,DIRECT"\n  - "SOURCE-IP-CIDR,192.168.1.201/32,DIRECT"\n  - "GEOIP,CN,DIRECT"\n  - "MATCH,✈️ Proxy"\n```\n',
    'author': None,
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/whtsky/clash-config-preprocessor',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
