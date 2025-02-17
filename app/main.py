# app/main.py
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.middleware.logger import LoggingMiddleware
from app.routes.auth_routes import router as auth_router
from app.routes.threat_model_routes import router as threat_model_router
from app.routes.report_routes import router as report_router
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
Instrumentator().instrument(app).expose(app)


# Add logging middleware
app.add_middleware(LoggingMiddleware)

# Include API routers
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(threat_model_router, prefix="/api", tags=["threat_models"])
app.include_router(report_router, prefix="/api", tags=["reports"])

# Global exception handler example
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"message": "An internal error occurred", "details": str(exc)})

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)

