from urllib.parse import urljoin

from qradar4py.endpoints.api_endpoint import QRadarAPIEndpoint
from qradar4py.endpoints.api_endpoint import request_vars
from qradar4py.endpoints.api_endpoint import header_vars


class DynamicSearch(QRadarAPIEndpoint):
    """
    The QRadar API endpoint group /dynamic_search and its endpoints.
    """
    __baseurl = 'dynamic_search/'

    def __init__(self, url, header, verify):
        super().__init__(urljoin(url, self.__baseurl),
                         header,
                         verify)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_saved_queries(self, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /dynamic_search/saved_queries
        Returns a list of all queries to which the caller has access.
        """
        function_endpoint = urljoin(self._baseurl, 'saved_queries')
        return self._call('GET', function_endpoint, **kwargs)

    def post_saved_queries(self, *, query, **kwargs):
        """
        POST /dynamic_search/saved_queries
        Creates a query to be saved for use in dynamic searches. A query represents a request for data. Queries are not the same as searches, which are the results of a request for data. The benefit of saving a query is that it may be referenced in dynamic searches and can be reused.
        """
        function_endpoint = urljoin(self._baseurl, 'saved_queries')
        return self._call('POST', function_endpoint, json=query, **kwargs)

    @request_vars('fields')
    def get_saved_queries_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /dynamic_search/saved_queries/{id}
        Returns a single query with the specified ID. The caller must have access to the query.
        """
        function_endpoint = urljoin(self._baseurl, 'saved_queries/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    def delete_saved_queries_by_id(self, id, **kwargs):
        """
        DELETE /dynamic_search/saved_queries/{id}
        Removes the specified query from the system.
        """
        function_endpoint = urljoin(self._baseurl, 'saved_queries/{id}'.format(id=id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_schemas(self, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /dynamic_search/schemas
        Gets the list of all schemas available to the user.
        """
        function_endpoint = urljoin(self._baseurl, 'schemas')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_schemas_by_name(self, name, *, fields=None, **kwargs):
        """
        GET /dynamic_search/schemas/{name}
        Gets the list of all schemas available to the user.
        """
        function_endpoint = urljoin(self._baseurl, 'schemas/{name}'.format(name=name))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_schemas_fields_by_name(self, name, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /dynamic_search/schemas/{name}/fields
        Gets the list of all available Fields
        """
        function_endpoint = urljoin(self._baseurl, 'schemas/{name}/fields'.format(name=name))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_schemas_functions_by_name(self, name, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /dynamic_search/schemas/{name}/functions
        Gets the list of all available Functions
        """
        function_endpoint = urljoin(self._baseurl, 'schemas/{name}/functions'.format(name=name))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_schemas_operators_by_name(self, name, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /dynamic_search/schemas/{name}/operators
        Gets the list of all available relational Operators
        """
        function_endpoint = urljoin(self._baseurl, 'schemas/{name}/operators'.format(name=name))
        return self._call('GET', function_endpoint, **kwargs)

    def post_searches(self, *, search, **kwargs):
        """
        POST /dynamic_search/searches
        Posts a search to be performed by the service.
        """
        function_endpoint = urljoin(self._baseurl, 'searches')
        return self._call('POST', function_endpoint, json=search, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_searches(self, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /dynamic_search/searches
        Gets the list of all searches performed by this user.
        """
        function_endpoint = urljoin(self._baseurl, 'searches')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_searches_by_handle(self, handle, *, fields=None, **kwargs):
        """
        GET /dynamic_search/searches/{handle}
        Gets the specific search performed by this user.
        """
        function_endpoint = urljoin(self._baseurl, 'searches/{handle}'.format(handle=handle))
        return self._call('GET', function_endpoint, **kwargs)

    def delete_searches_by_handle(self, handle, **kwargs):
        """
        DELETE /dynamic_search/searches/{handle}
        Deletes a search and any stored results.
        """
        function_endpoint = urljoin(self._baseurl, 'searches/{handle}'.format(handle=handle))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    def get_searches_results_by_handle(self, handle, **kwargs):
        """
        GET /dynamic_search/searches/{handle}/results
        Gets the specific search performed by this user.
        """
        function_endpoint = urljoin(self._baseurl, 'searches/{handle}/results'.format(handle=handle))
        return self._call('GET', function_endpoint, **kwargs)
