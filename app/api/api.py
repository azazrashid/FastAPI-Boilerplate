from fastapi import APIRouter

from app.api.endpoints import health
from app.api.endpoints import users


router = APIRouter()


router.include_router(health.health_router, prefix="/health")
router.include_router(users.user_router, prefix="/users")
