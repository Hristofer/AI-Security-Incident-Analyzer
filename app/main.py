from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(
    title="AI Security Incident Analyzer",
    description="Analyze security logs with AI to detect threats and generate incident reports.",
    version="1.0.0",
)


@app.get("/")
async def home():
    return {
        "application": "AI Security Incident Analyzer",
        "status": "running",
        "version": "1.0.0",
        "author": "Hristofer",
    }


@app.get("/health")
async def health():
    return JSONResponse(
        status_code=200,
        content={
            "status": "healthy",
            "api": True,
            "database": False,
            "ai": False,
        },
    )
