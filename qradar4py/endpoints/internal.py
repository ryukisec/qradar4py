from urllib.parse import urljoin

from qradar4py.endpoints.api_endpoint import QRadarAPIEndpoint
from qradar4py.endpoints.api_endpoint import request_vars
from qradar4py.endpoints.api_endpoint import header_vars


class Internal(QRadarAPIEndpoint):
    """
    The QRadar API endpoint group /internal and its endpoints.
    UNDOCUMENTED
    """
    __baseurl = 'internal/'

    def __init__(self, url, header, verify):
        super().__init__(urljoin(url, self.__baseurl),
                         header,
                         verify)

    @header_vars('Range')
    @request_vars('filter', 'sort', 'fields')
    def get_historical_correlation_hc_profiles(self, *, filter=None, sort=None, fields=None, Range=None, **kwargs):
        """
        GET /internal/historical_correlation/hc_profiles
        Retrieves a list of historical correlation profiles without returning any rules.
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'historical_correlation/hc_profiles')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_historical_correlation_hc_profiles_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /internal/historical_correlation/hc_profiles/{id}
        Get a Historical Search Profile by Id without returning rules
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'historical_correlation/hc_profiles/{id}'.format(id=id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_system_servers_by_server_id(self, server_id, *, fields=None, **kwargs):
        """
        GET /internal/system/servers/{server_id}
        Get server by id.
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'system/servers/{server_id}'.format(server_id=server_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    def put_system_servers_firewall_rules_by_server_id(self, server_id, *, rules, **kwargs):
        """
        PUT /internal/system/servers/{server_id}/firewall_rules
        Set access control iptable rules.
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'system/servers/{server_id}/firewall_rules'.format(server_id=server_id))
        return self._call('PUT', function_endpoint, headers=headers, **kwargs)

    def get_system_servers_firewall_rules_by_server_id(self, server_id, **kwargs):
        """
        GET /internal/system/servers/{server_id}/firewall_rules
        Get access control iptable rules by server id.
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'system/servers/{server_id}/firewall_rules'.format(server_id=server_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('interface_types', 'filter', 'sort', 'fields')
    def get_system_servers_network_interfaces_by_server_id(self, server_id, *, interface_types=None, Range=None,
                                                           filter=None, sort=None, fields=None, **kwargs):
        """
        GET /internal/system/servers/{server_id}/network_interfaces
        Get network interfaces by server id.
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'system/servers/{server_id}/network_interfaces'.format(server_id=server_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)
