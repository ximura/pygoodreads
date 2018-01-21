import requests
import xmltodict
import json

from urls import base_url


class RequestException(Exception):
    def __init__(self, error_msg, url):
        self.error_msg = error_msg
        self.url = url

    def __str__(self):
        return self.url, ':', self.error_msg


class Request:
    def __init__(self, dev_key, req_format='xml'):
        """Initialize request object."""
        self.dev_key = dev_key
        self.req_format = req_format

    def request(self, path, params):
        params.update({'key': self.dev_key})
        resp = requests.get("%s/%s" % (base_url, path), params=params)
        if resp.status_code != 200:
            raise RequestException(resp.reason, path)
        if self.req_format == 'xml':
            print(resp.content)
            data_dict = xmltodict.parse(resp.content)
            return data_dict['GoodreadsResponse']
        elif self.req_format == 'json':
            return json.loads(resp.content)
        else:
            raise Exception("Invalid format")