import pytest

from my_project.calculator import add, divide, divide2, multiply, subtract


class TestAdd:
    @pytest.mark.parametrize(
        ("a", "b", "expected"),
        [
            pytest.param(1, 2, 3, id="positive integers"),
            pytest.param(-1, 1, 0, id="negative and positive"),
            pytest.param(0, 0, 0, id="zeros"),
            pytest.param(2.5, 2.5, 5.0, id="floats"),
        ],
    )
    def test_add(self, a: float, b: float, expected: float) -> None:
        assert add(a, b) == expected


class TestSubtract:
    @pytest.mark.parametrize(
        ("a", "b", "expected"),
        [
            pytest.param(5, 3, 2, id="positive integers"),
            pytest.param(0, 1, -1, id="zero and positive"),
            pytest.param(-1, -1, 0, id="negative integers"),
            pytest.param(2.5, 1.5, 1.0, id="floats"),
        ],
    )
    def test_subtract(self, a: float, b: float, expected: float) -> None:
        assert subtract(a, b) == expected


class TestMultiply:
    @pytest.mark.parametrize(
        ("a", "b", "expected"),
        [
            pytest.param(2, 3, 6, id="positive integers"),
            pytest.param(-1, 1, -1, id="negative and positive"),
            pytest.param(0, 5, 0, id="zero"),
            pytest.param(2.0, 3.5, 7.0, id="floats"),
        ],
    )
    def test_multiply(self, a: float, b: float, expected: float) -> None:
        assert multiply(a, b) == expected


class TestDivide:
    @pytest.mark.parametrize(
        ("a", "b", "expected"),
        [
            pytest.param(6, 3, 2.0, id="positive integers"),
            pytest.param(-4, 2, -2.0, id="negative and positive"),
            pytest.param(5.0, 2.0, 2.5, id="floats"),
        ],
    )
    def test_divide(self, a: float, b: float, expected: float) -> None:
        assert divide(a, b) == expected

    @pytest.mark.parametrize(
        ("a", "b"),
        [
            pytest.param(5, 0, id="division by zero"),
            pytest.param(0, 0, id="zero division"),
        ],
    )
    def test_divide_by_zero(self, a: float, b: float) -> None:
        with pytest.raises(ValueError, match="Cannot divide by zero."):
            divide(a, b)


class TestDevide2:
    @pytest.mark.parametrize(
        ("a", "b", "expected"),
        [
            pytest.param(7, 3, (2, 1), id="positive integers"),
            pytest.param(10, 2, (5, 0), id="even division"),
            pytest.param(5, 2, (2, 1), id="odd division"),
        ],
    )
    def test_divide2(self, a: int, b: int, expected: tuple[int, int]) -> None:
        assert divide2(a, b) == expected

    @pytest.mark.parametrize(
        ("a", "b"),
        [
            pytest.param(5, 0, id="division by zero"),
            pytest.param(0, 0, id="zero division"),
        ],
    )
    def test_divide2_by_zero(self, a: int, b: int) -> None:
        with pytest.raises(ValueError, match="Cannot divide by zero."):
            divide2(a, b)
