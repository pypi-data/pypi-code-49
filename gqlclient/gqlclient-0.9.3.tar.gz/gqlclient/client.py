"""
Implementation of the Base graphql client to support the synchronous creation and
execution of graphql queries and mutations
"""
import logging

import requests

from gqlclient.base import GraphQLClientBase
from gqlclient.exceptions import ServerConnectionException, ServerResponseException


__all__ = ["GraphQLClient"]


logger = logging.getLogger(__name__)


class GraphQLClient(GraphQLClientBase):
    """
    Helper class for formatting and executing synchronous GraphQL queries and mutations
    """

    def execute_gql_call(self, query: dict) -> dict:
        """
        Executes a GraphQL query or mutation using requests.

        :param query: Dictionary formatted graphql query

        :return: Dictionary containing the response from the GraphQL endpoint
        """
        logger.debug(f"Executing graphql call: host={self.gql_uri}")
        try:
            response = requests.post(url=self.gql_uri, json=query)
        except requests.ConnectionError as e:
            logger.error(
                f"Error connecting to graphql server: " f"server={self.gql_uri}, " f"detail={e}"
            )
            raise ServerConnectionException(
                f"Error connecting to graphql server: " f"server={self.gql_uri}, " f"detail={e}"
            )
        # GraphQL encodes most errors within the body of a 200 response.
        # Non 200 statuses represent something outside of the query parsing and
        # execution having failed.
        if response.status_code > 499:
            raise ServerResponseException(
                f"Server returned invalid response: "
                f"code=HTTP{response.status_code}, "
                f"detail={response.json()} "
            )
        return response.json()
