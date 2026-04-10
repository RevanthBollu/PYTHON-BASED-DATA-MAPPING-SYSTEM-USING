import numpy as np

def test_deviation():

    y_test = 10
    y_ideal = 8

    deviation = abs(y_test - y_ideal)

    assert deviation == 2