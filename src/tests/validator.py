import pytest
from src.validator import is_valid_email

class TestEmailValidation:
    def test_valid_email(self):
        valides = ["user@example.com", "test.email@domain.org"]
        for email in valides:
            assert is_valid_email(email) == True
            
    def test_invalid_email(self):
        invalides = ["user", "user@", "@domain.com", "user@domain"]
        for email in invalides:
            assert is_valid_email(email) == False
            
    def test_type_invalide(self):
        with pytest.raises(TypeError):
            is_valid_email(123)
                
