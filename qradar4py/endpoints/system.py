from urllib.parse import urljoin

from qradar4py.endpoints.api_endpoint import QRadarAPIEndpoint
from qradar4py.endpoints.api_endpoint import request_vars
from qradar4py.endpoints.api_endpoint import header_vars


class System(QRadarAPIEndpoint):
    """
    The QRadar API endpoint group /system and its endpoints.
    """
    __baseurl = 'system/'

    def __init__(self, url, header, verify):
        super().__init__(urljoin(url, self.__baseurl),
                         header,
                         verify)

    @request_vars('fields')
    def get_about(self, *, fields=None, **kwargs):
        """
        GET /system/about
        Retrieves the current system information
        """
        function_endpoint = urljoin(self._baseurl, 'about')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_authorization_capabilities(self, *, fields=None, filter=None, Range=None, **kwargs):
        """
        GET /system/authorization/capabilities
        Retrieves a list of capabilities that are currently in the system.
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'authorization/capabilities')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_authorization_password_policies(self, *, fields=None, filter=None, Range=None, **kwargs):
        """
        GET /system/authorization/password_policies
        Retrieves a list of Password Policies that exist on the system
        """
        function_endpoint = urljoin(self._baseurl, 'authorization/password_policies')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_authorization_password_policies_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /system/authorization/password_policies/{id}
        Retrieves a single Password Policies that exist on the system
        """
        function_endpoint = urljoin(self._baseurl, 'authorization/password_policies/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_authorization_password_policies_by_id(self, id, *, policy, fields=None, **kwargs):
        """
        POST /system/authorization/password_policies/{id}
        See api_mapping.xml
        """
        function_endpoint = urljoin(self._baseurl, 'authorization/password_policies/{id}'.format(id=id))
        return self._call('POST', function_endpoint, json=policy, **kwargs)

    @header_vars('fields')
    def post_authorization_password_validators(self, *, body, fields=None, **kwargs):
        """
        POST /system/authorization/password_validators
        Creates a new password validator for the provided password based
        on the current Password Policy.
        """
        function_endpoint = urljoin(self._baseurl, 'authorization/password_validators')
        return self._call('POST', function_endpoint, json=body, **kwargs)

    @header_vars('fields')
    def post_authorization_settings(self, *, body, fields=None, **kwargs):
        """
        POST /system/authorization/settings
        Updates the Authentication Settings.
        """
        function_endpoint = urljoin(self._baseurl, 'authorization/settings')
        return self._call('POST', function_endpoint, json=body, **kwargs)

    @request_vars('fields')
    def get_authorization_settings(self, *, fields=None, **kwargs):
        """
        GET /system/authorization/settings
        Retrieves the current Authentication Settings.
        """
        function_endpoint = urljoin(self._baseurl, 'authorization/settings')
        return self._call('GET', function_endpoint, **kwargs)

    def post_email_servers(self, *, email_server_details, **kwargs):
        """
        POST /system/email_servers
        Creates a new email server.
        """
        function_endpoint = urljoin(self._baseurl, 'email_servers')
        return self._call('POST', function_endpoint, json=email_server_details, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_email_servers(self, *, Range=None, filter=None, fields=None, **kwargs):
        """
        GET /system/email_servers
        Retrieves a list of all email servers.
        """
        function_endpoint = urljoin(self._baseurl, 'email_servers')
        return self._call('GET', function_endpoint, **kwargs)

    def post_email_servers_by_email_server_id(self, email_server_id, *, email_server_details, **kwargs):
        """
        POST /system/email_servers/{email_server_id}
        Updates an existing email server.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'email_servers/{email_server_id}'.format(email_server_id=email_server_id))
        return self._call('POST', function_endpoint, json=email_server_details, **kwargs)

    def delete_email_servers_by_email_server_id(self, email_server_id, **kwargs):
        """
        DELETE /system/email_servers/{email_server_id}
        Deletes an email server.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'email_servers/{email_server_id}'.format(email_server_id=email_server_id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @request_vars('fields')
    def get_email_servers_by_email_server_id(self, email_server_id, *, fields=None, **kwargs):
        """
        GET /system/email_servers/{email_server_id}
        Retrieves an email server based on the supplied email server ID.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'email_servers/{email_server_id}'.format(email_server_id=email_server_id))
        return self._call('GET', function_endpoint, **kwargs)

    def get_eula_acceptances(self, **kwargs):
        """
        GET /system/eula_acceptances
        Retrieves the list of EULA acceptance statuses that the caller has permission to see.
        """
        function_endpoint = urljoin(self._baseurl, 'eula_acceptances')
        return self._call('GET', function_endpoint, **kwargs)

    def get_eula_acceptances_by_id(self, id, **kwargs):
        """
        GET /system/eula_acceptances/{id}
        Retrieves an individual EULA Acceptance by id.
        """
        function_endpoint = urljoin(self._baseurl, 'eula_acceptances/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_eula_acceptances_by_id(self, id, *, data, fields=None, **kwargs):
        """
        POST /system/eula_acceptances/{id}
        Updates an individual EULA acceptance.
        """
        function_endpoint = urljoin(self._baseurl, 'eula_acceptances/{id}'.format(id=id))
        return self._call('POST', function_endpoint, json=data, **kwargs)

    def get_eulas(self, **kwargs):
        """
        GET /system/eulas
        Retrieves a list of EULAs.
        """
        function_endpoint = urljoin(self._baseurl, 'eulas')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_information_encodings(self, *, fields=None, filter=None, Range=None, **kwargs):
        """
        GET /system/information/encodings
        Retrieves the list of encodings that are supported by the system for event data..
        """
        function_endpoint = urljoin(self._baseurl, 'information/encodings')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('sample_type', 'filter', 'fields', 'sort')
    def get_information_locales(self, *, sample_type=None, filter=None, fields=None, sort=None, Range=None, **kwargs):
        """
        GET /system/information/locales
        Retrieve Locales.
        """
        function_endpoint = urljoin(self._baseurl, 'information/locales')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('since', 'limit', 'fields')
    def get_notifications(self, *, since=None, limit=None, fields=None, **kwargs):
        """
        GET /system/notifications
        Retrieves notifications
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'notifications')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_notifications_by_qid(self, qid, *, fields=None, **kwargs):
        """
        GET /system/notifications/{qid}
        Retrieves notification by QID
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'notifications/{qid}'.format(qid=qid))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    def delete_notifications_by_qid(self, qid, **kwargs):
        """
        DELETE /system/notifications/{qid}
        dismisses a notification
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'notifications/{qid}'.format(qid=qid))
        return self._call('DELETE', function_endpoint, response_type='text/plain', headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_proxy_servers(self, *, Range=None, fields=None, filter=None, **kwargs):
        """
        GET /system/proxy_servers
        Read all proxy servers
        """
        function_endpoint = urljoin(self._baseurl, 'proxy_servers')
        return self._call('GET', function_endpoint, **kwargs)

    def post_proxy_servers(self, *, proxy_server_details, **kwargs):
        """
        POST /system/proxy_servers
        Create a proxy server
        """
        function_endpoint = urljoin(self._baseurl, 'proxy_servers')
        return self._call('POST', function_endpoint, json=proxy_server_details, **kwargs)

    @header_vars('fields')
    def post_proxy_servers_by_id(self, id, *, proxy_server_details, fields=None, **kwargs):
        """
        POST /system/proxy_servers/{id}
        Update a proxy server
        """
        function_endpoint = urljoin(self._baseurl, 'proxy_servers/{id}'.format(id=id))
        return self._call('POST', function_endpoint, json=proxy_server_details, **kwargs)

    def delete_proxy_servers_by_id(self, id, **kwargs):
        """
        DELETE /system/proxy_servers/{id}
        Delete a proxy server
        """
        function_endpoint = urljoin(self._baseurl, 'proxy_servers/{id}'.format(id=id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @request_vars('fields')
    def get_proxy_servers_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /system/proxy_servers/{id}
        Read a proxy server
        """
        function_endpoint = urljoin(self._baseurl, 'proxy_servers/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_server_connection_validator(self, *, request_details, fields=None, **kwargs):
        """
        POST /system/server_connection_validator
        Creates a server connection validator for the provided hostname and port, based
        on the provided host ids.
        """
        function_endpoint = urljoin(self._baseurl, 'server_connection_validator')
        return self._call('POST', function_endpoint, json=request_details, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_servers(self, *, Range=None, filter=None, fields=None, **kwargs):
        """
        GET /system/servers
        Retrieves a list of all server hosts in the deployment.
        """
        function_endpoint = urljoin(self._baseurl, 'servers')
        return self._call('GET', function_endpoint, **kwargs)

    def post_servers_by_server_id(self, server_id, *, details, **kwargs):
        """
        POST /system/servers/{server_id}
        Updates an existing server.
        """
        function_endpoint = urljoin(self._baseurl, 'servers/{server_id}'.format(server_id=server_id))
        return self._call('POST', function_endpoint, json=details, **kwargs)

    @request_vars('fields')
    def get_servers_by_server_id(self, server_id, *, fields=None, **kwargs):
        """
        GET /system/servers/{server_id}
        Retrieves a server host based on the supplied server ID.
        """
        function_endpoint = urljoin(self._baseurl, 'servers/{server_id}'.format(server_id=server_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_servers_firewall_rules_by_server_id(self, server_id, *, Range=None, filter=None, fields=None, **kwargs):
        """
        GET /system/servers/{server_id}/firewall_rules
        Retrieves a list of access control firewall rules based on the supplied server ID.
        """
        function_endpoint = urljoin(self._baseurl, 'servers/{server_id}/firewall_rules'.format(server_id=server_id))
        return self._call('GET', function_endpoint, **kwargs)

    def put_servers_firewall_rules_by_server_id(self, server_id, *, rules, **kwargs):
        """
        PUT /system/servers/{server_id}/firewall_rules
        Sets the access control firewall rules based on the supplied server ID.
        """
        function_endpoint = urljoin(self._baseurl, 'servers/{server_id}/firewall_rules'.format(server_id=server_id))
        return self._call('PUT', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_servers_network_interfaces_bonded_by_server_id(self, server_id, *, Range=None, filter=None, fields=None,
                                                           **kwargs):
        """
        GET /system/servers/{server_id}/network_interfaces/bonded
        Retrieves a list of the bonded network interfaces based on the supplied server ID.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'servers/{server_id}/network_interfaces/bonded'.format(server_id=server_id))
        return self._call('GET', function_endpoint, **kwargs)

    def post_servers_network_interfaces_bonded_by_server_id(self, server_id, *, details, **kwargs):
        """
        POST /system/servers/{server_id}/network_interfaces/bonded
        Creates a new bonded network interface.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'servers/{server_id}/network_interfaces/bonded'.format(server_id=server_id))
        return self._call('POST', function_endpoint, json=details, **kwargs)

    def delete_servers_server_id_network_interfaces_bonded_by_device_name(self, server_id, device_name, **kwargs):
        """
        DELETE /system/servers/{server_id}/network_interfaces/bonded/{device_name}
        Removes a bonded network interface.
        """
        function_endpoint = urljoin(self._baseurl, 'servers/{server_id}/network_interfaces/bonded/{device_name}'.format(
            server_id=server_id, device_name=device_name))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    def post_servers_server_id_network_interfaces_bonded_by_device_name(self, server_id, device_name, *, details,
                                                                        **kwargs):
        """
        POST /system/servers/{server_id}/network_interfaces/bonded/{device_name}
        Updates an existing bonded network interface.
        """
        function_endpoint = urljoin(self._baseurl, 'servers/{server_id}/network_interfaces/bonded/{device_name}'.format(
            server_id=server_id, device_name=device_name))
        return self._call('POST', function_endpoint, json=details, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_servers_network_interfaces_dag_by_server_id(self, server_id, *, Range=None, filter=None, fields=None,
                                                        **kwargs):
        """
        GET /system/servers/{server_id}/network_interfaces/dag
        Retrieves a list of DAG network interfaces based on the supplied server ID.
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'servers/{server_id}/network_interfaces/dag'.format(server_id=server_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    def post_servers_server_id_network_interfaces_dag_by_device_name(self, server_id, device_name, *, details,
                                                                     **kwargs):
        """
        POST /system/servers/{server_id}/network_interfaces/dag/{device_name}
        Updates an existing DAG network interface.
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'servers/{server_id}/network_interfaces/dag/{device_name}'.format(
            server_id=server_id, device_name=device_name))
        return self._call('POST', function_endpoint, json=details, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_servers_network_interfaces_ethernet_by_server_id(self, server_id, *, Range=None, filter=None, fields=None,
                                                             **kwargs):
        """
        GET /system/servers/{server_id}/network_interfaces/ethernet
        Retrieves a list of the ethernet network interfaces based on the supplied server ID.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'servers/{server_id}/network_interfaces/ethernet'.format(server_id=server_id))
        return self._call('GET', function_endpoint, **kwargs)

    def post_servers_server_id_network_interfaces_ethernet_by_device_name(self, server_id, device_name, *, details,
                                                                          **kwargs):
        """
        POST /system/servers/{server_id}/network_interfaces/ethernet/{device_name}
        Updates an ethernet network interface based on the suppied server_Id and device_name.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'servers/{server_id}/network_interfaces/ethernet/{device_name}'.format(
                                        server_id=server_id, device_name=device_name))
        return self._call('POST', function_endpoint, json=details, **kwargs)

    @header_vars('fields')
    def post_servers_system_time_settings_by_server_id(self, server_id, *, settings, fields=None, **kwargs):
        """
        POST /system/servers/{server_id}/system_time_settings
        Sets the system time and time zone settings of to a server host. Services are restarted after the call and service interruptions will occur.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'servers/{server_id}/system_time_settings'.format(server_id=server_id))
        return self._call('POST', function_endpoint, json=settings, **kwargs)

    @request_vars('fields')
    def get_servers_system_time_settings_by_server_id(self, server_id, *, fields=None, **kwargs):
        """
        GET /system/servers/{server_id}/system_time_settings
        Retrieves the system time and time zone settings of a server host based on the supplied server ID.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'servers/{server_id}/system_time_settings'.format(server_id=server_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_servers_timezones_by_server_id(self, server_id, *, fields=None, **kwargs):
        """
        GET /system/servers/{server_id}/timezones
        Retrieves all the available time zones that can be set for a server.
        """
        function_endpoint = urljoin(self._baseurl, 'servers/{server_id}/timezones'.format(server_id=server_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_summary(self, *, fields=None, **kwargs):
        """
        GET /system/summary
        Retrieves notifications summary
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'summary')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('task_id', 'email_addresses')
    def post_task_management_email_action(self, *, task_id, email_addresses, **kwargs):
        """
        POST /system/task_management/email_action
        Adds an email action to the TaskStatus. The email will be
        executed on Completion or Exception of the Task
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'task_management/email_action')
        return self._call('POST', function_endpoint, response_type='text/plain', headers=headers, **kwargs)

    @request_vars('host_id', 'app_id', 'status_uuid', 'task_class', 'task_type', 'children_ids', 'sub_task_ids',
                  'task_state', 'task_name_local_info', 'message_local_info', 'progress', 'minimum', 'maximum',
                  'created_by', 'cancelled_by', 'created_time', 'started_time', 'modified_time', 'completed_time',
                  'retention', 'result_url', 'result_delete_task', 'is_cancel_requested', 'delete_task_id', 'fields')
    def post_task_management_internal_tasks_by_id(self, id, *, host_id=None, app_id=None, status_uuid=None,
                                                  task_class=None, task_type=None, children_ids=None, sub_task_ids=None,
                                                  task_state=None, task_name_local_info=None, message_local_info=None,
                                                  progress=None, minimum=None, maximum=None, created_by=None,
                                                  cancelled_by=None, created_time=None, started_time=None,
                                                  modified_time=None, completed_time=None, retention=None,
                                                  result_url=None, result_delete_task=None, is_cancel_requested=None,
                                                  delete_task_id=None, fields=None, **kwargs):
        """
        POST /system/task_management/internal_tasks/{id}
        Updates a TaskStatus
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'task_management/internal_tasks/{id}'.format(id=id))
        return self._call('POST', function_endpoint, headers=headers, **kwargs)

    @request_vars('task_state', 'message_local_info', 'progress', 'minimum', 'maximum', 'created_time', 'started_time',
                  'modified_time', 'completed_time', 'fields')
    def post_task_management_subtasks(self, *, task_state, message_local_info, progress=None, minimum=None,
                                      maximum=None, created_time=None, started_time=None, modified_time=None,
                                      completed_time=None, fields=None, **kwargs):
        """
        POST /system/task_management/subtasks
        Create a TaskSubStatus
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'task_management/subtasks')
        return self._call('POST', function_endpoint, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_task_management_subtasks(self, *, filter=None, fields=None, Range=None, **kwargs):
        """
        GET /system/task_management/subtasks
        Gets all TaskSubStatuses
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'task_management/subtasks')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_task_management_subtasks_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /system/task_management/subtasks/{id}
        Gets a TaskSubStatus
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'task_management/subtasks/{id}'.format(id=id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('task_state', 'message_local_info', 'progress', 'minimum', 'maximum', 'created_time', 'started_time',
                  'modified_time', 'completed_time', 'fields')
    def post_task_management_subtasks_by_id(self, id, *, task_state=None, message_local_info=None, progress=None,
                                            minimum=None, maximum=None, created_time=None, started_time=None,
                                            modified_time=None, completed_time=None, fields=None, **kwargs):
        """
        POST /system/task_management/subtasks/{id}
        Updates a TaskSubStatus
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'task_management/subtasks/{id}'.format(id=id))
        return self._call('POST', function_endpoint, headers=headers, **kwargs)

    def delete_task_management_subtasks_by_id(self, id, **kwargs):
        """
        DELETE /system/task_management/subtasks/{id}
        Deletes a TaskSubStatus
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'task_management/subtasks/{id}'.format(id=id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', headers=headers, **kwargs)

    @request_vars('host_id', 'app_id', 'status_uuid', 'children_ids', 'task_type', 'task_state', 'task_name_local_info',
                  'message_local_info', 'progress', 'minimum', 'maximum', 'created_by', 'cancelled_by', 'created',
                  'started', 'modified', 'completed', 'retention', 'result_url', 'result_delete_task', 'delete_task_id',
                  'fields')
    def post_task_management_task(self, *, app_id, task_type, task_state, task_name_local_info, message_local_info,
                                  created_by, host_id=None, status_uuid=None, children_ids=None, progress=None,
                                  minimum=None, maximum=None, cancelled_by=None, created=None, started=None,
                                  modified=None, completed=None, retention=None, result_url=None,
                                  result_delete_task=None, delete_task_id=None, fields=None, **kwargs):
        """
        POST /system/task_management/task
        Create a TaskStatus
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'task_management/task')
        return self._call('POST', function_endpoint, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_task_management_task(self, *, filter=None, fields=None, Range=None, **kwargs):
        """
        GET /system/task_management/task
        Gets all TaskStatuses
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'task_management/task')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('id_type', 'fields')
    def get_task_management_task_by_id(self, id, *, id_type=None, fields=None, **kwargs):
        """
        GET /system/task_management/task/{id}
        Gets a TaskStatus
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'task_management/task/{id}'.format(id=id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('host_id', 'app_id', 'status_uuid', 'task_type', 'children_ids', 'task_state', 'task_name_local_info',
                  'message_local_info', 'progress', 'minimum', 'maximum', 'created_by', 'cancelled_by', 'created',
                  'started', 'modified', 'completed', 'retention', 'result_url', 'result_delete_task',
                  'is_cancel_requested', 'delete_task_id', 'fields')
    def post_task_management_task_by_id(self, id, *, host_id=None, app_id=None, status_uuid=None, task_type=None,
                                        children_ids=None, task_state=None, task_name_local_info=None,
                                        message_local_info=None, progress=None, minimum=None, maximum=None,
                                        created_by=None, cancelled_by=None, created=None, started=None, modified=None,
                                        completed=None, retention=None, result_url=None, result_delete_task=None,
                                        is_cancel_requested=None, delete_task_id=None, fields=None, **kwargs):
        """
        POST /system/task_management/task/{id}
        Updates a TaskStatus
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'task_management/task/{id}'.format(id=id))
        return self._call('POST', function_endpoint, headers=headers, **kwargs)

    @request_vars('delete_result')
    def delete_task_management_task_by_id(self, id, *, delete_result=None, **kwargs):
        """
        DELETE /system/task_management/task/{id}
        Deletes a TaskStatus
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'task_management/task/{id}'.format(id=id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', headers=headers, **kwargs)

    def delete_task_management_task_result_by_id(self, id, **kwargs):
        """
        DELETE /system/task_management/task/{id}/result
        Gets the result from the TaskStatus
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'task_management/task/{id}/result'.format(id=id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', headers=headers, **kwargs)

    @request_vars('resume_data')
    def post_task_management_task_resume_data_by_id(self, id, *, resume_data, **kwargs):
        """
        POST /system/task_management/task/{id}/resume_data
        Creates the result from the TaskStatus
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'task_management/task/{id}/resume_data'.format(id=id))
        return self._call('POST', function_endpoint, response_type='text/plain', headers=headers, **kwargs)

    def get_task_management_task_resume_data_by_id(self, id, **kwargs):
        """
        GET /system/task_management/task/{id}/resume_data
        Gets the resume from the TaskStatus
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'task_management/task/{id}/resume_data'.format(id=id))
        return self._call('GET', function_endpoint, response_type='text/plain', headers=headers, **kwargs)

    @request_vars('task_id')
    def post_task_management_task_id_by_uuid(self, uuid, *, task_id, **kwargs):
        """
        POST /system/task_management/task_id/{uuid}
        No summary provided
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'task_management/task_id/{uuid}'.format(uuid=uuid))
        return self._call('POST', function_endpoint, response_type='text/plain', headers=headers, **kwargs)

    def get_task_management_task_id_by_uuid(self, uuid, **kwargs):
        """
        GET /system/task_management/task_id/{uuid}
        No summary provided
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'task_management/task_id/{uuid}'.format(uuid=uuid))
        return self._call('GET', function_endpoint, response_type='text/plain', headers=headers, **kwargs)

    def delete_task_management_task_id_by_uuid(self, uuid, **kwargs):
        """
        DELETE /system/task_management/task_id/{uuid}
        No summary provided
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'task_management/task_id/{uuid}'.format(uuid=uuid))
        return self._call('DELETE', function_endpoint, response_type='text/plain', headers=headers, **kwargs)

    @request_vars('host_id', 'app_id', 'status_uuid', 'children_ids', 'sub_task_ids', 'task_class', 'task_type',
                  'task_state', 'task_name_local_info', 'message_local_info', 'progress', 'minimum', 'maximum',
                  'created_by', 'cancelled_by', 'created_time', 'started_time', 'modified_time', 'completed_time',
                  'retention', 'result_url', 'result_delete_task', 'delete_task_id', 'fields')
    def post_task_management_tasks(self, *, app_id, task_class, task_type, task_state, task_name_local_info,
                                   message_local_info, created_by, host_id=None, status_uuid=None, children_ids=None,
                                   sub_task_ids=None, progress=None, minimum=None, maximum=None, cancelled_by=None,
                                   created_time=None, started_time=None, modified_time=None, completed_time=None,
                                   retention=None, result_url=None, result_delete_task=None, delete_task_id=None,
                                   fields=None, **kwargs):
        """
        POST /system/task_management/tasks
        Create a TaskStatus
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'task_management/tasks')
        return self._call('POST', function_endpoint, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_task_management_tasks(self, *, filter=None, fields=None, Range=None, **kwargs):
        """
        GET /system/task_management/tasks
        Gets all TaskStatuses
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'task_management/tasks')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('is_cancel_requested', 'fields')
    def post_task_management_tasks_by_id(self, id, *, is_cancel_requested=None, fields=None, **kwargs):
        """
        POST /system/task_management/tasks/{id}
        Updates a TaskStatus
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'task_management/tasks/{id}'.format(id=id))
        return self._call('POST', function_endpoint, headers=headers, **kwargs)

    @request_vars('id_type', 'fields')
    def get_task_management_tasks_by_id(self, id, *, id_type=None, fields=None, **kwargs):
        """
        GET /system/task_management/tasks/{id}
        Gets a TaskStatus
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'task_management/tasks/{id}'.format(id=id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('delete_result')
    def delete_task_management_tasks_by_id(self, id, *, delete_result=None, **kwargs):
        """
        DELETE /system/task_management/tasks/{id}
        Deletes a TaskStatus
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'task_management/tasks/{id}'.format(id=id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', headers=headers, **kwargs)

    def get_task_management_tasks_result_by_id(self, id, **kwargs):
        """
        GET /system/task_management/tasks/{id}/result
        Gets the result from the TaskStatus
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'task_management/tasks/{id}/result'.format(id=id))
        return self._call('GET', function_endpoint, response_type='application/octet-stream', headers=headers, **kwargs)

    def post_task_management_tasks_result_by_id(self, id, *, result, **kwargs):
        """
        POST /system/task_management/tasks/{id}/result
        Creates the result from the TaskStatus
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'task_management/tasks/{id}/result'.format(id=id))
        return self._call('POST', function_endpoint, response_type='text/plain',
                          mime_type={'Content-Type': 'application/octet-stream'}, data=result, headers=headers,
                          **kwargs)

    def delete_task_management_tasks_result_by_id(self, id, **kwargs):
        """
        DELETE /system/task_management/tasks/{id}/result
        Deletes a result
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'task_management/tasks/{id}/result'.format(id=id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', headers=headers, **kwargs)
