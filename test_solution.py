import pytest
import solution

def test_basic():
    class Static():
        out = ''
    def o(v):
        Static.out = v
    i = iter(['5', '4 -1 2 3 1'])
    solution.input = lambda: next(i)
    solution.print = o
    solution.golf()
    assert Static.out == 1

def test_basic2():
    class Static():
        out = ''
    def o(v):
        Static.out = v
    i = iter(['5', '4 -1 2 3 1'])
    solution.input = lambda: next(i)
    solution.print = o
    solution.golf2()
    assert Static.out == 1