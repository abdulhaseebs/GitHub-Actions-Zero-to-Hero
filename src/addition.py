# app.py
# This is a test commit
# its an addition of numbers
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
