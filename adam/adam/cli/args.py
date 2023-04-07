import argparse
from adam.cli.actions import (
    UniquePathAction,
    UniqueVersionAction,
    UniqueKeyAction,
    UniqueServiceNameAction,
)
from adam.config.constants import DEFAULT_PATH
import os


def get_args():
    parser = argparse.ArgumentParser(
        prog="adam",
        description="takes path of OpenAPI Specification File and pushes to S3",
    )

    parser.add_argument(
        "-p",
        "--path",
        default=os.path.join(os.getcwd(), "openapi.json"),
        action=UniquePathAction,
        dest="_path",
        help="path of the OpenAPI Specification file (default = ./openapi.json)",
        nargs="?",
        required=False,
        type=str,
    )

    parser.add_argument(
        "-v",
        "--version",
        default="v30",
        dest="_version",
        help="version of the OpenAPI Specification (OAS)",
        action=UniqueVersionAction,
        choices=["v30", "v3", "v31", "v2"],
        nargs="?",
        required=False,
        type=str,
    )

    parser.add_argument(
        "-k",
        "--key",
        dest="_key",
        help="respective service key",
        action=UniqueKeyAction,
        nargs="?",
        required=True,
        type=str,
    )

    parser.add_argument(
        "-s",
        "--service_name",
        dest="_service_name",
        help="respective service name",
        action=UniqueServiceNameAction,
        nargs="?",
        required=True,
        type=str,
    )

    return parser.parse_args()
