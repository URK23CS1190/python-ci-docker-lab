import sys
import os
sys.path.append(os.path.dirname(os.p[ath.dirname(_file_)]))
from app import add


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0