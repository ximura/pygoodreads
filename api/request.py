import requests
import xmltodict

from urls import base_url


class RequestException(Exception):
    def __init__(self, error_msg, url):
        self.error_msg = error_msg
        self.url = url

    def __str__(self):
        return self.url, ':', self.error_msg


class Request:
    GET = "get"
    POST = "post"
    PUT = "put"

    def __init__(self, dev_key=None):
        """Initialize request object."""
        self.dev_key = dev_key

    def get(self, path, params):
        return self._request(Request.GET, path, params)

    def post(self, path, params):
        return self._request(Request.POST, path, params)

    def put(self, path, params):
        return self._request(Request.PUT, path, params)

    def _request(self, method, path, params):
        if self.dev_key:
            params.update({'key': self.dev_key})

        resp = requests.request(method=method, url="%s/%s" % (base_url, path), params=params)
        if resp.status_code != 200:
            raise RequestException(resp.reason, path)

        print(resp.content)
        data_dict = xmltodict.parse(resp.content)
        return data_dict['GoodreadsResponse']