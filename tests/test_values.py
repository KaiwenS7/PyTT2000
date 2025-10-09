import pytest

from PyTT2000.tt2k import unixTott2k


def test_answer():
    assert unixTott2k(1760042158,0) == 813314227184000000
    assert unixTott2k(1760042158,99) == 813314227184099000

def test_fail():
    with pytest.raises(ValueError) as excinfo:
        unixTott2k(-100, -100)
        print(excinfo)