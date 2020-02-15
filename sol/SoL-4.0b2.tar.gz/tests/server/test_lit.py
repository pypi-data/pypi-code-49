# -*- coding: utf-8 -*-
# :Project:   SoL -- Tests /lit/* views
# :Created:   sab 07 lug 2018 22:51:56 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2018, 2019 Lele Gaifax
#

import pytest

from sqlalchemy import and_, select
from webtest.app import AppError

from sol.models import Competitor, Match, MergedPlayer, Player


@pytest.fixture
def mergedplayer_fatta(session):
    return session.query(MergedPlayer).filter_by(firstname='Fatta').one()


def test_index(app):
    app.get_route('lit')


def test_latest(app):
    app.get_route('lit_latest')
    app.get_route('lit_latest', _query={'n': 10})
    with pytest.raises(AppError) as e:
        app.get_route('lit_latest', _query={'n': 'x'})
    assert '400' in str(e.value)


def test_championship(app, championship_current):
    app.get_route('lit_championship', guid=championship_current.guid)


def test_tourney(app, tourney_first):
    app.get_route('lit_tourney', guid=tourney_first.guid)
    app.get_route('lit_tourney', guid=tourney_first.guid, _query={'turn': 1})
    app.get_route('lit_tourney', guid=tourney_first.guid,
                  _query={'player': tourney_first.competitors[0].player1.guid})
    app.get_route('lit_tourney', guid=tourney_first.guid,
                  _query={'player': tourney_first.competitors[0].player1.guid,
                          'turn': 1})
    with pytest.raises(AppError) as e:
        app.get_route('lit_tourney', guid=tourney_first.guid,
                      _query={'player': tourney_first.competitors[0].player1.guid,
                              'turn': 'x'})
    assert '400' in str(e.value)


def test_player(app, player_lele):
    app.get_route('lit_player', guid=player_lele.guid)


def test_merged_player(app, mergedplayer_fatta):
    app.get_route('lit_player', guid=mergedplayer_fatta.guid)


def test_player_matches(app, player_lele, mergedplayer_fatta):
    app.get_route('lit_player_matches', guid=player_lele.guid)
    app.get_route('lit_player_matches', guid=mergedplayer_fatta.guid)


def test_players(app):
    app.get_route('lit_players')


def test_players_listing(app, player_lele):
    app.get_route('lit_players_list', country=player_lele.nationality,
                  _query={'letter': player_lele.lastname[0]})
    app.get_route('lit_players_list', country='None', _query={'letter': 'A'})
    app.get_route('lit_players_list', country='eur', _query={'letter': 'A'})
    app.get_route('lit_players_list', country='ITA')


def test_rating(app, rating_european):
    app.get_route('lit_rating', guid=rating_european.guid)


def test_club(app, club_scr):
    app.get_route('lit_club', guid=club_scr.guid)
    with pytest.raises(AppError) as e:
        app.get_route('lit_club', guid='foo')
    assert '404' in str(e.value)


def test_club_players(app, club_scr):
    app.get_route('lit_club_players', guid=club_scr.guid)


def test_emblem(app):
    response = app.get('/lit/emblem/emblem.png')
    assert response.headers['content-type'].startswith('image')

    with pytest.raises(AppError) as e:
        app.get('/lit/emblem')
    assert '404' in str(e.value)

    with pytest.raises(AppError) as e:
        app.get('/lit/emblem/foo')
    assert '404' in str(e.value)


def test_portrait(app):
    response = app.get('/lit/portrait/portrait.png')
    assert response.headers['content-type'].startswith('image')

    with pytest.raises(AppError) as e:
        app.get('/lit/portrait')
    assert '404' in str(e.value)

    with pytest.raises(AppError) as e:
        app.get('/lit/portrait/foo')
    assert '404' in str(e.value)


def test_opponent(app, session, mergedplayer_fatta):
    mt = Match.__table__
    ct1 = Competitor.__table__.alias('c1')
    ct2 = Competitor.__table__.alias('c2')
    pt1 = Player.__table__.alias('p1')
    pt2 = Player.__table__.alias('p2')
    q = select([pt1.c.guid, pt2.c.guid],
               and_(ct1.c.idplayer1 == pt1.c.idplayer,
                    ct2.c.idplayer1 == pt2.c.idplayer,
                    mt.c.idcompetitor1 == ct1.c.idcompetitor,
                    mt.c.idcompetitor2 == ct2.c.idcompetitor))
    r = session.execute(q).first()
    app.get_route('lit_player_opponent', guid=r[0], opponent=r[1])
    with pytest.raises(AppError) as e:
        app.get_route('lit_player_opponent', guid=r[0], opponent='badc0de')
    assert '404' in str(e.value)

    app.get_route('lit_player_opponent', guid=r[0], opponent=mergedplayer_fatta.guid)
    app.get_route('lit_player_opponent', guid=mergedplayer_fatta.guid, opponent=r[0])


def test_country(app):
    app.get_route('lit_country', country='None')
    app.get_route('lit_country', country='ITA')
    app.get_route('lit_country', country='eur')
