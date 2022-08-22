from urllib.parse import urljoin

from qradar4py.endpoints.api_endpoint import QRadarAPIEndpoint
from qradar4py.endpoints.api_endpoint import request_vars
from qradar4py.endpoints.api_endpoint import header_vars


class Qni(QRadarAPIEndpoint):
    """
    The QRadar API endpoint group /qni and its endpoints.
    """
    __baseurl = 'qni/'

    def __init__(self, url, header, verify):
        super().__init__(urljoin(url, self.__baseurl),
                         header,
                         verify)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_hosts_configs_by_host_id(self, host_id, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /qni/hosts/{host_id}/configs
        Retrieves a list of QNI configurations. The list contains a single configuration.
        """
        function_endpoint = urljoin(self._baseurl, 'hosts/{host_id}/configs'.format(host_id=host_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_hosts_host_id_configs_by_id(self, host_id, id, *, qni_configuration, fields=None, **kwargs):
        """
        POST /qni/hosts/{host_id}/configs/{id}
        Updates the configuration of a QNI host. You cannot use this endpoint to update a host that is a part of a QNI stack. Use the QNI Stacking API instead.
        """
        function_endpoint = urljoin(self._baseurl, 'hosts/{host_id}/configs/{id}'.format(host_id=host_id, id=id))
        return self._call('POST', function_endpoint, json=qni_configuration, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_stacking_stacks(self, *, Range=None, filter=None, fields=None, **kwargs):
        """
        GET /qni/stacking/stacks
        Retrieves a list of all QNI stacks in the system.
        """
        function_endpoint = urljoin(self._baseurl, 'stacking/stacks')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_stacking_stacks(self, *, stack, fields=None, **kwargs):
        """
        POST /qni/stacking/stacks
        Creates a QNI stack.
        """
        function_endpoint = urljoin(self._baseurl, 'stacking/stacks')
        return self._call('POST', function_endpoint, json=stack, **kwargs)

    def delete_stacking_stacks_by_stack_id(self, stack_id, **kwargs):
        """
        DELETE /qni/stacking/stacks/{stack_id}
        Deletes a QNI stack, as specified by the stack ID.
        """
        function_endpoint = urljoin(self._baseurl, 'stacking/stacks/{stack_id}'.format(stack_id=stack_id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @request_vars('fields')
    def get_stacking_stacks_by_stack_id(self, stack_id, *, fields=None, **kwargs):
        """
        GET /qni/stacking/stacks/{stack_id}
        Retrieves a QNI stack, as specified by the stack ID.
        """
        function_endpoint = urljoin(self._baseurl, 'stacking/stacks/{stack_id}'.format(stack_id=stack_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_stacking_stacks_by_stack_id(self, stack_id, *, stack, fields=None, **kwargs):
        """
        POST /qni/stacking/stacks/{stack_id}
        Updates a QNI stack, as specified by the stack ID.
        """
        function_endpoint = urljoin(self._baseurl, 'stacking/stacks/{stack_id}'.format(stack_id=stack_id))
        return self._call('POST', function_endpoint, json=stack, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_stacking_standalone_hosts(self, *, Range=None, filter=None, fields=None, **kwargs):
        """
        GET /qni/stacking/standalone_hosts
        Retrieves a list of all standalone QNI hosts that can be added to a stack. (Not all QNI appliance types are stackable.)
        """
        function_endpoint = urljoin(self._baseurl, 'stacking/standalone_hosts')
        return self._call('GET', function_endpoint, **kwargs)
