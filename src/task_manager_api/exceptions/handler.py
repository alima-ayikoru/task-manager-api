from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src.task_manager_api.exceptions.exceptions import ServiceError


def register_exception_handler(app: FastAPI):
    # Register a global exception handler for ServiceError
    @app.exception_handler(ServiceError)
    async def service_error_handler(request: Request, exc: ServiceError):
        return JSONResponse(
            status_code=int(exc.status_code),
            content={"detail": exc.message},
        )
