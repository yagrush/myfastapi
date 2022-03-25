import time
from typing import Dict

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html

version = "0.0.0"

app = FastAPI(
    title="my FastAPI",
    description="DockerとFastAPIで手軽にRESTAPIサーバを構築するサンプル。",
    version=version,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# NOTE: OpenAPI（Swagger仕様）のエントリー関数
@app.get("/docs", include_in_schema=False)
async def get_swagger_ui():
    return get_swagger_ui_html(openapi_url="/openapi.json", title=app.title + " - APIドキュメント")


@app.get(
    "/",
    response_model=Dict[str, str],
    tags=["root"],
    summary="このAPIの要約",
    description="このAPIの詳細",
    responses={200: {"xxx": "aaa"}},
    response_description="正常レスポンスの詳細",
)
async def root():
    return {"message": "Hello World"}


@app.middleware("http")
async def custom_middleware(req: Request, call_next):
    url = str(req.url).replace(str(req.base_url), "")
    start = time.time()
    response = await call_next(req)
    end = time.time()
    print(f"API:{url} 所要時間：{end-start}秒")
    return response


from api.v1 import v1_router as api_router

app.include_router(api_router)
