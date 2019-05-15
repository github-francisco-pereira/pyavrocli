from requests import post


class AvroSchemaRegistryApi:
    def __init__(self, schema_registry_url, timeout):
        self.schema_registry_url = schema_registry_url
        self.timeout = timeout
        self._API_PATH = '/api/schema-registry/'

    def apply_subject(self, subject, payload):
        url = f'{self.schema_registry_url}{self._API_PATH}subjects/{subject}/versions/'
        response = post(url, json=payload)
        response.raise_for_status()
        return response.json()
