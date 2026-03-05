import pytest

def sqr(m):
    return m**2
def cube(n):
    return n**3
def test_sqr():
    assert sqr(4) == 16
    assert sqr(5) == 25
def test_cube():
    assert cube(3) == 27
def test_invalid_input():
    with pytest.raises(TypeError):
        sqr("string")