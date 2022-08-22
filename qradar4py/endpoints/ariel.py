from urllib.parse import urljoin

from qradar4py.endpoints.api_endpoint import QRadarAPIEndpoint
from qradar4py.endpoints.api_endpoint import request_vars
from qradar4py.endpoints.api_endpoint import header_vars


class Ariel(QRadarAPIEndpoint):
    """
    The QRadar API endpoint group /ariel and its endpoints.
    """
    __baseurl = 'ariel/'

    def __init__(self, url, header, verify):
        super().__init__(urljoin(url, self.__baseurl),
                         header,
                         verify)

    @header_vars('Range')
    @request_vars('filter')
    def get_databases(self, *, Range=None, filter=None, **kwargs):
        """
        GET /ariel/databases
        Retrieves a list of available Ariel database names
        """
        function_endpoint = urljoin(self._baseurl, 'databases')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_databases_by_database_name(self, database_name, *, fields=None, Range=None, filter=None, **kwargs):
        """
        GET /ariel/databases/{database_name}
        Retrieve the columns that are defined for a specific Ariel database.
        """
        function_endpoint = urljoin(self._baseurl, 'databases/{database_name}'.format(database_name=database_name))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('id_type')
    def get_datanode_clusters(self, *, id_type=None, Range=None, **kwargs):
        """
        GET /ariel/datanode/clusters
        Get all datanode cluster ids
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'datanode/clusters')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('id_type', 'timeout_msec', 'fields')
    def get_datanode_clusters_by_id(self, id, *, id_type=None, timeout_msec=None, fields=None, **kwargs):
        """
        GET /ariel/datanode/clusters/{id}
        Get datanode cluster by id
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'datanode/clusters/{id}'.format(id=id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('id_type')
    def get_datanode_nodes(self, *, id_type=None, Range=None, **kwargs):
        """
        GET /ariel/datanode/nodes
        Get all datanode node ids
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'datanode/nodes')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('id_type', 'timeout_msec', 'fields')
    def get_datanode_nodes_by_id(self, id, *, id_type=None, timeout_msec=None, fields=None, **kwargs):
        """
        GET /ariel/datanode/nodes/{id}
        Get datanode node by id
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'datanode/nodes/{id}'.format(id=id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_event_saved_search_groups(self, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /ariel/event_saved_search_groups
        Retrieves a list the event Ariel saved search groups.
        """
        function_endpoint = urljoin(self._baseurl, 'event_saved_search_groups')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_event_saved_search_groups_by_group_id(self, group_id, *, group, fields=None, **kwargs):
        """
        POST /ariel/event_saved_search_groups/{group_id}
        Updates the owner of an event Ariel saved search group.
        """
        function_endpoint = urljoin(self._baseurl, 'event_saved_search_groups/{group_id}'.format(group_id=group_id))
        return self._call('POST', function_endpoint, json=group, **kwargs)

    def delete_event_saved_search_groups_by_group_id(self, group_id, **kwargs):
        """
        DELETE /ariel/event_saved_search_groups/{group_id}
        Deletes an event Ariel saved search group.
        """
        function_endpoint = urljoin(self._baseurl, 'event_saved_search_groups/{group_id}'.format(group_id=group_id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @request_vars('fields')
    def get_event_saved_search_groups_by_group_id(self, group_id, *, fields=None, **kwargs):
        """
        GET /ariel/event_saved_search_groups/{group_id}
        Retrieves an event Ariel saved search group.
        """
        function_endpoint = urljoin(self._baseurl, 'event_saved_search_groups/{group_id}'.format(group_id=group_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_flow_saved_search_groups(self, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /ariel/flow_saved_search_groups
        Retrieves a list of flow Ariel saved search groups.
        """
        function_endpoint = urljoin(self._baseurl, 'flow_saved_search_groups')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_flow_saved_search_groups_by_group_id(self, group_id, *, fields=None, **kwargs):
        """
        GET /ariel/flow_saved_search_groups/{group_id}
        Retrieves a flow Ariel saved search group.
        """
        function_endpoint = urljoin(self._baseurl, 'flow_saved_search_groups/{group_id}'.format(group_id=group_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_flow_saved_search_groups_by_group_id(self, group_id, *, group, fields=None, **kwargs):
        """
        POST /ariel/flow_saved_search_groups/{group_id}
        Updates the owner of a flow Ariel saved search group.
        """
        function_endpoint = urljoin(self._baseurl, 'flow_saved_search_groups/{group_id}'.format(group_id=group_id))
        return self._call('POST', function_endpoint, json=group, **kwargs)

    def delete_flow_saved_search_groups_by_group_id(self, group_id, **kwargs):
        """
        DELETE /ariel/flow_saved_search_groups/{group_id}
        Deletes a flow Ariel saved search group.
        """
        function_endpoint = urljoin(self._baseurl, 'flow_saved_search_groups/{group_id}'.format(group_id=group_id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @header_vars('fields')
    def post_flow_vlans(self, *, body, fields=None, **kwargs):
        """
        POST /ariel/flow_vlans
        Creates a new flow VLAN field as specified by input parameters.
        """
        function_endpoint = urljoin(self._baseurl, 'flow_vlans')
        return self._call('POST', function_endpoint, json=body, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_flow_vlans(self, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /ariel/flow_vlans
        Retrieves a list of available flow VLAN IDs in the Ariel database.
        """
        function_endpoint = urljoin(self._baseurl, 'flow_vlans')
        return self._call('GET', function_endpoint, **kwargs)

    def delete_flow_vlans_by_id(self, id, **kwargs):
        """
        DELETE /ariel/flow_vlans/{id}
        Deletes a flow VLAN ID with specified enterprise and customer VLAN ID's and removes any associated domain mappings.
        """
        function_endpoint = urljoin(self._baseurl, 'flow_vlans/{id}'.format(id=id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @request_vars('fields')
    def get_flow_vlans_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /ariel/flow_vlans/{id}
        Retrieves a flow VLAN ID object by VLAN ID.
        """
        function_endpoint = urljoin(self._baseurl, 'flow_vlans/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_function_by_function_name(self, function_name, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /ariel/function/{function_name}
        Retrieve the columns defined for a specific Ariel function
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'function/{function_name}'.format(function_name=function_name))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('database', 'fields')
    def get_functions(self, *, database, fields=None, **kwargs):
        """
        GET /ariel/functions
        Retrieves AQL Functions for given .
        """
        function_endpoint = urljoin(self._baseurl, 'functions')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('database', 'fields')
    def get_functions_by_function_name(self, function_name, *, database, fields=None, **kwargs):
        """
        GET /ariel/functions/{function_name}
        Retrieves AQL Function with given name for a given database.
        """
        function_endpoint = urljoin(self._baseurl, 'functions/{function_name}'.format(function_name=function_name))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_lookups(self, *, data=None, fields=None, **kwargs):
        """
        POST /ariel/lookups
        Creates a new tagged field lookup.
        """
        function_endpoint = urljoin(self._baseurl, 'lookups')
        return self._call('POST', function_endpoint, json=data, **kwargs)

    @request_vars('fields')
    def get_lookups(self, *, fields=None, **kwargs):
        """
        GET /ariel/lookups
        Retrieves a list of all tagged field lookups.
        """
        function_endpoint = urljoin(self._baseurl, 'lookups')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_lookups_by_name(self, name, *, fields=None, **kwargs):
        """
        GET /ariel/lookups/{name}
        Retrieves a tagged field lookup by name.
        """
        function_endpoint = urljoin(self._baseurl, 'lookups/{name}'.format(name=name))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def delete_lookups_by_name(self, name, *, fields=None, **kwargs):
        """
        DELETE /ariel/lookups/{name}
        Deletes a tagged field lookup with particular name.
        """
        function_endpoint = urljoin(self._baseurl, 'lookups/{name}'.format(name=name))
        return self._call('DELETE', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_lookups_by_name(self, name, *, data=None, fields=None, **kwargs):
        """
        POST /ariel/lookups/{name}
        Updates a tagged field lookup with particular name.
        """
        function_endpoint = urljoin(self._baseurl, 'lookups/{name}'.format(name=name))
        return self._call('POST', function_endpoint, json=data, **kwargs)

    @request_vars('fields')
    def get_parser_keywords(self, *, fields=None, **kwargs):
        """
        GET /ariel/parser_keywords
        Retrieves keywords applicable to AQL Parser.
        """
        function_endpoint = urljoin(self._baseurl, 'parser_keywords')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('query_expression', 'fields')
    def post_processors_aql_metadata(self, *, query_expression, fields=None, **kwargs):
        """
        POST /ariel/processors/aql_metadata
        Parses the AQL query expression and returns metadata for this query
        """
        function_endpoint = urljoin(self._baseurl, 'processors/aql_metadata')
        return self._call('POST', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_saved_search_delete_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):
        """
        GET /ariel/saved_search_delete_tasks/{task_id}
        Retrieves the delete the Ariel saved search task status.
        """
        function_endpoint = urljoin(self._baseurl, 'saved_search_delete_tasks/{task_id}'.format(task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_saved_search_dependent_tasks_by_task_id(self, task_id, *, task, fields=None, **kwargs):
        """
        POST /ariel/saved_search_dependent_tasks/{task_id}
        Cancels the dependent Ariel saved search task.
        """
        function_endpoint = urljoin(self._baseurl, 'saved_search_dependent_tasks/{task_id}'.format(task_id=task_id))
        return self._call('POST', function_endpoint, json=task, **kwargs)

    @request_vars('fields')
    def get_saved_search_dependent_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):
        """
        GET /ariel/saved_search_dependent_tasks/{task_id}
        Retrieves the dependent the Ariel saved search task status.
        """
        function_endpoint = urljoin(self._baseurl, 'saved_search_dependent_tasks/{task_id}'.format(task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_saved_search_dependent_tasks_results_by_task_id(self, task_id, *, fields=None, **kwargs):
        """
        GET /ariel/saved_search_dependent_tasks/{task_id}/results
        Retrieves the Ariel saved search dependent task results.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'saved_search_dependent_tasks/{task_id}/results'.format(task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_saved_searches(self, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /ariel/saved_searches
        Retrieves a list of Ariel saved searches.
        """
        function_endpoint = urljoin(self._baseurl, 'saved_searches')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def delete_saved_searches_by_id(self, id, *, fields=None, **kwargs):
        """
        DELETE /ariel/saved_searches/{id}
        Deletes an Ariel saved search. To ensure safe deletion, a dependency check is carried out. The check might take some time. An asynchronous task is started to do this check.
        """
        function_endpoint = urljoin(self._baseurl, 'saved_searches/{id}'.format(id=id))
        return self._call('DELETE', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_saved_searches_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /ariel/saved_searches/{id}
        Retrieves an Ariel saved search.
        """
        function_endpoint = urljoin(self._baseurl, 'saved_searches/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_saved_searches_by_id(self, id, *, saved_search, fields=None, **kwargs):
        """
        POST /ariel/saved_searches/{id}
        Updates the Ariel saved search.
        """
        function_endpoint = urljoin(self._baseurl, 'saved_searches/{id}'.format(id=id))
        return self._call('POST', function_endpoint, json=saved_search, **kwargs)

    @request_vars('fields')
    def get_saved_searches_dependents_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /ariel/saved_searches/{id}/dependents
        Retrieves the objects that depend on the Ariel saved search.
        """
        function_endpoint = urljoin(self._baseurl, 'saved_searches/{id}/dependents'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('db_name', 'data_lake', 'filter')
    def get_searches(self, *, db_name=None, data_lake=None, Range=None, filter=None, **kwargs):
        """
        GET /ariel/searches
        Retrieves the list of Ariel searches. Search IDs for completed and active searches are returned.
        """
        function_endpoint = urljoin(self._baseurl, 'searches')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('query_expression', 'saved_search_id', 'data_lake')
    def post_searches(self, *, query_expression=None, saved_search_id=None, data_lake=None, **kwargs):
        """
        POST /ariel/searches
        Create a new asynchronous Ariel search.
        """
        function_endpoint = urljoin(self._baseurl, 'searches')
        return self._call('POST', function_endpoint, **kwargs)

    @request_vars('data_lake')
    def delete_searches_by_search_id(self, search_id, *, data_lake=None, **kwargs):
        """
        DELETE /ariel/searches/{search_id}
        Deletes an Ariel search.
        """
        function_endpoint = urljoin(self._baseurl, 'searches/{search_id}'.format(search_id=search_id))
        return self._call('DELETE', function_endpoint, **kwargs)

    @header_vars('Prefer')
    @request_vars('data_lake')
    def get_searches_by_search_id(self, search_id, *, Prefer=None, data_lake=None, **kwargs):
        """
        GET /ariel/searches/{search_id}
        Retrieves information about an Ariel search.
        """
        function_endpoint = urljoin(self._baseurl, 'searches/{search_id}'.format(search_id=search_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('status', 'save_results', 'data_lake')
    def post_searches_by_search_id(self, search_id, *, status=None, save_results=None, data_lake=None, **kwargs):
        """
        POST /ariel/searches/{search_id}
        Updates an Ariel search.
        """
        function_endpoint = urljoin(self._baseurl, 'searches/{search_id}'.format(search_id=search_id))
        return self._call('POST', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_searches_metadata_by_search_id(self, search_id, *, fields=None, Range=None, filter=None, **kwargs):
        """
        GET /ariel/searches/{search_id}/metadata
        Retrieve the columns that are defined for a specific Ariel search id.
        """
        function_endpoint = urljoin(self._baseurl, 'searches/{search_id}/metadata'.format(search_id=search_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('data_lake')
    def get_searches_results_by_search_id(self, search_id, *, data_lake=None, Range=None, **kwargs):
        """
        GET /ariel/searches/{search_id}/results
        Retrieves search results in the requested format.
        """
        function_endpoint = urljoin(self._baseurl, 'searches/{search_id}/results'.format(search_id=search_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('id_type', 'server_types')
    def get_servers(self, *, id_type=None, server_types=None, Range=None, **kwargs):
        """
        GET /ariel/servers
        Get all ariel server ids
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'servers')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('id_type', 'timeout_msec', 'fields')
    def get_servers_by_id(self, id, *, id_type=None, timeout_msec=None, fields=None, **kwargs):
        """
        GET /ariel/servers/{id}
        Get ariel server by id
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'servers/{id}'.format(id=id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('tag', 'name', 'catalog', 'type', 'array', 'format_class_name', 'format_params', 'description',
                  'fields')
    def post_taggedfields(self, *, tag, name, catalog, type, array, format_class_name=None, format_params=None,
                          description=None, fields=None, **kwargs):
        """
        POST /ariel/taggedfields
        Create a new Tagged field.
        """
        function_endpoint = urljoin(self._baseurl, 'taggedfields')
        return self._call('POST', function_endpoint, **kwargs)

    @request_vars('catalog', 'fields')
    def get_taggedfields(self, *, catalog=None, fields=None, **kwargs):
        """
        GET /ariel/taggedfields
        Retrieves a list of available  tagged fields for Ariel catalog.
        """
        function_endpoint = urljoin(self._baseurl, 'taggedfields')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def delete_taggedfields_by_tag(self, tag, *, fields=None, **kwargs):
        """
        DELETE /ariel/taggedfields/{tag}
        Deletes a Tagged field with specified tag.
        """
        function_endpoint = urljoin(self._baseurl, 'taggedfields/{tag}'.format(tag=tag))
        return self._call('DELETE', function_endpoint, **kwargs)

    @request_vars('format_class_name', 'format_params', 'description', 'fields')
    def post_taggedfields_by_tag(self, tag, *, format_class_name=None, format_params=None, description=None,
                                 fields=None, **kwargs):
        """
        POST /ariel/taggedfields/{tag}
        Updates a tagged field with specified tag number.
        """
        function_endpoint = urljoin(self._baseurl, 'taggedfields/{tag}'.format(tag=tag))
        return self._call('POST', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_taggedfields_by_tag(self, tag, *, fields=None, **kwargs):
        """
        GET /ariel/taggedfields/{tag}
        Retrieves a tagged field with specified tag number.
        """
        function_endpoint = urljoin(self._baseurl, 'taggedfields/{tag}'.format(tag=tag))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('query_expression', 'fields')
    def post_validators_aql(self, *, query_expression, fields=None, **kwargs):
        """
        POST /ariel/validators/aql
        Validates the AQL query expression.
        """
        function_endpoint = urljoin(self._baseurl, 'validators/aql')
        return self._call('POST', function_endpoint, **kwargs)
