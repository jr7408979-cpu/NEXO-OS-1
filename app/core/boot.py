from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class BootStep:
    name: str
    status: str = "pending"
    message: str = ""


@dataclass
class BootResult:
    success: bool
    status: str
    started_at: str
    completed_at: str | None
    steps: list[BootStep] = field(default_factory=list)


class BootManager:
    def __init__(self):
        self.steps = [
            BootStep("configuration"),
            BootStep("core"),
            BootStep("database"),
            BootStep("event_bus"),
            BootStep("health"),
            BootStep("security"),
            BootStep("discord"),
        ]

    def _run_step(self, step: BootStep):
        step.status = "ready"
        step.message = f"{step.name} initialized."

    def start(self) -> BootResult:
        started_at = datetime.now(timezone.utc).isoformat()

        for step in self.steps:
            try:
                self._run_step(step)
            except Exception as error:
                step.status = "failed"
                step.message = str(error)

                return BootResult(
                    success=False,
                    status="boot_failed",
                    started_at=started_at,
                    completed_at=datetime.now(timezone.utc).isoformat(),
                    steps=self.steps,
                )

        return BootResult(
            success=True,
            status="ready",
            started_at=started_at,
            completed_at=datetime.now(timezone.utc).isoformat(),
            steps=self.steps,
        )
