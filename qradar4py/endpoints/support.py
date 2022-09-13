from urllib.parse import urljoin

from qradar4py.endpoints.api_endpoint import QRadarAPIEndpoint
from qradar4py.endpoints.api_endpoint import request_vars
from qradar4py.endpoints.api_endpoint import header_vars


class Support(QRadarAPIEndpoint):
    """
    The QRadar API endpoint group /support and its endpoints.
    UNDOCUMENTED
    """
    __baseurl = 'support/'

    def __init__(self, url, header, verify):
        super().__init__(urljoin(url, self.__baseurl),
                         header,
                         verify)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_log_bundles(self, *, Range=None, filter=None, fields=None, **kwargs):
        """
        GET /support/log_bundles
        get all get_logs tasks' statuses.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'log_bundles')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('fields')
    def post_log_bundles(self, *, get_logs_args, fields=None, **kwargs):
        """
        POST /support/log_bundles
        Collect logs according to user options.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'log_bundles')
        return self._call('POST', function_endpoint, json=get_logs_args, headers=headers, **kwargs)

    @request_vars('is_initial_id', 'fields')
    def get_log_bundles_by_log_bundle_id(self, log_bundle_id, *, is_initial_id=None, fields=None, **kwargs):
        """
        GET /support/log_bundles/{log_bundle_id}
        get specified get_logs task's status by id.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'log_bundles/{log_bundle_id}'.format(log_bundle_id=log_bundle_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    def post_log_bundles_by_log_bundle_id(self, log_bundle_id, **kwargs):
        """
        POST /support/log_bundles/{log_bundle_id}
        stop specified get_logs task if it is running
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'log_bundles/{log_bundle_id}'.format(log_bundle_id=log_bundle_id))
        return self._call('POST', function_endpoint, headers=headers, **kwargs)

    def delete_log_bundles_by_log_bundle_id(self, log_bundle_id, **kwargs):
        """
        DELETE /support/log_bundles/{log_bundle_id}
        delete a get_logs task by id.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'log_bundles/{log_bundle_id}'.format(log_bundle_id=log_bundle_id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', headers=headers, **kwargs)

    def get_log_bundles_result_by_log_bundle_id(self, log_bundle_id, **kwargs):
        """
        GET /support/log_bundles/{log_bundle_id}/result
        download generated support log file.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'log_bundles/{log_bundle_id}/result'.format(log_bundle_id=log_bundle_id))
        return self._call('GET', function_endpoint, response_type='application/octet-stream', headers=headers, **kwargs)
