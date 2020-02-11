# Imports go here!
from .api_bio_get import ApiBioGetStar
from .api_bio_set import ApiBioSetStar
from .api_diario_get import ApiDiarioGetStar
from .api_diario_list import ApiDiarioListStar
from .api_user_list import ApiUserListStar
from .api_user_get import ApiUserGetStar
from .api_discord_cv import ApiDiscordCvStar
from .api_discord_play import ApiDiscordPlayStar
from .api_wiki_edit import ApiWikiEditStar
from .api_wiki_get import ApiWikiGetStar
from .api_wiki_list import ApiWikiListStar

# Enter the PageStars of your Pack here!
available_page_stars = [
    ApiBioGetStar,
    ApiBioSetStar,
    ApiDiarioGetStar,
    ApiDiarioListStar,
    ApiDiscordCvStar,
    ApiDiscordPlayStar,
    ApiUserGetStar,
    ApiUserListStar,
    ApiWikiEditStar,
    ApiWikiGetStar,
    ApiWikiListStar,
]

# Don't change this, it should automatically generate __all__
__all__ = [star.__name__ for star in available_page_stars]
