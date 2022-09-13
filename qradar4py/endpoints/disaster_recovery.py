from urllib.parse import urljoin

from qradar4py.endpoints.api_endpoint import QRadarAPIEndpoint
from qradar4py.endpoints.api_endpoint import request_vars
from qradar4py.endpoints.api_endpoint import header_vars


class DisasterRecovery(QRadarAPIEndpoint):
    """
    The QRadar API endpoint group /disaster_recovery and its endpoints.
    """
    __baseurl = 'disaster_recovery/'

    def __init__(self, url, header, verify):
        super().__init__(urljoin(url, self.__baseurl),
                         header,
                         verify)

    @request_vars('filter', 'fields')
    def get_ariel_copy_profiles(self, *, filter=None, fields=None, **kwargs):
        """
        GET /disaster_recovery/ariel_copy_profiles
        Retrieves a list of the Ariel Copy Profiles.
        """
        function_endpoint = urljoin(self._baseurl, 'ariel_copy_profiles')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_ariel_copy_profiles(self, *, arielCopyProfileDTO, fields=None, **kwargs):
        """
        POST /disaster_recovery/ariel_copy_profiles
        Creates a new Ariel Copy Profile.
        """
        function_endpoint = urljoin(self._baseurl, 'ariel_copy_profiles')
        return self._call('POST', function_endpoint, json=arielCopyProfileDTO, **kwargs)

    @header_vars('fields')
    def post_ariel_copy_profiles_by_id(self, id, *, arielCopyProfileDTO, fields=None, **kwargs):
        """
        POST /disaster_recovery/ariel_copy_profiles/{id}
        Updates a Ariel Copy Profile by ID.
        """
        function_endpoint = urljoin(self._baseurl, 'ariel_copy_profiles/{id}'.format(id=id))
        return self._call('POST', function_endpoint, json=arielCopyProfileDTO, **kwargs)

    @request_vars('fields')
    def get_ariel_copy_profiles_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /disaster_recovery/ariel_copy_profiles/{id}
        Retrieves a Ariel Copy Profile by ID.
        """
        function_endpoint = urljoin(self._baseurl, 'ariel_copy_profiles/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    def delete_ariel_copy_profiles_by_id(self, id, **kwargs):
        """
        DELETE /disaster_recovery/ariel_copy_profiles/{id}
        Deletes a Ariel Copy Profile by ID.
        """
        function_endpoint = urljoin(self._baseurl, 'ariel_copy_profiles/{id}'.format(id=id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)
