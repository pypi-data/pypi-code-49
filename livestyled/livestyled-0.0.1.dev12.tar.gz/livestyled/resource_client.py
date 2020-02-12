from typing import Dict, Generator, Type

from marshmallow import Schema

from livestyled.client import LiveStyledAPIClient
from livestyled.models.competition import Competition
from livestyled.models.fixture import Fixture
from livestyled.models.league_table import LeagueTableGroup, LeagueTable
from livestyled.models.news import News
from livestyled.models.season import Season
from livestyled.models.sport_venue import SportVenue
from livestyled.models.team import Team
from livestyled.models.user import User, UserSSO
from livestyled.schemas.competition import CompetitionSchema
from livestyled.schemas.fixture import FixtureSchema
from livestyled.schemas.league_table import LeagueTableGroupSchema, LeagueTableSchema
from livestyled.schemas.news import NewsSchema
from livestyled.schemas.season import SeasonSchema
from livestyled.schemas.sport_venue import SportVenueSchema
from livestyled.schemas.team import TeamSchema
from livestyled.schemas.user import UserSchema, UserSSOSchema


class LiveStyledResourceClient(LiveStyledAPIClient):
    def __init__(
            self,
            api_domain: str,
            api_key: str
    ):
        super(LiveStyledResourceClient, self).__init__(api_domain, api_key)

    def _get_resource_list(
            self,
            resource_schema: Type[Schema],
            external_id: str or None = None,
            filters=None
    ):
        filter_params = {}
        if filters:
            filter_params = filters
        if external_id:
            filter_params['externalId'] = external_id
        resources = self._get_resources(
            resource_schema,
            params=filter_params
        )
        for resource in resources:
            yield resource_schema.Meta.model(**resource)

    def _get_resource_by_id(
            self,
            schema: Type[Schema],
            id: int
    ):
        return schema.Meta.model(**self._get_resource(id, schema))

    def _create_resource(
            self,
            schema: Type[Schema],
            model_instance
    ):
        if model_instance.id is not None:
            raise ValueError('Cannot create a {} with an ID'.format(schema.Meta.model.__name__))
        payload = schema().dump(model_instance)
        for key, value in list(payload.items()):
            if value is None:
                payload.pop(key)
        new_instance = self._api_post(
            '{}'.format(schema.Meta.url),
            payload
        )
        return schema.Meta.model(**schema().load(new_instance))

    def _update_resource(
            self,
            schema: Type[Schema],
            resource_id,
            attributes: Dict,
    ):
        attributes_to_update = list(attributes.keys())
        update_payload = schema(only=attributes_to_update).dump(attributes)
        updated_resource = self._api_patch(
            '{}/{}'.format(schema.Meta.url, resource_id),
            update_payload
        )
        return schema.Meta.model(**schema().load(updated_resource))

    def get_teams(
            self,
            external_id: str or None = None,
    ) -> Generator[Team, None, None]:
        return self._get_resource_list(TeamSchema, external_id)

    # ---- TEAMS

    def get_team(
            self,
            id: int
    ) -> Team:
        return self._get_resource_by_id(TeamSchema, id)

    def create_team(
            self,
            team: Team
    ) -> Team:
        return self._create_resource(TeamSchema, team)

    def update_team(
            self,
            team: Team,
            attributes: Dict
    ) -> Team:
        return self._update_resource(TeamSchema, team, attributes)
    
    # ---- FIXTURES

    def get_fixtures(
            self,
            external_id: str or None = None,
    ) -> Generator[Fixture, None, None]:
        return self._get_resource_list(FixtureSchema, external_id)

    def get_fixture(
            self,
            id: int
    ) -> Fixture:
        return self._get_resource_by_id(FixtureSchema, id)

    def create_fixture(
            self,
            fixture: Fixture
    ) -> Fixture:
        return self._create_resource(FixtureSchema, fixture)

    def update_fixture(
            self,
            fixture: Fixture,
            attributes: Dict
    ) -> Fixture:
        return self._update_resource(FixtureSchema, fixture, attributes)

    # ---- COMPETITIONS

    def get_competitions(
            self,
            external_id: str or None = None,
    ) -> Generator[Competition, None, None]:
        return self._get_resource_list(CompetitionSchema, external_id)

    def get_competition(
            self,
            id: int
    ) -> Competition:
        return self._get_resource_by_id(CompetitionSchema, id)

    def create_competition(
            self,
            competition: Competition
    ) -> Competition:
        return self._create_resource(CompetitionSchema, competition)

    def update_competition(
            self,
            competition: Competition,
            attributes: Dict
    ) -> Competition:
        return self._update_resource(CompetitionSchema, competition, attributes)

    # ---- SEASONS

    def get_seasons(
            self,
            external_id: str or None = None,
    ) -> Generator[Season, None, None]:
        return self._get_resource_list(SeasonSchema, external_id)

    def get_season(
            self,
            id: int
    ) -> Season:
        return self._get_resource_by_id(SeasonSchema, id)

    def create_season(
            self,
            season: Season
    ) -> Season:
        return self._create_resource(SeasonSchema, season)

    def update_season(
            self,
            season: Season,
            attributes: Dict
    ) -> Season:
        return self._update_resource(SeasonSchema, season, attributes)

    # ---- SPORTS VENUES

    def get_sport_venues(
            self,
            external_id: str or None = None,
    ) -> Generator[SportVenue, None, None]:
        return self._get_resource_list(SportVenueSchema, external_id)

    def get_sport_venue(
            self,
            id: int
    ) -> SportVenue:
        return self._get_resource_by_id(SportVenueSchema, id)

    def create_sport_venue(
            self,
            sport_venue: SportVenue
    ) -> SportVenue:
        return self._create_resource(SportVenueSchema, sport_venue)

    def update_sport_venue(
            self,
            sport_venue: SportVenue,
            attributes: Dict
    ) -> SportVenue:
        return self._update_resource(SportVenueSchema, sport_venue, attributes)

    # ---- LEAGUE TABLES

    def get_league_tables(
            self,
            external_id: str or None = None,
    ) -> Generator[LeagueTable, None, None]:
        return self._get_resource_list(LeagueTableSchema, external_id)

    def get_league_table(
            self,
            id: int
    ) -> LeagueTable:
        return self._get_resource_by_id(LeagueTableSchema, id)

    def create_league_table(
            self,
            league_table: LeagueTableSchema
    ) -> LeagueTable:
        return self._create_resource(LeagueTableSchema, league_table)

    def update_league_table(
            self,
            league_table: LeagueTableSchema,
            attributes: Dict
    ) -> LeagueTable:
        return self._update_resource(LeagueTableSchema, league_table, attributes)

    # ---- LEAGUE TABLE GROUPS

    def get_league_table_groups(
            self,
    ) -> Generator[LeagueTableGroup, None, None]:
        return self._get_resource_list(LeagueTableGroupSchema)

    def get_league_table_group(
            self,
            id: int
    ) -> LeagueTableGroup:
        return self._get_resource_by_id(LeagueTableGroupSchema, id)

    def create_league_table_group(
            self,
            league_table_group: LeagueTableSchema
    ) -> LeagueTableGroup:
        return self._create_resource(LeagueTableGroupSchema, league_table_group)

    def update_league_table_group(
            self,
            league_table: LeagueTableGroupSchema,
            attributes: Dict
    ) -> LeagueTableGroup:
        return self._update_resource(LeagueTableGroupSchema, league_table, attributes)

    # ---- NEWS

    def get_news_articles(
            self,
            external_id: str or None = None,
    ) -> Generator[News, None, None]:
        return self._get_resource_list(NewsSchema, external_id)

    def get_news_article(
            self,
            id: int
    ) -> News:
        return self._get_resource_by_id(NewsSchema, id)

    def create_news_article(
            self,
            news: News
    ) -> News:
        return self._create_resource(NewsSchema, news)

    def update_news(
            self,
            news: News,
            attributes: Dict
    ) -> NewsSchema:
        return self._update_resource(NewsSchema, news, attributes)

    # ---- USER

    def get_users(
            self,
            email: str or None = None,
    ) -> Generator[User, None, None]:
        if email:
            return self._get_resource_list(UserSchema, {'email': email})
        else:
            return self._get_resource_list(UserSchema)

    def get_user(
            self,
            id: int
    ) -> User:
        return self._get_resource_by_id(UserSchema, id)

    def create_user(
            self,
            user: User
    ) -> User:
        return self._create_resource(UserSchema, user)

    def update_user(
            self,
            user: User,
            attributes: Dict
    ) -> UserSchema:
        return self._update_resource(UserSchema, user, attributes)

    # ---- USER SSO

    def get_user_ssos(
            self,
            sub: str or None = None,
    ) -> Generator[UserSSO, None, None]:
        if sub:
            return self._get_resource_list(UserSSOSchema, {'sub': sub})
        else:
            return self._get_resource_list(UserSSOSchema)

    def get_user_sso(
            self,
            id: int
    ) -> UserSSO:
        return self._get_resource_by_id(UserSSOSchema, id)

    def create_user_sso(
            self,
            user_sso: UserSSO
    ) -> UserSSO:
        return self._create_resource(UserSSOSchema, user_sso)

    def update_user_sso(
            self,
            user_sso: UserSSO,
            attributes: Dict
    ) -> UserSSOSchema:
        return self._update_resource(UserSSOSchema, user_sso, attributes)
