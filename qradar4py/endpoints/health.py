from urllib.parse import urljoin

from qradar4py.endpoints.api_endpoint import QRadarAPIEndpoint
from qradar4py.endpoints.api_endpoint import request_vars
from qradar4py.endpoints.api_endpoint import header_vars


class Health(QRadarAPIEndpoint):
    """
    The QRadar API endpoint group /health and its endpoints.
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
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'alerts')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_metrics_config(self, *, fields=None, filter=None, Range=None, **kwargs):
        """
        GET /health/metrics/config
        No summary provided
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'metrics/config')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_metrics_config_by_metric_id(self, metric_id, *, fields=None, **kwargs):
        """
        GET /health/metrics/config/{metric_id}
        No summary provided
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'metrics/config/{metric_id}'.format(metric_id=metric_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_metrics_meta(self, *, fields=None, filter=None, Range=None, **kwargs):
        """
        GET /health/metrics/meta
        No summary provided
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'metrics/meta')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_metrics_meta_by_metric_id(self, metric_id, *, fields=None, **kwargs):
        """
        GET /health/metrics/meta/{metric_id}
        No summary provided
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'metrics/meta/{metric_id}'.format(metric_id=metric_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_metrics_qradar_metrics(self, *, fields=None, filter=None, Range=None, **kwargs):
        """
        GET /health/metrics/qradar_metrics
        Gets the list of QRadar component metrics
        """
        function_endpoint = urljoin(self._baseurl, 'metrics/qradar_metrics')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_metrics_qradar_metrics_by_id(self, id, *, qradar_metric, fields=None, **kwargs):
        """
        POST /health/metrics/qradar_metrics/{id}
        Updates the time_resolution and enable field of a QRadar metric identified by metric ID.
        """
        function_endpoint = urljoin(self._baseurl, 'metrics/qradar_metrics/{id}'.format(id=id))
        return self._call('POST', function_endpoint, json=qradar_metric, **kwargs)

    @request_vars('fields')
    def get_metrics_qradar_metrics_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /health/metrics/qradar_metrics/{id}
        Retrieves the QRadar health metric identified by ID.
        """
        function_endpoint = urljoin(self._baseurl, 'metrics/qradar_metrics/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_metrics_qradar_metrics_global_config(self, *, global_config, fields=None, **kwargs):
        """
        POST /health/metrics/qradar_metrics_global_config
        Updates the frequency and enabled fields of all the qradar metrics.
        """
        function_endpoint = urljoin(self._baseurl, 'metrics/qradar_metrics_global_config')
        return self._call('POST', function_endpoint, json=global_config, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_metrics_system_metrics(self, *, fields=None, filter=None, Range=None, **kwargs):
        """
        GET /health/metrics/system_metrics
        Gets the list of system metrics.
        """
        function_endpoint = urljoin(self._baseurl, 'metrics/system_metrics')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_metrics_system_metrics_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /health/metrics/system_metrics/{id}
        Retrieves the system health metric identified by metric ID.
        """
        function_endpoint = urljoin(self._baseurl, 'metrics/system_metrics/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_metrics_system_metrics_by_id(self, id, *, system_metric, fields=None, **kwargs):
        """
        POST /health/metrics/system_metrics/{id}
        Enable or disable a system metric identified by metric ID
        """
        function_endpoint = urljoin(self._baseurl, 'metrics/system_metrics/{id}'.format(id=id))
        return self._call('POST', function_endpoint, json=system_metric, **kwargs)

    @header_vars('fields')
    def post_metrics_system_metrics_global_config(self, *, global_config, fields=None, **kwargs):
        """
        POST /health/metrics/system_metrics_global_config
        Updates the frequency and enabled value of all the qradar metrics identified by metric_id parameter.
        """
        function_endpoint = urljoin(self._baseurl, 'metrics/system_metrics_global_config')
        return self._call('POST', function_endpoint, json=global_config, **kwargs)
