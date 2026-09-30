from typing import Any

from app.core.ai import ai_client
from app.core.ai_router import ai_router


class AIExecutor:
    """Ejecuta solicitudes de IA usando el modelo seleccionado."""

    async def execute(
        self,
        model_name: str,
        payload: dict[str, Any],
    ) -> dict[str, Any]:
        """Envía una solicitud al proveedor seleccionado."""

        selected = ai_router.select_model(model_name)

        model = selected["model"]
        provider = selected["provider"]

        url = provider["base_url"].rstrip("/") + "/chat/completions"

        request_payload = {
            "model": model["model_id"],
            **payload,
        }

        return await ai_client.request(
            url=url,
            payload=request_payload,
        )


ai_executor = AIExecutor()
