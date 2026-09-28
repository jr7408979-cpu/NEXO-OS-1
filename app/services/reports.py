from dataclasses import dataclass


@dataclass
class UsageReport:
    tenant_id: str
    period: str
    messages: int
    users: int
    tokens: int


def create_report(
    tenant_id: str,
    period: str,
    messages: int = 0,
    users: int = 0,
    tokens: int = 0,
) -> UsageReport:
    return UsageReport(
        tenant_id=tenant_id,
        period=period,
        messages=messages,
        users=users,
        tokens=tokens,
    )
