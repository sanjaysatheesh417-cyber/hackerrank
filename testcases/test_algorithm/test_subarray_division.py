import pytest

from solutions.algorithms.subarray_division import birthday

@pytest.mark.parametrize("s,d,m,expected",[([2,2,1,3,2],4,2,2),([1,2,1,3,2],3,2,2)
,([1,1,1,1,1,1],3,2,0),([4],4,1,1)], ids=["TESTCASE1","TESTCASE2","TESTCASE3","TESTCASE4"])

def test_birthday(s, d, m, expected):
    assert birthday(s, d, m) == expected