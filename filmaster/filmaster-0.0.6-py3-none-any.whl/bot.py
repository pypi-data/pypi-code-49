"""Discord bot module."""
from os import getenv
from textwrap import shorten

from discord import Client, Embed

from .tmdb import TMDB_URL, Film

#: The bot client instance.
client = Client()

#: The command prefix of the bot.
PREFIX = '$'


class FilmEmbed(Embed):
    """A Discord :class:`~discord.Embed` made specifically for films."""
    @classmethod
    def from_film(cls, film: Film, *, cast: bool = False) -> 'FilmEmbed':
        """
        Create a new embed given a film object.

        :param film: The film to generate the embed from.
        :param cast: Whether the embed should show the cast of the film.

        :return: An instance of the class.
        """
        embed = super().from_dict({
            'url': film.url,
            'title': shorten(film.title, 256),
            'thumbnail': {'url': film.thumbnail},
            'provider': {'name': 'TMDB', 'url': TMDB_URL}
        })
        embed.colour = client.user.colour
        if cast:
            for person in film.cast:
                embed.add_field(name=person.role, value=person)
            return embed
        footer = shorten(film.tagline, 1280)
        genres = shorten(', '.join(film.genres) or 'None', 1024)
        writer = getattr(film.writer, 'role', 'Writer')
        embed.description = shorten(film.description, 2048)
        return embed.set_footer(text=footer) \
            .add_field(name='Language', value=film.language) \
            .add_field(name='Runtime', value=film.runtime) \
            .add_field(name='Year', value=film.year) \
            .add_field(name='Director', value=film.director) \
            .add_field(name='Score', value=film.score) \
            .add_field(name=writer, value=film.writer) \
            .add_field(name='Genres', value=genres, inline=False)


__all__ = ['PREFIX', 'client', 'FilmEmbed']
