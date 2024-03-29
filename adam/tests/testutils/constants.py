import json

TEMP_DIR: str = "Users/rajdeep/Desktop/adam/temp"
DEFAULT_PATH: str = "/openapi.json"
DEFAULT_VERSION: str = "v30"
OPENAPI_SPEC_TEST_DATA: dict = {
    "openapi": "3.0.3",
    "info": {"title": "API", "version": "1.0.0", "contact": {}},
    "paths": {
        "/ping": {
            "get": {
                "operationId": "get~ping",
                "summary": "Ping",
                "responses": {"default": {"description": "OK"}},
            }
        },
        "/v4/pull-from-s3-bucket": {
            "get": {
                "operationId": "get~S3-Operations.pull_from_s3_bucket",
                "summary": "Pull From S3 Bucket",
                "tags": ["S3-Operations"],
                "responses": {"default": {"description": "OK"}},
            }
        },
        "/v4/push-to-s3-bucket": {
            "post": {
                "operationId": "post~S3-Operations.push_to_s3_bucket",
                "summary": "Push To S3 Bucket",
                "tags": ["S3-Operations"],
                "responses": {"default": {"description": "OK"}},
            }
        },
        "/v4/ping/{name}": {
            "get": {
                "operationId": "get~ads.get_products",
                "summary": ":param request:",
                "description": ":return:",
                "tags": ["ads"],
                "parameters": [
                    {
                        "name": "name",
                        "schema": {"type": "string"},
                        "required": True,
                        "in": "path",
                    }
                ],
                "responses": {"default": {"description": "OK"}},
            }
        },
    },
    "tags": [{"name": "S3-Operations"}, {"name": "ads"}],
    "servers": [],
    "security": [],
}
