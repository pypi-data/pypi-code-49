"""TMDB API module."""
from random import choice
from typing import (
    List, NamedTuple, Optional as Opt, SupportsInt as SInt
)

import isle as api

#: The TMDB website URL.
TMDB_URL = 'https://themoviedb.org'


class ApiError(Exception):
    """An exception raised after receiving a blank response."""


class Person(NamedTuple):
    """A class representing a person (director or actor) entity."""
    #: The name of the person.
    name: str
    #: The URL of the person on TMDB.
    url: str
    #: The role of the person.
    role: Opt[str] = None

    @classmethod
    def from_args(cls, *args) -> Opt['Person']:
        """
        Create a ``Person`` object from the given arguments.

        :param args: The role, name, and ID of the person.

        :return: An instance of the class.
        """
        if not args:
            return None
        role, person, id = args
        return cls.__new__(
            cls, role=role, name=person,
            url=f'{TMDB_URL}/person/{id}'
        )

    def __str__(self) -> str:
        """
        Return a string representation of the object.

        :return: The name/URL of the person as a markdown link.
        """
        return f'[{self.name}]({self.url})'


class Film(NamedTuple):
    """A class representing a film entity."""
    #: The title of the film.
    title: str
    #: The URL of the film.
    url: str
    #: The thumbnail URL of the film.
    thumbnail: str
    #: The description of the film.
    description: Opt[str] = None
    #: The tagline of the film.
    tagline: Opt[str] = None
    #: The original language of the film.
    language: Opt[str] = None
    #: The year the film was released.
    year: Opt[int] = None
    #: The runtime of the film.
    runtime: Opt[str] = None
    #: The average score of the film.
    score: Opt[float] = None
    #: The genres of the film.
    genres: Opt[List[str]] = None
    #: The writer of the film.
    writer: Opt[Person] = None
    #: The director of the film.
    director: Opt[Person] = None
    #: The cast of the film.
    cast: Opt[List[Person]] = None


def get_film(*, film: Opt[str] = None,
             director: Opt[str] = None,
             actor: Opt[str] = None,
             year: Opt[SInt] = None) -> Film:
    """
    Get the info of a film given a query.

    :param film: The title of the film.
    :param director: The director of the film.
    :param actor: An actor playing in the film.
    :param year: The year of the film. Only used
                 when ``film`` is also given.

    :raises TypeError: If no arguments were provided.
    :raises ApiError: If a film was not found.

    :return: A class containing the film's info.
    """
    if film:
        try:
            year = int(year) if year else None
            res = next(api.search_movie(film, year=year))
        except StopIteration as err:
            raise ApiError(
                f"Couldn't find a film titled '{film}'."
            ) from err
    elif director and actor:
        try:
            a_id = next(api.search_person(actor)).tmdb_id
        except StopIteration as err:
            raise ApiError(
                f"Couldn't find a film starring '{actor}'."
            ) from err
        try:
            d_id = next(api.search_person(director)).tmdb_id
        except StopIteration as err:
            raise ApiError(
                f"Couldn't find a film directed by '{director}'."
            ) from err
        try:
            res = choice(list(api.discover_movies({
                'with_cast': str(a_id), 'with_crew': str(d_id)
            })))
        except IndexError as err:
            raise ApiError(
                "Couldn't find a film directed by "
                f"'{director}' and starring '{actor}'"
            ) from err
    elif director or actor:
        try:
            res = next(api.search_person(director or actor))
            res = res.crew if director else res.cast
        except StopIteration as err:
            job = 'directed by' if director else 'starring'
            raise ApiError(
                f"Couldn't find a film {job} '{director or actor}'"
            ) from err
        else:  # get a random movie from the results
            res = choice([
                m for m, c in res if type(m) is api.Movie and
                c.job == ('Director' if director else 'Actor')
            ])
    else:
        raise TypeError(
            "You must provide one of: 'film', 'director', 'actor'."
        )
    runtime = res.runtime and f'{res.runtime // 60}h {res.runtime % 60}m'
    director = Person.from_args(*next((
        (c.job, p.name, p.tmdb_id) for p, c
        in res.crew if c.job == 'Director'
    ), ()))
    writer = Person.from_args(*next((
        (c.job, p.name, p.tmdb_id) for p, c in res.crew
        if c.job in ('Writer', 'Novel', 'Story')
    ), ()))
    thumb = res.posters[0].url['w342'] if res.posters else None
    lang = res.data.get('original_language', None)
    return Film(
        title=res.title['original'],
        url=f'{TMDB_URL}/movie/{res.tmdb_id}',
        description=res.overview['default'],
        thumbnail=thumb, language=lang,
        runtime=runtime, year=res.year,
        genres=[g.name for g in res.genres],
        score=res.vote.average, writer=writer,
        tagline=res.tagline, director=director
    )


def get_cast(*, film: str, year: Opt[SInt] = None) -> Film:
    """
    Get the cast of a film by the title.

    :param film: The title of the film.
    :param year: The year of the film. Only used
                 when ``film`` is also given.

    :raises TypeError: If no arguments were provided.
    :raises ApiError: If a film was not found.

    :return: A class containing the film's cast.
    """
    try:
        year = int(year) if year else None
        res = next(api.search_movie(film, year=year))
    except StopIteration as err:
        raise ApiError(
            f"Couldn't find a film titled '{film}'."
        ) from err
    return Film(
        title=res.title['original'],
        url=f'{TMDB_URL}/movie/{res.tmdb_id}',
        thumbnail=res.posters[0].url['w342'],
        cast=[Person.from_args(
            c.character, p.name, p.tmdb_id
        ) for p, c in res.cast[:10]]
    )


__all__ = [
    'TMDB_URL', 'ApiError',
    'get_film', 'get_cast',
    'api', 'Person', 'Film'
]
