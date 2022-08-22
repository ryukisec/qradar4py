from urllib.parse import urljoin

from qradar4py.endpoints.api_endpoint import QRadarAPIEndpoint
from qradar4py.endpoints.api_endpoint import request_vars
from qradar4py.endpoints.api_endpoint import header_vars


class DataClassification(QRadarAPIEndpoint):
    """
    The QRadar API endpoint group /data_classification and its endpoints.
    """
    __baseurl = 'data_classification/'

    def __init__(self, url, header, verify):
        super().__init__(urljoin(url, self.__baseurl),
                         header,
                         verify)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_dsm_event_mappings(self, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /data_classification/dsm_event_mappings
        Retrieve a list of DSM event mappings.
        """
        function_endpoint = urljoin(self._baseurl, 'dsm_event_mappings')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_dsm_event_mappings(self, *, data, fields=None, **kwargs):
        """
        POST /data_classification/dsm_event_mappings
        Creates a new custom DSM event mapping.
        """
        function_endpoint = urljoin(self._baseurl, 'dsm_event_mappings')
        return self._call('POST', function_endpoint, json=data, **kwargs)

    @request_vars('fields')
    def get_dsm_event_mappings_by_dsm_event_mapping_id(self, dsm_event_mapping_id, *, fields=None, **kwargs):
        """
        GET /data_classification/dsm_event_mappings/{dsm_event_mapping_id}
        Retrieves a DSM event mapping based on the supplied DSM event mapping ID.
        """
        function_endpoint = urljoin(self._baseurl, 'dsm_event_mappings/{dsm_event_mapping_id}'.format(
            dsm_event_mapping_id=dsm_event_mapping_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_dsm_event_mappings_by_dsm_event_mapping_id(self, dsm_event_mapping_id, *, data, fields=None, **kwargs):
        """
        POST /data_classification/dsm_event_mappings/{dsm_event_mapping_id}
        Updates an existing custom DSM event mapping.
        """
        function_endpoint = urljoin(self._baseurl, 'dsm_event_mappings/{dsm_event_mapping_id}'.format(
            dsm_event_mapping_id=dsm_event_mapping_id))
        return self._call('POST', function_endpoint, json=data, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'sort', 'fields')
    def get_high_level_categories(self, *, filter=None, sort=None, Range=None, fields=None, **kwargs):
        """
        GET /data_classification/high_level_categories
        Retrieves a list of high level categories.
        """
        function_endpoint = urljoin(self._baseurl, 'high_level_categories')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_high_level_categories_by_high_level_category_id(self, high_level_category_id, *, fields=None, **kwargs):
        """
        GET /data_classification/high_level_categories/{high_level_category_id}
        Retrieves a high level category based on the supplied high level category ID.
        """
        function_endpoint = urljoin(self._baseurl, 'high_level_categories/{high_level_category_id}'.format(
            high_level_category_id=high_level_category_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'sort', 'fields')
    def get_low_level_categories(self, *, filter=None, sort=None, Range=None, fields=None, **kwargs):
        """
        GET /data_classification/low_level_categories
        Retrieves a list of low level categories.
        """
        function_endpoint = urljoin(self._baseurl, 'low_level_categories')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_low_level_categories_by_low_level_category_id(self, low_level_category_id, *, fields=None, **kwargs):
        """
        GET /data_classification/low_level_categories/{low_level_category_id}
        Retrieves a low level category based on the supplied low level category ID.
        """
        function_endpoint = urljoin(self._baseurl, 'low_level_categories/{low_level_category_id}'.format(
            low_level_category_id=low_level_category_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_qid_records(self, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /data_classification/qid_records
        Retrieves a list of QID records.
        """
        function_endpoint = urljoin(self._baseurl, 'qid_records')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_qid_records(self, *, data, fields=None, **kwargs):
        """
        POST /data_classification/qid_records
        Creates a new QID record.
        """
        function_endpoint = urljoin(self._baseurl, 'qid_records')
        return self._call('POST', function_endpoint, json=data, **kwargs)

    @header_vars('fields')
    def post_qid_records_by_qid_record_id(self, qid_record_id, *, qid_record, fields=None, **kwargs):
        """
        POST /data_classification/qid_records/{qid_record_id}
        Updates an existing QID record.
        """
        function_endpoint = urljoin(self._baseurl, 'qid_records/{qid_record_id}'.format(qid_record_id=qid_record_id))
        return self._call('POST', function_endpoint, json=qid_record, **kwargs)

    @request_vars('fields')
    def get_qid_records_by_qid_record_id(self, qid_record_id, *, fields=None, **kwargs):
        """
        GET /data_classification/qid_records/{qid_record_id}
        Retrieves a QID record that is based on the supplied qid_record_id.
        """
        function_endpoint = urljoin(self._baseurl, 'qid_records/{qid_record_id}'.format(qid_record_id=qid_record_id))
        return self._call('GET', function_endpoint, **kwargs)
