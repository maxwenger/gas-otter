import pytest
from user_input import UserInput

class TestGas:
    def test_default_value(self):
        assert UserInput.getFloatInput('', 0, 1, default_value=5) == 5

