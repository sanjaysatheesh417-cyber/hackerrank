import pytest

from solutions.algorithms.migratory_birds import migratoryBirds

@pytest.mark.parametrize("arr,expected", [([1,1,2,2,3],1),([1,4,4,4,5,3],4),
([1,2,3,4,5,4,3,2,1,3,4],3)], ids=["TESTCASE1", "TESTCASE2", "TESTCASE3"])

def test_migratoryBirds(arr, expected):
    assert migratoryBirds(arr) == expected