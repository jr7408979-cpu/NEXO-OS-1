import re


def sanitize_text(text: str) -> str:
    if not text:
        return ""

    text = text.replace("\x00", "")
    return text.strip()


def is_safe_text(text: str) -> bool:
    if not text:
        return True

    suspicious_patterns = [
        r"<script",
        r"javascript:",
        r"drop\s+table",
        r"union\s+select",
    ]

    return not any(
        re.search(pattern, text, re.IGNORECASE)
        for pattern in suspicious_patterns
    )
