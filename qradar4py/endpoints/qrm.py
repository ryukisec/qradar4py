from urllib.parse import urljoin

from qradar4py.endpoints.api_endpoint import QRadarAPIEndpoint
from qradar4py.endpoints.api_endpoint import request_vars
from qradar4py.endpoints.api_endpoint import header_vars


class Qrm(QRadarAPIEndpoint):
    """
    The QRadar API endpoint group /qrm and its endpoints.
    """
    __baseurl = 'qrm/'

    def __init__(self, url, header, verify):
        super().__init__(urljoin(url, self.__baseurl),
                         header,
                         verify)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_model_groups(self, *, Range=None, filter=None, fields=None, **kwargs):
        """
        GET /qrm/model_groups
        Retrieves a list of model groups.
        """
        function_endpoint = urljoin(self._baseurl, 'model_groups')
        return self._call('GET', function_endpoint, **kwargs)

    def delete_model_groups_by_group_id(self, group_id, **kwargs):
        """
        DELETE /qrm/model_groups/{group_id}
        Deletes a model group.
        """
        function_endpoint = urljoin(self._baseurl, 'model_groups/{group_id}'.format(group_id=group_id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @header_vars('fields')
    def post_model_groups_by_group_id(self, group_id, *, group, fields=None, **kwargs):
        """
        POST /qrm/model_groups/{group_id}
        Updates the owner of a model group.
        """
        function_endpoint = urljoin(self._baseurl, 'model_groups/{group_id}'.format(group_id=group_id))
        return self._call('POST', function_endpoint, json=group, **kwargs)

    @request_vars('fields')
    def get_model_groups_by_group_id(self, group_id, *, fields=None, **kwargs):
        """
        GET /qrm/model_groups/{group_id}
        Retrieves a model group.
        """
        function_endpoint = urljoin(self._baseurl, 'model_groups/{group_id}'.format(group_id=group_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_qrm_saved_search_groups(self, *, Range=None, filter=None, fields=None, **kwargs):
        """
        GET /qrm/qrm_saved_search_groups
        Retrieves a list of QRM saved search groups.
        """
        function_endpoint = urljoin(self._baseurl, 'qrm_saved_search_groups')
        return self._call('GET', function_endpoint, **kwargs)

    def delete_qrm_saved_search_groups_by_group_id(self, group_id, **kwargs):
        """
        DELETE /qrm/qrm_saved_search_groups/{group_id}
        Deletes a QRM saved search group.
        """
        function_endpoint = urljoin(self._baseurl, 'qrm_saved_search_groups/{group_id}'.format(group_id=group_id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @request_vars('fields')
    def get_qrm_saved_search_groups_by_group_id(self, group_id, *, fields=None, **kwargs):
        """
        GET /qrm/qrm_saved_search_groups/{group_id}
        Retrieves a QRM saved search group.
        """
        function_endpoint = urljoin(self._baseurl, 'qrm_saved_search_groups/{group_id}'.format(group_id=group_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_qrm_saved_search_groups_by_group_id(self, group_id, *, group, fields=None, **kwargs):
        """
        POST /qrm/qrm_saved_search_groups/{group_id}
        Updates the owner of a QRM saved search group.
        """
        function_endpoint = urljoin(self._baseurl, 'qrm_saved_search_groups/{group_id}'.format(group_id=group_id))
        return self._call('POST', function_endpoint, json=group, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_question_groups(self, *, Range=None, filter=None, fields=None, **kwargs):
        """
        GET /qrm/question_groups
        Retrieves a list of question groups.
        """
        function_endpoint = urljoin(self._baseurl, 'question_groups')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_question_groups_by_group_id(self, group_id, *, group, fields=None, **kwargs):
        """
        POST /qrm/question_groups/{group_id}
        Updates the owner of a question group.
        """
        function_endpoint = urljoin(self._baseurl, 'question_groups/{group_id}'.format(group_id=group_id))
        return self._call('POST', function_endpoint, json=group, **kwargs)

    def delete_question_groups_by_group_id(self, group_id, **kwargs):
        """
        DELETE /qrm/question_groups/{group_id}
        Deletes a question group.
        """
        function_endpoint = urljoin(self._baseurl, 'question_groups/{group_id}'.format(group_id=group_id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @request_vars('fields')
    def get_question_groups_by_group_id(self, group_id, *, fields=None, **kwargs):
        """
        GET /qrm/question_groups/{group_id}
        Retrieves a question group.
        """
        function_endpoint = urljoin(self._baseurl, 'question_groups/{group_id}'.format(group_id=group_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_simulation_groups(self, *, Range=None, filter=None, fields=None, **kwargs):
        """
        GET /qrm/simulation_groups
        Retrieves a of list the simulation groups.
        """
        function_endpoint = urljoin(self._baseurl, 'simulation_groups')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_simulation_groups_by_group_id(self, group_id, *, group, fields=None, **kwargs):
        """
        POST /qrm/simulation_groups/{group_id}
        Updates the owner of a simulation group.
        """
        function_endpoint = urljoin(self._baseurl, 'simulation_groups/{group_id}'.format(group_id=group_id))
        return self._call('POST', function_endpoint, json=group, **kwargs)

    def delete_simulation_groups_by_group_id(self, group_id, **kwargs):
        """
        DELETE /qrm/simulation_groups/{group_id}
        Deletes a simulation group.
        """
        function_endpoint = urljoin(self._baseurl, 'simulation_groups/{group_id}'.format(group_id=group_id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @request_vars('fields')
    def get_simulation_groups_by_group_id(self, group_id, *, fields=None, **kwargs):
        """
        GET /qrm/simulation_groups/{group_id}
        Retrieves a simulation group.
        """
        function_endpoint = urljoin(self._baseurl, 'simulation_groups/{group_id}'.format(group_id=group_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_topology_saved_search_groups(self, *, Range=None, filter=None, fields=None, **kwargs):
        """
        GET /qrm/topology_saved_search_groups
        Retrieves a list of topology saved search groups.
        """
        function_endpoint = urljoin(self._baseurl, 'topology_saved_search_groups')
        return self._call('GET', function_endpoint, **kwargs)

    def delete_topology_saved_search_groups_by_group_id(self, group_id, **kwargs):
        """
        DELETE /qrm/topology_saved_search_groups/{group_id}
        Deletes a topology saved search group.
        """
        function_endpoint = urljoin(self._baseurl, 'topology_saved_search_groups/{group_id}'.format(group_id=group_id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @header_vars('fields')
    def post_topology_saved_search_groups_by_group_id(self, group_id, *, group, fields=None, **kwargs):
        """
        POST /qrm/topology_saved_search_groups/{group_id}
        Updates the owner of an topology saved search group.
        """
        function_endpoint = urljoin(self._baseurl, 'topology_saved_search_groups/{group_id}'.format(group_id=group_id))
        return self._call('POST', function_endpoint, json=group, **kwargs)

    @request_vars('fields')
    def get_topology_saved_search_groups_by_group_id(self, group_id, *, fields=None, **kwargs):
        """
        GET /qrm/topology_saved_search_groups/{group_id}
        Retrieves a topology saved search group.
        """
        function_endpoint = urljoin(self._baseurl, 'topology_saved_search_groups/{group_id}'.format(group_id=group_id))
        return self._call('GET', function_endpoint, **kwargs)
