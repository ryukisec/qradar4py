from urllib.parse import urljoin

from qradar4py.endpoints.api_endpoint import QRadarAPIEndpoint
from qradar4py.endpoints.api_endpoint import request_vars
from qradar4py.endpoints.api_endpoint import header_vars


class ReferenceDataCollections(QRadarAPIEndpoint):
    """
    The QRadar API endpoint group /reference_data_collections and its endpoints.
    """
    __baseurl = 'reference_data_collections/'

    def __init__(self, url, header, verify):
        super().__init__(urljoin(url, self.__baseurl),
                         header,
                         verify)

    @request_vars('fields')
    def get_set_bulk_update_tasks_by_task_status_id(self, task_status_id, *, fields=None, **kwargs):
        """
        GET /reference_data_collections/set_bulk_update_tasks/{task_status_id}
        Get the Bulk Update status
        """
        function_endpoint = urljoin(self._baseurl,
                                    'set_bulk_update_tasks/{task_status_id}'.format(task_status_id=task_status_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_set_bulk_update_tasks_results_by_task_status_id(self, task_status_id, *, fields=None, **kwargs):
        """
        GET /reference_data_collections/set_bulk_update_tasks/{task_status_id}/results
        Get the results of the Bulk Update task
        """
        function_endpoint = urljoin(self._baseurl, 'set_bulk_update_tasks/{task_status_id}/results'.format(
            task_status_id=task_status_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_set_delete_tasks_by_task_status_id(self, task_status_id, *, fields=None, **kwargs):
        """
        GET /reference_data_collections/set_delete_tasks/{task_status_id}
        Get results of the asynchronous delete Set task
        """
        function_endpoint = urljoin(self._baseurl,
                                    'set_delete_tasks/{task_status_id}'.format(task_status_id=task_status_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_set_dependents_tasks_by_task_status_id(self, task_status_id, *, fields=None, **kwargs):
        """
        GET /reference_data_collections/set_dependents_tasks/{task_status_id}
        Get the status of the Get Dependents task
        """
        function_endpoint = urljoin(self._baseurl,
                                    'set_dependents_tasks/{task_status_id}'.format(task_status_id=task_status_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_set_dependents_tasks_by_task_status_id(self, task_status_id, *, body, fields=None, **kwargs):
        """
        POST /reference_data_collections/set_dependents_tasks/{task_status_id}
        Cancel the Get Dependents request
        """
        function_endpoint = urljoin(self._baseurl,
                                    'set_dependents_tasks/{task_status_id}'.format(task_status_id=task_status_id))
        return self._call('POST', function_endpoint, json=body, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_set_dependents_tasks_results_by_task_status_id(self, task_status_id, *, fields=None, filter=None,
                                                           Range=None, **kwargs):
        """
        GET /reference_data_collections/set_dependents_tasks/{task_status_id}/results
        Get the results of the Get Dependents task
        """
        function_endpoint = urljoin(self._baseurl, 'set_dependents_tasks/{task_status_id}/results'.format(
            task_status_id=task_status_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_set_entries(self, *, body, fields=None, **kwargs):
        """
        POST /reference_data_collections/set_entries
        Create an entry within a set
        """
        function_endpoint = urljoin(self._baseurl, 'set_entries')
        return self._call('POST', function_endpoint, json=body, **kwargs)

    @header_vars('fields')
    def patch_set_entries(self, *, body, fields=None, **kwargs):
        """
        PATCH /reference_data_collections/set_entries
        Perform asynchronous bulk update - series of add and updates
        """
        if not isinstance(body, list):
            body = [body]
        function_endpoint = urljoin(self._baseurl, 'set_entries')
        return self._call('PATCH', function_endpoint, json=body, **kwargs)

    @header_vars('Range')
    @request_vars('entry_type', 'fields', 'filter', 'sort')
    def get_set_entries(self, *, entry_type=None, fields=None, filter=None, sort=None, Range=None, **kwargs):
        """
        GET /reference_data_collections/set_entries
        Get a list of set entries which match a search criteria.
        """
        function_endpoint = urljoin(self._baseurl, 'set_entries')
        return self._call('GET', function_endpoint, **kwargs)

    def delete_set_entries_by_id(self, id, **kwargs):
        """
        DELETE /reference_data_collections/set_entries/{id}
        Delete a set entry
        """
        function_endpoint = urljoin(self._baseurl, 'set_entries/{id}'.format(id=id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @header_vars('fields')
    def post_set_entries_by_id(self, id, *, body, fields=None, **kwargs):
        """
        POST /reference_data_collections/set_entries/{id}
        Update a Set Entry given the properties based in the body DTO. Only the notes field
        can be modified in an existing entry. The source and last_seen timestamp will be updated
        automatically.
        """
        function_endpoint = urljoin(self._baseurl, 'set_entries/{id}'.format(id=id))
        return self._call('POST', function_endpoint, json=body, **kwargs)

    @request_vars('fields')
    def get_set_entries_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /reference_data_collections/set_entries/{id}
        Get a set entry
        """
        function_endpoint = urljoin(self._baseurl, 'set_entries/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter', 'sort')
    def get_sets(self, *, fields=None, filter=None, sort=None, Range=None, **kwargs):
        """
        GET /reference_data_collections/sets
        Get a list of set meta data information based on search criteria
        """
        function_endpoint = urljoin(self._baseurl, 'sets')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_sets(self, *, body, fields=None, **kwargs):
        """
        POST /reference_data_collections/sets
        Create a set given the properties based in the body DTO
        """
        function_endpoint = urljoin(self._baseurl, 'sets')
        return self._call('POST', function_endpoint, json=body, **kwargs)

    @request_vars('fields')
    def get_sets_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /reference_data_collections/sets/{id}
        Get the meta data information for a specific set
        """
        function_endpoint = urljoin(self._baseurl, 'sets/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def delete_sets_by_id(self, id, *, fields=None, **kwargs):
        """
        DELETE /reference_data_collections/sets/{id}
        Delete a set by starting an asynchronous task
        """
        function_endpoint = urljoin(self._baseurl, 'sets/{id}'.format(id=id))
        return self._call('DELETE', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_sets_by_id(self, id, *, body, fields=None, **kwargs):
        """
        POST /reference_data_collections/sets/{id}
        Update a Set given the properties based in the body DTO
        """
        function_endpoint = urljoin(self._baseurl, 'sets/{id}'.format(id=id))
        return self._call('POST', function_endpoint, json=body, **kwargs)

    @request_vars('fields')
    def get_sets_dependents_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /reference_data_collections/sets/{id}/dependents
        Create an asynchronous task to get the dependents of a Set
        """
        function_endpoint = urljoin(self._baseurl, 'sets/{id}/dependents'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)
