from urllib.parse import urljoin

from qradar4py.endpoints.api_endpoint import QRadarAPIEndpoint
from qradar4py.endpoints.api_endpoint import request_vars
from qradar4py.endpoints.api_endpoint import header_vars


class Qvm(QRadarAPIEndpoint):
    """
    The QRadar API endpoint group /qvm and its endpoints.
    """
    __baseurl = 'qvm/'

    def __init__(self, url, header, verify):
        super().__init__(urljoin(url, self.__baseurl),
                         header,
                         verify)

    @request_vars('savedSearchId', 'savedSearchName', 'filters')
    def get_assets(self, *, savedSearchId=None, savedSearchName=None, filters=None, **kwargs):
        """
        GET /qvm/assets
        List the assets with discovered vulnerabilities present in the asset model.  The response will contain all available RESTful resources
        """
        function_endpoint = urljoin(self._baseurl, 'assets')
        return self._call('GET', function_endpoint, **kwargs)

    def get_filters(self, **kwargs):
        """
        GET /qvm/filters
        Get a list of the allowable filters that can be used or applied against the:

        /qvm/assets
        /qvm/vulns
        /qvm/vulninstances
        /qvm/openservices
        /qvm/networks
        queries

        """
        function_endpoint = urljoin(self._baseurl, 'filters')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('savedSearchId', 'savedSearchName', 'filters')
    def get_network(self, *, savedSearchId=None, savedSearchName=None, filters=None, **kwargs):
        """
        GET /qvm/network
        List the networks present in the asset model with vulnerabilities present.  The response will contain all available RESTful resources
        """
        function_endpoint = urljoin(self._baseurl, 'network')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('savedSearchId', 'savedSearchName', 'filters')
    def get_openservices(self, *, savedSearchId=None, savedSearchName=None, filters=None, **kwargs):
        """
        GET /qvm/openservices
        List the openservices present in the asset model with vulnerabilities present.  The response will contain all available RESTful resources
        """
        function_endpoint = urljoin(self._baseurl, 'openservices')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_saved_search_groups(self, *, fields=None, Range=None, filter=None, **kwargs):
        """
        GET /qvm/saved_search_groups
        Retrieves a list of vulnerability saved search groups.
        """
        function_endpoint = urljoin(self._baseurl, 'saved_search_groups')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_saved_search_groups_by_group_id(self, group_id, *, group, fields=None, **kwargs):
        """
        POST /qvm/saved_search_groups/{group_id}
        Updates the owner of an vulnerability saved search group.
        """
        function_endpoint = urljoin(self._baseurl, 'saved_search_groups/{group_id}'.format(group_id=group_id))
        return self._call('POST', function_endpoint, json=group, **kwargs)

    @request_vars('fields')
    def get_saved_search_groups_by_group_id(self, group_id, *, fields=None, **kwargs):
        """
        GET /qvm/saved_search_groups/{group_id}
        Retrieves a vulnerability saved search group.
        """
        function_endpoint = urljoin(self._baseurl, 'saved_search_groups/{group_id}'.format(group_id=group_id))
        return self._call('GET', function_endpoint, **kwargs)

    def delete_saved_search_groups_by_group_id(self, group_id, **kwargs):
        """
        DELETE /qvm/saved_search_groups/{group_id}
        Deletes a vulnerability saved search group.
        """
        function_endpoint = urljoin(self._baseurl, 'saved_search_groups/{group_id}'.format(group_id=group_id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_saved_searches(self, *, fields=None, Range=None, filter=None, **kwargs):
        """
        GET /qvm/saved_searches
        Retrieves a list of  vulnerability instance saved searches.
        """
        function_endpoint = urljoin(self._baseurl, 'saved_searches')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_saved_searches_vuln_instances_results_assets_by_task_id(self, task_id, *, fields=None, Range=None,
                                                                    filter=None, **kwargs):
        """
        GET /qvm/saved_searches/vuln_instances/{task_id}/results/assets
        Lists the Vulnerability Instances assets that are returned from the vulnerability instance saved search.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'saved_searches/vuln_instances/{task_id}/results/assets'.format(task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_saved_searches_vuln_instances_results_vuln_instances_by_task_id(self, task_id, *, fields=None, Range=None,
                                                                            filter=None, **kwargs):
        """
        GET /qvm/saved_searches/vuln_instances/{task_id}/results/vuln_instances
        Lists the Vulnerability Instances returned from a vulnerability instance saved search.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'saved_searches/vuln_instances/{task_id}/results/vuln_instances'.format(
                                        task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_saved_searches_vuln_instances_results_vulnerabilities_by_task_id(self, task_id, *, fields=None, Range=None,
                                                                             filter=None, **kwargs):
        """
        GET /qvm/saved_searches/vuln_instances/{task_id}/results/vulnerabilities
        List the Vulnerability Instances vulnerabilities returned from the saved search.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'saved_searches/vuln_instances/{task_id}/results/vulnerabilities'.format(
                                        task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('status', 'retention_period_in_days', 'fields')
    def post_saved_searches_vuln_instances_status_by_task_id(self, task_id, *, status=None,
                                                             retention_period_in_days=None, fields=None, **kwargs):
        """
        POST /qvm/saved_searches/vuln_instances/{task_id}/status
        Updates the status of a vulnerability instance saved search.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'saved_searches/vuln_instances/{task_id}/status'.format(task_id=task_id))
        return self._call('POST', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_saved_searches_vuln_instances_status_by_task_id(self, task_id, *, fields=None, **kwargs):
        """
        GET /qvm/saved_searches/vuln_instances/{task_id}/status
        Retrieves the current status of a vulnerability instance search that was initiated.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'saved_searches/vuln_instances/{task_id}/status'.format(task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    def delete_saved_searches_by_saved_search_id(self, saved_search_id, **kwargs):
        """
        DELETE /qvm/saved_searches/{saved_search_id}
        Deletes a vulnerability saved search.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'saved_searches/{saved_search_id}'.format(saved_search_id=saved_search_id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @request_vars('fields')
    def get_saved_searches_by_saved_search_id(self, saved_search_id, *, fields=None, **kwargs):
        """
        GET /qvm/saved_searches/{saved_search_id}
        Retrieves a vulnerability instance saved search.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'saved_searches/{saved_search_id}'.format(saved_search_id=saved_search_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_saved_searches_by_saved_search_id(self, saved_search_id, *, saved_search, fields=None, **kwargs):
        """
        POST /qvm/saved_searches/{saved_search_id}
        Updates the vulnerability saved search owner only.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'saved_searches/{saved_search_id}'.format(saved_search_id=saved_search_id))
        return self._call('POST', function_endpoint, json=saved_search, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_saved_searches_vuln_instances_by_saved_search_id(self, saved_search_id, *, fields=None, Range=None,
                                                             filter=None, **kwargs):
        """
        GET /qvm/saved_searches/{saved_search_id}/vuln_instances
        Creates the Vulnerability Instances search. This search will return a maximum of 100,000 results.
        """
        function_endpoint = urljoin(self._baseurl, 'saved_searches/{saved_search_id}/vuln_instances'.format(
            saved_search_id=saved_search_id))
        return self._call('GET', function_endpoint, **kwargs)

    def get_savedsearches(self, **kwargs):
        """
        GET /qvm/savedsearches
        Get a list of saved searchs that can be used or applied against the:

        /qvm/assets
        /qvm/vulns
        /qvm/vulninstances
        /qvm/openservices
        /qvm/networks
        queries

        """
        function_endpoint = urljoin(self._baseurl, 'savedsearches')
        return self._call('GET', function_endpoint, **kwargs)

    def post_tickets_assign(self, *, ticket, **kwargs):
        """
        POST /qvm/tickets/assign
        Update the remediation ticket for the assigned vulnerability
        """
        function_endpoint = urljoin(self._baseurl, 'tickets/assign')
        return self._call('POST', function_endpoint, json=ticket, **kwargs)

    @request_vars('savedSearchId', 'savedSearchName', 'filters')
    def get_vulninstances(self, *, savedSearchId=None, savedSearchName=None, filters=None, **kwargs):
        """
        GET /qvm/vulninstances
        List the Vulnerability Instances present in the asset model.  The response will contain all available RESTful resources
        """
        function_endpoint = urljoin(self._baseurl, 'vulninstances')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('savedSearchId', 'savedSearchName', 'filters')
    def get_vulns(self, *, savedSearchId=None, savedSearchName=None, filters=None, **kwargs):
        """
        GET /qvm/vulns
        List the Vulnerabilities present in the asset model.  The response will contain all available RESTful resources
        """
        function_endpoint = urljoin(self._baseurl, 'vulns')
        return self._call('GET', function_endpoint, **kwargs)
