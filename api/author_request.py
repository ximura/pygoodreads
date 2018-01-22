from api.request import Request


class AuthorRequest(Request):
    def show(self, author_id: int):
        """Get an xml response with info about an author. """
        resp = self.get("author/show", {'id': author_id})
        return resp['author']

    def books(self, author_id: int, page: int = 1):
        """Get an xml response with a paginated list of an authors books. """
        resp = self.get("author/list", {'id': author_id, 'page': page})
        return resp