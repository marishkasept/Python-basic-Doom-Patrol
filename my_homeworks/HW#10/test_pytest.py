import pytest
import functions_pytest as fp
import functions_for_testing as fft

def test_season():
    assert fp.season('snow') == 'winter'
    assert fp.season('sun') == 'summer'
    assert fp.season('asdasdsa') is None

def test_range_list():
    assert 6 in fp.range_list(5, 10)
    assert 150 in fp.range_list(10, 200)
    assert 1500 in fp.range_list(10, 2000)

def test_div():
    try:
        fft.div(5, 0)
    except ZeroDivisionError:
        assert fft.div(1, 1) == 1
    assert fft.div(10, 5) == 2
    assert fft.div(7, 20) == 0.35
    assert fft.div(21, 2) == 10.5
