from fastapi import APIRouter

from .api.getClientHost.endpoint import router as getClientHost
from .api.returnParameter.endpoint import router as returnParameter

router = APIRouter()
router.include_router(returnParameter)
router.include_router(getClientHost)
