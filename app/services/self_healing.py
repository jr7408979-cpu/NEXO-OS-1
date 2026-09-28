from dataclasses import dataclass


@dataclass
class RepairResult:
    success: bool
    action: str
    message: str


class SelfHealing:
    def diagnose(self, error: str) -> str:
        if not error:
            return "no_error"

        error_lower = error.lower()

        if "timeout" in error_lower:
            return "retry"

        if "connection" in error_lower:
            return "restart_connection"

        return "manual_review"

    def repair(self, error: str) -> RepairResult:
        diagnosis = self.diagnose(error)

        if diagnosis == "retry":
            return RepairResult(
                True,
                "safe_retry",
                "Safe retry recommended.",
            )

        if diagnosis == "restart_connection":
            return RepairResult(
                True,
                "restart_connection",
                "Connection restart recommended.",
            )

        if diagnosis == "no_error":
            return RepairResult(
                True,
                "none",
                "No error detected.",
            )

        return RepairResult(
            False,
            "manual_review",
            "Human review required.",
        )
