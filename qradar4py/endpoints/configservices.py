from urllib.parse import urljoin

from qradar4py.endpoints.api_endpoint import QRadarAPIEndpoint
from qradar4py.endpoints.api_endpoint import request_vars
from qradar4py.endpoints.api_endpoint import header_vars


class Configservices(QRadarAPIEndpoint):
    """
    The QRadar API endpoint group /configservices and its endpoints.
    UNDOCUMENTED
    """
    __baseurl = 'configservices/'

    def __init__(self, url, header, verify):
        super().__init__(urljoin(url, self.__baseurl),
                         header,
                         verify)

    @request_vars('fields')
    def get_deployment_token(self, *, fields=None, **kwargs):
        """
        GET /configservices/deployment/token
        Getting hdeploymentost token.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'deployment/token')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('fields')
    def post_host_capabilities_report(self, *, hostcapabilities, fields=None, **kwargs):
        """
        POST /configservices/host_capabilities/report
        Host Capabilities report to Console.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'host_capabilities/report')
        return self._call('POST', function_endpoint, json=hostcapabilities, headers=headers, **kwargs)

    @request_vars('fields')
    def get_host_capabilities_report_by_task_id(self, task_id, *, fields=None, **kwargs):
        """
        GET /configservices/host_capabilities/report/{task_id}
        Getting status of the Host Capabilities reporting task.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'host_capabilities/report/{task_id}'.format(task_id=task_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)
