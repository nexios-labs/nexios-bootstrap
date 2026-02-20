from nexios import NexiosApp
from nexios.middleware.cors import CORSMiddleware, CorsConfig
from src.core.middleware.logging import LoggingMiddleware
from src.core.database import init_db, close_db
from src.api.health.router import router as health_router

app = NexiosApp(
    title="Nexios Starter",
    description="A clean, modular Nexios starter template with scalable structure, API versioning, and Docker support.",
    version="0.1.0",
)

# Setup CORS
app.add_middleware(CORSMiddleware(config=CorsConfig(allow_origins=["*"])))

# Setup Logging Middleware
app.add_middleware(LoggingMiddleware())

# Include routers
app.mount_router(health_router)

# Setup TortoiseORM
app.on_startup(init_db)
app.on_shutdown(close_db)
