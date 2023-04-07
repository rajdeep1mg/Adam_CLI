from enum import Enum
from adam.utils.validation import ValidateOpenAPISpec


class OpenAPISpecVersion(Enum):
    v30 = ValidateOpenAPISpec.run_validation_with_openapi_v30_spec_validator
    v3 = ValidateOpenAPISpec.run_validation_with_openapi_v3_spec_validator
    v31 = ValidateOpenAPISpec.run_validation_with_openapi_v31_spec_validator
    v2 = ValidateOpenAPISpec.run_validation_with_openapi_v2_spec_validator
