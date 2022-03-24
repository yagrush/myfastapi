from fastapi import APIRouter, Request

router = APIRouter()
API_NAME = "getClientHost"


@router.get(f"/{API_NAME}", tags=["サンプルAPI"])
async def get_client_host(req: Request):
    ret_val = req.client.host
    return {"result": ret_val}
