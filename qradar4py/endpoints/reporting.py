from urllib.parse import urljoin

from qradar4py.endpoints.api_endpoint import QRadarAPIEndpoint
from qradar4py.endpoints.api_endpoint import request_vars
from qradar4py.endpoints.api_endpoint import header_vars


class Reporting(QRadarAPIEndpoint):
    """
    The QRadar API endpoint group /reporting and its endpoints.
    UNDOCUMENTED
    """
    __baseurl = 'reporting/'

    def __init__(self, url, header, verify):
        super().__init__(urljoin(url, self.__baseurl),
                         header,
                         verify)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_groups(self, *, filter=None, fields=None, Range=None, **kwargs):
        """
        GET /reporting/groups
        Get a list the Report Groups
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'groups')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_groups_by_group_id(self, group_id, *, fields=None, **kwargs):
        """
        GET /reporting/groups/{group_id}
        Get the Report Group
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'groups/{group_id}'.format(group_id=group_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    def delete_groups_by_group_id(self, group_id, **kwargs):
        """
        DELETE /reporting/groups/{group_id}
        Delete the Report Group
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'groups/{group_id}'.format(group_id=group_id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', headers=headers, **kwargs)

    @header_vars('fields')
    def post_groups_by_group_id(self, group_id, *, group, fields=None, **kwargs):
        """
        POST /reporting/groups/{group_id}
        Update the owner of an Report Group
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'groups/{group_id}'.format(group_id=group_id))
        return self._call('POST', function_endpoint, json=group, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_templates(self, *, filter=None, fields=None, Range=None, **kwargs):
        """
        GET /reporting/templates
        Retrieve the Report Templates
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'templates')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    def delete_templates_by_template_id(self, template_id, **kwargs):
        """
        DELETE /reporting/templates/{template_id}
        Delete the Report Template.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'templates/{template_id}'.format(template_id=template_id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', headers=headers, **kwargs)

    @header_vars('fields')
    def post_templates_by_template_id(self, template_id, *, report_template, fields=None, **kwargs):
        """
        POST /reporting/templates/{template_id}
        Update the Report Template owner only.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'templates/{template_id}'.format(template_id=template_id))
        return self._call('POST', function_endpoint, json=report_template, headers=headers, **kwargs)

    @request_vars('fields')
    def get_templates_by_template_id(self, template_id, *, fields=None, **kwargs):
        """
        GET /reporting/templates/{template_id}
        Retrieve the Report Template
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'templates/{template_id}'.format(template_id=template_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    def get_templates_template_id_output_type_by_output_type(self, template_id, output_type, **kwargs):
        """
        GET /reporting/templates/{template_id}/output_type/{output_type}
        Retrieve the Report Template's latest generated content
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'templates/{template_id}/output_type/{output_type}'.format(template_id=template_id,
                                                                                               output_type=output_type))
        return self._call('GET', function_endpoint, response_type='text/plain', headers=headers, **kwargs)
