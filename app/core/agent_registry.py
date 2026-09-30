from typing import Any, Awaitable, Callable


Agent = Callable[[dict[str, Any]], Awaitable[Any]]


class AgentRegistry:
    """Registro central de agentes de NEXO OS."""

    def __init__(self) -> None:
        self._agents: dict[str, Agent] = {}

    def register(self, name: str, agent: Agent) -> None:
        if not name.strip():
            raise ValueError("El nombre del agente no puede estar vacío.")

        self._agents[name] = agent

    def unregister(self, name: str) -> None:
        self._agents.pop(name, None)

    def get(self, name: str) -> Agent | None:
        return self._agents.get(name)

    def exists(self, name: str) -> bool:
        return name in self._agents

    def list_agents(self) -> list[str]:
        return list(self._agents.keys())


agent_registry = AgentRegistry()
