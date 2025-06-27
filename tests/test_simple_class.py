# A class that takes two values 

import pytest
from lib.high_value import *

def test_wrong_value():
    with pytest.raises(TypeError) as e:
        hv = HighValue("s", "f")
    error_message = str(e.value)
    assert error_message == "Incorrect datatype"

def test_first_value_higher():
    hv = HighValue(6,3)
    result = hv.get_highest()
    assert result == "First value is higher"

def test_second_value_higher():
    hv = HighValue(4,8)
    result = hv.get_highest()
    assert result == "Second value is higher"

def test_same_value():
    hv = HighValue(4,4)
    result = hv.get_highest()
    assert result == "Values are equal"

def test_add_value_one():
    hv = HighValue(3,4)
    hv.add(4, "first")
    result = hv.get_highest()
    assert result == "First value is higher"

def test_add_value_two():
    hv = HighValue(6,4)
    hv.add(4, "second")
    result = hv.get_highest()
    assert result == "Second value is higher"

def test_negative_numbers():
    hv = HighValue(-5, 4)
    result = hv.get_highest()
    assert result == "Second value is higher"

def test_add_negative():
    hv = HighValue(-5,4)
    hv.add(-6, "second")
    result = hv.get_highest()
    assert result == "Second value is higher" 

def test_add_function():
    hv = HighValue(4,5)
    hv.add(4, "third")
    result = hv.add(4, "third")
    assert result == "Select first or second"

def test_zero_value():
    hv = HighValue(0, 5)
    result = hv.get_highest()
    assert result == "Second value is higher"

def test_add_zero():
    hv = HighValue(0, 5)
    hv.add(0, "first")
    result = hv.get_highest()
    assert result == "Second value is higher"

def test_multiple_add():
    hv = HighValue(0, 5)
    hv.add(-4, "first")
    hv.add(6, "second")
    hv.add(16, "first")
    result = hv.get_highest()
    assert result == "First value is higher"