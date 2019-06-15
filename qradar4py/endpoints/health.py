from urllib.parse import urljoin

from qradar4py.endpoints.api_endpoint import QRadarAPIEndpoint
from qradar4py.endpoints.api_endpoint import request_vars
from qradar4py.endpoints.api_endpoint import header_vars


class Health(QRadarAPIEndpoint):
    """
    The QRadar API endpoint group /health and its endpoints.
    UNDOCUMENTED
    """
    __baseurl = 'health/'

    def __init__(self, url, header, verify):
        super().__init__(urljoin(url, self.__baseurl),
                         header,
                         verify)

    @request_vars('since', 'fields')
    def get_alerts(self, *, since=None, fields=None, **kwargs):
        """
        GET /health/alerts
        Retrieves all health alerts currently in the system
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'alerts')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_metrics_config(self, *, Range=None, fields=None, filter=None, **kwargs):
        """
        GET /health/metrics/config
        No summary provided
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'metrics/config')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_metrics_config_by_metric_id(self, metric_id, *, fields=None, **kwargs):
        """
        GET /health/metrics/config/{metric_id}
        No summary provided
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'metrics/config/{metric_id}'.format(metric_id=metric_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_metrics_meta(self, *, Range=None, fields=None, filter=None, **kwargs):
        """
        GET /health/metrics/meta
        No summary provided
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'metrics/meta')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_metrics_meta_by_metric_id(self, metric_id, *, fields=None, **kwargs):
        """
        GET /health/metrics/meta/{metric_id}
        No summary provided
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'metrics/meta/{metric_id}'.format(metric_id=metric_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)
