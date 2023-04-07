import shlex
import logging
import sys
import os
from tests.testutils.constants import TEMP_DIR
from unittest import TestCase
from unittest.mock import patch
from testutils.utils import _create_openapi_file, _destroy_openapi_file, _test_cwd
from parameterized import parameterized
from adam.cli.args import get_args
import contextlib
from testutils.constants import DEFAULT_VERSION, DEFAULT_PATH
from adam.utils.files import get_openapi_specification_file
from openapi_spec_validator.validation.validators import OpenAPIValidationError
from adam.versions.version import OpenAPISpecVersion


class TestCli(TestCase):
    _rootdir = os.path.join(os.getcwd())
    _openapi_file_created = "/openapi.json"

    def setUp(self):
        _create_openapi_file(self._openapi_file_created, chroot=self._rootdir)
        super().setUp()

    def tearDown(self) -> None:
        _destroy_openapi_file(self._openapi_file_created, self._rootdir)
        super().tearDown()

    @parameterized.expand([(_openapi_file_created, _rootdir)])
    def test_cli_argument_success(self, _openapi_file_created: str, _rootdir: str):
        test_args = shlex.split("adam --path")
        test_args.extend([_rootdir + _openapi_file_created])
        test_args.extend(["--key", "c43f42cc-8499-43c1-be98-573eb2ec2dfc"])
        test_args.extend(["--service_name", "ad_mon"])
        with contextlib.ExitStack() as stack:
            stack.enter_context(_test_cwd(_rootdir))
            stack.enter_context(patch.object(sys, "argv", test_args))

            args = get_args()

            self.assertEqual(args._version, DEFAULT_VERSION)
            self.assertEqual(args._path, _rootdir + _openapi_file_created)

    @parameterized.expand([(_openapi_file_created, _rootdir)])
    def test_cli_no_path_argument(self, _openapi_file_created: str, _rootdir: str):
        test_args = shlex.split("adam")
        test_args.extend(["--key", "c43f42cc-8499-43c1-be98-573eb2ec2dfc"])
        test_args.extend(["--service_name", "ad_mon"])
        with contextlib.ExitStack() as stack:
            stack.enter_context(_test_cwd(_rootdir))
            stack.enter_context(patch.object(sys, "argv", test_args))

            args = get_args()
            self.assertEqual(args._version, DEFAULT_VERSION)
            self.assertEqual(args._path, os.path.join(os.getcwd()) + DEFAULT_PATH)

    @parameterized.expand([(_openapi_file_created, _rootdir)])
    def test_cli_argument_path_duplication(
        self, _openapi_file_created: str, _rootdir: str
    ):
        test_args = shlex.split("adam --path")
        test_args.extend([_rootdir + _openapi_file_created])
        test_args.extend(["--path"])
        test_args.extend([_rootdir + _openapi_file_created])
        test_args.extend(["--key", "c43f42cc-8499-43c1-be98-573eb2ec2dfc"])
        test_args.extend(["--service_name", "ad_mon"])

        with contextlib.ExitStack() as stack:
            stack.enter_context(_test_cwd(_rootdir))
            stack.enter_context(patch.object(sys, "argv", test_args))

            with patch("sys.exit") as context:
                _args = get_args()
                self.assertTrue(context.called)

    @parameterized.expand([(_openapi_file_created, _rootdir)])
    def test_cli_argument_invalid_path(self, _openapi_file_created: str, _rootdir: str):
        invalid_path = "invalid_path/openapi.json"
        test_args = shlex.split("adam --path")
        test_args.extend([invalid_path])
        test_args.extend(["--key", "c43f42cc-8499-43c1-be98-573eb2ec2dfc"])
        test_args.extend(["--service_name", "ad_mon"])

        with contextlib.ExitStack() as stack:
            stack.enter_context(_test_cwd(_rootdir))
            stack.enter_context(patch.object(sys, "argv", test_args))
            print(stack)

            with self.assertRaises(FileNotFoundError) as cm:
                file = get_openapi_specification_file(invalid_path)
            self.assertTrue(isinstance(cm.exception, FileNotFoundError))

    @parameterized.expand([(_openapi_file_created, _rootdir)])
    def test_cli_argument_key_duplication(
        self, _openapi_file_created: str, _rootdir: str
    ):
        test_args = shlex.split("adam --path")
        test_args.extend([_rootdir + _openapi_file_created])
        test_args.extend(["--key", "c43f42cc-8499-43c1-be98-573eb2ec2dfc"])
        test_args.extend(["--key", "c43f42cc-8499-43c1-be98-573eb2ec2dfc"])
        test_args.extend(["--service_name", "ad_mon"])

        with contextlib.ExitStack() as stack:
            stack.enter_context(_test_cwd(_rootdir))
            stack.enter_context(patch.object(sys, "argv", test_args))

            with patch("sys.exit") as context:
                _args = get_args()
                self.assertTrue(context.called)

    @parameterized.expand([(_openapi_file_created, _rootdir)])
    def test_cli_argument_service_name_duplication(
        self, _openapi_file_created: str, _rootdir: str
    ):
        test_args = shlex.split("adam --path")
        test_args.extend([_rootdir + _openapi_file_created])
        test_args.extend(["--key", "c43f42cc-8499-43c1-be98-573eb2ec2dfc"])
        test_args.extend(["--service_name", "ad_mon"])
        test_args.extend(["--service_name", "health_service"])

        with contextlib.ExitStack() as stack:
            stack.enter_context(_test_cwd(_rootdir))
            stack.enter_context(patch.object(sys, "argv", test_args))

            with patch("sys.exit") as context:
                _args = get_args()
                self.assertTrue(context.called)

    @parameterized.expand([(_openapi_file_created, _rootdir)])
    def test_cli_openapi_validation_error(
        self, _openapi_file_created: str, _rootdir: str
    ):
        test_args = shlex.split("adam --path")
        test_args.extend([_rootdir + _openapi_file_created])
        test_args.extend(["--key", "c43f42cc-8499-43c1-be98-573eb2ec2dfc"])
        test_args.extend(["--service_name", "ad_mon"])
        with contextlib.ExitStack() as stack:
            stack.enter_context(_test_cwd(_rootdir))
            stack.enter_context(patch.object(sys, "argv", test_args))
            """
             Test OpenAPI Validation Exception when a required property is None
            """
            with self.assertRaises(OpenAPIValidationError) as test_exception_1:
                openapi_spec_file = get_openapi_specification_file(
                    _rootdir + _openapi_file_created
                )
                openapi_spec_file["info"]["title"] = None
                getattr(OpenAPISpecVersion, DEFAULT_VERSION)(spec=openapi_spec_file)
            self.assertTrue(
                isinstance(test_exception_1.exception, OpenAPIValidationError)
            )

            """
            Test OpenAPI Validation Exception when a required property is not defined
            """
            with self.assertRaises(OpenAPIValidationError) as test_exception_2:
                openapi_spec_file = get_openapi_specification_file(
                    _rootdir + _openapi_file_created
                )
                del openapi_spec_file["info"]["title"]
                del openapi_spec_file["info"]["version"]
                getattr(OpenAPISpecVersion, DEFAULT_VERSION)(spec=openapi_spec_file)
            self.assertTrue(
                isinstance(test_exception_2.exception, OpenAPIValidationError)
            )
            """
            Test OpenAPI Validation Exception when a version is incorrectly defined
            """
            with self.assertRaises(OpenAPIValidationError) as test_exception_3:
                openapi_spec_file = get_openapi_specification_file(
                    _rootdir + _openapi_file_created
                )
                openapi_spec_file["info"]["version"] = 3.1
                getattr(OpenAPISpecVersion, DEFAULT_VERSION)(spec=openapi_spec_file)
            self.assertTrue(
                isinstance(test_exception_2.exception, OpenAPIValidationError)
            )

            """
                Test OpenAPI Validation Exception when a extra parameter is specified
            """
            with self.assertRaises(OpenAPIValidationError) as test_exception_3:
                openapi_spec_file = get_openapi_specification_file(
                    _rootdir + _openapi_file_created
                )
                openapi_spec_file["tags"] = ["Test_Operations"]
                getattr(OpenAPISpecVersion, DEFAULT_VERSION)(spec=openapi_spec_file)
            self.assertTrue(
                isinstance(test_exception_2.exception, OpenAPIValidationError)
            )
