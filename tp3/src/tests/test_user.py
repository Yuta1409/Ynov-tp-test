import pytest
from src.bibliotheque.user import User
from src.bibliotheque.book import Book

class TestUserCreation:
    """Tests de création d'utilisateur"""

    def test_create_valid_user(self):
        """Test création utilisateur valide"""
        user = User("John Doe", "john@example.com")
        assert user.name == "John Doe"
        assert user.email == "john@example.com"
        assert user.borrowed_books == []

    def test_create_user_empty_name_raises_error(self):
        """Test nom vide lève une erreur"""
        with pytest.raises(ValueError, match="Name cannot be empty"):
            User("", "john@example.com")
        
        with pytest.raises(ValueError, match="Name cannot be empty"):
            User("   ", "john@example.com")

    def test_create_user_invalid_email_raises_error(self):
        """Test email invalide lève une erreur"""
        with pytest.raises(ValueError, match="Email must contain @"):
            User("John Doe", "invalid-email")
        
        with pytest.raises(ValueError, match="Email must contain @"):
            User("John Doe", "")

class TestUserBorrowing:
    """Tests d'emprunt utilisateur"""

    def setup_method(self):
        """Fixture : prépare un utilisateur pour chaque test"""
        self.user = User("John Doe", "john@example.com")
        self.book1 = Book("Book 1", "Author 1", "1234567890123")
        self.book2 = Book("Book 2", "Author 2", "1234567890124")

    def test_new_user_can_borrow(self):
        """Test nouvel utilisateur peut emprunter"""
        assert self.user.can_borrow() == True

    def test_add_borrowed_book(self):
        """Test ajout livre emprunté"""
        self.user.add_borrowed_book(self.book1)
        assert self.book1 in self.user.borrowed_books
        assert len(self.user.borrowed_books) == 1

    def test_add_same_book_twice_doesnt_duplicate(self):
        """Test ajout même livre deux fois ne duplique pas"""
        self.user.add_borrowed_book(self.book1)
        self.user.add_borrowed_book(self.book1)
        assert len(self.user.borrowed_books) == 1

    def test_remove_borrowed_book_success(self):
        """Test retrait livre emprunté avec succès"""
        self.user.add_borrowed_book(self.book1)
        result = self.user.remove_borrowed_book(self.book1)
        assert result == True
        assert self.book1 not in self.user.borrowed_books

    def test_remove_non_borrowed_book_fails(self):
        """Test retrait livre non emprunté échoue"""
        result = self.user.remove_borrowed_book(self.book1)
        assert result == False

    def test_cannot_borrow_when_limit_reached(self):
        """Test ne peut pas emprunter quand limite atteinte"""
        # Ajouter 3 livres (limite par défaut)
        book3 = Book("Book 3", "Author 3", "1234567890125")
        self.user.add_borrowed_book(self.book1)
        self.user.add_borrowed_book(self.book2)
        self.user.add_borrowed_book(book3)
        
        assert self.user.can_borrow() == False
