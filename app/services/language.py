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


SPANISH_WORDS = {
    "hola",
    "gracias",
    "por",
    "para",
    "que",
    "como",
    "donde",
    "cuando",
    "quiero",
    "necesito",
    "buenos",
    "buenas",
    "estoy",
    "puedo",
}


def detect_language(text: str) -> str:
    """Detecta el idioma básico de un texto."""

    if not isinstance(text, str):
        raise TypeError("El texto debe ser una cadena.")

    cleaned_text = text.lower().strip()

    if not cleaned_text:
        return "en"

    words = set(cleaned_text.split())

    if words.intersection(SPANISH_WORDS):
        return "es"

    return "en"


def get_supported_languages() -> dict[str, str]:
    """Devuelve los idiomas compatibles."""

    return SUPPORTED_LANGUAGES.copy()


def is_supported(language: str) -> bool:
    """Comprueba si un idioma está soportado."""

    return language.lower().strip() in SUPPORTED_LANGUAGES
