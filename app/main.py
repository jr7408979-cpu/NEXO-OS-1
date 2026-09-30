from typing import Any

from fastapi import FastAPI

from app.core.ai_executor import ai_executor
from app.core.orchestrator import orchestrator
from app.core.boot_manager import BootManager
from app.integrations.discord import discord_service
from app.integrations.paypal import paypal_service
from app.integrations.telegram import telegram_service
from app.services.health import get_health_status
from app.services.language import detect_language
from app.services.self_healing import SelfHealing


app = FastAPI(title="NEXO OS")

boot_manager = BootManager()
self_healing = SelfHealing()

boot_result = boot_manager.start()


@app.get("/")
def root() -> dict[str, Any]:
    """Estado principal de NEXO OS."""
    return {
        "name": "NEXO OS",
        "status": boot_manager.status(),
        "boot": boot_result,
        "ai_available": orchestrator.ai_available,
    }


@app.get("/health")
def health() -> Any:
    """Estado de salud del sistema."""
    return get_health_status()


@app.get("/system/status")
def system_status() -> dict[str, Any]:
    """Estado general del sistema."""
    return {
        "status": boot_manager.status(),
        "boot": boot_result,
        "ai_available": orchestrator.ai_available,
    }


@app.get("/system/integrations")
def integrations_status() -> dict[str, Any]:
    """Estado de las integraciones principales."""
    return {
        "telegram": telegram_service.status(),
        "discord": discord_service.status(),
        "paypal": paypal_service.status(),
    }


@app.get("/system/ai")
def ai_status() -> dict[str, Any]:
    """Estado del sistema de IA."""
    return {
        "configured": orchestrator.ai_available,
        "available_models": [],
        "executor_ready": ai_executor is not None,
    }


@app.post("/language/detect")
def language_detect(text: str) -> dict[str, str]:
    """Detecta el idioma de un texto."""
    return {
        "language": detect_language(text),
    }


@app.post("/self-healing/check")
def self_healing_check(error: str) -> dict[str, Any]:
    """Ejecuta una comprobación de reparación automática."""
    result = self_healing.repair(error)

    return {
        "success": result.success,
        "action": result.action,
        "message": result.message,
    }
