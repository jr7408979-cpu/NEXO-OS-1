import logging


LOGGER_NAME = "nexo"

logger = logging.getLogger(LOGGER_NAME)


def setup_logger() -> logging.Logger:
    """Configura y devuelve el logger principal de NEXO OS."""

    if not logger.handlers:
        handler = logging.StreamHandler()

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )

        handler.setFormatter(formatter)
        logger.addHandler(handler)

    logger.setLevel(logging.INFO)
    logger.propagate = False

    return logger
