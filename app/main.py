from fastapi import FastAPI
from core.boot import BootManager
from services.health import get_health_status
from services.language import detect_language
from services.self_healing import SelfHealing


app = FastAPI(title="NEXO OS")

self_healing = SelfHealing()


@app.get("/")
def root():
    return {
        "name": "NEXO OS",
        "status": "online",
    }


@app.get("/health")
def health():
    return get_health_status()


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
