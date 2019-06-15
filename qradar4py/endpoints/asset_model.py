from urllib.parse import urljoin

from qradar4py.endpoints.api_endpoint import QRadarAPIEndpoint
from qradar4py.endpoints.api_endpoint import request_vars
from qradar4py.endpoints.api_endpoint import header_vars


class AssetModel(QRadarAPIEndpoint):
    """
    The QRadar API endpoint group /asset_model and its endpoints.
    """
    __baseurl = 'asset_model/'

    def __init__(self, url, header, verify):
        super().__init__(urljoin(url, self.__baseurl),
                         header,
                         verify)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_assets(self, *, fields=None, Range=None, filter=None, **kwargs):
        """
        GET /asset_model/assets
        List all assets found in the model.
        """
        function_endpoint = urljoin(self._baseurl, 'assets')
        return self._call('GET', function_endpoint, **kwargs)

    def post_assets_by_asset_id(self, asset_id, *, asset, **kwargs):
        """
        POST /asset_model/assets/{asset_id}
        Update an asset with several pertinent pieces of information.
        """
        function_endpoint = urljoin(self._baseurl, 'assets/{asset_id}'.format(asset_id=asset_id))
        return self._call('POST', function_endpoint, response_type='text/plain', json=asset, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_properties(self, *, fields=None, Range=None, filter=None, **kwargs):
        """
        GET /asset_model/properties
        Get a list of available asset property types that can be used.
        """
        function_endpoint = urljoin(self._baseurl, 'properties')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_saved_search_groups(self, *, fields=None, Range=None, filter=None, **kwargs):
        """
        GET /asset_model/saved_search_groups
        Retrieves a list the asset saved search groups.
        """
        function_endpoint = urljoin(self._baseurl, 'saved_search_groups')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_saved_search_groups_by_group_id(self, group_id, *, group, fields=None, **kwargs):
        """
        POST /asset_model/saved_search_groups/{group_id}
        Updates the owner of an asset saved search group.
        """
        function_endpoint = urljoin(self._baseurl, 'saved_search_groups/{group_id}'.format(group_id=group_id))
        return self._call('POST', function_endpoint, json=group, **kwargs)

    def delete_saved_search_groups_by_group_id(self, group_id, **kwargs):
        """
        DELETE /asset_model/saved_search_groups/{group_id}
        Deletes an asset saved search group.
        """
        function_endpoint = urljoin(self._baseurl, 'saved_search_groups/{group_id}'.format(group_id=group_id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @request_vars('fields')
    def get_saved_search_groups_by_group_id(self, group_id, *, fields=None, **kwargs):
        """
        GET /asset_model/saved_search_groups/{group_id}
        Retrieves an asset saved search group.
        """
        function_endpoint = urljoin(self._baseurl, 'saved_search_groups/{group_id}'.format(group_id=group_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_saved_searches(self, *, fields=None, Range=None, filter=None, **kwargs):
        """
        GET /asset_model/saved_searches
        Retrieves a list of saved searches that can be used or applied against the /asset_model/saved_searches/{saved_search_id}/results query.
        """
        function_endpoint = urljoin(self._baseurl, 'saved_searches')
        return self._call('GET', function_endpoint, **kwargs)

    def delete_saved_searches_by_saved_search_id(self, saved_search_id, **kwargs):
        """
        DELETE /asset_model/saved_searches/{saved_search_id}
        Deletes an asset saved search.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'saved_searches/{saved_search_id}'.format(saved_search_id=saved_search_id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @request_vars('fields')
    def get_saved_searches_by_saved_search_id(self, saved_search_id, *, fields=None, **kwargs):
        """
        GET /asset_model/saved_searches/{saved_search_id}
        Retrieves an asset saved search.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'saved_searches/{saved_search_id}'.format(saved_search_id=saved_search_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_saved_searches_by_saved_search_id(self, saved_search_id, *, saved_search, fields=None, **kwargs):
        """
        POST /asset_model/saved_searches/{saved_search_id}
        Updates the asset saved search owner only.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'saved_searches/{saved_search_id}'.format(saved_search_id=saved_search_id))
        return self._call('POST', function_endpoint, json=saved_search, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_saved_searches_results_by_saved_search_id(self, saved_search_id, *, fields=None, Range=None, filter=None,
                                                      **kwargs):
        """
        GET /asset_model/saved_searches/{saved_search_id}/results
        Retrieves a list of assets based on the results of an asset saved search.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'saved_searches/{saved_search_id}/results'.format(saved_search_id=saved_search_id))
        return self._call('GET', function_endpoint, **kwargs)
