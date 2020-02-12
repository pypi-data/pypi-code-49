from cytoolz import first
from cytoolz import get_in
from cytoolz import partial
from cytoolz import second
from merlin import cfg
from merlin import chips
from merlin import specs
from merlin.formats import pyccd
import test


def data(cfg, acquired):
    x, y = get_in(['chip', 'proj-pt'], cfg['snap_fn'](x=test.x, y=test.y))

    # get specs
    specmap = cfg['specs_fn'](specs=cfg['registry_fn']())

    # get function that will return chipmap.
    # Don't create state with a realized variable to preserve memory
    chipmap = partial(chips.mapped,
                      x=test.x,
                      y=test.y,
                      acquired=acquired,
                      specmap=specmap,
                      chips_fn=cfg['chips_fn'])

    # calculate locations chip.  There's another function
    # here to be split out and organized.
    
    grid = first(filter(lambda x: x['name'] == 'chip',
                        cfg['grid_fn']()))

    cw, ch = specs.refspec(specmap).get('data_shape')
    
    locations = chips.locations(x=x,
                                y=y,
                                cw=cw,
                                ch=ch,
                                rx=grid.get('rx'),
                                ry=grid.get('ry'),
                                sx=grid.get('sx'),
                                sy=grid.get('sy'))
    
    return cfg['format_fn'](x=x,
                            y=y,
                            locations=locations,
                            dates_fn=cfg['dates_fn'],
                            specmap=specmap,
                            chipmap=chipmap()) 


@test.vcr.use_cassette(test.cassette)
def test_pyccd():

    d = data(cfg.get('chipmunk-ard', env=test.ard_env),
             test.ard_acquired)

    # we are only testing the structure of the response here.
    # Full data validation is being done in the test for merlin.create()
    assert type(d) is tuple
    assert len(d) == 10000
    assert type(first(d)) is tuple
    assert type(first(first(d))) is tuple
    assert type(second(first(d))) is dict
    assert type(second(second(first(d)))) is tuple or list
    assert len(second(second(first(d)))) > 0


@test.vcr.use_cassette(test.cassette)
def test_aux():

    d = data(cfg.get('chipmunk-aux', env=test.aux_env),
             test.aux_acquired)

    # we are only testing the structure of the response here.
    # Full data validation is being done in the test for merlin.create()
    assert type(d) is tuple
    assert len(d) == 10000
    assert type(first(d)) is tuple
    assert type(first(first(d))) is tuple
    assert type(second(first(d))) is dict
    assert type(second(second(first(d)))) is tuple or list
    assert len(second(second(first(d)))) > 0
