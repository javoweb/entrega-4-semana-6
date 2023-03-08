from fastapi import APIRouter
from .orden.router import router as order_router

router = APIRouter()
router.include_router(order_router, prefix="/orden", tags=["Order"])
