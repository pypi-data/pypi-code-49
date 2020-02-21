import os

from diraccfg.cfg import CFG

EXAMPLE_CFG_FILE = os.path.join(os.path.dirname(__file__), 'releases.cfg')


def test_load():
  rels = CFG().loadFromFile(EXAMPLE_CFG_FILE)
  assert rels['Releases']['v6r22']['DIRACOS'] == 'v1r2'  # pylint: disable=unsubscriptable-object


def test_comment():
  c = CFG().loadFromFile(EXAMPLE_CFG_FILE)
  c.getComment('Releases').strip() == 'Here is where the releases go:'
