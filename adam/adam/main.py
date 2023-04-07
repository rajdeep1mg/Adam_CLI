import logging
import asyncio
import sys
import coloredlogs
from adam.versions.version import OpenAPISpecVersion
from adam.cli.args import get_args
from adam.utils.files import get_openapi_specification_file
from adam.utils.s3 import S3Utils
from adam.utils.service_authentication import CheckServiceKey
from openapi_spec_validator.validation.validators import (
    OpenAPIValidationError,
    ParameterDuplicateError,
    UnresolvableParameterError,
    DuplicateOperationIDError,
)
from argparse import ArgumentError, ArgumentTypeError
from json import JSONDecodeError
from adam.config.constants import (
    PUSH_TO_S3_BUCKET_ENDPOINT,
    OPENAPI_SUCCESSFULLY_PUSHED_TO_S3,
)
from adam.exceptions import ServiceKeyInvalid, ServiceNotFound


def main():
    try:
        args = get_args()
        _path = getattr(args, "_path")
        _version = getattr(args, "_version")
        _service_name = getattr(args, "_service_name")
        # checking service key
        CheckServiceKey.verify_service_key()
        openapi_spec_file = get_openapi_specification_file(_path)
        getattr(OpenAPISpecVersion, _version)(spec=openapi_spec_file)
        _response = S3Utils.push_openapi_spec_to_s3(
            url=f"{PUSH_TO_S3_BUCKET_ENDPOINT}",
            body={"service_name": _service_name, "contents": openapi_spec_file},
        )
        logging.info(OPENAPI_SUCCESSFULLY_PUSHED_TO_S3)
    except (
        FileNotFoundError,
        JSONDecodeError,
        OpenAPIValidationError,
        ArgumentError,
        ArgumentTypeError,
        ValueError,
        ParameterDuplicateError,
        UnresolvableParameterError,
        DuplicateOperationIDError,
        ServiceNotFound,
        ServiceKeyInvalid,
    ) as exception:
        logging.warning(str(exception))
        sys.exit(1)
