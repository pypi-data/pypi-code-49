# -*- coding: utf-8 -*-
# :Project:   SoL -- Tourney's finals behaviours tests
# :Created:   ven 06 lug 2018 21:04:52 CEST
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2018 Lele Gaifax
#

import pytest

from sol.models.errors import OperationAborted


def test_no_finals(tourney_first):
    with pytest.raises(OperationAborted):
        tourney_first.makeFinalTurn()


def test_apr24_finals_same_winners(tourney_apr24):
    tourney_apr24.updateRanking()
    c1, c2, c3, c4 = tourney_apr24.ranking[:4]

    tourney_apr24.makeFinalTurn()
    finals = [m for m in tourney_apr24.matches if m.final]
    assert len(finals) == 2
    assert finals[0].turn == tourney_apr24.currentturn
    assert tourney_apr24.finalturns is True
    assert tourney_apr24.prized is False
    finals[0].score1 = 10
    finals[1].score2 = 10

    tourney_apr24.updateRanking()
    tourney_apr24.makeNextTurn()
    finals = [m for m in tourney_apr24.matches if m.final]
    assert len(finals) == 4
    finals[2].score1 = 10
    finals[3].score2 = 10

    tourney_apr24.updateRanking()
    assert tourney_apr24.prized is True
    assert tourney_apr24.ranking[:4] == [c1, c2, c4, c3]


def test_apr24_finals_two_and_three(tourney_apr24):
    assert tourney_apr24.prized is False

    tourney_apr24.updateRanking()
    c1, c2, c3, c4 = tourney_apr24.ranking[:4]

    tourney_apr24.makeFinalTurn()
    assert tourney_apr24.prized is False
    finals = [m for m in tourney_apr24.matches if m.final]
    finals[0].score1 = 10
    finals[1].score2 = 10

    tourney_apr24.updateRanking()
    tourney_apr24.makeNextTurn()
    finals = [m for m in tourney_apr24.matches if m.final]
    assert len(finals) == 4
    finals[2].score1 = 10
    finals[3].score1 = 10

    tourney_apr24.updateRanking()
    tourney_apr24.makeNextTurn()
    finals = [m for m in tourney_apr24.matches if m.final]
    assert len(finals) == 5
    finals[4].score1 = 10

    tourney_apr24.updateRanking()
    assert tourney_apr24.prized is True
    assert tourney_apr24.ranking[:4] == [c1, c2, c3, c4]


def test_rated_finals_two(tourney_rated):
    assert tourney_rated.prized is False

    tourney_rated.updateRanking()
    c1, c2 = tourney_rated.ranking[:2]

    tourney_rated.makeFinalTurn()
    finals = [m for m in tourney_rated.matches if m.final]
    assert len(finals) == 1
    assert tourney_rated.finalturns is True
    finals[0].score2 = 10

    tourney_rated.updateRanking()
    tourney_rated.makeNextTurn()
    finals = [m for m in tourney_rated.matches if m.final]
    assert len(finals) == 2
    finals[1].score2 = 10

    tourney_rated.updateRanking()
    with pytest.raises(OperationAborted):
        tourney_rated.makeNextTurn()

    assert tourney_rated.prized is True
    assert tourney_rated.ranking[:2] == [c2, c1]


def test_rated_finals_three(tourney_rated):
    assert tourney_rated.prized is False

    tourney_rated.updateRanking()
    c1, c2 = tourney_rated.ranking[:2]

    tourney_rated.makeFinalTurn()
    finals = [m for m in tourney_rated.matches if m.final]
    assert len(finals) == 1
    assert tourney_rated.finalturns is True
    finals[0].score2 = 10

    tourney_rated.updateRanking()
    tourney_rated.makeNextTurn()
    finals = [m for m in tourney_rated.matches if m.final]
    assert len(finals) == 2
    finals[1].score1 = 10

    tourney_rated.updateRanking()
    tourney_rated.makeNextTurn()
    finals = [m for m in tourney_rated.matches if m.final]
    assert len(finals) == 3
    finals[2].score2 = 20

    tourney_rated.updateRanking()
    with pytest.raises(OperationAborted):
        tourney_rated.makeNextTurn()

    assert tourney_rated.prized is True
    assert tourney_rated.ranking[:2] == [c2, c1]
