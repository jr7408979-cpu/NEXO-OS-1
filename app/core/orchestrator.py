from typing import Any, Awaitable, Callable

from app.core.ai import ai_client


Agent = Callable[[dict[str, Any]], Awaitable[Any]]


class AIOrchestrator:
    """Orquestador central de los agentes de IA de NEXO OS."""

    def __init__(self) -> None:
        self._agents: dict[str, Agent] = {}

    def register_agent(self, name: str, agent: Agent) -> None:
        """Registra un agente."""
        if not name.strip():
            raise ValueError("El nombre del agente no puede estar vacío.")

        self._agents[name] = agent

    def unregister_agent(self, name: str) -> None:
        """Elimina un agente."""
        self._agents.pop(name, None)

    def list_agents(self) -> list[str]:
        """Lista los agentes registrados."""
        return list(self._agents.keys())

    async def run_agent(
        self,
        name: str,
        context: dict[str, Any],
    ) -> Any:
        """Ejecuta un agente específico."""
        agent = self._agents.get(name)

        if agent is None:
            raise ValueError(f"Agente no registrado: {name}")

        return await agent(context)

    async def run_all(
        self,
        context: dict[str, Any],
    ) -> dict[str, Any]:
        """Ejecuta todos los agentes registrados."""
        results: dict[str, Any] = {}

        for name, agent in self._agents.items():
            try:
                results[name] = await agent(context)
            except Exception as exc:
                results[name] = {
                    "success": False,
                    "error": str(exc),
                }

        return results

    @property
    def ai_available(self) -> bool:
        """Indica si NEXO OS tiene una API de IA configurada."""
        return ai_client.configured


orchestrator = AIOrchestrator()
