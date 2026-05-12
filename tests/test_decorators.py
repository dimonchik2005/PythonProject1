from pathlib import Path

import pytest

from src.decorators import log


def test_log_console_success(capsys: pytest.CaptureFixture[str]) -> None:
    @log()
    def add(x: int, y: int) -> int:
        return x + y

    result = add(1, 2)
    captured = capsys.readouterr()

    assert result == 3
    assert "add ok" in captured.out


def test_log_console_error(capsys: pytest.CaptureFixture[str]) -> None:
    @log()
    def divide(x: int, y: int) -> float:
        return x / y

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    captured = capsys.readouterr()

    assert "divide error: ZeroDivisionError" in captured.out
    assert "Inputs: (1, 0), {}" in captured.out


def test_log_file_success(tmp_path: Path) -> None:
    log_file = tmp_path / "test_log.txt"

    @log(filename=str(log_file))
    def multiply(x: int, y: int) -> int:
        return x * y

    result = multiply(2, 3)

    assert result == 6
    assert "multiply ok" in log_file.read_text(encoding="utf-8")


def test_log_file_error(tmp_path: Path) -> None:
    log_file = tmp_path / "test_log.txt"

    @log(filename=str(log_file))
    def broken_function() -> None:
        raise ValueError("Test error")

    with pytest.raises(ValueError):
        broken_function()

    content = log_file.read_text(encoding="utf-8")

    assert "broken_function error: ValueError" in content
    assert "Inputs: (), {}" in content
