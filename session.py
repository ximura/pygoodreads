from rauth.service import OAuth1Service, OAuth1Session
import xmltodict

from urls import base_url, request_token_url, authorize_url, access_token_url


class Session:
    """Handle OAuth sessions"""
    def __init__(self, oauth_key: str, oauth_secret: str):
        self.oauth_key = oauth_key
        self.oauth_secret = oauth_secret

    def get_authorize_url(self):
        """Start outh and return authorization url."""
        self.service = OAuth1Service(
            consumer_key=self.oauth_key,
            consumer_secret=self.oauth_secret,
            name='goodreads',
            request_token_url=request_token_url,
            authorize_url=authorize_url,
            access_token_url=access_token_url,
            base_url=base_url
        )

        self.request_token, self.request_token_secret = self.service.get_request_token(header_auth=True)

        return self.service.get_authorize_url(self.request_token)

    def finish_authorization(self):
        self.session = self.service.get_auth_session(self.request_token,
                                                     self.request_token_secret)

    def get(self, path, params=None):
        """OAuth get request"""
        if not params:
            params = {}
        base = "https://www.goodreads.com/"
        resp = self.session.get(base + path, params=params)
        return xmltodict.parse(resp.content)['GoodreadsResponse']