import json

from src.utility import get_json_property


class ScanConfig:
    def __init__(self, json_obj, scan_name):
        custom_obj = get_json_property(json_obj, scan_name)
        self.enabled = get_json_property(custom_obj, "enabled")
        self.custom_payload = get_json_property(custom_obj, "custom_payload")
        self.exception = get_json_property(custom_obj, "exception")


class ConfigPipeline:
    def __init__(self, json_obj):
        repository = json_obj['repository']
        self.org = repository['organization']
        self.name = repository['name']
        self.history = json_obj['history']
        self.config = json_obj['config']

    def get_secure_task(self, task_name):
        if self.config is not None and task_name in self.config:
            return self.config[task_name]
        return None

    @staticmethod
    def get_custom_payload(task):
        if 'custom_payload' in task:
            return task['custom_payload']
        return None


class ConfigPipelineHelper:
    @staticmethod
    def parse_config_pipeline_from_json(json_content) -> ConfigPipeline:
        resultDict = json.loads(json_content)
        obj = ConfigPipeline(resultDict)
        return obj
