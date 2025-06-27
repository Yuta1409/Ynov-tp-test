import pytest
from src.bibliotheque.book import Book

class TestBookCreation:
    """Tests de création de livre"""

    def test_create_valid_book(self):
        """Test création livre valide"""
        book = Book("Le Petit Prince", "Antoine de Saint-Exupéry", "9782070612758")
        assert book.title == "Le Petit Prince"
        assert book.author == "Antoine de Saint-Exupéry"
        assert book.isbn == "9782070612758"

    def test_create_book_empty_title_raises_error(self):
        """Test titre vide lève une erreur"""
        with pytest.raises(ValueError, match="Title cannot be empty"):
            Book("", "Antoine de Saint-Exupéry", "9782070612758")
        
        with pytest.raises(ValueError, match="Title cannot be empty"):
            Book("   ", "Antoine de Saint-Exupéry", "9782070612758")

    def test_create_book_invalid_isbn_raises_error(self):
        """Test ISBN invalide lève une erreur"""
        # ISBN trop court
        with pytest.raises(ValueError, match="ISBN must be exactly 13 characters long"):
            Book("Le Petit Prince", "Antoine de Saint-Exupéry", "123456789")
        
        # ISBN trop long
        with pytest.raises(ValueError, match="ISBN must be exactly 13 characters long"):
            Book("Le Petit Prince", "Antoine de Saint-Exupéry", "12345678901234")

class TestBookBorrowing:
    """Tests d'emprunt de livre"""

    def setup_method(self):
        """Fixture : prépare un livre pour chaque test"""
        self.book = Book("Le Petit Prince", "Antoine de Saint-Exupéry", "9782070612758")

    def test_new_book_is_available(self):
        """Test livre neuf disponible"""
        assert self.book.is_available() == True

    def test_borrow_available_book_success(self):
        """Test emprunt livre disponible"""
        result = self.book.borrow()
        assert result == True
        assert self.book.is_available() == False

    def test_borrow_already_borrowed_book_fails(self):
        """Test emprunt livre déjà emprunté"""
        self.book.borrow()
        result = self.book.borrow()
        assert result == False