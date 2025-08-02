import pytest

from solutions.algorithms.divisible_sum_pairs import divisibleSumPairs

@pytest.mark.parametrize('n,k,ar,expected', [(6,5,[1,2,3,4,5,6],3),(6,3,[1,3,2,6,1,2],5)],
ids=["TESTCASE1","TESTCASE2"])

def test_divisible_sum_pairs(n, k, ar, expected):
    assert divisibleSumPairs(n, k, ar) == expected