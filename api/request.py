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
    def __init__(self, req_format='xml'):
        """Initialize request object."""
        self.req_format = req_format

    def request(self, path, params):
        params.update({'key': 'JXSdeANk24Z97P0AjH3Vsg'})
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