# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['brickschema']

package_data = \
{'': ['*'], 'brickschema': ['ontologies/*']}

install_requires = \
['owlrl>=5.2,<6.0',
 'pytest>=5.3,<6.0',
 'rdflib>=4.2,<5.0',
 'sqlalchemy>=1.3,<2.0']

extras_require = \
{'allegro': ['docker>=4.1,<5.0'], 'reasonable': ['reasonable>=0.1.6,<0.2.0']}

setup_kwargs = {
    'name': 'brickschema',
    'version': '0.1.2a1',
    'description': 'A library for working with the Brick ontology for buildings (brickschema.org)',
    'long_description': '# Brick Ontology Python package\n\n[![Build Status](https://travis-ci.org/BrickSchema/py-brickschema.svg?branch=master)](https://travis-ci.org/BrickSchema/py-brickschema)\n[![Documentation Status](https://readthedocs.org/projects/brickschema/badge/?version=latest)](https://brickschema.readthedocs.io/en/latest/?badge=latest)\n\nDocumentation available at [readthedocs](https://brickschema.readthedocs.io/en/latest/)\n\n## Installation\n\nThe `brickschema` package requires Python >= 3.6. It can be installed with `pip`:\n\n```\npip install brickschema\n```\n\nThe `brickschema` package offers several installation configuration options for reasoning.\nThe default bundled [OWLRL](https://pypi.org/project/owlrl/) reasoner delivers correct results, but exhibits poor performance on large or complex ontologies (we have observed minutes to hours) due to its bruteforce implementation.\n\nThe [Allegro reasoner](https://franz.com/agraph/support/documentation/current/materializer.html) has better performance and implements enough of the OWLRL profile to be useful. We execute Allegrograph in a Docker container, which requires the `docker` package. To install support for the Allegrograph reasoner, use\n\n```\npip install brickschema[allegro]\n```\n\nThe [reasonable Reasoner](https://github.com/gtfierro/reasonable) offers even better performance than the Allegro reasoner, but is currently only packaged for Linux platforms. (_Note: no fundamental limitations here, just some packaging complexity due to cross-compiling the `.so`_). To install support for the reasonable Reasoner, use\n\n```\npip install brickschema[reasonable]\n```\n\n## OWLRL Inference\n\n`brickschema` makes it easier to employ OWLRL reasoning on your graphs. The package will automatically use the fastest available reasoning implementation for your system:\n\n- `reasonable` (fastest, Linux-only for now): `pip install brickschema[reasonable]`\n- `Allegro` (next-fastest, requires Docker): `pip install brickschema[allegro]`\n- OWLRL (default, native Python implementation): `pip install brickschema`\n\nTo use OWL inference, import the `OWLRLInferenceSession` class (this automatically chooses the fastest reasoner; check out the [inference module documentation](https://brickschema.readthedocs.io/en/latest/source/brickschema.html#module-brickschema.inference) for how to use a specific reasoner). Create a `brickschema.Graph` with your ontology rules and instances loaded in and apply the reasoner\'s session to it:\n\n```python\nfrom brickschema.graph import Graph\nfrom brickschema.namespaces import BRICK\nfrom brickschema.inference import OWLRLInferenceSession\n\ng = Graph(load_brick=True)\ng.load_file("test.ttl")\n\nsess = OWLRLInferenceSession()\ninferred_graph = sess.expand(g)\nprint(f"Inferred graph has {len(inferred_graph)} triples")\n```\n\n\n## Haystack Inference\n\nRequires a JSON export of a Haystack model.\nFirst, export your Haystack model as JSON; we are using the public reference model `carytown.json`.\nThen you can use this package as follows:\n\n```python\nimport json\nfrom brickschema.inference import HaystackInferenceSession\nhaysess = HaystackInferenceSession("http://project-haystack.org/carytown#")\nmodel = json.load(open(\'carytown.json\'))\nmodel = haysess.infer_model(model)\nprint(len(model))\n\npoints = model.query("""SELECT ?point ?type WHERE {\n    ?point rdf:type/rdfs:subClassOf* brick:Point .\n    ?point rdf:type ?type\n}""")\nprint(points)\n```\n\n## SQL ORM\n\n```python\nfrom brickschema.graph import Graph\nfrom brickschema.namespaces import BRICK\nfrom brickschema.orm import SQLORM, Location, Equipment, Point\n\n# loads in default Brick ontology\ng = Graph(load_brick=True)\n# load in our model\ng.load_file("test.ttl")\n# put the ORM in a SQLite database file called "brick_test.db"\norm = SQLORM(g, connection_string="sqlite:///brick_test.db")\n\n# get the points for each equipment\nfor equip in orm.session.query(Equipment):\n    print(f"Equpiment {equip.name} is a {equip.type} with {len(equip.points)} points")\n    for point in equip.points:\n        print(f"    Point {point.name} has type {point.type}")\n# filter for a given name or type\nhvac_zones = orm.session.query(Location)\\\n                        .filter(Location.type==BRICK.HVAC_Zone)\\\n                        .all()\nprint(f"Model has {len(hvac_zones)} HVAC Zones")\n```\n',
    'author': 'Gabe Fierro',
    'author_email': 'gtfierro@cs.berkeley.edu',
    'url': 'https://brickschema.org',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
