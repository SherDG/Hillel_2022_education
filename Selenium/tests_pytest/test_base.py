def test_first_ever_check():
    assert 5 + 5 == 10

def test_second():
    assert 5 + 5 == 11

def test_third():
    assert 9//5 == 1


def increment(x):
    return x + 1


def test_answer():
    assert increment(4) == 5