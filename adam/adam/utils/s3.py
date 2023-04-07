import requests


class S3Utils:
    @classmethod
    def push_openapi_spec_to_s3(cls, url, body):
        _response = requests.post(url=url, json=body)
        return _response

    @classmethod
    def get_service_key(cls, url, params):
        _response = requests.get(url=url, params=params)
        return _response.json()
