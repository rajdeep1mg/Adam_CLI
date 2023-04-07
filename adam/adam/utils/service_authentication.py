import asyncio
import json
import logging
from adam.cli.args import get_args
import sys
from adam.utils.s3 import S3Utils
from adam.config.constants import GET_SERVICE_KEY_ENDPOINT, AdamExceptions
from adam.exceptions import ServiceKeyInvalid, ServiceNotFound


class CheckServiceKey:
    def _get_service_key_from_adam(service_name: str):
        _response = S3Utils.get_service_key(
            url=f"{GET_SERVICE_KEY_ENDPOINT}", params={"service_name": service_name}
        )
        if not _response:
            raise ServiceNotFound(
                message=AdamExceptions.SERVICE_NOT_FOUND_EXCEPTION_MESSAGE.value.format(
                    service_name=service_name
                )
            )

        return _response["data"]["key"]

    __service_key = getattr(get_args(), "_key")
    __service_name = getattr(get_args(), "_service_name")

    @classmethod
    def verify_service_key(self):
        __service_key_from_adam = self._get_service_key_from_adam(
            service_name=self.__service_name
        )

        if self.__service_key != __service_key_from_adam:
            raise ServiceKeyInvalid(
                message=AdamExceptions.SERVICE_KEY_INVALID_EXCEPTION_MESSAGE.value.format(
                    service_name=self.__service_name
                )
            )
