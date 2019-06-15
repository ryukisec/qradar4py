from urllib.parse import urljoin

from qradar4py.endpoints.api_endpoint import QRadarAPIEndpoint
from qradar4py.endpoints.api_endpoint import request_vars
from qradar4py.endpoints.api_endpoint import header_vars


class HistoricalCorrelation(QRadarAPIEndpoint):
    """
    The QRadar API endpoint group /historical_correlation and its endpoints.
    UNDOCUMENTED
    """
    __baseurl = 'historical_correlation/'

    def __init__(self, url, header, verify):
        super().__init__(urljoin(url, self.__baseurl),
                         header,
                         verify)

    @request_vars('offense_id', 'fields')
    def get_hc_offense_info(self, *, offense_id, fields=None, **kwargs):
        """
        GET /historical_correlation/hc_offense_info
        Retrieves a historical correlation instance information associated with given offense
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'hc_offense_info')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_potential_event_rules(self, *, fields=None, Range=None, filter=None, **kwargs):
        """
        GET /historical_correlation/potential_event_rules
        Retrieves a list of common/event custom rules that can be added to a historical correlation
        profile with a network_event_type of event (0).
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'potential_event_rules')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_potential_event_saved_searches(self, *, fields=None, Range=None, filter=None, **kwargs):
        """
        GET /historical_correlation/potential_event_saved_searches
        Retrieves a list of non-aggregated event saved searches that can be added to a historical correlation
        profile with a network_event_type of event (0).
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'potential_event_saved_searches')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_potential_flow_rules(self, *, fields=None, Range=None, filter=None, **kwargs):
        """
        GET /historical_correlation/potential_flow_rules
        Retrieves a list of common/flow rules that can added to a historical correlation profile with a
        network_event_type of flow (1).
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'potential_flow_rules')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_potential_flow_saved_searches(self, *, fields=None, Range=None, filter=None, **kwargs):
        """
        GET /historical_correlation/potential_flow_saved_searches
        Retrieves a list of non-aggregated flow saved searches that can be added to a historical correlation
        profile with a network_event_type of flow (1).
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'potential_flow_saved_searches')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'sort', 'filter')
    def get_profiles(self, *, fields=None, Range=None, sort=None, filter=None, **kwargs):
        """
        GET /historical_correlation/profiles
        Retrieves a list of historical correlation profiles
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'profiles')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('fields')
    def post_profiles(self, *, profileData, fields=None, **kwargs):
        """
        POST /historical_correlation/profiles
        Create a new historical correlation profile
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'profiles')
        return self._call('POST', function_endpoint, json=profileData, headers=headers, **kwargs)

    def delete_profiles_by_id(self, id, **kwargs):
        """
        DELETE /historical_correlation/profiles/{id}
        Delete a Historical Correlation Profile by Id
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'profiles/{id}'.format(id=id))
        return self._call('DELETE', function_endpoint, headers=headers, **kwargs)

    @header_vars('fields')
    def post_profiles_by_id(self, id, *, profileData, fields=None, **kwargs):
        """
        POST /historical_correlation/profiles/{id}
        Update a historical correlation profile
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'profiles/{id}'.format(id=id))
        return self._call('POST', function_endpoint, json=profileData, headers=headers, **kwargs)

    @request_vars('fields')
    def get_profiles_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /historical_correlation/profiles/{id}
        Get a Historical Search Profile by Id
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'profiles/{id}'.format(id=id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def post_profiles_runs_by_id(self, id, *, fields=None, **kwargs):
        """
        POST /historical_correlation/profiles/{id}/runs
        Causes the Historical Profile server to run a given historical correlation profile.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'profiles/{id}/runs'.format(id=id))
        return self._call('POST', function_endpoint, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'sort', 'filter')
    def get_profiles_runs_by_id(self, id, *, fields=None, Range=None, sort=None, filter=None, **kwargs):
        """
        GET /historical_correlation/profiles/{id}/runs
        Retrieves a collection of historical correlation profile run structure for a given profile id.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'profiles/{id}/runs'.format(id=id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_profiles_id_runs_by_run_id(self, id, run_id, *, fields=None, **kwargs):
        """
        GET /historical_correlation/profiles/{id}/runs/{run_id}
        Retrieves a historical correlation profile run structure for a given profile running id.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'profiles/{id}/runs/{run_id}'.format(id=id, run_id=run_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)
