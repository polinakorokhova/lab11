import math
import pytest
from lab11_1 import multiply, divide, distance, solve_quadratic, geometric_sum

# Корохова Полина 107В1


def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
    assert multiply(0, 100) == 0


def test_divide():
    assert divide(10, 2) == 5
    with pytest.raises(ValueError):
        divide(10, 0)


def test_distance():
    assert math.isclose(distance(0, 0, 3, 4), 5, rel_tol=1e-9)
    assert math.isclose(distance(1, 1, 4, 5), 5, rel_tol=1e-9)


def test_solve_quadratic():
    assert solve_quadratic(1, -3, 2) == (2.0, 1.0)
    assert solve_quadratic(1, 2, 1) == (-1.0,)
    assert solve_quadratic(1, 0, 1) is None


def test_geometric_sum():
    assert geometric_sum(1, 2, 3) == 7  # 1 + 2 + 4
    assert geometric_sum(1, 1, 3) == 3
