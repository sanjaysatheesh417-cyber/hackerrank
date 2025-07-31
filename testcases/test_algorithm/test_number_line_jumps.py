import pytest

from solutions.algorithms.number_line_jumps import kangaroo

@pytest.mark.parametrize("x1, v1, x2, v2, expected", [(0 ,3 ,4 ,2 , "YES"), (0 ,2 ,5 ,3 ,"NO")
,(2 ,1 ,1 ,2 , "yes")] , ids=["TEST CASE 1", "TEST CASE 2", "TEST CASE 3"] )

def test_kangaroo(x1, v1, x2, v2, expected):
    assert  kangaroo(x1, v1, x2, v2) == expected