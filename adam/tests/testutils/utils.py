import json
import os
import contextlib
from tests.testutils.constants import TEMP_DIR, OPENAPI_SPEC_TEST_DATA
from typing import Union
from pathlib import Path


@contextlib.contextmanager
def _test_cwd(current_working_directory: Union[str, Path, None] = None):
    """
    Sets the <current_working_directory>

    :param str current_working_directory: path of directory to be set
    """

    cwd = os.getcwd()
    try:
        if current_working_directory is not None:
            os.chdir(current_working_directory)
        yield
    finally:
        os.chdir(cwd)


def _create_openapi_file(path: str, chroot: str = TEMP_DIR) -> None:
    if not os.path.exists(chroot):
        os.makedirs(chroot)

    with open(chroot + "/openapi.json", "w") as file:
        file.write(json.dumps(OPENAPI_SPEC_TEST_DATA))


def _destroy_openapi_file(path: str, chroot: str = TEMP_DIR) -> None:
    path = chroot + "/openapi.json"
    if os.path.exists(path) and os.path.isfile(path):
        os.remove(path)
