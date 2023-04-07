from openapi_spec_validator import (
    openapi_v30_spec_validator,
    openapi_v3_spec_validator,
    openapi_v31_spec_validator,
    openapi_v2_spec_validator,
)
from openapi_spec_validator import validate_spec


class ValidateOpenAPISpec:
    @classmethod
    def run_validation_with_openapi_v30_spec_validator(cls, spec):
        validate_spec(spec=spec, validator=openapi_v30_spec_validator)

    @classmethod
    def run_validation_with_openapi_v3_spec_validator(cls, spec):
        validate_spec(spec=spec, validator=openapi_v3_spec_validator)

    @classmethod
    def run_validation_with_openapi_v31_spec_validator(cls, spec):
        validate_spec(spec=spec, validator=openapi_v31_spec_validator)

    @classmethod
    def run_validation_with_openapi_v2_spec_validator(cls, spec):
        validate_spec(spec=spec, validator=openapi_v2_spec_validator)
