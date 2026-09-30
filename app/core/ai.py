import os
from typing import Any, Optional

import httpx


class AIClient:
    """Cliente base para conectar NEXO OS con un proveedor de IA."""

    def __init__(self) -> None:
        self.api_key = os.getenv("AI_API_KEY", "").strip()

    @property
    def configured(self) -> bool:
        """Indica si existe una clave de API configurada."""
        return bool(self.api_key)

    async def request(
        self,
        url: str,
        payload: dict[str, Any],
        headers: Optional[dict[str, str]] = None,
        timeout: float = 30.0,
    ) -> dict[str, Any]:
        """Envía una solicitud al proveedor de IA."""

        if not self.configured:
            raise RuntimeError("AI_API_KEY no está configurada.")

        request_headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        if headers:
            request_headers.update(headers)

        async with httpx.AsyncClient(timeout=timeout) as client:
            response = await client.post(
                url,
                json=payload,
                headers=request_headers,
            )

        response.raise_for_status()
        return response.json()


ai_client = AIClient()
