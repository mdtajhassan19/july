import json
from jsonschema import validate

def validate_schema(data, schema_path):
    with open(schema_path, "r", encoding="utf-8") as file:
        content = file.read().strip()

        if not content:
            raise AssertionError(f"Schema file '{schema_path}' is empty.")

        schema = json.loads(content)

    validate(instance=data, schema=schema)