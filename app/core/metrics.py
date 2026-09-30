from dataclasses import dataclass, field


@dataclass
class SystemMetrics:
    """Métricas principales de NEXO OS."""

    requests: int = 0
    errors: int = 0
    active_services: int = 0
    counters: dict[str, int] = field(default_factory=dict)

    def record_request(self) -> None:
        """Registra una solicitud."""
        self.requests += 1

    def record_error(self) -> None:
        """Registra un error."""
        self.errors += 1

    def set_active_services(self, count: int) -> None:
        """Actualiza el número de servicios activos."""
        if count < 0:
            raise ValueError("El número de servicios no puede ser negativo.")

        self.active_services = count

    def increment(self, name: str, amount: int = 1) -> None:
        """Incrementa un contador personalizado."""
        if not name.strip():
            raise ValueError("El nombre de la métrica no puede estar vacío.")

        if amount < 1:
            raise ValueError("El incremento debe ser mayor que cero.")

        self.counters[name] = self.counters.get(name, 0) + amount

    def get(self, name: str) -> int:
        """Obtiene el valor de un contador personalizado."""
        return self.counters.get(name, 0)

    def snapshot(self) -> dict[str, object]:
        """Devuelve una copia de las métricas actuales."""
        return {
            "requests": self.requests,
            "errors": self.errors,
            "active_services": self.active_services,
            "counters": dict(self.counters),
        }
