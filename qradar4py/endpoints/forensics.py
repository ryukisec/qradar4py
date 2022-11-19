from urllib.parse import urljoin

from qradar4py.endpoints.api_endpoint import QRadarAPIEndpoint
from qradar4py.endpoints.api_endpoint import request_vars
from qradar4py.endpoints.api_endpoint import header_vars


class Forensics(QRadarAPIEndpoint):
    """
    The QRadar API endpoint group /forensics and its endpoints.
    """
    __baseurl = 'forensics/'

    def __init__(self, url, header, verify):
        super().__init__(urljoin(url, self.__baseurl),
                         header,
                         verify)

    def post_alerting_jobs_by_id(self, id, *, alerting_job, **kwargs):
        """
        POST /forensics/alerting_jobs/{id}
        Updates the specified Workflow Alerting Job.
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': 'True'})
        function_endpoint = urljoin(self._baseurl, 'alerting_jobs/{id}'.format(id=id))
        return self._call('POST', function_endpoint, json=alerting_job, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_capture_recoveries(self, *, fields=None, Range=None, filter=None, **kwargs):
        """
        GET /forensics/capture/recoveries
        Retrieves a list of capture recoveries.
        """
        function_endpoint = urljoin(self._baseurl, 'capture/recoveries')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_capture_recoveries(self, *, recovery, fields=None, **kwargs):
        """
        POST /forensics/capture/recoveries
        Creates a new capture recovery.
        """
        function_endpoint = urljoin(self._baseurl, 'capture/recoveries')
        return self._call('POST', function_endpoint, json=recovery, **kwargs)

    @request_vars('fields')
    def get_capture_recoveries_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /forensics/capture/recoveries/{id}
        Retrieves a recovery based on the supplied ID.
        """
        function_endpoint = urljoin(self._baseurl, 'capture/recoveries/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_capture_recovery_tasks(self, *, fields=None, Range=None, filter=None, **kwargs):
        """
        GET /forensics/capture/recovery_tasks
        Retrieves a list of recovery tasks.
        """
        function_endpoint = urljoin(self._baseurl, 'capture/recovery_tasks')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_capture_recovery_tasks_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /forensics/capture/recovery_tasks/{id}
        Retrieves a recovery task based on the supplied ID.
        """
        function_endpoint = urljoin(self._baseurl, 'capture/recovery_tasks/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_case_management_case_create_tasks_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /forensics/case_management/case_create_tasks/{id}
        Retrieves a case create task based on the supplied id.
        """
        function_endpoint = urljoin(self._baseurl, 'case_management/case_create_tasks/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_case_management_cases(self, *, fields=None, Range=None, filter=None, **kwargs):
        """
        GET /forensics/case_management/cases
        Retrieves a list of cases.
        """
        function_endpoint = urljoin(self._baseurl, 'case_management/cases')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_case_management_cases(self, *, case, fields=None, **kwargs):
        """
        POST /forensics/case_management/cases
        Creates a new case.
        """
        function_endpoint = urljoin(self._baseurl, 'case_management/cases')
        return self._call('POST', function_endpoint, json=case, **kwargs)

    @request_vars('fields')
    def get_case_management_cases_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /forensics/case_management/cases/{id}
        Retrieves a case based on the supplied id.
        """
        function_endpoint = urljoin(self._baseurl, 'case_management/cases/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_managed_updates_by_host(self, host, *, fields=None, **kwargs):
        """
        GET /forensics/managed_updates/{host}
        Retrieves case, job, scheduled action and user information for the
        specified host.  The intent of if API is to give QIF managed hosts the
        ability to retrieve this information in a more timely manner than the db
        replication provides.  The information is combined into a single call
        to reduce the number of calls each QIF managed host must make.
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': 'True'})
        function_endpoint = urljoin(self._baseurl, 'managed_updates/{host}'.format(host=host))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    def post_recovery_jobs_by_id(self, id, *, recovery_job, **kwargs):
        """
        POST /forensics/recovery_jobs/{id}
        Updates the specified Workflow Recovery Job.
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': 'True'})
        function_endpoint = urljoin(self._baseurl, 'recovery_jobs/{id}'.format(id=id))
        return self._call('POST', function_endpoint, json=recovery_job, headers=headers, **kwargs)

    def post_scheduledactions_statuses_id_by_host(self, id, host, *, status, **kwargs):
        """
        POST /forensics/scheduledactions/statuses/{id}/{host}
        Updates the specified Scheduled Action Status.
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': 'True'})
        function_endpoint = urljoin(self._baseurl, 'scheduledactions/statuses/{id}/{host}'.format(id=id, host=host))
        return self._call('POST', function_endpoint, json=status, headers=headers, **kwargs)

    @request_vars('fields')
    def get_usermanagement_users_by_username(self, username, *, fields=None, **kwargs):
        """
        GET /forensics/usermanagement/users/{username}
        Retrieves the specified User.
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': 'True'})
        function_endpoint = urljoin(self._baseurl, 'usermanagement/users/{username}'.format(username=username))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)
