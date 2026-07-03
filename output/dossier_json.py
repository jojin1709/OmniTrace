import json


class JSONDossier:
    def generate(self, data: dict) -> str:
        return json.dumps(data, indent=2, default=str)
