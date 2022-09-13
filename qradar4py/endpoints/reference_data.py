from urllib.parse import urljoin

from qradar4py.endpoints.api_endpoint import QRadarAPIEndpoint
from qradar4py.endpoints.api_endpoint import request_vars
from qradar4py.endpoints.api_endpoint import header_vars


class ReferenceData(QRadarAPIEndpoint):
    """
    The QRadar API endpoint group /reference_data and its endpoints.
    """
    __baseurl = 'reference_data/'

    def __init__(self, url, header, verify):
        super().__init__(urljoin(url, self.__baseurl),
                         header,
                         verify)

    @request_vars('fields')
    def get_map_delete_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):
        """
        GET /reference_data/map_delete_tasks/{task_id}
        Retrieves the delete reference data map task status.
        """
        function_endpoint = urljoin(self._baseurl, 'map_delete_tasks/{task_id}'.format(task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_map_dependent_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):
        """
        GET /reference_data/map_dependent_tasks/{task_id}
        Retrieves the dependent reference data map task status.
        """
        function_endpoint = urljoin(self._baseurl, 'map_dependent_tasks/{task_id}'.format(task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_map_dependent_tasks_by_task_id(self, task_id, *, task, fields=None, **kwargs):
        """
        POST /reference_data/map_dependent_tasks/{task_id}
        Cancels the dependent reference data map task.
        """
        function_endpoint = urljoin(self._baseurl, 'map_dependent_tasks/{task_id}'.format(task_id=task_id))
        return self._call('POST', function_endpoint, json=task, **kwargs)

    @request_vars('fields')
    def get_map_dependent_tasks_results_by_task_id(self, task_id, *, fields=None, **kwargs):
        """
        GET /reference_data/map_dependent_tasks/{task_id}/results
        Retrieves the reference data map dependent task results.
        """
        function_endpoint = urljoin(self._baseurl, 'map_dependent_tasks/{task_id}/results'.format(task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('name', 'element_type', 'key_label', 'value_label', 'timeout_type', 'time_to_live', 'fields')
    def post_map_of_sets(self, *, name, element_type, key_label=None, value_label=None, timeout_type=None,
                         time_to_live=None, fields=None, **kwargs):
        """
        POST /reference_data/map_of_sets
        Create a new reference map of sets.
        """
        function_endpoint = urljoin(self._baseurl, 'map_of_sets')
        return self._call('POST', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_map_of_sets(self, *, fields=None, filter=None, Range=None, **kwargs):
        """
        GET /reference_data/map_of_sets
        Retrieve a list of all reference map of sets.
        """
        function_endpoint = urljoin(self._baseurl, 'map_of_sets')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_map_of_sets_bulk_load_namespace_name_by_domain_id(self, namespace, name, domain_id, *, data, fields=None,
                                                               **kwargs):
        """
        POST /reference_data/map_of_sets/bulk_load/{namespace}/{name}/{domain_id}
        Adds or updates data in a reference map of sets.
        """
        if not isinstance(data, list):
            data = [data]
        function_endpoint = urljoin(self._baseurl,
                                    'map_of_sets/bulk_load/{namespace}/{name}/{domain_id}'.format(namespace=namespace,
                                                                                                  name=name,
                                                                                                  domain_id=domain_id))
        return self._call('POST', function_endpoint, json=data, **kwargs)

    @header_vars('fields')
    def post_map_of_sets_bulk_load_by_name(self, name, *, data, fields=None, **kwargs):
        """
        POST /reference_data/map_of_sets/bulk_load/{name}
        Adds or updates data in a reference map of sets.
        """
        if not isinstance(data, list):
            data = [data]
        function_endpoint = urljoin(self._baseurl, 'map_of_sets/bulk_load/{name}'.format(name=name))
        return self._call('POST', function_endpoint, json=data, **kwargs)

    @request_vars('namespace', 'purge_only', 'fields')
    def delete_map_of_sets_by_name(self, name, *, namespace=None, purge_only=None, fields=None, **kwargs):
        """
        DELETE /reference_data/map_of_sets/{name}
        Removes a map of sets or purges its contents.
        """
        function_endpoint = urljoin(self._baseurl, 'map_of_sets/{name}'.format(name=name))
        return self._call('DELETE', function_endpoint, **kwargs)

    @request_vars('namespace', 'key', 'value', 'source', 'domain_id', 'fields')
    def post_map_of_sets_by_name(self, name, *, key, value, namespace=None, source=None, domain_id=None, fields=None,
                                 **kwargs):
        """
        POST /reference_data/map_of_sets/{name}
        Add or update an element in a reference map of sets.
        """
        function_endpoint = urljoin(self._baseurl, 'map_of_sets/{name}'.format(name=name))
        return self._call('POST', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('namespace', 'fields')
    def get_map_of_sets_by_name(self, name, *, namespace=None, fields=None, Range=None, **kwargs):
        """
        GET /reference_data/map_of_sets/{name}
        Return the reference map of sets identified by name.
        """
        function_endpoint = urljoin(self._baseurl, 'map_of_sets/{name}'.format(name=name))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_map_of_sets_dependents_by_name(self, name, *, fields=None, **kwargs):
        """
        GET /reference_data/map_of_sets/{name}/dependents
        Retrieves the objects that depend on the reference data map of sets.
        """
        function_endpoint = urljoin(self._baseurl, 'map_of_sets/{name}/dependents'.format(name=name))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('value', 'fields')
    def delete_map_of_sets_name_values_by_key(self, name, key, *, value, fields=None, **kwargs):
        """
        DELETE /reference_data/map_of_sets/{name}/values/{key}
        Remove a value from a reference map of sets.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'map_of_sets/{name}/values/{key}'.format(name=name, key=key))
        return self._call('DELETE', function_endpoint, headers=headers, **kwargs)

    @request_vars('namespace', 'value', 'domain_id', 'fields')
    def delete_map_of_sets_name_by_key(self, name, key, *, value, namespace=None, domain_id=None, fields=None,
                                       **kwargs):
        """
        DELETE /reference_data/map_of_sets/{name}/{key}
        Remove a value from a reference map of sets.
        """
        function_endpoint = urljoin(self._baseurl, 'map_of_sets/{name}/{key}'.format(name=name, key=key))
        return self._call('DELETE', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_map_of_sets_delete_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):
        """
        GET /reference_data/map_of_sets_delete_tasks/{task_id}
        Retrieves the delete reference data map of sets task status.
        """
        function_endpoint = urljoin(self._baseurl, 'map_of_sets_delete_tasks/{task_id}'.format(task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_map_of_sets_dependent_tasks_by_task_id(self, task_id, *, task, fields=None, **kwargs):
        """
        POST /reference_data/map_of_sets_dependent_tasks/{task_id}
        Cancels the dependent reference data map of sets task.
        """
        function_endpoint = urljoin(self._baseurl, 'map_of_sets_dependent_tasks/{task_id}'.format(task_id=task_id))
        return self._call('POST', function_endpoint, json=task, **kwargs)

    @request_vars('fields')
    def get_map_of_sets_dependent_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):
        """
        GET /reference_data/map_of_sets_dependent_tasks/{task_id}
        Retrieves the dependent reference data map of sets task status.
        """
        function_endpoint = urljoin(self._baseurl, 'map_of_sets_dependent_tasks/{task_id}'.format(task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_map_of_sets_dependent_tasks_results_by_task_id(self, task_id, *, fields=None, **kwargs):
        """
        GET /reference_data/map_of_sets_dependent_tasks/{task_id}/results
        Retrieves the reference data map of sets dependent task results.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'map_of_sets_dependent_tasks/{task_id}/results'.format(task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('name', 'key_label', 'value_label', 'element_type', 'timeout_type', 'time_to_live', 'fields')
    def post_maps(self, *, name, element_type, key_label=None, value_label=None, timeout_type=None, time_to_live=None,
                  fields=None, **kwargs):
        """
        POST /reference_data/maps
        Create a new reference map.
        """
        function_endpoint = urljoin(self._baseurl, 'maps')
        return self._call('POST', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_maps(self, *, fields=None, filter=None, Range=None, **kwargs):
        """
        GET /reference_data/maps
        Retrieve a list of all reference maps.
        """
        function_endpoint = urljoin(self._baseurl, 'maps')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_maps_bulk_load_namespace_name_by_domain_id(self, namespace, name, domain_id, *, data, fields=None,
                                                        **kwargs):
        """
        POST /reference_data/maps/bulk_load/{namespace}/{name}/{domain_id}
        Adds or updates data in a reference map.
        """
        if not isinstance(data, list):
            data = [data]
        function_endpoint = urljoin(self._baseurl,
                                    'maps/bulk_load/{namespace}/{name}/{domain_id}'.format(namespace=namespace,
                                                                                           name=name,
                                                                                           domain_id=domain_id))
        return self._call('POST', function_endpoint, json=data, **kwargs)

    @header_vars('fields')
    def post_maps_bulk_load_by_name(self, name, *, data, fields=None, **kwargs):
        """
        POST /reference_data/maps/bulk_load/{name}
        Adds or updates data in a reference map.
        """
        if not isinstance(data, list):
            data = [data]
        function_endpoint = urljoin(self._baseurl, 'maps/bulk_load/{name}'.format(name=name))
        return self._call('POST', function_endpoint, json=data, **kwargs)

    @request_vars('namespace', 'purge_only', 'fields')
    def delete_maps_by_name(self, name, *, namespace=None, purge_only=None, fields=None, **kwargs):
        """
        DELETE /reference_data/maps/{name}
        Removes a reference map or purges its contents.
        """
        function_endpoint = urljoin(self._baseurl, 'maps/{name}'.format(name=name))
        return self._call('DELETE', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('namespace', 'fields', 'filter')
    def get_maps_by_name(self, name, *, namespace=None, fields=None, filter=None, Range=None, **kwargs):
        """
        GET /reference_data/maps/{name}
        Retrieve the reference map identified by name.
        """
        function_endpoint = urljoin(self._baseurl, 'maps/{name}'.format(name=name))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('namespace', 'key', 'value', 'source', 'domain_id', 'fields')
    def post_maps_by_name(self, name, *, key, value, namespace=None, source=None, domain_id=None, fields=None,
                          **kwargs):
        """
        POST /reference_data/maps/{name}
        Add or update an element in a reference map.
        """
        function_endpoint = urljoin(self._baseurl, 'maps/{name}'.format(name=name))
        return self._call('POST', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_maps_dependents_by_name(self, name, *, fields=None, **kwargs):
        """
        GET /reference_data/maps/{name}/dependents
        Retrieves the objects that depend on the reference data map.
        """
        function_endpoint = urljoin(self._baseurl, 'maps/{name}/dependents'.format(name=name))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('value', 'fields')
    def delete_maps_name_values_by_key(self, name, key, *, value, fields=None, **kwargs):
        """
        DELETE /reference_data/maps/{name}/values/{key}
        Remove a value from a reference map.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'maps/{name}/values/{key}'.format(name=name, key=key))
        return self._call('DELETE', function_endpoint, headers=headers, **kwargs)

    @request_vars('namespace', 'value', 'domain_id', 'fields')
    def delete_maps_name_by_key(self, name, key, *, value, namespace=None, domain_id=None, fields=None, **kwargs):
        """
        DELETE /reference_data/maps/{name}/{key}
        Remove a value from a reference map.
        """
        function_endpoint = urljoin(self._baseurl, 'maps/{name}/{key}'.format(name=name, key=key))
        return self._call('DELETE', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_set_delete_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):
        """
        GET /reference_data/set_delete_tasks/{task_id}
        Retrieves the delete reference data set task status.
        """
        function_endpoint = urljoin(self._baseurl, 'set_delete_tasks/{task_id}'.format(task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_set_dependent_tasks_by_task_id(self, task_id, *, task, fields=None, **kwargs):
        """
        POST /reference_data/set_dependent_tasks/{task_id}
        Cancels the dependent reference data set task.
        """
        function_endpoint = urljoin(self._baseurl, 'set_dependent_tasks/{task_id}'.format(task_id=task_id))
        return self._call('POST', function_endpoint, json=task, **kwargs)

    @request_vars('fields')
    def get_set_dependent_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):
        """
        GET /reference_data/set_dependent_tasks/{task_id}
        Retrieves the dependent reference data set task status.
        """
        function_endpoint = urljoin(self._baseurl, 'set_dependent_tasks/{task_id}'.format(task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_set_dependent_tasks_results_by_task_id(self, task_id, *, fields=None, **kwargs):
        """
        GET /reference_data/set_dependent_tasks/{task_id}/results
        Retrieves the reference data set dependent task results.
        """
        function_endpoint = urljoin(self._baseurl, 'set_dependent_tasks/{task_id}/results'.format(task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_sets(self, *, fields=None, filter=None, Range=None, **kwargs):
        """
        GET /reference_data/sets
        Retrieve a list of all reference sets.
        """
        function_endpoint = urljoin(self._baseurl, 'sets')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('name', 'element_type', 'timeout_type', 'time_to_live', 'fields')
    def post_sets(self, *, name, element_type, timeout_type=None, time_to_live=None, fields=None, **kwargs):
        """
        POST /reference_data/sets
        Create a new reference set.
        """
        function_endpoint = urljoin(self._baseurl, 'sets')
        return self._call('POST', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_sets_bulk_load_namespace_name_by_domain_id(self, namespace, name, domain_id, *, data, fields=None,
                                                        **kwargs):
        """
        POST /reference_data/sets/bulk_load/{namespace}/{name}/{domain_id}
        Add or update data in a reference set.
        """
        if not isinstance(data, list):
            data = [data]
        function_endpoint = urljoin(self._baseurl,
                                    'sets/bulk_load/{namespace}/{name}/{domain_id}'.format(namespace=namespace,
                                                                                           name=name,
                                                                                           domain_id=domain_id))
        return self._call('POST', function_endpoint, json=data, **kwargs)

    @header_vars('fields')
    def post_sets_bulk_load_by_name(self, name, *, data, fields=None, **kwargs):
        """
        POST /reference_data/sets/bulk_load/{name}
        Add or update data in a reference set.
        """
        if not isinstance(data, list):
            data = [data]
        function_endpoint = urljoin(self._baseurl, 'sets/bulk_load/{name}'.format(name=name))
        return self._call('POST', function_endpoint, json=data, **kwargs)

    @header_vars('Range')
    @request_vars('value', 'fields', 'filter')
    def get_sets_search(self, *, value, fields=None, filter=None, Range=None, **kwargs):
        """
        GET /reference_data/sets/search
        Search a value in reference sets.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'sets/search')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('namespace', 'fields', 'filter')
    def get_sets_by_name(self, name, *, namespace=None, fields=None, filter=None, Range=None, **kwargs):
        """
        GET /reference_data/sets/{name}
        Retrieve the reference set identified by name.
        """
        function_endpoint = urljoin(self._baseurl, 'sets/{name}'.format(name=name))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('namespace', 'value', 'source', 'domain_id', 'fields')
    def post_sets_by_name(self, name, *, value, namespace=None, source=None, domain_id=None, fields=None, **kwargs):
        """
        POST /reference_data/sets/{name}
        Add or update an element in a reference set.
        """
        function_endpoint = urljoin(self._baseurl, 'sets/{name}'.format(name=name))
        return self._call('POST', function_endpoint, **kwargs)

    @request_vars('namespace', 'purge_only', 'fields')
    def delete_sets_by_name(self, name, *, namespace=None, purge_only=None, fields=None, **kwargs):
        """
        DELETE /reference_data/sets/{name}
        Removes a reference set or purges its contents.
        """
        function_endpoint = urljoin(self._baseurl, 'sets/{name}'.format(name=name))
        return self._call('DELETE', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_sets_dependents_by_name(self, name, *, fields=None, **kwargs):
        """
        GET /reference_data/sets/{name}/dependents
        Retrieves the objects that depend on the reference data set.
        """
        function_endpoint = urljoin(self._baseurl, 'sets/{name}/dependents'.format(name=name))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def delete_sets_name_values_by_value(self, name, value, *, fields=None, **kwargs):
        """
        DELETE /reference_data/sets/{name}/values/{value}
        Remove a value from a reference set.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'sets/{name}/values/{value}'.format(name=name, value=value))
        return self._call('DELETE', function_endpoint, headers=headers, **kwargs)

    @request_vars('namespace', 'domain_id', 'fields')
    def delete_sets_name_by_value(self, name, value, *, namespace=None, domain_id=None, fields=None, **kwargs):
        """
        DELETE /reference_data/sets/{name}/{value}
        Remove a value from a reference set.
        """
        function_endpoint = urljoin(self._baseurl, 'sets/{name}/{value}'.format(name=name, value=value))
        return self._call('DELETE', function_endpoint, **kwargs)

    @request_vars('name', 'element_type', 'outer_key_label', 'timeout_type', 'time_to_live', 'key_name_types', 'fields')
    def post_tables(self, *, name, element_type, outer_key_label=None, timeout_type=None, time_to_live=None,
                    key_name_types=None, fields=None, **kwargs):
        """
        POST /reference_data/tables
        Create a new reference table.
        """
        function_endpoint = urljoin(self._baseurl, 'tables')
        return self._call('POST', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_tables(self, *, fields=None, filter=None, Range=None, **kwargs):
        """
        GET /reference_data/tables
        Retrieve a list of all reference tables.
        """
        function_endpoint = urljoin(self._baseurl, 'tables')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_tables_bulk_load_namespace_name_by_domain_id(self, namespace, name, domain_id, *, data, fields=None,
                                                          **kwargs):
        """
        POST /reference_data/tables/bulk_load/{namespace}/{name}/{domain_id}
        Adds or updates data in a reference table.
        """
        if not isinstance(data, list):
            data = [data]
        function_endpoint = urljoin(self._baseurl,
                                    'tables/bulk_load/{namespace}/{name}/{domain_id}'.format(namespace=namespace,
                                                                                             name=name,
                                                                                             domain_id=domain_id))
        return self._call('POST', function_endpoint, json=data, **kwargs)

    @header_vars('fields')
    def post_tables_bulk_load_by_name(self, name, *, data, fields=None, **kwargs):
        """
        POST /reference_data/tables/bulk_load/{name}
        Adds or updates data in a reference table.
        """
        if not isinstance(data, list):
            data = [data]
        function_endpoint = urljoin(self._baseurl, 'tables/bulk_load/{name}'.format(name=name))
        return self._call('POST', function_endpoint, json=data, **kwargs)

    @request_vars('namespace', 'outer_key', 'inner_key', 'value', 'source', 'domain_id', 'fields')
    def post_tables_by_name(self, name, *, outer_key, inner_key, value, namespace=None, source=None, domain_id=None,
                            fields=None, **kwargs):
        """
        POST /reference_data/tables/{name}
        Add or update an element in a reference table.
        """
        function_endpoint = urljoin(self._baseurl, 'tables/{name}'.format(name=name))
        return self._call('POST', function_endpoint, **kwargs)

    @request_vars('namespace', 'purge_only', 'fields')
    def delete_tables_by_name(self, name, *, namespace=None, purge_only=None, fields=None, **kwargs):
        """
        DELETE /reference_data/tables/{name}
        Remove a reference table or purge its contents.
        """
        function_endpoint = urljoin(self._baseurl, 'tables/{name}'.format(name=name))
        return self._call('DELETE', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('namespace', 'fields')
    def get_tables_by_name(self, name, *, namespace=None, fields=None, Range=None, **kwargs):
        """
        GET /reference_data/tables/{name}
        Return the reference table identified by name.
        """
        function_endpoint = urljoin(self._baseurl, 'tables/{name}'.format(name=name))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_tables_dependents_by_name(self, name, *, fields=None, **kwargs):
        """
        GET /reference_data/tables/{name}/dependents
        Find the objects that depend on the Reference Data Tables
        """
        function_endpoint = urljoin(self._baseurl, 'tables/{name}/dependents'.format(name=name))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('value', 'fields')
    def delete_tables_name_values_outer_key_by_inner_key(self, name, outer_key, inner_key, *, value, fields=None,
                                                         **kwargs):
        """
        DELETE /reference_data/tables/{name}/values/{outer_key}/{inner_key}
        Remove a value from a reference table.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'tables/{name}/values/{outer_key}/{inner_key}'.format(name=name,
                                                                                                         outer_key=outer_key,
                                                                                                         inner_key=inner_key))
        return self._call('DELETE', function_endpoint, headers=headers, **kwargs)

    @request_vars('namespace', 'value', 'domain_id', 'fields')
    def delete_tables_name_outer_key_by_inner_key(self, name, outer_key, inner_key, *, value, namespace=None,
                                                  domain_id=None, fields=None, **kwargs):
        """
        DELETE /reference_data/tables/{name}/{outer_key}/{inner_key}
        Remove a value from a reference table.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'tables/{name}/{outer_key}/{inner_key}'.format(name=name, outer_key=outer_key,
                                                                                   inner_key=inner_key))
        return self._call('DELETE', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_tables_delete_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):
        """
        GET /reference_data/tables_delete_tasks/{task_id}
        Retrieve the delete the Reference Data Tables task status.
        """
        function_endpoint = urljoin(self._baseurl, 'tables_delete_tasks/{task_id}'.format(task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_tables_dependent_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):
        """
        GET /reference_data/tables_dependent_tasks/{task_id}
        Retrieve the dependent the Reference Data Tables task status.
        """
        function_endpoint = urljoin(self._baseurl, 'tables_dependent_tasks/{task_id}'.format(task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_tables_dependent_tasks_by_task_id(self, task_id, *, task, fields=None, **kwargs):
        """
        POST /reference_data/tables_dependent_tasks/{task_id}
        Cancel the dependent the Reference Data Tables task.
        """
        function_endpoint = urljoin(self._baseurl, 'tables_dependent_tasks/{task_id}'.format(task_id=task_id))
        return self._call('POST', function_endpoint, json=task, **kwargs)

    @request_vars('fields')
    def get_tables_dependent_tasks_results_by_task_id(self, task_id, *, fields=None, **kwargs):
        """
        GET /reference_data/tables_dependent_tasks/{task_id}/results
        Retrieve the Reference Data Tables Dependent Task Results
        """
        function_endpoint = urljoin(self._baseurl, 'tables_dependent_tasks/{task_id}/results'.format(task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)
