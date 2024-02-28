from main import convert, gauge
import pytest

def test_f():
    assert gauge(100) == "F"
    assert gauge(99) == "F"
def test_e():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
def test_procent_gauge():
    assert gauge(25.00) == "25.0 %"
    assert gauge(10.00) == "10.0 %"
    assert gauge(50.00) == "50.0 %"
    assert gauge(70.00) == "70.0 %"
    assert gauge(40.00) == "40.0 %"
def test_procent():
    assert convert("1/4") == 25.00
    assert convert("1/10") == 10.00
    assert convert("2/4") == 50.00
    assert convert("70/100") == 70.00
    assert convert("2/5") == 40.00
def test_errors():
    with pytest.raises(ValueError):
        assert convert("12/10") is ValueError
    with pytest.raises(ValueError):
        assert convert("1231/1") is ValueError
    with pytest.raises(ValueError):
        assert convert("9/-8") is ValueError
    with pytest.raises(ZeroDivisionError):
        assert convert("31/0") is ZeroDivisionError
    with pytest.raises(ZeroDivisionError):
        assert convert("0/0") is ZeroDivisionError   
