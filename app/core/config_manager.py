import os


class ConfigManager:
    def get(self, key: str, default=None):
        return os.getenv(key, default)

    def get_bool(self, key: str, default: bool = False) -> bool:
        value = self.get(key)

        if value is None:
            return default

        return value.lower() in {"true", "1", "yes", "on"}
