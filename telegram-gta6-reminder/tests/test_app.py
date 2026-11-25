import sys
from datetime import date
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import app  # noqa: E402
import gta_tips  # noqa: E402


def test_many_days_left():
    msg = app.build_message(date(2026, 11, 9))
    assert "Faltan 10 días" in msg


def test_message_has_headline_quote_and_tip():
    headline, quote, tip = app.build_message(date(2026, 11, 9)).split("\n\n")
    assert headline.startswith("🎮")
    assert any(q[0] in quote for q in app.random_quote.__globals__["QUOTES"])
    assert tip.startswith("💡 Tip GTA 6: ")
    assert tip.removeprefix("💡 Tip GTA 6: ").removesuffix(".") in gta_tips.TIPS


def test_tips_shape_and_no_repeat():
    assert gta_tips.TIPS
    assert len(set(gta_tips.TIPS)) == len(gta_tips.TIPS), "duplicate tip"
    assert all(not t.endswith((".", "!", "?")) for t in gta_tips.TIPS)
    prev = gta_tips.random_tip()
    for _ in range(20):
        cur = gta_tips.random_tip()
        assert cur != prev
        prev = cur


def test_message_is_html_safe(monkeypatch):
    monkeypatch.setattr(app, "random_tip", lambda: "a < b & c")
    assert "a &lt; b &amp; c" in app.build_message(date(2026, 11, 9))


def test_day_after_release():
    assert "salió ayer" in app.build_message(date(2026, 11, 20))


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
