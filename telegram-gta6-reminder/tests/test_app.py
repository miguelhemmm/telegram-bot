import sys
from datetime import date
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import app  # noqa: E402


def test_many_days_left():
    msg = app.build_message(date(2026, 11, 9))
    assert "Faltan 10 días" in msg
    assert "09/11/2026" in msg


def test_one_day_left():
    msg = app.build_message(date(2026, 11, 18))
    assert "Falta 1 día" in msg


def test_release_day():
    msg = app.build_message(date(2026, 11, 19))
    assert "HOY SALE GTA 6" in msg


def test_after_release():
    msg = app.build_message(date(2026, 11, 22))
    assert "salió hace 3 días" in msg


def test_missing_env_raises(monkeypatch):
    monkeypatch.delenv("TELEGRAM_TOKEN", raising=False)
    monkeypatch.delenv("CHAT_ID", raising=False)
    with pytest.raises(RuntimeError, match="TELEGRAM_TOKEN"):
        app.send_telegram_message("hola")
