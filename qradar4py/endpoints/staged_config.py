from urllib.parse import urljoin

from qradar4py.endpoints.api_endpoint import QRadarAPIEndpoint
from qradar4py.endpoints.api_endpoint import request_vars
from qradar4py.endpoints.api_endpoint import header_vars


class StagedConfig(QRadarAPIEndpoint):
    """
    The QRadar API endpoint group /staged_config and its endpoints.
    """
    __baseurl = 'staged_config/'

    def __init__(self, url, header, verify):
        super().__init__(urljoin(url, self.__baseurl),
                         header,
                         verify)

    @header_vars('Range')
    @request_vars('tenant_id', 'fields', 'filter')
    def get_access_security_profiles(self, *, tenant_id=None, fields=None, filter=None, Range=None, **kwargs):
        """
        GET /staged_config/access/security_profiles
        Get the list of staged security profiles available in the system.
        """
        function_endpoint = urljoin(self._baseurl, 'access/security_profiles')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_access_security_profiles_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /staged_config/access/security_profiles/{id}
        Get a staged security profile by ID.
        """
        function_endpoint = urljoin(self._baseurl, 'access/security_profiles/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_access_user_delete_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):
        """
        GET /staged_config/access/user_delete_tasks/{task_id}
        Retrieves the delete user task status.
        """
        function_endpoint = urljoin(self._baseurl, 'access/user_delete_tasks/{task_id}'.format(task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('contains', 'fields', 'filter')
    def get_access_user_roles(self, *, contains=None, fields=None, filter=None, Range=None, **kwargs):
        """
        GET /staged_config/access/user_roles
        Get the list of staged user roles available in the system.
        """
        function_endpoint = urljoin(self._baseurl, 'access/user_roles')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_access_user_roles_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /staged_config/access/user_roles/{id}
        Get a staged user role by ID.
        """
        function_endpoint = urljoin(self._baseurl, 'access/user_roles/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter', 'sort')
    def get_access_users(self, *, fields=None, filter=None, sort=None, Range=None, **kwargs):
        """
        GET /staged_config/access/users
        Retrieves a list of all staged users.
        """
        function_endpoint = urljoin(self._baseurl, 'access/users')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_access_users(self, *, body, fields=None, **kwargs):
        """
        POST /staged_config/access/users
        Create a staged user.
        """
        function_endpoint = urljoin(self._baseurl, 'access/users')
        return self._call('POST', function_endpoint, json=body, **kwargs)

    @header_vars('fields')
    def post_access_users_by_id(self, id, *, body, fields=None, **kwargs):
        """
        POST /staged_config/access/users/{id}
        Update a staged user.
        """
        function_endpoint = urljoin(self._baseurl, 'access/users/{id}'.format(id=id))
        return self._call('POST', function_endpoint, json=body, **kwargs)

    @request_vars('fields')
    def get_access_users_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /staged_config/access/users/{id}
        Retrieves a staged user.
        """
        function_endpoint = urljoin(self._baseurl, 'access/users/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def delete_access_users_by_id(self, id, *, fields=None, **kwargs):
        """
        DELETE /staged_config/access/users/{id}
        Deletes a user from staging. To ensure safe deletion, dependencies are checked. This might take some time. An asynchronous task is started to do this check.
        """
        function_endpoint = urljoin(self._baseurl, 'access/users/{id}'.format(id=id))
        return self._call('DELETE', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('capabilities', 'fields', 'filter')
    def get_access_users_with_capability_filter(self, *, capabilities, fields=None, filter=None, Range=None, **kwargs):
        """
        GET /staged_config/access/users_with_capability_filter
        Retrieves a list of staged users.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'access/users_with_capability_filter')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_access_control_user_delete_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):
        """
        GET /staged_config/access_control/user_delete_tasks/{task_id}
        Retrieve the delete the User task status.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'access_control/user_delete_tasks/{task_id}'.format(task_id=task_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_access_control_users(self, *, fields=None, filter=None, Range=None, **kwargs):
        """
        GET /staged_config/access_control/users
        Retrieve the Staged Users
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'access_control/users')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def delete_access_control_users_by_id(self, id, *, fields=None, **kwargs):
        """
        DELETE /staged_config/access_control/users/{id}
        Delete the User. To ensure safe deletion we check if anything depends on it, this may take some time. Therefore we start an asynchronous task to do this.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'access_control/users/{id}'.format(id=id))
        return self._call('DELETE', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_access_control_users_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /staged_config/access_control/users/{id}
        Retrieve the Staged User
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'access_control/users/{id}'.format(id=id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_backup_and_restore_scheduled_backup_configurations(self, *, fields=None, **kwargs):
        """
        GET /staged_config/backup_and_restore/scheduled_backup_configurations
        Retrieves a list of the Staged Backup Configurations.
        """
        function_endpoint = urljoin(self._baseurl, 'backup_and_restore/scheduled_backup_configurations')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_backup_and_restore_scheduled_backup_configurations_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /staged_config/backup_and_restore/scheduled_backup_configurations/{id}
        Retrieves a Staged Backup Configuration by ID.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'backup_and_restore/scheduled_backup_configurations/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_backup_and_restore_scheduled_backup_configurations_by_id(self, id, *, backupConfiguration, fields=None,
                                                                      **kwargs):
        """
        POST /staged_config/backup_and_restore/scheduled_backup_configurations/{id}
        Updates a Staged Backup Configuration.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'backup_and_restore/scheduled_backup_configurations/{id}'.format(id=id))
        return self._call('POST', function_endpoint, json=backupConfiguration, **kwargs)

    def post_certificates_certificate_signing_request(self, *, CSRModel, **kwargs):
        """
        POST /staged_config/certificates/certificate_signing_request
         Creates a new Certificate Signing Request (CSR) file.
         A private key is generated and used to create the CSR file. The private key is kept secure on the Console. Use the GET call to download the CSR file.
         You must have System Administrator or Security Administrator permissions to use this endpoint.
        """
        function_endpoint = urljoin(self._baseurl, 'certificates/certificate_signing_request')
        return self._call('POST', function_endpoint, response_type='text/plain', json=CSRModel, **kwargs)

    @request_vars('filter', 'fields')
    def get_certificates_certificate_signing_request(self, *, filter=None, fields=None, **kwargs):
        """
        GET /staged_config/certificates/certificate_signing_request
        List of Certificate Signing Request (CSR) metadata that is stored in the certificate_signing_request database table.
        """
        function_endpoint = urljoin(self._baseurl, 'certificates/certificate_signing_request')
        return self._call('GET', function_endpoint, **kwargs)

    def delete_certificates_certificate_signing_request_by_id(self, id, **kwargs):
        """
        DELETE /staged_config/certificates/certificate_signing_request/{id}
        Deletes the Certificate Signing Request (CSR) resource.
        """
        function_endpoint = urljoin(self._baseurl, 'certificates/certificate_signing_request/{id}'.format(id=id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    def get_certificates_certificate_signing_request_by_id(self, id, **kwargs):
        """
        GET /staged_config/certificates/certificate_signing_request/{id}
        Download the generated Certificate Signing Request (CSR) file.
        """
        function_endpoint = urljoin(self._baseurl, 'certificates/certificate_signing_request/{id}'.format(id=id))
        return self._call('GET', function_endpoint, response_type='application/octet-stream', **kwargs)

    @header_vars('fields')
    def post_certificates_end_certificates(self, *, CertificateDTO, fields=None, **kwargs):
        """
        POST /staged_config/certificates/end_certificates
        Use this endpoint to create a new certificate resource on the Console.
        This endpoint creates a keystore file that contains the supplied security objects.
        You must have System Administrator or Security Administrator permissions to use this endpoint. An administrator must deploy the configuration change.
        """
        function_endpoint = urljoin(self._baseurl, 'certificates/end_certificates')
        return self._call('POST', function_endpoint, json=CertificateDTO, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_certificates_end_certificates(self, *, Range=None, filter=None, fields=None, **kwargs):
        """
        GET /staged_config/certificates/end_certificates
        Gets the list of uploaded certificates from the staged area.
        You must have System Administrator, Security Administrator, Manage Log Sources, or WinCollect permissions to use this endpoint.
        """
        function_endpoint = urljoin(self._baseurl, 'certificates/end_certificates')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_certificates_end_certificates_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /staged_config/certificates/end_certificates/{id}
        Gets information about a specific certificate, as specified by the certificate ID.
        You must have System Administrator, Security Administrator, Manage Log Sources, or WinCollect permissions to use this endpoint.
        """
        function_endpoint = urljoin(self._baseurl, 'certificates/end_certificates/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    def delete_certificates_end_certificates_by_id(self, id, **kwargs):
        """
        DELETE /staged_config/certificates/end_certificates/{id}
        Marks the certificate for deletion, but doesn't immediately remove it.
        After this request, the value of the certificate's Status field is change to DELETE_PENDING. To remove the certificate from the console and managed hosts, you must deploy the change after invoking this API.
        You must have System Administrator or Security Administrator permissions to use this endpoint.
        """
        function_endpoint = urljoin(self._baseurl, 'certificates/end_certificates/{id}'.format(id=id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @header_vars('fields')
    def post_certificates_end_certificates_by_id(self, id, *, CertificateDTO, fields=None, **kwargs):
        """
        POST /staged_config/certificates/end_certificates/{id}
        Use this endpoint to update an existing certificate resource.
         The ID that is specified in the URL path indicates the target resource to be modified. The parameter to be modified on the target resource is included in the
        body as a JSON object, with the new data value. The endpoint updates only the specified parameters. Empty values or missing parameters are ignored.
        You must have System Administrator or Security Administrator permissions to use this endpoint. After the certificate resource is updated, an administrator must deploy the updated Keystore file.
        """
        function_endpoint = urljoin(self._baseurl, 'certificates/end_certificates/{id}'.format(id=id))
        return self._call('POST', function_endpoint, json=CertificateDTO, **kwargs)

    @header_vars('fields')
    def post_certificates_root_certificates(self, *, certificate_content, fields=None, **kwargs):
        """
        POST /staged_config/certificates/root_certificates
        Uploads a new single root certificate to the staged configuration folder on the Console.
        This API enables the deployment of new root certificates to managed hosts, which enables the TLS handshake between a managed host and a destination device.
        The following steps are required to push the root certificate to the managed host:

        Invoke this synchronous endpoint to upload the new single root certificate to the staged configuration folder on the Console.
        Deploy the changes to push the new root certificate to the managed host.


        You must have System Administrator permissions to use this endpoint.
        """
        function_endpoint = urljoin(self._baseurl, 'certificates/root_certificates')
        return self._call('POST', function_endpoint, mime_type={'Content-Type': 'text/plain'}, data=certificate_content,
                          **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_certificates_root_certificates(self, *, Range=None, filter=None, fields=None, **kwargs):
        """
        GET /staged_config/certificates/root_certificates
        Gets the list of all of the root certificates that are uploaded.
        You must have System Administrator or Security Administrator permissions to use this endpoint.
        """
        function_endpoint = urljoin(self._baseurl, 'certificates/root_certificates')
        return self._call('GET', function_endpoint, **kwargs)

    def delete_certificates_root_certificates_by_id(self, id, **kwargs):
        """
        DELETE /staged_config/certificates/root_certificates/{id}
        Deletes a certificate from the staged configuration folder on the Console, but does not remove the certificate from the managed host.
        To remove the certificate from managed hosts, invoke this API and then deploy the configuration changes.
        You must have System Administrator permissions to use this endpoint.
        """
        function_endpoint = urljoin(self._baseurl, 'certificates/root_certificates/{id}'.format(id=id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @request_vars('fields')
    def get_certificates_root_certificates_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /staged_config/certificates/root_certificates/{id}
        Gets details of an uploaded root certificate, as specified by the ID.
        You must have System Administrator or Security Administrator permissions to use this endpoint.
        """
        function_endpoint = urljoin(self._baseurl, 'certificates/root_certificates/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    def post_deploy_status(self, *, deploy_status, **kwargs):
        """
        POST /staged_config/deploy_status
        Executes a deploy.
        """
        function_endpoint = urljoin(self._baseurl, 'deploy_status')
        return self._call('POST', function_endpoint, json=deploy_status, **kwargs)

    def get_deploy_status(self, **kwargs):
        """
        GET /staged_config/deploy_status
        Retrieves the status of a deploy in progress.
        """
        function_endpoint = urljoin(self._baseurl, 'deploy_status')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_deployment_hosts(self, *, Range=None, filter=None, fields=None, **kwargs):
        """
        GET /staged_config/deployment/hosts
        Retrieves a list of all staged hosts.
        """
        function_endpoint = urljoin(self._baseurl, 'deployment/hosts')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_deployment_hosts_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /staged_config/deployment/hosts/{id}
        Retrieves a staged host by ID. The Host object has the following fields:
        """
        function_endpoint = urljoin(self._baseurl, 'deployment/hosts/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_deployment_hosts_tunnels_by_id(self, id, *, Range=None, filter=None, fields=None, **kwargs):
        """
        GET /staged_config/deployment/hosts/{id}/tunnels
        Gets the list of tunnels for the host.
        """
        function_endpoint = urljoin(self._baseurl, 'deployment/hosts/{id}/tunnels'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_deployment_hosts_id_tunnels_by_name(self, id, name, *, tunnel, fields=None, **kwargs):
        """
        POST /staged_config/deployment/hosts/{id}/tunnels/{name}
        Updates a tunnel by host ID and tunnel name.  The update is in the staged configuration and a deployment is needed.

        The only editable field is reverse_source. The default is false and can be set to true.
        """
        function_endpoint = urljoin(self._baseurl, 'deployment/hosts/{id}/tunnels/{name}'.format(id=id, name=name))
        return self._call('POST', function_endpoint, json=tunnel, **kwargs)

    @request_vars('fields')
    def get_disaster_recovery_disaster_recovery_config(self, *, fields=None, **kwargs):
        """
        GET /staged_config/disaster_recovery/disaster_recovery_config
        Retrieves the Staged Disaster Recovery Config.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'disaster_recovery/disaster_recovery_config')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('fields')
    def post_disaster_recovery_disaster_recovery_config(self, *, drConfig, fields=None, **kwargs):
        """
        POST /staged_config/disaster_recovery/disaster_recovery_config
        Update the Staged Disaster Recovery Config.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'disaster_recovery/disaster_recovery_config')
        return self._call('POST', function_endpoint, json=drConfig, headers=headers, **kwargs)

    @header_vars('fields')
    def post_flow_applications_active_applications(self, *, body, fields=None, **kwargs):
        """
        POST /staged_config/flow/applications/active_applications
        Create a new active flow application in the staged configuration area.
        """
        function_endpoint = urljoin(self._baseurl, 'flow/applications/active_applications')
        return self._call('POST', function_endpoint, json=body, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields', 'sort')
    def get_flow_applications_active_applications(self, *, Range=None, filter=None, fields=None, sort=None, **kwargs):
        """
        GET /staged_config/flow/applications/active_applications
        Gets the list of active flow applications that are in the staged configuration area.
        """
        function_endpoint = urljoin(self._baseurl, 'flow/applications/active_applications')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_flow_applications_active_applications_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /staged_config/flow/applications/active_applications/{id}
        Gets an individual active flow application that is in the staged configuration area, as specified by the application ID.

        Active applications are flow applications that are currently in-use by the system. Active applications that are in the staged configuration area are not yet deployed.
        Changes or modifications to a flow application should always be made to the active applications list. Do not update the default applications.

        You must have System Administrator or Security Administrator permissions to use this endpoint.
        """
        function_endpoint = urljoin(self._baseurl, 'flow/applications/active_applications/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_flow_applications_active_applications_by_id(self, id, *, body, fields=None, **kwargs):
        """
        POST /staged_config/flow/applications/active_applications/{id}
        Updates an active flow application that is in the staged configuration area, as specified by the application ID.
        """
        function_endpoint = urljoin(self._baseurl, 'flow/applications/active_applications/{id}'.format(id=id))
        return self._call('POST', function_endpoint, json=body, **kwargs)

    def delete_flow_applications_active_applications_by_id(self, id, **kwargs):
        """
        DELETE /staged_config/flow/applications/active_applications/{id}
        Removes the active flow application from the staged configuration area, as specified by the application ID.
        """
        function_endpoint = urljoin(self._baseurl, 'flow/applications/active_applications/{id}'.format(id=id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_remote_networks(self, *, fields=None, filter=None, Range=None, **kwargs):
        """
        GET /staged_config/remote_networks
        Retrieves a list of staged remote networks.
        """
        function_endpoint = urljoin(self._baseurl, 'remote_networks')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_remote_networks(self, *, network, fields=None, **kwargs):
        """
        POST /staged_config/remote_networks
        Adds a new staged remote network.
        """
        function_endpoint = urljoin(self._baseurl, 'remote_networks')
        return self._call('POST', function_endpoint, json=network, **kwargs)

    @request_vars('fields')
    def get_remote_networks_by_network_id(self, network_id, *, fields=None, **kwargs):
        """
        GET /staged_config/remote_networks/{network_id}
        Retrieves a staged remote network by ID.
        """
        function_endpoint = urljoin(self._baseurl, 'remote_networks/{network_id}'.format(network_id=network_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_remote_networks_by_network_id(self, network_id, *, network, fields=None, **kwargs):
        """
        POST /staged_config/remote_networks/{network_id}
        Updates an existing staged remote network.
        """
        function_endpoint = urljoin(self._baseurl, 'remote_networks/{network_id}'.format(network_id=network_id))
        return self._call('POST', function_endpoint, json=network, **kwargs)

    def delete_remote_networks_by_network_id(self, network_id, **kwargs):
        """
        DELETE /staged_config/remote_networks/{network_id}
        Deletes an existing staged remote network.
        """
        function_endpoint = urljoin(self._baseurl, 'remote_networks/{network_id}'.format(network_id=network_id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_remote_services(self, *, fields=None, filter=None, Range=None, **kwargs):
        """
        GET /staged_config/remote_services
        Retrieves a list of staged remote services.
        """
        function_endpoint = urljoin(self._baseurl, 'remote_services')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_remote_services(self, *, service, fields=None, **kwargs):
        """
        POST /staged_config/remote_services
        Adds a staged remote service.
        """
        function_endpoint = urljoin(self._baseurl, 'remote_services')
        return self._call('POST', function_endpoint, json=service, **kwargs)

    @header_vars('fields')
    def post_remote_services_by_service_id(self, service_id, *, service, fields=None, **kwargs):
        """
        POST /staged_config/remote_services/{service_id}
        Updates an existing staged remote service.
        """
        function_endpoint = urljoin(self._baseurl, 'remote_services/{service_id}'.format(service_id=service_id))
        return self._call('POST', function_endpoint, json=service, **kwargs)

    def delete_remote_services_by_service_id(self, service_id, **kwargs):
        """
        DELETE /staged_config/remote_services/{service_id}
        Deletes an existing staged remote service.
        """
        function_endpoint = urljoin(self._baseurl, 'remote_services/{service_id}'.format(service_id=service_id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @request_vars('fields')
    def get_remote_services_by_service_id(self, service_id, *, fields=None, **kwargs):
        """
        GET /staged_config/remote_services/{service_id}
        Retrieves a staged remote service by ID.
        """
        function_endpoint = urljoin(self._baseurl, 'remote_services/{service_id}'.format(service_id=service_id))
        return self._call('GET', function_endpoint, **kwargs)

    def delete_yara_rules(self, **kwargs):
        """
        DELETE /staged_config/yara_rules
        Deletes all Yara rules from the QRadar system.
        """
        function_endpoint = urljoin(self._baseurl, 'yara_rules')
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    def put_yara_rules(self, *, file, **kwargs):
        """
        PUT /staged_config/yara_rules
        Uploads the supplied Yara rule file to the QRadar system.
        If the provided Yara file is empty - all rules are deleted from the system.
        """
        function_endpoint = urljoin(self._baseurl, 'yara_rules')
        return self._call('PUT', function_endpoint, response_type='text/plain', **kwargs)
