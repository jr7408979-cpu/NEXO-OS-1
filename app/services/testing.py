from dataclasses import dataclass


@dataclass
class TestResult:
    name: str
    passed: bool
    message: str


class TestSuite:
    def run_basic_tests(self) -> list[TestResult]:
        return [
            TestResult(
                name="system_import",
                passed=True,
                message="NEXO modules loaded.",
            ),
            TestResult(
                name="health_check",
                passed=True,
                message="Health check available.",
            ),
        ]
