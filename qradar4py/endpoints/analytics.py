from urllib.parse import urljoin

from qradar4py.endpoints.api_endpoint import QRadarAPIEndpoint
from qradar4py.endpoints.api_endpoint import request_vars
from qradar4py.endpoints.api_endpoint import header_vars


class Analytics(QRadarAPIEndpoint):
    """
    The QRadar API endpoint group /analytics and its endpoints.
    """
    __baseurl = 'analytics/'

    def __init__(self, url, header, verify):
        super().__init__(urljoin(url, self.__baseurl),
                         header,
                         verify)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_ade_rules(self, *, fields=None, filter=None, Range=None, **kwargs):
        """
        GET /analytics/ade_rules
        Retrieves a list of ADE rules.
        """
        function_endpoint = urljoin(self._baseurl, 'ade_rules')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_ade_rules_ade_rule_delete_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):
        """
        GET /analytics/ade_rules/ade_rule_delete_tasks/{task_id}
        Retrieves the delete the ADE rule task status.
        """
        function_endpoint = urljoin(self._baseurl, 'ade_rules/ade_rule_delete_tasks/{task_id}'.format(task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_ade_rules_ade_rule_dependent_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):
        """
        GET /analytics/ade_rules/ade_rule_dependent_tasks/{task_id}
        Retrieves the dependent the ADE rule task status.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'ade_rules/ade_rule_dependent_tasks/{task_id}'.format(task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_ade_rules_ade_rule_dependent_tasks_by_task_id(self, task_id, *, task, fields=None, **kwargs):
        """
        POST /analytics/ade_rules/ade_rule_dependent_tasks/{task_id}
        Cancels a dependent the ADE rule task.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'ade_rules/ade_rule_dependent_tasks/{task_id}'.format(task_id=task_id))
        return self._call('POST', function_endpoint, json=task, **kwargs)

    @request_vars('fields')
    def get_ade_rules_ade_rule_dependent_tasks_results_by_task_id(self, task_id, *, fields=None, **kwargs):
        """
        GET /analytics/ade_rules/ade_rule_dependent_tasks/{task_id}/results
        Retrieves the ADE rule dependent task results.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'ade_rules/ade_rule_dependent_tasks/{task_id}/results'.format(task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_ade_rules_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /analytics/ade_rules/{id}
        Retrieves an ADE rule.
        """
        function_endpoint = urljoin(self._baseurl, 'ade_rules/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_ade_rules_by_id(self, id, *, ade_rule, fields=None, **kwargs):
        """
        POST /analytics/ade_rules/{id}
        Updates the ADE rule owner or enabled/disabled only.
        """
        function_endpoint = urljoin(self._baseurl, 'ade_rules/{id}'.format(id=id))
        return self._call('POST', function_endpoint, json=ade_rule, **kwargs)

    @request_vars('fields')
    def delete_ade_rules_by_id(self, id, *, fields=None, **kwargs):
        """
        DELETE /analytics/ade_rules/{id}
        Deletes an ADE rule. To ensure safe deletion, a dependency check is carried out. The check might take some time. An asynchronous task is started to do this check.
        """
        function_endpoint = urljoin(self._baseurl, 'ade_rules/{id}'.format(id=id))
        return self._call('DELETE', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_ade_rules_dependents_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /analytics/ade_rules/{id}/dependents
        Retrieves the objects that depend on the ADE rule.
        """
        function_endpoint = urljoin(self._baseurl, 'ade_rules/{id}/dependents'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_building_blocks(self, *, fields=None, filter=None, Range=None, **kwargs):
        """
        GET /analytics/building_blocks
        Retrieves a list of building block rules.
        """
        function_endpoint = urljoin(self._baseurl, 'building_blocks')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_building_blocks_building_block_delete_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):
        """
        GET /analytics/building_blocks/building_block_delete_tasks/{task_id}
        Retrieves the delete the building block rule task status.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'building_blocks/building_block_delete_tasks/{task_id}'.format(task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_building_blocks_building_block_dependent_tasks_by_task_id(self, task_id, *, task, fields=None, **kwargs):
        """
        POST /analytics/building_blocks/building_block_dependent_tasks/{task_id}
        Cancels the dependent the building block rule task.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'building_blocks/building_block_dependent_tasks/{task_id}'.format(task_id=task_id))
        return self._call('POST', function_endpoint, json=task, **kwargs)

    @request_vars('fields')
    def get_building_blocks_building_block_dependent_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):
        """
        GET /analytics/building_blocks/building_block_dependent_tasks/{task_id}
        Retrieves the dependent the building block rule task status.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'building_blocks/building_block_dependent_tasks/{task_id}'.format(task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_building_blocks_building_block_dependent_tasks_results_by_task_id(self, task_id, *, fields=None, **kwargs):
        """
        GET /analytics/building_blocks/building_block_dependent_tasks/{task_id}/results
        Retrieves the building block rule dependent task results.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'building_blocks/building_block_dependent_tasks/{task_id}/results'.format(
                                        task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_building_blocks_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /analytics/building_blocks/{id}
        Retrieves a building block rule.
        """
        function_endpoint = urljoin(self._baseurl, 'building_blocks/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_building_blocks_by_id(self, id, *, building_block, fields=None, **kwargs):
        """
        POST /analytics/building_blocks/{id}
        Updates the building block rule owner or enabled/disabled only.
        """
        function_endpoint = urljoin(self._baseurl, 'building_blocks/{id}'.format(id=id))
        return self._call('POST', function_endpoint, json=building_block, **kwargs)

    @request_vars('fields')
    def delete_building_blocks_by_id(self, id, *, fields=None, **kwargs):
        """
        DELETE /analytics/building_blocks/{id}
        Deletes the building block rule. To ensure safe deletion, a dependency check is carried out. This check might take some time. An asynchronous task to do is started for this check.
        """
        function_endpoint = urljoin(self._baseurl, 'building_blocks/{id}'.format(id=id))
        return self._call('DELETE', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_building_blocks_dependents_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /analytics/building_blocks/{id}/dependents
        Retrieves the objects that depend on the building block rule.
        """
        function_endpoint = urljoin(self._baseurl, 'building_blocks/{id}/dependents'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_building_blocks_with_data(self, *, building_block, fields=None, **kwargs):
        """
        POST /analytics/building_blocks_with_data
        Creates a building block with supplied rule_data xml
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'building_blocks_with_data')
        return self._call('POST', function_endpoint, json=building_block, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_building_blocks_with_data(self, *, fields=None, filter=None, Range=None, **kwargs):
        """
        GET /analytics/building_blocks_with_data
        Retrieves a list of building block rules.
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'building_blocks_with_data')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('fields')
    def post_building_blocks_with_data_by_id(self, id, *, building_block, fields=None, **kwargs):
        """
        POST /analytics/building_blocks_with_data/{id}
        Same as com.q1labs.core.api.R1_2017.customrule.BuildingBlockAPI.updateBuildingBlock(IFrameworkServices, ISessionContext, ILogger, Long, BuildingBlockDTO) but updates rule_data xml as well
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'building_blocks_with_data/{id}'.format(id=id))
        return self._call('POST', function_endpoint, json=building_block, headers=headers, **kwargs)

    @request_vars('fields')
    def get_building_blocks_with_data_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /analytics/building_blocks_with_data/{id}
        Retrieves a building block rule.
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'building_blocks_with_data/{id}'.format(id=id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('fields')
    def post_custom_actions_actions(self, *, custom_action, fields=None, **kwargs):
        """
        POST /analytics/custom_actions/actions
        Creates a new custom action with the supplied fields.
        """
        function_endpoint = urljoin(self._baseurl, 'custom_actions/actions')
        return self._call('POST', function_endpoint, json=custom_action, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_custom_actions_actions(self, *, fields=None, filter=None, Range=None, **kwargs):
        """
        GET /analytics/custom_actions/actions
        Retrieves a list of available custom actions.
        """
        function_endpoint = urljoin(self._baseurl, 'custom_actions/actions')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_custom_actions_actions_by_action_id(self, action_id, *, custom_action, fields=None, **kwargs):
        """
        POST /analytics/custom_actions/actions/{action_id}
        Updates an existing custom action.
        """
        function_endpoint = urljoin(self._baseurl, 'custom_actions/actions/{action_id}'.format(action_id=action_id))
        return self._call('POST', function_endpoint, json=custom_action, **kwargs)

    def delete_custom_actions_actions_by_action_id(self, action_id, **kwargs):
        """
        DELETE /analytics/custom_actions/actions/{action_id}
        Deletes an existing custom action.
        """
        function_endpoint = urljoin(self._baseurl, 'custom_actions/actions/{action_id}'.format(action_id=action_id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @request_vars('fields')
    def get_custom_actions_actions_by_action_id(self, action_id, *, fields=None, **kwargs):
        """
        GET /analytics/custom_actions/actions/{action_id}
        Retrieves a custom action based on the supplied action_id.
        """
        function_endpoint = urljoin(self._baseurl, 'custom_actions/actions/{action_id}'.format(action_id=action_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_custom_actions_interpreters(self, *, fields=None, filter=None, Range=None, **kwargs):
        """
        GET /analytics/custom_actions/interpreters
        Retrieves a list of available custom action interpreters.
        """
        function_endpoint = urljoin(self._baseurl, 'custom_actions/interpreters')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_custom_actions_interpreters_by_interpreter_id(self, interpreter_id, *, fields=None, **kwargs):
        """
        GET /analytics/custom_actions/interpreters/{interpreter_id}
        Retrieves a custom action interpreter based on supplied interpreter_id.
        """
        function_endpoint = urljoin(self._baseurl, 'custom_actions/interpreters/{interpreter_id}'.format(
            interpreter_id=interpreter_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_custom_actions_scripts(self, *, file, fields=None, **kwargs):
        """
        POST /analytics/custom_actions/scripts
        Creates a new custom action script file. Newly created custom action script files require a deployment before using.
        """
        function_endpoint = urljoin(self._baseurl, 'custom_actions/scripts')
        return self._call('POST', function_endpoint, mime_type={'Content-Type': 'application/octet-stream'}, data=file,
                          **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_custom_actions_scripts(self, *, fields=None, filter=None, Range=None, **kwargs):
        """
        GET /analytics/custom_actions/scripts
        Retrieves a list of meta-data for available custom action script files.
        """
        function_endpoint = urljoin(self._baseurl, 'custom_actions/scripts')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_custom_actions_scripts_by_script_id(self, script_id, *, fields=None, **kwargs):
        """
        GET /analytics/custom_actions/scripts/{script_id}
        Retrieves meta-data of a custom action script file based on supplied script_id.
        """
        function_endpoint = urljoin(self._baseurl, 'custom_actions/scripts/{script_id}'.format(script_id=script_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_custom_actions_scripts_by_script_id(self, script_id, *, file, fields=None, **kwargs):
        """
        POST /analytics/custom_actions/scripts/{script_id}
        Updates an existing custom action script file. Updated custom action script files require a deployment before using.
        """
        function_endpoint = urljoin(self._baseurl, 'custom_actions/scripts/{script_id}'.format(script_id=script_id))
        return self._call('POST', function_endpoint, mime_type={'Content-Type': 'application/octet-stream'}, data=file,
                          **kwargs)

    def delete_custom_actions_scripts_by_script_id(self, script_id, **kwargs):
        """
        DELETE /analytics/custom_actions/scripts/{script_id}
        Deletes an existing custom action script file.
        """
        function_endpoint = urljoin(self._baseurl, 'custom_actions/scripts/{script_id}'.format(script_id=script_id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @header_vars('fields')
    def post_custom_actions_test(self, *, custom_action_test_request, fields=None, **kwargs):
        """
        POST /analytics/custom_actions/test
        Hidden end-point to perform a test execution of a custom action
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'custom_actions/test')
        return self._call('POST', function_endpoint, json=custom_action_test_request, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_rule_groups(self, *, fields=None, filter=None, Range=None, **kwargs):
        """
        GET /analytics/rule_groups
        Retrieves a list of the rule groups.
        """
        function_endpoint = urljoin(self._baseurl, 'rule_groups')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_rule_groups_by_group_id(self, group_id, *, fields=None, **kwargs):
        """
        GET /analytics/rule_groups/{group_id}
        Retrieves a rule group.
        """
        function_endpoint = urljoin(self._baseurl, 'rule_groups/{group_id}'.format(group_id=group_id))
        return self._call('GET', function_endpoint, **kwargs)

    def delete_rule_groups_by_group_id(self, group_id, **kwargs):
        """
        DELETE /analytics/rule_groups/{group_id}
        Deletes a rule. To ensure safe deletion, a dependency check is carried out. This check might take some time. An asynchronous task to do is started for this check.
        """
        function_endpoint = urljoin(self._baseurl, 'rule_groups/{group_id}'.format(group_id=group_id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @header_vars('fields')
    def post_rule_groups_by_group_id(self, group_id, *, group, fields=None, **kwargs):
        """
        POST /analytics/rule_groups/{group_id}
        Updates the owner of a rule group.
        """
        function_endpoint = urljoin(self._baseurl, 'rule_groups/{group_id}'.format(group_id=group_id))
        return self._call('POST', function_endpoint, json=group, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_rules(self, *, fields=None, filter=None, Range=None, **kwargs):
        """
        GET /analytics/rules
        Retrieves a list of rules.
        """
        function_endpoint = urljoin(self._baseurl, 'rules')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_rules_rule_delete_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):
        """
        GET /analytics/rules/rule_delete_tasks/{task_id}
        Retrieves the delete the rule task status.
        """
        function_endpoint = urljoin(self._baseurl, 'rules/rule_delete_tasks/{task_id}'.format(task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_rules_rule_dependent_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):
        """
        GET /analytics/rules/rule_dependent_tasks/{task_id}
        Retrieves the dependent rule task status.
        """
        function_endpoint = urljoin(self._baseurl, 'rules/rule_dependent_tasks/{task_id}'.format(task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_rules_rule_dependent_tasks_by_task_id(self, task_id, *, task, fields=None, **kwargs):
        """
        POST /analytics/rules/rule_dependent_tasks/{task_id}
        Cancels the dependent the rule task.
        """
        function_endpoint = urljoin(self._baseurl, 'rules/rule_dependent_tasks/{task_id}'.format(task_id=task_id))
        return self._call('POST', function_endpoint, json=task, **kwargs)

    @request_vars('fields')
    def get_rules_rule_dependent_tasks_results_by_task_id(self, task_id, *, fields=None, **kwargs):
        """
        GET /analytics/rules/rule_dependent_tasks/{task_id}/results
        Retrieves the rule dependent task results.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'rules/rule_dependent_tasks/{task_id}/results'.format(task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_rules_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /analytics/rules/{id}
        Retrieves a rule.
        """
        function_endpoint = urljoin(self._baseurl, 'rules/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_rules_by_id(self, id, *, rule, fields=None, **kwargs):
        """
        POST /analytics/rules/{id}
        Updates the rule owner or enabled/disabled only.
        """
        function_endpoint = urljoin(self._baseurl, 'rules/{id}'.format(id=id))
        return self._call('POST', function_endpoint, json=rule, **kwargs)

    @request_vars('fields')
    def delete_rules_by_id(self, id, *, fields=None, **kwargs):
        """
        DELETE /analytics/rules/{id}
        Delete the rule. To ensure safe deletion, a dependency check is carried out. This check might take some time. An asynchronous task to do is started for this check.
        """
        function_endpoint = urljoin(self._baseurl, 'rules/{id}'.format(id=id))
        return self._call('DELETE', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_rules_dependents_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /analytics/rules/{id}/dependents
        Retrieves the objects that depend on the rule.
        """
        function_endpoint = urljoin(self._baseurl, 'rules/{id}/dependents'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter', 'sort')
    def get_rules_offense_contributions(self, *, fields=None, filter=None, sort=None, Range=None, **kwargs):
        """
        GET /analytics/rules_offense_contributions
        Retrieves Rule Offense contributions

        Retieves Rule and Offense references in the system.
        """
        function_endpoint = urljoin(self._baseurl, 'rules_offense_contributions')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_rules_with_data(self, *, rule, fields=None, **kwargs):
        """
        POST /analytics/rules_with_data
        Creates a CRE rule with supplied rule_data xml
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'rules_with_data')
        return self._call('POST', function_endpoint, json=rule, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter', 'sort')
    def get_rules_with_data(self, *, fields=None, filter=None, sort=None, Range=None, **kwargs):
        """
        GET /analytics/rules_with_data
        Retrieves a list of rules.
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'rules_with_data')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('fields')
    def post_rules_with_data_by_id(self, id, *, rule, fields=None, **kwargs):
        """
        POST /analytics/rules_with_data/{id}
        Updates a CRE rule with supplied rule_data xml
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'rules_with_data/{id}'.format(id=id))
        return self._call('POST', function_endpoint, json=rule, headers=headers, **kwargs)

    @request_vars('fields')
    def get_rules_with_data_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /analytics/rules_with_data/{id}
        Retrieves a rule.
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'rules_with_data/{id}'.format(id=id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)
