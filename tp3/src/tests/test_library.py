import pytest
from src.bibliotheque.library import Library
from src.bibliotheque.book import Book
from src.bibliotheque.user import User

class TestLibraryCreation:
    """Tests de création de bibliothèque"""

    def test_create_valid_library(self):
        """Test création bibliothèque valide"""
        library = Library("Bibliothèque Municipale")
        assert library.name == "Bibliothèque Municipale"
        assert library.books == []

    def test_create_library_empty_name_raises_error(self):
        """Test nom vide lève une erreur"""
        with pytest.raises(ValueError, match="Library name cannot be empty"):
            Library("")
        
        with pytest.raises(ValueError, match="Library name cannot be empty"):
            Library("   ")

class TestLibraryBookManagement:
    """Tests de gestion des livres"""

    def setup_method(self):
        """Fixture : prépare une bibliothèque pour chaque test"""
        self.library = Library("Test Library")
        self.book1 = Book("Book 1", "Author 1", "1234567890123")
        self.book2 = Book("Book 2", "Author 2", "1234567890124")

    def test_add_book_success(self):
        """Test ajout livre avec succès"""
        self.library.add_book(self.book1)
        assert self.book1 in self.library.books
        assert len(self.library.books) == 1

    def test_add_invalid_book_raises_error(self):
        """Test ajout objet non-livre lève une erreur"""
        with pytest.raises(TypeError, match="Only Book instances can be added"):
            self.library.add_book("not a book")

    def test_find_book_by_isbn_success(self):
        """Test recherche livre par ISBN avec succès"""
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        
        found_book = self.library.find_book_by_isbn("1234567890123")
        assert found_book == self.book1

    def test_find_book_by_isbn_not_found(self):
        """Test recherche livre par ISBN non trouvé"""
        self.library.add_book(self.book1)
        
        found_book = self.library.find_book_by_isbn("9999999999999")
        assert found_book is None

class TestLibraryBorrowing:
    """Tests d'emprunt en bibliothèque"""

    def setup_method(self):
        """Fixture : prépare bibliothèque, utilisateur et livre"""
        self.library = Library("Test Library")
        self.user = User("John Doe", "john@example.com")
        self.book = Book("Test Book", "Test Author", "1234567890123")
        self.library.add_book(self.book)

    def test_borrow_book_success(self):
        """Test emprunt livre avec succès"""
        result = self.library.borrow_book(self.user, "1234567890123")
        assert result == True
        assert not self.book.is_available()
        assert self.book in self.user.borrowed_books

    def test_borrow_nonexistent_book_fails(self):
        """Test emprunt livre inexistant échoue"""
        result = self.library.borrow_book(self.user, "9999999999999")
        assert result == False

    def test_borrow_already_borrowed_book_fails(self):
        """Test emprunt livre déjà emprunté échoue"""
        # Premier emprunt
        self.library.borrow_book(self.user, "1234567890123")
        
        # Tentative second emprunt par autre utilisateur
        user2 = User("Jane Doe", "jane@example.com")
        result = self.library.borrow_book(user2, "1234567890123")
        assert result == False

    def test_borrow_with_invalid_user_fails(self):
        """Test emprunt avec utilisateur invalide échoue"""
        result = self.library.borrow_book("not a user", "1234567890123")
        assert result == False

    def test_borrow_when_user_cannot_borrow_fails(self):
        """Test emprunt quand utilisateur ne peut pas emprunter échoue"""
        # Simuler utilisateur qui a atteint sa limite
        for i in range(3):
            book = Book(f"Book {i}", f"Author {i}", f"123456789012{i}")
            self.library.add_book(book)
            self.user.add_borrowed_book(book)
        
        result = self.library.borrow_book(self.user, "1234567890123")
        assert result == False
