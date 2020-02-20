from unittest import mock
from uuid import uuid4

from minty.cqrs import EventService


class InfraFactoryMock:
    """Mock for our InfraFactory"""

    def __init__(self, infra):
        self.infra = infra

    def get_infrastructure(self, context, infrastructure_name):
        return self.infra[infrastructure_name]


class MockRepositoryFactory:
    """Mock for our repository factory"""

    def __init__(self, infra_factory):
        self.infrastructure_factory = infra_factory
        self.repositories = {}

    def get_repository(self, name, context, event_service):
        mock_repo = self.repositories[name]
        return mock_repo


class TestBase:
    """Utilities for making tests on our CQRS infrastructure without
    database access
    """

    def load_query_instance(
        self, domain: object, repositoryname: str, inframocks: dict = {}
    ):
        """ Loads your object with a qry attribute pointing to the query
        instance

        Will set the self.qry property to the loaded Queries() object,
        containing mocks for:
        * Database
        * S3

        Args:
            domain: Domain object to use in this test,
            e.g.: zsnl_domains.case_management
            repositoryname: The repository to use, e.g.: "case"
            inframocks: A key-value pair containing mocks for every component
            (e.g { "database": MagicMock })

        """

        mock_session = mock.MagicMock()
        self.qry = self._get_mocked_domain_instance(
            session_mock=mock_session,
            domain=domain,
            repositoryname=repositoryname,
            instance_type="query",
            inframocks=inframocks,
        )
        self.session = mock_session

    def load_command_instance(
        self, domain: object, repositoryname: str, inframocks: dict = {}
    ):
        """ Loads your object with a cmd attribute pointing to the command
        instance

        Will set the self.cmd property to the loaded Queries() object,
        containing mocks for:
        * Database
        * S3

        Args:
            domain: Domain object to use in this test,
                    e.g.: zsnl_domains.case_management
            repositoryname: The repository to use, e.g.: "case"
            inframocks: A key-value pair containing mocks for every component
                        (e.g { "database": MagicMock })

        """

        mock_session = mock.MagicMock()
        self.cmd = self._get_mocked_domain_instance(
            session_mock=mock_session,
            domain=domain,
            repositoryname=repositoryname,
            instance_type="command",
            inframocks=inframocks,
        )
        self.session = mock_session

    def assert_has_event_name(self, event_name: str, description: str = None):
        list_of_events = [
            ev
            for ev in self.cmd.event_service.event_list
            if ev.event_name == event_name
        ]

        if description:
            assert len(list_of_events) > 0, description
        else:
            assert len(list_of_events) > 0

        return True

    def get_last_sql_query(self):
        (args, kwargs) = self.session.execute.call_args
        query = args[0].compile()

        return query

    def _get_mocked_domain_instance(
        self,
        session_mock,
        domain,
        repositoryname,
        instance_type,
        inframocks={},
        user_uuid=None,
    ):
        """Generates a mock for a command or query instance"""

        # Some defaults
        mocked_infra = {
            "database": session_mock,
            "s3": mock.MagicMock(),
            **inframocks,
        }

        repository = domain.REQUIRED_REPOSITORIES[repositoryname]

        if not user_uuid:
            user_uuid = str(uuid4())

        event_service = EventService(
            correlation_id=str(uuid4()),
            domain="domain",
            context="context",
            user_uuid=user_uuid,
        )

        infra = InfraFactoryMock(infra=mocked_infra)
        repo_factory = MockRepositoryFactory(infra_factory=infra)
        repo_factory.repositories[repositoryname] = repository(
            infrastructure_factory=infra,
            context=None,
            event_service=event_service,
        )

        if instance_type == "query":
            return domain.get_query_instance(
                repository_factory=repo_factory,
                context=None,
                user_uuid=user_uuid,
            )
        elif instance_type == "command":
            return domain.get_command_instance(
                repository_factory=repo_factory,
                event_service=event_service,
                context=None,
                user_uuid=user_uuid,
            )
