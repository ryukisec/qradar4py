from urllib.parse import urljoin

from qradar4py.endpoints.api_endpoint import QRadarAPIEndpoint
from qradar4py.endpoints.api_endpoint import request_vars
from qradar4py.endpoints.api_endpoint import header_vars


class Scanner(QRadarAPIEndpoint):
    """
    The QRadar API endpoint group /scanner and its endpoints.
    """
    __baseurl = 'scanner/'

    def __init__(self, url, header, verify):
        super().__init__(urljoin(url, self.__baseurl),
                         header,
                         verify)

    def get_profiles(self, **kwargs):
        """
        GET /scanner/profiles
        Retrieves all of the currently created scan profiles. No parameters are required and the following information
        should be retrieved for each scan profile

        - scanProfileId
        - scanProfileName
        - description
        - scanType
        - scannerName
        """
        function_endpoint = urljoin(self._baseurl, 'profiles')
        return self._call('GET', function_endpoint, **kwargs)

    def post_profiles_create(self, *, scanProfile, **kwargs):
        """
        POST /scanner/profiles/create
        Initiates a request to create a new scanProfile. The request takes one parameter - createScanRequest, which is just a POJO.

        To create the scan, you will need to build up a JSON object that contains the Scan Profile name and ips to scan e.g.
        {'name':'New Scan Profile', 'ips':['10.100.85.135']}
        """
        function_endpoint = urljoin(self._baseurl, 'profiles/create')
        return self._call('POST', function_endpoint, response_type='text/plain', json=scanProfile, **kwargs)

    @request_vars('scanProfileId')
    def post_profiles_start(self, *, scanProfileId, **kwargs):
        """
        POST /scanner/profiles/start
        Initiates a request to start an already created scanProfile. The request takes one parameter - scanProfileId.

        To get a list of scanProfileIds, simply get a list of the current scan profiles by initiating a 'profiles' request on the
        scanner endpoint. The scanProfileId will be validated and an appropriate message returned.
        """
        function_endpoint = urljoin(self._baseurl, 'profiles/start')
        return self._call('POST', function_endpoint, response_type='text/plain', **kwargs)

    def post_scanprofiles(self, *, scanProfile, **kwargs):
        """
        POST /scanner/scanprofiles
        Initiates a request to create a new scanProfile. The request takes one parameter - createScanRequest, which is just a POJO.

        To create the scan, you will need to build up a JSON object that contains the Scan Profile name and hosts to scan e.g.
        {'name':'New Scan Profile', 'hosts':['10.100.85.135']}
        """
        function_endpoint = urljoin(self._baseurl, 'scanprofiles')
        return self._call('POST', function_endpoint, response_type='text/plain', json=scanProfile, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_scanprofiles(self, *, fields=None, Range=None, filter=None, **kwargs):
        """
        GET /scanner/scanprofiles
        See api_mapping.xml
        """
        function_endpoint = urljoin(self._baseurl, 'scanprofiles')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_scanprofiles_by_profileid(self, profileid, *, fields=None, Range=None, filter=None, **kwargs):
        """
        GET /scanner/scanprofiles/{profileid}
        See api_mapping.xml
        """
        function_endpoint = urljoin(self._baseurl, 'scanprofiles/{profileid}'.format(profileid=profileid))
        return self._call('GET', function_endpoint, **kwargs)

    def delete_scanprofiles_by_profileid(self, profileid, **kwargs):
        """
        DELETE /scanner/scanprofiles/{profileid}
        Initiates a request to delete a  scanProfile. The request takes one parameter - the Scan Profile ID.
        """
        function_endpoint = urljoin(self._baseurl, 'scanprofiles/{profileid}'.format(profileid=profileid))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    def post_scanprofiles_by_profileid(self, profileid, *, scanProfile, **kwargs):
        """
        POST /scanner/scanprofiles/{profileid}
        Update a scan profile. The Scan Profile ID is required.
        The following information on a scan profile can be updated

        - name
        - description
        - ips
        eg  {'name':'Updated Scan Profile', 'ips':['10.100.85.135']}
        """
        function_endpoint = urljoin(self._baseurl, 'scanprofiles/{profileid}'.format(profileid=profileid))
        return self._call('POST', function_endpoint, json=scanProfile, **kwargs)

    @header_vars('Range')
    @request_vars('fields')
    def get_scanprofiles_runs_by_profileid(self, profileid, *, fields=None, Range=None, **kwargs):
        """
        GET /scanner/scanprofiles/{profileid}/runs
        No summary provided
        """
        function_endpoint = urljoin(self._baseurl, 'scanprofiles/{profileid}/runs'.format(profileid=profileid))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_scanprofiles_profileid_runs_by_run_id(self, profileid, run_id, *, fields=None, **kwargs):
        """
        GET /scanner/scanprofiles/{profileid}/runs/{run_id}
        No summary provided
        """
        function_endpoint = urljoin(self._baseurl,
                                    'scanprofiles/{profileid}/runs/{run_id}'.format(profileid=profileid, run_id=run_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('fields')
    def get_scanprofiles_profileid_runs_results_by_run_id(self, profileid, run_id, *, fields=None, Range=None,
                                                          **kwargs):
        """
        GET /scanner/scanprofiles/{profileid}/runs/{run_id}/results
        No summary provided
        """
        function_endpoint = urljoin(self._baseurl,
                                    'scanprofiles/{profileid}/runs/{run_id}/results'.format(profileid=profileid,
                                                                                            run_id=run_id))
        return self._call('GET', function_endpoint, **kwargs)

    def post_scanprofiles_start_by_profileid(self, profileid, *, ips=None, **kwargs):
        """
        POST /scanner/scanprofiles/{profileid}/start
        Initiates a request to start an already created scanProfile. The request takes one parameter - scanProfileId, and one optional parameter - ips.

        To get a list of scanProfileIds, simply get a list of the current scan profiles by initiating a 'profiles' request on the
        scanner endpoint. The scanProfileId will be validated and an appropriate message returned.
        """
        function_endpoint = urljoin(self._baseurl, 'scanprofiles/{profileid}/start'.format(profileid=profileid))
        return self._call('POST', function_endpoint, response_type='text/plain', json=ips, **kwargs)
