from fastapi import FastAPI

app = FastAPI(title="NEXO OS")


@app.get("/")
def root():
    return {
        "name": "NEXO OS",
        "status": "online"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
