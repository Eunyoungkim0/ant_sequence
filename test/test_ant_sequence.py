import pytest
from src.ant_sequence import find_middle_two

def test_find_middle_two():
    assert find_middle_two(5) == "12"
    assert find_middle_two(7) == "12"
    assert find_middle_two(8) == "21"
