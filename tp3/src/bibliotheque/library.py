from .book import Book
from .user import User
class Library:
    def __init__(self, name):
        """Initialise une bibliothèque avec un nom"""
        if not name or name.strip() == "":
            raise ValueError("Library name cannot be empty")
        
        self.name = name.strip()
        self.books = []
    
    def add_book(self, book):
        """Ajoute un livre à la bibliothèque"""
        from .book import Book
        if not isinstance(book, Book):
            raise TypeError("Only Book instances can be added")
        
        self.books.append(book)
    
    def find_book_by_isbn(self, isbn):
        """Trouve un livre par son ISBN"""
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None
    
    def borrow_book(self, user, isbn):
        """Permet à un utilisateur d'emprunter un livre"""
        from .user import User
        
        # Vérifier que l'utilisateur est valide
        if not isinstance(user, User):
            return False
        
        # Vérifier que l'utilisateur peut emprunter
        if not user.can_borrow():
            return False
        
        # Trouver le livre
        book = self.find_book_by_isbn(isbn)
        if book is None:
            return False
        
        # Vérifier que le livre est disponible
        if not book.is_available():
            return False
        
        # Effectuer l'emprunt
        book.borrow()
        user.add_borrowed_book(book)
        return True