from io import StringIO
from unittest.mock import patch
from tesco.main import *    
import pytest


class TestMathsOperations:
    def test_addition(self):
        assert 1 + 1 == 2

    def test_subtraction(self):
        assert 5 - 3 == 6
        
    def test_multiplication_simple(self):
        assert 6 / 2 == 3
        

@pytest.mark.parametrize("expected_output", ["Hello, I am ⭐️ Tesco Package"])
def test_hello_prints_correct_message(expected_output):
    # Redirect the standard output to a StringIO object
    output = StringIO()
    with patch('sys.stdout', new=output):
        # Call the hello function
        hello()

    # Get the value from the StringIO object
    output_value = output.getvalue().strip()

    # Assert that the printed message is correct
    assert output_value == expected_output