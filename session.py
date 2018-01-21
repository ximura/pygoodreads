import oauth2 as oauth
from urllib.parse import parse_qsl
import xmltodict

import webbrowser
from urls import request_token_url, authorize_url, access_token_url

class Session:
    """Handle OAuth sessions"""
    def __init__(self, oauth_key: str, oauth_secret: str):
        consumer = oauth.Consumer(key=oauth_key,
                                  secret=oauth_secret)

        self.client = oauth.Client(consumer)

    def authorize(self):
        response, content = self.client.request(request_token_url, 'GET')
        if response['status'] != '200':
            raise Exception('Invalid response: %s' % response['status'])

        request_token = dict(parse_qsl(content.decode("utf-8")))

        token = oauth.Token(request_token['oauth_token'],
                            request_token['oauth_token_secret'])

        authorize_link = '%s?oauth_token=%s' % (authorize_url,
                                                token.key)
        webbrowser.open(authorize_link)

        print(token)


if __name__ == "__main__":
    session = Session("JXSdeANk24Z97P0AjH3Vsg", "TcZPrUAqtfAisrDE6plOV4ibvsCpBm4JJQDViXqc")
    session.authorize()