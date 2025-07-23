from urllib.parse import urljoin

from qradar4py.endpoints.api_endpoint import QRadarAPIEndpoint
from qradar4py.endpoints.api_endpoint import request_vars
from qradar4py.endpoints.api_endpoint import header_vars


class BackupAndRestore(QRadarAPIEndpoint):
    """
    The QRadar API endpoint group /backup_and_restore and its endpoints.
    """
    __baseurl = 'backup_and_restore/'

    def __init__(self, url, header, verify):
        super().__init__(urljoin(url, self.__baseurl),
                         header,
                         verify)

    @header_vars('fields')
    def post_app_restores(self, *, restore, fields=None, **kwargs):
        """
        POST /backup_and_restore/app_restores
        This API will be useful to restore apps volume backup in failover and failback.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'app_restores')
        return self._call('POST', function_endpoint, json=restore, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields', 'sort')
    def get_backups(self, *, Range=None, filter=None, fields=None, sort=None, **kwargs):
        """
        GET /backup_and_restore/backups
        Retrieves a list of backups.
        """
        function_endpoint = urljoin(self._baseurl, 'backups')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('backup_type', 'fields')
    def post_backups(self, *, backup_type, backup, fields=None, **kwargs):
        """
        POST /backup_and_restore/backups
        Submits a request to the Backup and Restore Engine to create a new backup.
        """
        function_endpoint = urljoin(self._baseurl, 'backups')
        return self._call('POST', function_endpoint, json=backup, **kwargs)

    @request_vars('fields')
    def delete_backups_by_id(self, id, *, fields=None, **kwargs):
        """
        DELETE /backup_and_restore/backups/{id}
        Sends a request to the Backup and Restore Engine to delete an existing backup.
        """
        function_endpoint = urljoin(self._baseurl, 'backups/{id}'.format(id=id))
        return self._call('DELETE', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_backups_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /backup_and_restore/backups/{id}
        Retrieves an individual backup by ID.
        """
        function_endpoint = urljoin(self._baseurl, 'backups/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_backups_by_id(self, id, *, backup, fields=None, **kwargs):
        """
        POST /backup_and_restore/backups/{id}
        Updates an existing backup.
        """
        function_endpoint = urljoin(self._baseurl, 'backups/{id}'.format(id=id))
        return self._call('POST', function_endpoint, json=backup, **kwargs)

    @request_vars('fields')
    def get_haAction_by_flag(self, flag, *, fields=None, **kwargs):
        """
        GET /backup_and_restore/haAction/{flag}
        Done an individual HA Action as per passing flag.
        """
        function_endpoint = urljoin(self._baseurl, 'haAction/{flag}'.format(flag=flag))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_restores(self, *, restore, fields=None, **kwargs):
        """
        POST /backup_and_restore/restores
        Creates a restore object in the PENDING state.
        """
        function_endpoint = urljoin(self._baseurl, 'restores')
        return self._call('POST', function_endpoint, json=restore, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields', 'sort')
    def get_restores(self, *, Range=None, filter=None, fields=None, sort=None, **kwargs):
        """
        GET /backup_and_restore/restores
        Retrieves a list of restores.
        """
        function_endpoint = urljoin(self._baseurl, 'restores')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_restores_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /backup_and_restore/restores/{id}
        Retrieves an individual restore by ID.
        """
        function_endpoint = urljoin(self._baseurl, 'restores/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_restores_by_id(self, id, *, restore, fields=None, **kwargs):
        """
        POST /backup_and_restore/restores/{id}
        Updates an existing restore by ID.
        """
        function_endpoint = urljoin(self._baseurl, 'restores/{id}'.format(id=id))
        return self._call('POST', function_endpoint, json=restore, **kwargs)

    def delete_restores_by_id(self, id, **kwargs):
        """
        DELETE /backup_and_restore/restores/{id}
        Deletes an individual restore by ID.
        """
        function_endpoint = urljoin(self._baseurl, 'restores/{id}'.format(id=id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @header_vars('fields')
    def post_updateiptablesprefile(self, *, restore, fields=None, **kwargs):
        """
        POST /backup_and_restore/updateiptablesprefile
        Done an individual HA Action as per passing flag.
        """
        function_endpoint = urljoin(self._baseurl, 'updateiptablesprefile')
        return self._call('POST', function_endpoint, json=restore, **kwargs)
