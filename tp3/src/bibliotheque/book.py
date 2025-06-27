class Book:
    """Représente un livre dans la bibliothèque"""

    def __init__(self, title, author, isbn):
        if not title or not title.strip():
            raise ValueError("Title cannot be empty")
        if not author or not author.strip():
            raise ValueError("Author cannot be empty")
        if len(isbn) != 13:
            raise ValueError("ISBN must be exactly 13 characters long")
        
        self.title = title.strip()
        self.author = author.strip()
        self.isbn = isbn
        self.borrowed = False

    def is_available(self):
        return not self.borrowed

    def borrow(self):
        if not self.borrowed:
            self.borrowed = True
            return True
        return False

    def return_book(self):
        if self.borrowed:
            self.borrowed = False
            return True
        return False