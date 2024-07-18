from hello import add_nos, subtract_nos


def test_add_nos():
    assert add_nos(1, 2, 3) == 6

def test_subtract_nos():
    assert subtract_nos(1,2,3) == -4
