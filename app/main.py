from fastapi import FastAPI

from core.boot_manager import BootManager
from services.health import get_health_status
from services.language import detect_language
from services.self_healing import SelfHealing


app = FastAPI(title="NEXO OS")

boot_manager = BootManager()
self_healing = SelfHealing()

boot_result = boot_manager.start()


@app.get("/")
def root():
    return {
        "name": "NEXO OS",
        "status": boot_manager.status(),
        "boot": boot_result,
    }


@app.get("/health")
def health():
    return get_health_status()


@app.get("/system/status")
def system_status():
    return {
        "status": boot_manager.status(),
        "boot": boot_result,
    }


@app.post("/language/detect")
def language_detect(text: str):
    return {
        "language": detect_language(text),
    }


@app.post("/self-healing/check")
def self_healing_check(error: str):
    result = self_healing.repair(error)

    return {
        "success": result.success,
        "action": result.action,
        "message": result.message,
    }
