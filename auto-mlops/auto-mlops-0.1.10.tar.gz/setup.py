# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['auto_mlops']

package_data = \
{'': ['*']}

install_requires = \
['cloudpickle>=1.3.0,<2.0.0',
 'requests>=2.23.0,<3.0.0',
 'scikit-learn>=0.22.1,<0.23.0']

setup_kwargs = {
    'name': 'auto-mlops',
    'version': '0.1.10',
    'description': 'Deploy your model in one line of code',
    'long_description': '# Deploy your ML pipelines in production painlessly, immediately and scalably\n\nDatarmada aims at **removing all the friction that comes with Machine Learning in production**.\nWe understand that Data Scientists are not trained to do that, and sometimes they are\nnot even attracted by this Software Engineering / DevOps aspect.\n\n**This package aims at deploying your scikit-learn pipeline on a server in one line**.\n\nYour pipeline is deployed on an OVH server so that you own your data and it is compliant with European regulations.\n\n## Installation\nInstall the package python using pip\n```\npip install auto-mlops\n```\n\n## Deploy your pipeline\n\nImport the ```Deployer``` class from the package.\n\n```python\nfrom auto_mlops import Deployer\ndeployer = Deployer()\n```\n\nNow, deploy your pipeline by passing to the ```deploy``` method a list containing all of its elements.\nThe pipeline elements (except for the last one) must be either :\n- A function returning transformed data if your pipeline element doesn\'t need to be fitted\n- An instance of a class implementing ```fit``` and ```transform``` methods otherwise\n\nThe last element of the pipeline must be an instance of a class implementing ```fit``` and ```predict``` methods.\n```python\n\nfrom sklearn.linear_model import LogisticRegression\n\ndef preprocess(raw_data):\n    # preprocess the data\n    return preprocessed_data\n\nclass Featurizer:\n    def fit(self, preprocessed_data, y):\n        # fit the featurizer\n        return self\n\n    def transform(self, preprocessed_data):\n        # transform the data\n        return featurized_data\n\nfeaturizer = Featurizer().fit(preprocessed_data)\n\nlog_reg = LogisticRegression()\nlog_reg.fit(featurized_data, y)\n\ndeployer.deploy([preprocess, featurizer, log_reg])\n\n```\n**Remember your elements must be fitted if they need to !**\n\n**You will be asked for your email address** so that we can keep track of the ownership of the pipelines deployed, and give you\naccess to monitoring functions in the future.\n\n```python\ndeployer.deploy([preprocess, featurizer, log_reg])\n\n>> Please enter your email address so that we can keep track of your pipelines:\nyou@example.com\n\n>> Your pipeline has been deployed to https://cloud.datarmada.com/id\n```\n\nYou can access your route whenever you want through ```deployer.route```\n## Make predictions\n\nYou can now send data to the route by making a POST request as following\n```python\nimport requests\n\nres = requests.post(\n  "https://cloud.datarmada.com/id",\n  json = {\n    "data": your_raw_data\n  }\n)\n\nprint(res.json())\n\n>> { "prediction" : prediction }\n```\n\nIt may be possible that one of the package you are using is not available in the environment we are deploying your model. \nIf you receive an error saying so, please email us at contact@datarmada.com so that we can fix it.',
    'author': 'Datarmada',
    'author_email': 'contact@datarmada.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
