from typing import List

from api.request import Request


class ShelfRequest(Request):
    def add_book(self, shelf_name: str, book_id: int):
        """ Add a book to a shelf."""
        resp = self.post("shelf/add_to_shelf", {'name': shelf_name, 'book_id': book_id})
        return resp

    def add_books(self, shelves_name: List[str], books_id: List[int]):
        """Add books to many shelves."""
        resp = self.post("shelf/add_books_to_shelves",
                         {'shelves': ','.join(shelves_name), 'bookids': ','.join(books_id)})
        return resp

    def list(self, user_id: int, page: int = 1):
        """Get a user's shelves."""
        resp = self.get("shelf/list", {'id': user_id, 'page': page})
        return resp['shelves']
