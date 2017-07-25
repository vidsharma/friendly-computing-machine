"""
Testing for the nath.py module
"""

import friendly_computing_machine as fcm
import pytest

def test_add():
    assert fcm.math.add(5, 2) == 7
    assert fcm.math.add(2, 5) == 7
    assert fcm.math.add(1, 2) == 3

def test_mult():
    assert fcm.math.mult(2, 5) == 10 
