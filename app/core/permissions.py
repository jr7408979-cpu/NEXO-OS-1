from enum import IntEnum


class AuthorityLevel(IntEnum):
    OBSERVE = 1
    SAFE_REPAIR = 2
    APPROVAL_REQUIRED = 3
    CRITICAL = 4


class PermissionManager:
    def __init__(self):
        self.level = AuthorityLevel.OBSERVE

    def set_level(self, level: AuthorityLevel):
        self.level = level

    def can_execute(self, required_level: AuthorityLevel) -> bool:
        return self.level >= required_level
