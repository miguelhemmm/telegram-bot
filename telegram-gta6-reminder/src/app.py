"""Daily GTA 6 countdown reminder sent to a Telegram chat.

Triggered by an EventBridge schedule (see template.yaml).
Configuration comes from environment variables:
  TELEGRAM_TOKEN  - bot token from @BotFather
  CHAT_ID         - target chat/group id
"""

import json
import os
import urllib.error
import urllib.request
from datetime import date, datetime, timedelta, timezone
from quotes import random_quote

RELEASE_DATE = date(2026, 11, 19)

# Mexico City has had no DST since 2022, so a fixed UTC-6 offset is correct
# and avoids depending on tzdata being present in the Lambda runtime.
MX_TZ = timezone(timedelta(hours=-6), name="America/Mexico_City")


def build_message(today: date) -> str:
    """Countdown headline for a given date + a random quote (quotes.py)."""
    days_left = (RELEASE_DATE - today).days

    if days_left > 1:
        headline = f"🎮 Faltan {days_left} días para GTA 6 🚔"
    elif days_left == 1:
        headline = "🎮 ¡Falta 1 día para GTA 6! 🚔🔥"
    elif days_left == 0:
        headline = "🎮🎉 ¡HOY SALE GTA 6! 🚔🔥💥"
    else:
        headline = f"🎮 GTA 6 salió hace {abs(days_left)} días. ¿Ya lo jugaste? 🚔"

    return f"{headline}\n\n{random_quote()}"


def _require_env(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


def send_telegram_message(text: str) -> dict:
    token = _require_env("TELEGRAM_TOKEN")
    chat_id = _require_env("CHAT_ID")

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = json.dumps(
        {"chat_id": chat_id, "text": text, "parse_mode": "HTML"}
    ).encode("utf-8")
    req = urllib.request.Request(
        url, data=payload, headers={"Content-Type": "application/json"}
    )

    try:
        with urllib.request.urlopen(req, timeout=8) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as err:
        body = err.read().decode("utf-8", errors="replace")
        # Re-raise so the Lambda invocation is marked as failed in CloudWatch.
        raise RuntimeError(f"Telegram API error {err.code}: {body}") from err


def lambda_handler(event, context):
    today_mx = datetime.now(MX_TZ).date()
    text = build_message(today_mx)

    result = send_telegram_message(text)
    print(f"Mensaje enviado: {json.dumps(result)}")

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "success": True,
                "dias_faltantes": (RELEASE_DATE - today_mx).days,
            }
        ),
    }
