import pytest

from my_project.__main__ import app


def test_app_function_runs_without_error(capsys: pytest.CaptureFixture[str]) -> None:
    app()
    captured = capsys.readouterr()
    assert "The result of adding 3 and 5 is: 8" in captured.out
