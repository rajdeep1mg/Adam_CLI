from enum import Enum

DEFAULT_PATH = "./openapi.json"
GET_SERVICE_KEY_ENDPOINT = "http://0.0.0.0:8090/v1/s3/key"
PUSH_TO_S3_BUCKET_ENDPOINT = "http://0.0.0.0:8090/v1/s3/openapi"
OPENAPI_SUCCESSFULLY_PUSHED_TO_S3 = (
    "OpenAPI specification file successfully pushed to s3 bucket"
)


class AdamExceptions(Enum):
    SERVICE_KEY_INVALID_EXCEPTION_MESSAGE = (
        "The service key for {service_name} service is invalid"
    )
    SERVICE_NOT_FOUND_EXCEPTION_MESSAGE = "There is no service named {service_name}"
