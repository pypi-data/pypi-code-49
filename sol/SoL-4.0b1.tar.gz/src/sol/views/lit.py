# -*- coding: utf-8 -*-
# :Project:   SoL -- Light user interface controller
# :Created:   ven 12 dic 2008 09:18:37 CET
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2008, 2009, 2010, 2013, 2014, 2016, 2018, 2020 Lele Gaifax
#

from datetime import date
from functools import cmp_to_key, wraps
from itertools import groupby
from operator import itemgetter
import logging


from babel.numbers import format_decimal
from markupsafe import escape

from pyramid.httpexceptions import (
    HTTPBadRequest,
    HTTPMovedPermanently,
    HTTPNotFound,
    )
from pyramid.view import view_config

from sqlalchemy import distinct, func, select
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.sql import and_, or_, exists

from . import get_request_logger
from ..i18n import country_name, translatable_string as _, translator, gettext, ngettext
from ..models import (
    Championship,
    Club,
    MergedPlayer,
    Player,
    Rating,
    Tourney,
    )


logger = logging.getLogger(__name__)


@view_config(route_name="lit", renderer="lit/index.mako")
def index(request):
    sess = request.dbsession

    clubs_t = Club.__table__
    players_t = Player.__table__
    championships_t = Championship.__table__
    tourneys_t = Tourney.__table__
    ratings_t = Rating.__table__

    bycountry = {}
    query = (select([clubs_t.c.nationality, clubs_t.c.isfederation])
             .where(or_(exists().where(players_t.c.idclub == clubs_t.c.idclub),
                        exists().where(championships_t.c.idclub == clubs_t.c.idclub))))
    nclubs = nfeds = 0
    for nationality, isfederation in sess.execute(query):
        country = country_name(nationality, request=request)
        nclubs += 1
        counts = bycountry.setdefault((country, nationality), [0, 0, 0])
        counts[0] += 1
        if isfederation:
            nfeds += 1
            counts[1] += 1

    query = (select([players_t.c.nationality, func.count(players_t.c.idplayer)])
             .where(players_t.c.nationality != None)
             .group_by(players_t.c.nationality))
    for nationality, count in sess.execute(query):
        country = country_name(nationality, request=request)
        counts = bycountry.setdefault((country, nationality), [0, 0, 0])
        counts[2] += count

    query = select([func.count(tourneys_t.c.idtourney)])
    ntourneys = sess.execute(query).scalar()

    query = select([func.count(championships_t.c.idchampionship)])
    nchampionships = sess.execute(query).scalar()

    query = select([func.count(players_t.c.idplayer)])
    nplayers = sess.execute(query).scalar()

    query = (select([func.count(distinct(players_t.c.nationality))])
             .where(players_t.c.nationality != None))
    npcountries = sess.execute(query).scalar()

    query = select([func.count(ratings_t.c.idrating)])
    nratings = sess.execute(query).scalar()

    return {
        "_": gettext,
        "bycountry": bycountry,
        "nccountries": len(bycountry),
        "nchampionships": nchampionships,
        "nclubs": nclubs,
        "nfederations": nfeds,
        "ngettext": ngettext,
        "npcountries": npcountries,
        "nplayers": nplayers,
        "nratings": nratings,
        "ntourneys": ntourneys,
        "request": request,
        "session": sess,
        "today": date.today(),
        "version": request.registry.settings['desktop.version'],
    }


def _build_template_data(request, session, entity, **kwargs):
    data = {
        '_': gettext,
        'escape': escape,
        'entity': entity,
        'ngettext': ngettext,
        'request': request,
        'session': session,
        'today': date.today(),
        'version': request.registry.settings['desktop.version'],
    }
    data.update(kwargs)
    return data


def resolve_guids(*pairs):
    def decorator(func):
        @wraps(func)
        def wrapper(request):
            t = translator(request)
            params = request.matchdict
            sess = request.dbsession
            entities = []
            # Take paired arguments two-by-two, inline simpler version of
            # itertools::grouper recipe
            ipairs = iter(pairs)
            for pname, iclass in zip(ipairs, ipairs):
                try:
                    guid = params[pname]
                except KeyError:  # pragma: nocover
                    msg = "Missing required argument: %s" % pname
                    get_request_logger(request, logger).warning(msg)
                    raise HTTPBadRequest(msg)
                try:
                    instance = sess.query(iclass).filter_by(guid=guid).one()
                except NoResultFound:
                    if iclass is Player:
                        try:
                            merged = sess.query(MergedPlayer).filter_by(guid=guid).one()
                        except NoResultFound:
                            get_request_logger(request, logger).warning(
                                "Couldn't create page: no %s with guid %s",
                                iclass.__name__.lower(), guid)
                            msg = t(_('No $entity with guid $guid'),
                                    mapping=dict(entity=iclass.__name__.lower(), guid=guid))
                            raise HTTPNotFound(msg)
                        entities.append((guid, merged.player.guid))
                    else:
                        get_request_logger(request, logger).warning(
                            "Couldn't create page: no %s with guid %s",
                            iclass.__name__.lower(), guid)
                        msg = t(_('No $entity with guid $guid'),
                                mapping=dict(entity=iclass.__name__.lower(), guid=guid))
                        raise HTTPNotFound(msg)
                else:
                    entities.append(instance)
            return func(request, sess, entities)
        return wrapper
    return decorator


@view_config(route_name="lit_championship", renderer="lit/championship.mako")
@resolve_guids('guid', Championship)
def championship(request, session, entities):
    cship = entities[0]
    data = _build_template_data(request, session, cship)

    if cship.closed:
        request.response.cache_control.public = True
        request.response.cache_control.max_age = 60*60*24*365

    if cship.prizes != 'centesimal':
        def format_prize(p):
            return format_decimal(p, '###0', request.locale_name)
    else:
        def format_prize(p):
            return format_decimal(p, '###0.00', request.locale_name)
    data["format_prize"] = format_prize
    return data


def compare_cships_by_sequence(c1, c2):
    previous_c1 = {c1.idchampionship}
    previous = c1.previous
    while previous is not None:
        previous_c1.add(previous.idchampionship)
        previous = previous.previous
    if c2.idchampionship in previous_c1:
        return 1
    previous_c2 = {c2.idchampionship}
    previous = c2.previous
    while previous is not None:
        previous_c2.add(previous.idchampionship)
        previous = previous.previous
    if c1.idchampionship in previous_c2:
        return -1
    return 0


@view_config(route_name="lit_club", renderer="lit/club.mako")
@resolve_guids('guid', Club)
def club(request, session, entities):
    club = entities[0]
    # The championships are already ordered by their description: perform another pass
    # taking into account their "previous" relationship
    cships = sorted(club.championships, key=cmp_to_key(compare_cships_by_sequence))
    data = _build_template_data(request, session, club)
    data['championships'] = cships
    return data


@view_config(route_name="lit_club_players", renderer="lit/club_players.mako")
@resolve_guids('guid', Club)
def club_players(request, session, entities):
    club = entities[0]
    query = session.query(Player) \
                   .filter(or_(Player.idclub == club.idclub,
                               Player.idfederation == club.idclub)) \
                   .order_by(Player.lastname, Player.firstname)
    players = groupby(query, lambda player: player.lastname[0])
    return _build_template_data(request, session, club, players=players)


@view_config(route_name="lit_country", renderer="lit/country.mako")
def country(request):
    ccode = request.matchdict['country']

    if ccode == 'None':
        ccode = None

    country = country_name(ccode, request=request)

    sess = request.dbsession

    clubs_t = Club.__table__
    players_t = Player.__table__
    championships_t = Championship.__table__

    clubs = []
    query = (select([clubs_t.c.description,
                     clubs_t.c.guid,
                     clubs_t.c.emblem,
                     clubs_t.c.isfederation,
                     select([func.count(championships_t.c.idchampionship)],
                            championships_t.c.idclub == clubs_t.c.idclub).as_scalar(),
                     select([func.count(players_t.c.idplayer)],
                            or_(players_t.c.idclub == clubs_t.c.idclub,
                                players_t.c.idfederation == clubs_t.c.idclub)).as_scalar()])
             .where(clubs_t.c.nationality == ccode))
    nfeds = 0
    for description, guid, emblem, isfed, nc, np in sess.execute(query):
        clubs.append((description, guid, emblem, isfed, nc, np))
        if isfed:
            nfeds += 1

    query = (select([func.count(players_t.c.idplayer)])
             .where(players_t.c.nationality == ccode))
    nplayers = sess.execute(query).scalar()

    return {
        '_': gettext,
        'ngettext': ngettext,
        'code': ccode,
        'country': country,
        'clubs': clubs,
        'nclubs': len(clubs),
        'nfederations': nfeds,
        'nplayers': nplayers,
        'request': request,
        'today': date.today(),
        'version': request.registry.settings['desktop.version'],
    }


@view_config(route_name="lit_player", renderer="lit/player.mako")
@resolve_guids('guid', Player)
def player(request, session, entities):
    player = entities[0]
    if isinstance(player, tuple):
        old_guid, new_guid = player
        get_request_logger(request, logger).debug(
            "Redirecting from player %s to %s", old_guid, new_guid)
        raise HTTPMovedPermanently(
            request.route_path('lit_player', guid=new_guid))
    else:
        data = _build_template_data(request, session, player)

        def format_prize(p):
            return format_decimal(p, '###0.00', request.locale_name)

        data["format_prize"] = format_prize
        return data


@view_config(route_name="lit_player_opponent", renderer="lit/player_opponent.mako")
@resolve_guids('guid', Player, 'opponent', Player)
def opponent(request, session, entities):
    player = entities[0]
    opponent = entities[1]
    if isinstance(player, tuple) or isinstance(opponent, tuple):
        if isinstance(player, tuple):
            p_old_guid, p_new_guid = player
        else:
            p_old_guid = p_new_guid = player.guid
        if isinstance(opponent, tuple):
            o_old_guid, o_new_guid = opponent
        else:
            o_old_guid = o_new_guid = opponent.guid
        get_request_logger(request, logger).debug(
            "Redirecting from player %s to %s and from opponent %s to %s",
            p_old_guid, p_new_guid, o_old_guid, o_new_guid)
        raise HTTPMovedPermanently(
            request.route_path('lit_player_opponent', guid=p_new_guid, opponent=o_new_guid))
    else:
        return _build_template_data(request, session, player, opponent=opponent)


@view_config(route_name="lit_player_matches", renderer="lit/player_matches.mako")
@resolve_guids('guid', Player)
def matches(request, session, entities):
    player = entities[0]
    if isinstance(player, tuple):
        old_guid, new_guid = player
        get_request_logger(request, logger).debug(
            "Redirecting from player %s to %s", old_guid, new_guid)
        raise HTTPMovedPermanently(
            request.route_path('lit_player', guid=new_guid))
    else:
        return _build_template_data(request, session, player)


@view_config(route_name="lit_players", renderer="lit/players.mako")
def players(request):
    sess = request.dbsession
    pt = Player.__table__
    query = sess.execute(select([func.substr(pt.c.lastname, 1, 1),
                                 pt.c.nationality,
                                 func.count()]).group_by(func.substr(pt.c.lastname, 1, 1),
                                                         pt.c.nationality))
    index = []
    for letter, countsbycountry in groupby(query, itemgetter(0)):
        bycountry = []
        for country in countsbycountry:
            ccode = country[1]
            cname = country_name(ccode, request=request)
            bycountry.append(dict(code=ccode, country=cname, count=country[2]))
        bycountry.sort(key=itemgetter('country'))
        index.append((letter, bycountry))

    return {
        '_': gettext,
        'ngettext': ngettext,
        'today': date.today(),
        'version': request.registry.settings['desktop.version'],
        'index': index,
        'request': request,
    }


@view_config(route_name="lit_players_list", renderer="lit/players_list.mako")
def players_list(request):
    ccode = request.matchdict['country']
    letter = request.params.get('letter')

    if ccode == 'None':
        ccode = None

    cname = country_name(ccode, request=request)

    sess = request.dbsession
    if letter:
        expr = and_(Player.nationality == ccode,
                    Player.lastname.startswith(letter))
    else:
        expr = Player.nationality == ccode
    players = (sess.query(Player)
               .filter(expr)
               .order_by(Player.lastname, Player.firstname))

    return {
        '_': gettext,
        'code': ccode,
        'country': cname,
        'letter': letter,
        'ngettext': ngettext,
        'players': players,
        'request': request,
        'today': date.today(),
        'version': request.registry.settings['desktop.version'],
    }


@view_config(route_name="lit_rating", renderer="lit/rating.mako")
@resolve_guids('guid', Rating)
def rating(request, session, entities):
    rating = entities[0]
    tt = Tourney.__table__
    ntourneys = session.execute(select([func.count(tt.c.idtourney)],
                                       tt.c.idrating == rating.idrating)).first()[0]
    return _build_template_data(request, session, rating, ntourneys=ntourneys)


@view_config(route_name="lit_tourney", renderer="lit/tourney.mako")
@resolve_guids('guid', Tourney)
def tourney(request, session, entities):
    t = translator(request)

    tourney = entities[0]
    turn = request.params.get('turn')
    if turn is not None:
        try:
            turn = int(turn)
        except ValueError:
            get_request_logger(request, logger).warning(
                "Couldn't create page: argument “turn” is not an integer: %r", turn)
            e = t(_('Invalid turn: $turn'), mapping=dict(turn=repr(turn)))
            raise HTTPBadRequest(str(e))

    data = _build_template_data(request, session, tourney, turn=turn,
                                player=request.params.get('player'))

    if tourney.championship.prizes != 'centesimal':
        def format_prize(p):
            return format_decimal(p, '###0', request.locale_name)
    else:
        def format_prize(p):
            return format_decimal(p, '###0.00', request.locale_name)

    data["format_prize"] = format_prize

    if tourney.prized:
        request.response.cache_control.public = True
        request.response.cache_control.max_age = 60*60*24*365

    return data


@view_config(route_name="lit_latest", renderer="lit/latest.mako")
def latest(request):
    t = translator(request)

    n = request.params.get('n')
    if n is not None:
        try:
            n = int(n)
        except ValueError:
            get_request_logger(request, logger).warning(
                "Couldn't create page: argument “n” is not an integer: %r", n)
            e = t(_('Invalid number of tourneys: $n'), mapping=dict(n=repr(n)))
            raise HTTPBadRequest(str(e))
    else:
        n = 20

    sess = request.dbsession
    tourneys = sess.query(Tourney).filter_by(prized=True).order_by(Tourney.date.desc())[:n]

    return {
        '_': gettext,
        'escape': escape,
        'n': len(tourneys),
        'ngettext': ngettext,
        'request': request,
        'session': request.dbsession,
        'today': date.today(),
        'tourneys': tourneys,
        'version': request.registry.settings['desktop.version'],
    }
