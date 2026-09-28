import hashlib
import hmac
import os


def verify_hmac(payload: bytes, signature: str) -> bool:
    secret = os.getenv("NEXO_WEBHOOK_SECRET", "")

    if not secret or not signature:
        return False

    expected = hmac.new(
        secret.encode(),
        payload,
        hashlib.sha256,
    ).hexdigest()

    return hmac.compare_digest(expected, signature)
