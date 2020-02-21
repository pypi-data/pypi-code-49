import json
import sys

from sonarqube_api.exceptions import ValidationError, ClientError


class SonarAPIQGates(object):
    # Endpoint for resources and rules
    LIST_ENDPOINT = '/api/qualitygates/list'
    DETAIL_ENDPOINT = '/api/qualitygates/show'
    CREATE_ENDPOINT = '/api/qualitygates/create'
    DESTROY_ENDPOINT = '/api/qualitygates/destroy'
    SELECT_ENDPOINT = '/api/qualitygates/select'
    SEARCH_ENDPOINT = '/api/qualitygates/search'

    CREATE_COND_ENDPOINT = '/api/qualitygates/create_condition'
    DELETE_COND_ENDPOINT = '/api/qualitygates/delete_condition'
    UPDATE_COND_ENDPOINT = '/api/qualitygates/update_condition'

    def __init__(self, api=None):
        self._api = api

    def create_quality_gate_from_json(self, data, project_name):
        """
        create quality gate and conditions with json information
        if quality gate already exists it deletes it

        :param data: json information

        :return: request response
        """

        # Set the quality gate's name to the project's name
        data["name"] = project_name

        # Check if the qg exists already, and if so, deletes it
        try:
            existing_qg = self.show(None, data["name"])
            if existing_qg is not None:
                self.destroy(existing_qg["id"])
        except:
            # QG does not exist
            True

        qualitygate = self.create(data["name"])
        if qualitygate is not None:
            for c in data['conditions']:
                self.create_condition(qualitygate["id"], c["metric"], c["op"], c["error"])
            return qualitygate

    def list(self):
        """
        list quality gates.

        :return: request response
        """
        # Make call (might raise exception) and return
        res = self._api._make_call('get', self.LIST_ENDPOINT)
        return json.loads(res.content)

    def show(self, id=None, name=None):
        """
        get quality gate details, using id or name (id is prior is both are set)

        :param id: id of the quality gate
        :param name: name of the quality gate
        :return: request response
        """
        # Build main data to post
        params = {
            'id' if id is not None else 'name': id if id is not None else name
        }

        # Make call (might raise exception) and return
        res = self._api._make_call('get', self.DETAIL_ENDPOINT, params=params)
        return json.loads(res.content)

    def create(self, name):
        """
        create a new empty quality agte

        :param name: name of the quality gate
        :return: request response
        """
        # Build main data to post
        data = {
            'name': name
        }

        # Make call (might raise exception) and return
        try:
            res = self._api._make_call('post', self.CREATE_ENDPOINT, data=data)
            return json.loads(res.content)
        except ValidationError:
            print ('Error trying to create quality gate: ', sys.exc_info()[1])

    def destroy(self, id):
        """
        delete a quality agte

        :param id: id of the quality gate
        :return: 204 no content
        """
        # Build main data to post
        data = {
            'id': id
        }

        # Make call (return nothing)
        self._api._make_call('post', self.DESTROY_ENDPOINT, data=data)

    def select(self, gateId, projectId):
        """
        assign a quality gate to a project

        :param gateId: id of the quality gate
        :param projectid: id of the project
        :return: 204 no content
        """
        # Build main data to post
        data = {
            'gateId': gateId,
            'projectId': projectId
        }

        # Make call (return nothing)
        self._api._make_call('post', self.SELECT_ENDPOINT, data=data)

    def search_project(self, gateId, query, ps=50, selected='all'):
        """
        get projets list.

        :param gateId: Id of the qualitygate
        :param query: query to send
        :param ps: pageSize
        :param selected: all/selected/deselected
        :return: request response
        """
        # Build main data to post
        query = {
            'query': query,
            'ps': ps,
            'selected': selected,
            'gateId': gateId
        }

        # Make call (might raise exception) and return
        res = self._api._make_call('post', self.SEARCH_ENDPOINT, params=query)
        return json.loads(res.content)

    def create_condition(self, gateid, metric, op, error):
        """
        create a condition for a quality gate

        :param gateid: id of the quality gate
        :param metric: metric of the condition
        :param op: operator of the condition
        :param error: value of the condition
        :return: request response
        """
        # Build main data to post
        data = {
            'gateId': gateid,
            'metric': metric,
            'op': op,
            'error': error
        }

        # Make call (might raise exception) and return
        try:
            res = self._api._make_call('post', self.CREATE_COND_ENDPOINT, data=data)
            return json.loads(res.content)
        except ClientError:
            print ('Error trying to create condition for quality gate %s with metric %s, op %s, and error %s.' % (gateid, metric, op, error))

    def delete_condition(self, id):
        """
        delete a condition in quality gate

        :param id: id of the condition gate
        :return: request response
        """
        # Build main data to post
        data = {
            'id': id
        }

        # Make call (might raise exception) and return
        res = self._api._make_call('post', self.DELETE_COND_ENDPOINT, data=data)
        # Return none in case of 404 not found
        if res is None:
            return res
        return json.loads(res.content)

    def update_condition(self, id, metric, op, error):
        """
        update a condition for a quality gate

        :param id: id of the condition
        :param metric: metric of the condition
        :param op: operator of the condition
        :param error: value of the condition
        :return: request response
        """
        # Build main data to post
        data = {
            'id': id,
            'metric': metric,
            'op': op,
            'error': error
        }

        # Make call (might raise exception) and return
        res = self._api._make_call('post', self.UPDATE_COND_ENDPOINT, data=data)
        return json.loads(res.content)