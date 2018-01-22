import webbrowser

from session import Session
from api.author_request import AuthorRequest
from api.shelf_request import ShelfRequest


class Client:

    def authorize(self, oauth_key: str, oauth_secret: str):
        self.session = Session(oauth_key, oauth_secret)
        authorize_url = self.session.get_authorize_url()
        webbrowser.open(authorize_url)
        self.session.finish_authorization()

    def auth_user(self):
        """Return user who authorized OAuth"""
        if not hasattr(self, 'session'):
            raise Exception("No authenticated session")
        resp = self._request_oauth('api/auth_user', {})
        user_id = resp['user']['@id']
        return user_id

    # author requests
    def author_info(self, author_id):
        req = AuthorRequest(self.session)
        return req.show(author_id)

    def author_books(self, author_id):
        req = AuthorRequest(self.session)
        return req.books(author_id)

    # shelf requests
    def shelf_add(self, shelf_name, book_id):
        req = ShelfRequest(self.session)
        #resp = self._request_oauth("shelf/add_to_shelf", {'name': shelf_name, 'book_id': book_id})
        return req.add_book(shelf_name, book_id)

    def shelf_list(self, user_id):
        req = ShelfRequest(self.session)
        return req.list(user_id)

    # private methods
    def _request_oauth(self, *args, **kwargs):
        resp = self.session.get(*args, **kwargs)
        return resp


if __name__ == "__main__":
    client = Client()
    client.authorize("JXSdeANk24Z97P0AjH3Vsg", "TcZPrUAqtfAisrDE6plOV4ibvsCpBm4JJQDViXqc")
    print(client.auth_user())
    print(client.author_info(123))
    print(client.author_books(123))
    print(client.shelf_list(31285592))
    print("shelf_add\n")
    print(client.shelf_add('test', 123))
