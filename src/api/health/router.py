from datetime import datetime, timezone
from nexios.routing import Router
from nexios.http import Request, Response
from .schemas import HealthResponse, HealthCheckRequest
from utils.counting import count_numbers_lazy

router = Router(prefix="/health", tags=["Health-Check"])


@router.get(
    "/",
    summary="Application Health Status",
    description="Checks the availability and operational status of the application. "
                "Used for monitoring, Docker health checks, and load balancer verification.",
    response_model=HealthResponse
)
async def get_health(request: Request, response: Response):

    response.set_header("X-Service-Status", "healthy")
    response.set_header("Cache-Control", "no-store")

    return HealthResponse(
        status="ok",
        service="nexios-starter",
        timestamp=datetime.now(timezone.utc),
        version="0.1.0"
    )


@router.post(
    "/",
    summary="Submit Health Check",
    description="Accepts health check requests with optional parameters for customized responses.",
    request_model=HealthCheckRequest,
    response_model=HealthResponse
)
async def post_health(request: Request, response: Response):
    json_data = await request.json
    body = HealthCheckRequest(**json_data)    
    service_name = body.service_name or "nexios-starter"
    
    # Perform async counting using AsyncLazy
    start_num = body.start_number or 1
    end_num = body.end_number or 10
    step_size = body.step or 1
    
    # Use AsyncLazy for lazy evaluation and concurrency
    lazy_count = count_numbers_lazy(start_num, end_num, step_size)
    counted_numbers = await lazy_count
    
    health_data = {
        "status": "ok",
        "service": service_name,
        "timestamp": datetime.now(timezone.utc),
        "version": "0.1.0"
    }
    
    if body.include_details:
        health_data["check_type"] = body.check_type
        health_data["counting_result"] = {
            "start": start_num,
            "end": end_num,
            "step": step_size,
            "numbers": counted_numbers,
            "total_count": len(counted_numbers)
        }
        health_data["details"] = {
            "database": "connected",
            "cache": "available",
            "external_apis": "responsive"
        }
    
    return HealthResponse(**health_data)
