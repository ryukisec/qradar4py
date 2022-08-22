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
    @request_vars('tenant_id', 'filter', 'fields')
    def get_access_security_profiles(self, *, tenant_id=None, filter=None, Range=None, fields=None, **kwargs):
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
    @request_vars('contains', 'filter', 'fields')
    def get_access_user_roles(self, *, contains=None, filter=None, Range=None, fields=None, **kwargs):
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
    @request_vars('sort', 'filter', 'fields')
    def get_access_users(self, *, sort=None, filter=None, Range=None, fields=None, **kwargs):
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

    @request_vars('fields')
    def get_access_users_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /staged_config/access/users/{id}
        Retrieves a staged user.
        """
        function_endpoint = urljoin(self._baseurl, 'access/users/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_access_users_by_id(self, id, *, body, fields=None, **kwargs):
        """
        POST /staged_config/access/users/{id}
        Update a staged user.
        """
        function_endpoint = urljoin(self._baseurl, 'access/users/{id}'.format(id=id))
        return self._call('POST', function_endpoint, json=body, **kwargs)

    @request_vars('fields')
    def delete_access_users_by_id(self, id, *, fields=None, **kwargs):
        """
        DELETE /staged_config/access/users/{id}
        Deletes a user from staging. To ensure safe deletion, dependencies are checked. This might take some time. An asynchronous task is started to do this check.
        """
        function_endpoint = urljoin(self._baseurl, 'access/users/{id}'.format(id=id))
        return self._call('DELETE', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('capabilities', 'filter', 'fields')
    def get_access_users_with_capability_filter(self, *, capabilities, filter=None, Range=None, fields=None, **kwargs):
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
    @request_vars('filter', 'fields')
    def get_access_control_users(self, *, filter=None, Range=None, fields=None, **kwargs):
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

    @header_vars('fields')
    def post_ca_certs(self, *, file, fields=None, **kwargs):
        """
        POST /staged_config/ca_certs

        Uploads a new CA certificate to the staged configuration folder on the QRadar Console.
        This API enables the deployment of new CA certificates to managed hosts, which enables the TLS handshake between a managed host and a destination device.
        The following steps are required to push the CA certificate to the managed host:

        Invoke this synchronous endpoint to upload the new CA certificate to the staged configuration folder on the QRadar Console
        Start a deployment process to push the new CA certificate to the managed host


        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'ca_certs')
        return self._call('POST', function_endpoint, mime_type={'Content-Type': 'multipart/form-data'}, data=file,
                          headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_ca_certs(self, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /staged_config/ca_certs
        Gets the list of uploaded CA certificates. A Certificate object has the following fields:
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'ca_certs')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    def delete_ca_certs_by_id(self, id, **kwargs):
        """
        DELETE /staged_config/ca_certs/{id}
        Deletes a certificate from the staged configuration folder on the QRadar Console but does not remove the certificate from the managed host.
        To remove the certificate from managed hosts, start the deployment process after you invoke this API.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'ca_certs/{id}'.format(id=id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', headers=headers, **kwargs)

    @request_vars('fields')
    def get_ca_certs_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /staged_config/ca_certs/{id}
        Gets information about the uploaded CA certificate, which is identified by its ID.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'ca_certs/{id}'.format(id=id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('filter', 'fields')
    def get_certificates_certificate_signing_request(self, *, filter=None, fields=None, **kwargs):
        """
        GET /staged_config/certificates/certificate_signing_request
        List of Certificate Signing Request (CSR) metadata that is stored in the certificate_signing_request database table.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'certificates/certificate_signing_request')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    def post_certificates_certificate_signing_request(self, *, CSRModel, **kwargs):
        """
        POST /staged_config/certificates/certificate_signing_request
        Creates a new Certificate Signing Request (CSR) file. A private key is generated and used to create the CSR file. The private key is kept secure in the QRadar server. Use the GET call to download the CSR file.

        This endpoint creates a certificate signing request file.
        You must have ADMIN or SAASADMIN capabilities to invoke this API.

        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'certificates/certificate_signing_request')
        return self._call('POST', function_endpoint, response_type='text/plain', json=CSRModel, headers=headers,
                          **kwargs)

    def get_certificates_certificate_signing_request_by_id(self, id, **kwargs):
        """
        GET /staged_config/certificates/certificate_signing_request/{id}
        Download the generated support log file.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'certificates/certificate_signing_request/{id}'.format(id=id))
        return self._call('GET', function_endpoint, response_type='application/octet-stream', headers=headers, **kwargs)

    def delete_certificates_certificate_signing_request_by_id(self, id, **kwargs):
        """
        DELETE /staged_config/certificates/certificate_signing_request/{id}
        Deletes the Certificate Signing Request (CSR) resource.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'certificates/certificate_signing_request/{id}'.format(id=id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_certificates_end_certificates(self, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /staged_config/certificates/end_certificates
        Gets the list of uploaded certificates from the staged area.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'certificates/end_certificates')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('fields')
    def post_certificates_end_certificates(self, *, CertificateDTO, fields=None, **kwargs):
        """
        POST /staged_config/certificates/end_certificates
        Use this endpoint to create a new certificate resource on the server.

        This endpoint creates a keystore file of the supplied security objects.
        Users must have ADMIN or SAASADMIN capabilities to invoke this API. An administrator must deploy the configuration change.

        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'certificates/end_certificates')
        return self._call('POST', function_endpoint, json=CertificateDTO, headers=headers, **kwargs)

    @header_vars('fields')
    def post_certificates_end_certificates_by_id(self, id, *, CertificateDTO, fields=None, **kwargs):
        """
        POST /staged_config/certificates/end_certificates/{id}
        Updates a certificate resource

        Use this endpoint to update an existing certificate resource.


        The ID that is specified in the URL path indicates the target resource to be modified. The parameter to be modified on the target resource is included in the
        body as a JSON object, with the new data value. The endpoint updates only the specified parameter(s). Empty values or missing parameters are ignored.
        After the certificate resource is updated, an administrator must deploy the updated keystore file.

         Users must have ADMIN or SAASADMIN capabilities to invoke this API. An administrator must deploy the configuration change.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'certificates/end_certificates/{id}'.format(id=id))
        return self._call('POST', function_endpoint, json=CertificateDTO, headers=headers, **kwargs)

    def delete_certificates_end_certificates_by_id(self, id, **kwargs):
        """
        DELETE /staged_config/certificates/end_certificates/{id}
        Marks the certificate for deletion, but doesn't immediately remove it.

        After this request, the value of the certificate's Status field is change to DELETE_PENDING.
        To remove the certificate from the console and managed hosts, you must deploy the change after invoking this API.

        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'certificates/end_certificates/{id}'.format(id=id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', headers=headers, **kwargs)

    @request_vars('fields')
    def get_certificates_end_certificates_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /staged_config/certificates/end_certificates/{id}
        Gets information about a specific certificate, which is identified by its ID.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'certificates/end_certificates/{id}'.format(id=id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_certificates_root_certificates(self, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /staged_config/certificates/root_certificates
        Gets the list of all root certificates that have been uploaded.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'certificates/root_certificates')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('fields')
    def post_certificates_root_certificates(self, *, certificate_content, fields=None, **kwargs):
        """
        POST /staged_config/certificates/root_certificates

        Uploads a new single root certificate to the staged configuration folder on the QRadar Console.
        This API enables the deployment of new root certificates to managed hosts, which enables the TLS handshake between a managed host and a destination device.
        The following steps are required to push the root certificate to the managed host:

        Invoke this synchronous endpoint to upload the new single root certificate to the staged configuration folder on the QRadar Console
        Start a deployment process to push the new root certificate to the managed host


        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'certificates/root_certificates')
        return self._call('POST', function_endpoint, mime_type={'Content-Type': 'text/plain'}, data=certificate_content,
                          headers=headers, **kwargs)

    @request_vars('fields')
    def get_certificates_root_certificates_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /staged_config/certificates/root_certificates/{id}
        Gets details of an uploaded root certificate by id.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'certificates/root_certificates/{id}'.format(id=id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    def delete_certificates_root_certificates_by_id(self, id, **kwargs):
        """
        DELETE /staged_config/certificates/root_certificates/{id}
        Deletes a certificate from the staged configuration folder on the QRadar Console but does not remove the certificate from the managed host.
        To remove the certificate from managed hosts, start the deployment process after you invoke this API.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'certificates/root_certificates/{id}'.format(id=id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', headers=headers, **kwargs)

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
    def get_deployment_hosts(self, *, filter=None, Range=None, fields=None, **kwargs):
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
    def get_deployment_hosts_tunnels_by_id(self, id, *, filter=None, Range=None, fields=None, **kwargs):
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

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_remote_networks(self, *, filter=None, Range=None, fields=None, **kwargs):
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

    def delete_remote_networks_by_network_id(self, network_id, **kwargs):
        """
        DELETE /staged_config/remote_networks/{network_id}
        Deletes an existing staged remote network.
        """
        function_endpoint = urljoin(self._baseurl, 'remote_networks/{network_id}'.format(network_id=network_id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

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

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_remote_services(self, *, filter=None, Range=None, fields=None, **kwargs):
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

    def delete_remote_services_by_service_id(self, service_id, **kwargs):
        """
        DELETE /staged_config/remote_services/{service_id}
        Deletes an existing staged remote service.
        """
        function_endpoint = urljoin(self._baseurl, 'remote_services/{service_id}'.format(service_id=service_id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @header_vars('fields')
    def post_remote_services_by_service_id(self, service_id, *, service, fields=None, **kwargs):
        """
        POST /staged_config/remote_services/{service_id}
        Updates an existing staged remote service.
        """
        function_endpoint = urljoin(self._baseurl, 'remote_services/{service_id}'.format(service_id=service_id))
        return self._call('POST', function_endpoint, json=service, **kwargs)

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
