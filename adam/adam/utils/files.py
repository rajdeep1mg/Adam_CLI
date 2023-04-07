from typing import Dict
import ujson


def get_openapi_specification_file(path) -> Dict:
    with open(path) as file:
        openapi_specification_file = ujson.load(file)

    return openapi_specification_file
