from urllib.parse import urljoin

from qradar4py.endpoints.api_endpoint import QRadarAPIEndpoint
from qradar4py.endpoints.api_endpoint import request_vars
from qradar4py.endpoints.api_endpoint import header_vars


class Siem(QRadarAPIEndpoint):
    """
    The QRadar API endpoint group /siem and its endpoints.
    """
    __baseurl = 'siem/'

    def __init__(self, url, header, verify):
        super().__init__(urljoin(url, self.__baseurl),
                         header,
                         verify)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_local_destination_addresses(self, *, fields=None, Range=None, filter=None, **kwargs):
        """
        GET /siem/local_destination_addresses
        Retrieve a list offense local destination addresses currently in the system.
        """
        function_endpoint = urljoin(self._baseurl, 'local_destination_addresses')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_local_destination_addresses_by_local_destination_address_id(self, local_destination_address_id, *,
                                                                        fields=None, **kwargs):
        """
        GET /siem/local_destination_addresses/{local_destination_address_id}
        Retrieve an offense local destination address.
        """
        function_endpoint = urljoin(self._baseurl, 'local_destination_addresses/{local_destination_address_id}'.format(
            local_destination_address_id=local_destination_address_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('include_reserved', 'include_deleted', 'fields', 'filter')
    def get_offense_closing_reasons(self, *, include_reserved=None, include_deleted=None, fields=None, Range=None,
                                    filter=None, **kwargs):
        """
        GET /siem/offense_closing_reasons
        Retrieve a list of all offense closing reasons.
        """
        function_endpoint = urljoin(self._baseurl, 'offense_closing_reasons')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('reason', 'fields')
    def post_offense_closing_reasons(self, *, reason, fields=None, **kwargs):
        """
        POST /siem/offense_closing_reasons
        Create an offense closing reason.
        """
        function_endpoint = urljoin(self._baseurl, 'offense_closing_reasons')
        return self._call('POST', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_offense_closing_reasons_by_closing_reason_id(self, closing_reason_id, *, fields=None, **kwargs):
        """
        GET /siem/offense_closing_reasons/{closing_reason_id}
        Retrieve an offense closing reason.
        """
        function_endpoint = urljoin(self._baseurl, 'offense_closing_reasons/{closing_reason_id}'.format(
            closing_reason_id=closing_reason_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_offense_saved_search_delete_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):
        """
        GET /siem/offense_saved_search_delete_tasks/{task_id}
        Retrieves the delete the offense saved search task status.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'offense_saved_search_delete_tasks/{task_id}'.format(task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_offense_saved_search_dependent_tasks_by_task_id(self, task_id, *, task, fields=None, **kwargs):
        """
        POST /siem/offense_saved_search_dependent_tasks/{task_id}
        Cancels the dependent the offense saved search task.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'offense_saved_search_dependent_tasks/{task_id}'.format(task_id=task_id))
        return self._call('POST', function_endpoint, json=task, **kwargs)

    @request_vars('fields')
    def get_offense_saved_search_dependent_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):
        """
        GET /siem/offense_saved_search_dependent_tasks/{task_id}
        Retrieves the dependent the offense saved search task status.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'offense_saved_search_dependent_tasks/{task_id}'.format(task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_offense_saved_search_dependent_tasks_results_by_task_id(self, task_id, *, fields=None, **kwargs):
        """
        GET /siem/offense_saved_search_dependent_tasks/{task_id}/results
        Retrieves the offense saved search dependent task results.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'offense_saved_search_dependent_tasks/{task_id}/results'.format(task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_offense_saved_search_groups(self, *, fields=None, Range=None, filter=None, **kwargs):
        """
        GET /siem/offense_saved_search_groups
        Retrieves a list of offense saved search groups.
        """
        function_endpoint = urljoin(self._baseurl, 'offense_saved_search_groups')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_offense_saved_search_groups_by_group_id(self, group_id, *, group, fields=None, **kwargs):
        """
        POST /siem/offense_saved_search_groups/{group_id}
        Updates the owner of an offense saved search group.
        """
        function_endpoint = urljoin(self._baseurl, 'offense_saved_search_groups/{group_id}'.format(group_id=group_id))
        return self._call('POST', function_endpoint, json=group, **kwargs)

    def delete_offense_saved_search_groups_by_group_id(self, group_id, **kwargs):
        """
        DELETE /siem/offense_saved_search_groups/{group_id}
        Deletes an offense saved search group.
        """
        function_endpoint = urljoin(self._baseurl, 'offense_saved_search_groups/{group_id}'.format(group_id=group_id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @request_vars('fields')
    def get_offense_saved_search_groups_by_group_id(self, group_id, *, fields=None, **kwargs):
        """
        GET /siem/offense_saved_search_groups/{group_id}
        Retrieves an offense saved search group.
        """
        function_endpoint = urljoin(self._baseurl, 'offense_saved_search_groups/{group_id}'.format(group_id=group_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_offense_saved_searches(self, *, fields=None, Range=None, filter=None, **kwargs):
        """
        GET /siem/offense_saved_searches
        Retrieves a list of offense saved searches.
        """
        function_endpoint = urljoin(self._baseurl, 'offense_saved_searches')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_offense_saved_searches_by_id(self, id, *, fields=None, Range=None, filter=None, **kwargs):
        """
        GET /siem/offense_saved_searches/{id}
        Retrieves an offense saved search.
        """
        function_endpoint = urljoin(self._baseurl, 'offense_saved_searches/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def delete_offense_saved_searches_by_id(self, id, *, fields=None, Range=None, filter=None, **kwargs):
        """
        DELETE /siem/offense_saved_searches/{id}
        Deletes an offense saved search. To ensure safe deletion, a dependency check is carried out. This check might take some time. An asynchronous task to do is started for this check.
        """
        function_endpoint = urljoin(self._baseurl, 'offense_saved_searches/{id}'.format(id=id))
        return self._call('DELETE', function_endpoint, **kwargs)

    @header_vars('fields', 'Range', 'filter')
    def post_offense_saved_searches_by_id(self, id, *, saved_search, fields=None, Range=None, filter=None, **kwargs):
        """
        POST /siem/offense_saved_searches/{id}
        Updates the offense saved search owner only.
        """
        function_endpoint = urljoin(self._baseurl, 'offense_saved_searches/{id}'.format(id=id))
        return self._call('POST', function_endpoint, json=saved_search, **kwargs)

    @request_vars('fields')
    def get_offense_saved_searches_dependents_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /siem/offense_saved_searches/{id}/dependents
        Retrieves the objects that depend on an offense saved search.
        """
        function_endpoint = urljoin(self._baseurl, 'offense_saved_searches/{id}/dependents'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'sort', 'filter')
    def get_offense_types(self, *, fields=None, sort=None, Range=None, filter=None, **kwargs):
        """
        GET /siem/offense_types
        Retrieve all the Offense Types
        """
        function_endpoint = urljoin(self._baseurl, 'offense_types')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_offense_types_by_offense_type_id(self, offense_type_id, *, fields=None, **kwargs):
        """
        GET /siem/offense_types/{offense_type_id}
        Retrieve an offense type structure that describes the properties of an offense type.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'offense_types/{offense_type_id}'.format(offense_type_id=offense_type_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'sort', 'filter')
    def get_offenses(self, *, fields=None, sort=None, Range=None, filter=None, **kwargs):
        """
        GET /siem/offenses
        Retrieve a list of offenses currently in the system.
        """
        function_endpoint = urljoin(self._baseurl, 'offenses')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('protected', 'follow_up', 'status', 'closing_reason_id', 'assigned_to', 'fields')
    def post_offenses_by_offense_id(self, offense_id, *, protected=None, follow_up=None, status=None,
                                    closing_reason_id=None, assigned_to=None, fields=None, **kwargs):
        """
        POST /siem/offenses/{offense_id}
        Update an offense.
        """
        function_endpoint = urljoin(self._baseurl, 'offenses/{offense_id}'.format(offense_id=offense_id))
        return self._call('POST', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_offenses_by_offense_id(self, offense_id, *, fields=None, **kwargs):
        """
        GET /siem/offenses/{offense_id}
        Retrieve an offense structure that describes  properties of an offense
        """
        function_endpoint = urljoin(self._baseurl, 'offenses/{offense_id}'.format(offense_id=offense_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('note_text', 'fields')
    def post_offenses_notes_by_offense_id(self, offense_id, *, note_text, fields=None, **kwargs):
        """
        POST /siem/offenses/{offense_id}/notes
        Create a note on an offense.
        """
        function_endpoint = urljoin(self._baseurl, 'offenses/{offense_id}/notes'.format(offense_id=offense_id))
        return self._call('POST', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_offenses_notes_by_offense_id(self, offense_id, *, fields=None, Range=None, filter=None, **kwargs):
        """
        GET /siem/offenses/{offense_id}/notes
        Retrieve a list of notes for an offense.
        """
        function_endpoint = urljoin(self._baseurl, 'offenses/{offense_id}/notes'.format(offense_id=offense_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_offenses_offense_id_notes_by_note_id(self, offense_id, note_id, *, fields=None, **kwargs):
        """
        GET /siem/offenses/{offense_id}/notes/{note_id}
        Retrieve a note for an offense.
        """
        function_endpoint = urljoin(self._baseurl, 'offenses/{offense_id}/notes/{note_id}'.format(offense_id=offense_id,
                                                                                                  note_id=note_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_source_addresses(self, *, fields=None, Range=None, filter=None, **kwargs):
        """
        GET /siem/source_addresses
        Retrieve a list offense source addresses currently in the system.
        """
        function_endpoint = urljoin(self._baseurl, 'source_addresses')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_source_addresses_by_source_address_id(self, source_address_id, *, fields=None, **kwargs):
        """
        GET /siem/source_addresses/{source_address_id}
        Retrieve an offense source address.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'source_addresses/{source_address_id}'.format(source_address_id=source_address_id))
        return self._call('GET', function_endpoint, **kwargs)
