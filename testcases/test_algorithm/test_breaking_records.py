import pytest

from solutions.algorithms.breaking_records import breakingRecords

@pytest.mark.parametrize("scores,expected",[([10,5,20,20,4,5,2,25,1],[2,4])
,([3,4,21,36,10,28,35,5,24,42],[4,0])] ,ids=["TESTCASE1","TESTCASE2"])

def test_breakingrecords(scores,expected):
    assert breakingRecords(scores) == expected