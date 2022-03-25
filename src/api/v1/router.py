from fastapi import APIRouter

from .user import user

router = APIRouter()
router.include_router(user)
