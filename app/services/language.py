SUPPORTED_LANGUAGES = {
    "es": "Español",
    "en": "English",
    "pt": "Português",
    "fr": "Français",
    "de": "Deutsch",
    "it": "Italiano",
    "zh": "中文",
    "ja": "日本語",
    "ko": "한국어",
    "ar": "العربية",
}


def detect_language(text: str) -> str:
    text = text.lower()

    spanish_words = {
        "hola", "gracias", "por", "para", "que", "como",
        "donde", "cuando", "quiero", "necesito"
    }

    if any(word in text.split() for word in spanish_words):
        return "es"

    return "en"
