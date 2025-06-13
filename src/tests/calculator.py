import pytest
from src.calculator import add, divise, power

class TestCalculatorAddition:
    def test_add_integers(self):
        assert add(5, 3) == 8

    def test_add_floats(self):
        assert add(2.5, 3.7) == pytest.approx(6.2)

    def test_add_avec_zero(self):
        assert add(0, 5) == 5
        assert add(5, 0) == 5

    def test_add_negatifs(self):
        assert add(-5, -3) == -8
        assert add(10, -7) == 3

    def test_add_type_invalide(self):
        with pytest.raises(TypeError):
            add("5", a)
        with pytest.raises(TypeError):
            add(5, "3")
            
class TestCalculatorDivision:
    def test_divise_integers(self):
        assert divise(10, 2) == 5
            
if __name__ == "__main__":
    pytest.main()
