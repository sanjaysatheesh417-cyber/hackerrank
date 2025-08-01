import pytest

from solutions.algorithms.between_two_sets import getTotalX

@pytest.mark.parametrize("a,b,expected", [([2,6],[24,36],2) , ([2,4],[16,32,96],3)],
ids=["TEST CASE 1", "TEST CASE 2"])

def test_gettotalx(a, b, expected):
    assert getTotalX(a, b) == expected