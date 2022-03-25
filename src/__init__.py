from api.v1 import v1_router as api_router
from prog import app

app.include_router(api_router)
