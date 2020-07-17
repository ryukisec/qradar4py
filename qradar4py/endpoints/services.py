from urllib.parse import urljoin

from qradar4py.endpoints.api_endpoint import QRadarAPIEndpoint
from qradar4py.endpoints.api_endpoint import request_vars


class Services(QRadarAPIEndpoint):
    """
    The QRadar API endpoint group /services and its endpoints.
    """
    __baseurl = 'siem/'

    def __init__(self, url, header, verify):
        super().__init__(urljoin(url, self.__baseurl),
                         header,
                         verify)

    @request_vars('IP', 'fields')
    def post_dig_lookups(self, *, IP, fields=None, **kwargs):
        """
        POST /services/dig_lookups
        Creates a new DIG lookup. Lookup completes in the background.
        """
        function_endpoint = urljoin(self._baseurl, 'dig_lookups')
        return self._call('POST', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_dig_lookups_by_dig_lookup_id(self, dig_lookup_id, *, fields=None, **kwargs):
        """
        GET /services/dig_lookups/{dig_lookup_id}
        Retrieves the DIG lookup status. The result is included if the lookup completed.
        """
        function_endpoint = urljoin(self._baseurl, 'dig_lookups/{dig_lookup_id}'.format(dig_lookup_id=dig_lookup_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('IP', 'fields')
    def post_dns_lookups(self, *, IP, fields=None, **kwargs):
        """
        POST /services/dns_lookups
        Creates a new DNS lookup. Lookup completes in the background.
        """
        function_endpoint = urljoin(self._baseurl, 'dns_lookups')
        return self._call('POST', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_dns_lookups_by_dns_lookup_id(self, dns_lookup_id, *, fields=None, **kwargs):
        """
        GET /services/dns_lookups/{dns_lookup_id}
        Retrieves the DNS lookup status. The result is included if the lookup completes.
        """
        function_endpoint = urljoin(self._baseurl, 'dns_lookups/{dns_lookup_id}'.format(dns_lookup_id=dns_lookup_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('filter', 'fields')
    def get_geolocations(self, *, filter=None, fields=None, **kwargs):
        """
        GET /services/geolocations
        Retrieves the MaxMind geoip data for the given IP address.
        """
        function_endpoint = urljoin(self._baseurl, 'geolocations')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('IP', 'fields')
    def post_port_scans(self, *, IP, fields=None, **kwargs):
        """
        POST /services/port_scans
        Creates a new PortScans lookup. Port scan completes in the background.
        """
        function_endpoint = urljoin(self._baseurl, 'port_scans')
        return self._call('POST', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_port_scans_by_port_scan_id(self, port_scan_id, *, fields=None, **kwargs):
        """
        GET /services/port_scans/{port_scan_id}
        Retrieves the port scan status. The result is included if the port scan completes.
        """
        function_endpoint = urljoin(self._baseurl, 'port_scans/{port_scan_id}'.format(port_scan_id=port_scan_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('IP', 'fields')
    def post_whois_lookups(self, *, IP, fields=None, **kwargs):
        """
        POST /services/whois_lookups
        Creates a new WHOIS lookup. Lookup completes in the background.
        """
        function_endpoint = urljoin(self._baseurl, 'whois_lookups')
        return self._call('POST', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_whois_lookups_by_whois_lookup_id(self, whois_lookup_id, *, fields=None, **kwargs):
        """
        GET /services/whois_lookups/{whois_lookup_id}
        Retrieves the WHOIS lookup status. The result is included if the lookup completes.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'whois_lookups/{whois_lookup_id}'.format(whois_lookup_id=whois_lookup_id))
        return self._call('GET', function_endpoint, **kwargs)
