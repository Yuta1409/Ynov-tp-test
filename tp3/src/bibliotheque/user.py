class User:
    """Représente un utilisateur de la bibliothèque"""

    def __init__(self, name, email):
        if not name or not name.strip():
            raise ValueError("Name cannot be empty")
        if not email or '@' not in email:
            raise ValueError("Email must contain @")
        
        self.name = name.strip()
        self.email = email.strip()
        self.borrowed_books = []

    def can_borrow(self, max_books=3):
        return len(self.borrowed_books) < max_books

    def add_borrowed_book(self, book):
        if book not in self.borrowed_books:
            self.borrowed_books.append(book)

    def remove_borrowed_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            return True
        return False