from urllib.parse import urljoin

from qradar4py.endpoints.api_endpoint import QRadarAPIEndpoint
from qradar4py.endpoints.api_endpoint import request_vars
from qradar4py.endpoints.api_endpoint import header_vars


class Application(QRadarAPIEndpoint):
    """
    The QRadar API endpoint group /application and its endpoints.
    UNDOCUMENTED
    """
    __baseurl = 'application/'

    def __init__(self, url, header, verify):
        super().__init__(urljoin(url, self.__baseurl),
                         header,
                         verify)

    @header_vars('fields')
    def post_data_ingestion_configuration(self, *, data, fields=None, **kwargs):
        """
        POST /application/data_ingestion/configuration
        No summary provided
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'data_ingestion/configuration')
        return self._call('POST', function_endpoint, json=data, headers=headers, **kwargs)

    @request_vars('log_source_type_id')
    def delete_data_ingestion_custom_event_mapping(self, *, log_source_type_id=None, **kwargs):
        """
        DELETE /application/data_ingestion/custom_event_mapping
        endpoint to clean up the temp mapping entries in the staging table (dsmevent_stage)
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'data_ingestion/custom_event_mapping')
        return self._call('DELETE', function_endpoint, response_type='text/plain', headers=headers, **kwargs)

    @header_vars('fields')
    def post_data_ingestion_custom_property_definitions(self, *, data, fields=None, **kwargs):
        """
        POST /application/data_ingestion/custom_property_definitions
        Creates a new event regex property.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'data_ingestion/custom_property_definitions')
        return self._call('POST', function_endpoint, json=data, headers=headers, **kwargs)

    @request_vars('fields')
    def get_data_ingestion_event_regex_properties_by_regex_property_id(self, regex_property_id, *, fields=None,
                                                                       **kwargs):
        """
        GET /application/data_ingestion/event/regex_properties/{regex_property_id}
        Retrieves a event regex property based on the supplied regex property ID.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'data_ingestion/event/regex_properties/{regex_property_id}'.format(
            regex_property_id=regex_property_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_data_ingestion_event_regex_properties_dependents_by_regex_property_id(self, regex_property_id, *,
                                                                                  fields=None, **kwargs):
        """
        GET /application/data_ingestion/event/regex_properties/{regex_property_id}/dependents
        Retrieves the objects that depend on the event regex property.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'data_ingestion/event/regex_properties/{regex_property_id}/dependents'.format(
                                        regex_property_id=regex_property_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('fields')
    def post_data_ingestion_event_regex_property_dependent_tasks_by_task_id(self, task_id, *, task, fields=None,
                                                                            **kwargs):
        """
        POST /application/data_ingestion/event/regex_property_dependent_tasks/{task_id}
        Cancels the regex property dependent task.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'data_ingestion/event/regex_property_dependent_tasks/{task_id}'.format(
                                        task_id=task_id))
        return self._call('POST', function_endpoint, json=task, headers=headers, **kwargs)

    @request_vars('fields')
    def get_data_ingestion_event_regex_property_dependent_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):
        """
        GET /application/data_ingestion/event/regex_property_dependent_tasks/{task_id}
        Retrieves the event regex property dependent task status.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'data_ingestion/event/regex_property_dependent_tasks/{task_id}'.format(
                                        task_id=task_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_data_ingestion_event_regex_property_dependent_tasks_results_by_task_id(self, task_id, *, fields=None,
                                                                                   **kwargs):
        """
        GET /application/data_ingestion/event/regex_property_dependent_tasks/{task_id}/results
        Retrieves the regex property dependent task results.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'data_ingestion/event/regex_property_dependent_tasks/{task_id}/results'.format(
                                        task_id=task_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_data_ingestion_flow_regex_properties_by_regex_property_id(self, regex_property_id, *, fields=None,
                                                                      **kwargs):
        """
        GET /application/data_ingestion/flow/regex_properties/{regex_property_id}
        Retrieves a flow regex property based on the supplied regex property ID.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'data_ingestion/flow/regex_properties/{regex_property_id}'.format(
            regex_property_id=regex_property_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_data_ingestion_flow_regex_properties_dependents_by_regex_property_id(self, regex_property_id, *,
                                                                                 fields=None, **kwargs):
        """
        GET /application/data_ingestion/flow/regex_properties/{regex_property_id}/dependents
        Retrieves the objects that depend on the flow regex property.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'data_ingestion/flow/regex_properties/{regex_property_id}/dependents'.format(
                                        regex_property_id=regex_property_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_data_ingestion_flow_regex_property_dependent_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):
        """
        GET /application/data_ingestion/flow/regex_property_dependent_tasks/{task_id}
        Retrieves the flow regex property dependent task status.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'data_ingestion/flow/regex_property_dependent_tasks/{task_id}'.format(
                                        task_id=task_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('fields')
    def post_data_ingestion_flow_regex_property_dependent_tasks_by_task_id(self, task_id, *, task, fields=None,
                                                                           **kwargs):
        """
        POST /application/data_ingestion/flow/regex_property_dependent_tasks/{task_id}
        Cancels the flow regex property dependent task.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'data_ingestion/flow/regex_property_dependent_tasks/{task_id}'.format(
                                        task_id=task_id))
        return self._call('POST', function_endpoint, json=task, headers=headers, **kwargs)

    @request_vars('fields')
    def get_data_ingestion_flow_regex_property_dependent_tasks_results_by_task_id(self, task_id, *, fields=None,
                                                                                  **kwargs):
        """
        GET /application/data_ingestion/flow/regex_property_dependent_tasks/{task_id}/results
        Retrieves the regex property dependent task results.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'data_ingestion/flow/regex_property_dependent_tasks/{task_id}/results'.format(
                                        task_id=task_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_data_ingestion_identity_fields(self, *, fields=None, **kwargs):
        """
        GET /application/data_ingestion/identity_fields
        Gets the list of identity fields that can be populated for a normalized event
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'data_ingestion/identity_fields')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_data_ingestion_keyNameMappings(self, *, filter=None, fields=None, Range=None, **kwargs):
        """
        GET /application/data_ingestion/keyNameMappings
        No summary provided
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'data_ingestion/keyNameMappings')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    def post_data_ingestion_mappings_by_log_source_type_id(self, log_source_type_id, *, data, **kwargs):
        """
        POST /application/data_ingestion/mappings/{log_source_type_id}
        No summary provided
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'data_ingestion/mappings/{log_source_type_id}'.format(
            log_source_type_id=log_source_type_id))
        return self._call('POST', function_endpoint, json=data, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('produce_identity', 'custom_only', 'filter_text', 'override_only')
    def get_data_ingestion_mappings_by_log_source_type_id(self, log_source_type_id, *, produce_identity=None,
                                                          custom_only=None, filter_text=None, override_only=None,
                                                          Range=None, **kwargs):
        """
        GET /application/data_ingestion/mappings/{log_source_type_id}
        Retrieves a list of mappings.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'data_ingestion/mappings/{log_source_type_id}'.format(
            log_source_type_id=log_source_type_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    def put_data_ingestion_mappings_log_source_type_id_by_id(self, log_source_type_id, id, *, data, **kwargs):
        """
        PUT /application/data_ingestion/mappings/{log_source_type_id}/{id}
        This endpoint updates an existing temp mapping entry in the staging table (dsmevent_staging).
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'data_ingestion/mappings/{log_source_type_id}/{id}'.format(
            log_source_type_id=log_source_type_id, id=id))
        return self._call('PUT', function_endpoint, headers=headers, **kwargs)

    def delete_data_ingestion_mappings_log_source_type_id_by_id(self, log_source_type_id, id, **kwargs):
        """
        DELETE /application/data_ingestion/mappings/{log_source_type_id}/{id}
        delete a mapping entry in the staging table (dsmevent_stage)
        Note: this endpoint currently does not do anything. Its existence is to meet some front-end
        requirement (i.e., needed so some widget has a place to call the delete endpoint).
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'data_ingestion/mappings/{log_source_type_id}/{id}'.format(
            log_source_type_id=log_source_type_id, id=id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('handle_id', 'ids', 'filter', 'fields')
    def get_data_ingestion_payloads(self, *, handle_id, ids, filter=None, fields=None, Range=None, **kwargs):
        """
        GET /application/data_ingestion/payloads
        No summary provided
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'data_ingestion/payloads')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_data_ingestion_properties_by_log_source_type_id(self, log_source_type_id, *, fields=None, **kwargs):
        """
        GET /application/data_ingestion/properties/{log_source_type_id}
        Retrieves a list of properties belonging to a certain log source type.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'data_ingestion/properties/{log_source_type_id}'.format(
            log_source_type_id=log_source_type_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('qid', 'name', 'low_level_category_id', 'high_level_category_id', 'log_source_type_id', 'filter',
                  'fields', 'sort')
    def get_data_ingestion_qid_records(self, *, qid=None, name=None, low_level_category_id=None,
                                       high_level_category_id=None, log_source_type_id=None, filter=None, fields=None,
                                       sort=None, Range=None, **kwargs):
        """
        GET /application/data_ingestion/qid_records
        Retrieves a list of qid records.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'data_ingestion/qid_records')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_data_ingestion_qid_records_by_qid_record_id(self, qid_record_id, *, fields=None, **kwargs):
        """
        GET /application/data_ingestion/qid_records/{qid_record_id}
        Retrieves a qid record based on supplied qid_record_id.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'data_ingestion/qid_records/{qid_record_id}'.format(qid_record_id=qid_record_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('fields')
    def post_data_ingestion_simulate(self, *, data, fields=None, **kwargs):
        """
        POST /application/data_ingestion/simulate
        Simulates the parsing of a list of payloads given a log-source-type-id, a list of properties, and an optional
        list of event mappings.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'data_ingestion/simulate')
        return self._call('POST', function_endpoint, json=data, headers=headers, **kwargs)
