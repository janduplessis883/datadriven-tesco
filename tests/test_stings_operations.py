import pytest

def test_string_concaterantion():
    assert "hello " + "world" == "hello  world"

def test_math_still_works():
    assert 1 + 1 == 2, "Math Still Works ✅"
    
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        x = 1 / 0
        
@pytest.mark.parametrize("input1, input2, output", [(5, 5, 25), (2, 3, 6), (7, 3, 21)])
def test_multiplication(input1, input2, output):
    assert input1 * input2 == output
        