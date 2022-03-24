from typing import Optional

from fastapi import APIRouter, Query, Request
from pydantic import BaseModel, Field

router = APIRouter()
API_NAME = "returnParameter"


class ResponseReturnParameter(BaseModel):
    path_param: str = Field(
        ...,
        title="パスパラメータ",
        description="""
        パスパラメータ path_param で指定された文字列をそのまま返す。
        """,
        example="hoge",
    )
    query_param: str = Field(
        None,
        title="クエリパラメータ",
        description="""
        クエリパラメータ query_param で指定された文字列をそのまま返す。
        指定がない場合は null を返す。
        """,
        example="foobar",
    )

    class Config:
        schema_extra = {
            "example": {
                "path_param": "hoge",
                "query_param": "foobar",
            }
        }


response_definition = {
    "response_model": ResponseReturnParameter,
    "responses": {
        200: {
            "model": ResponseReturnParameter,
            "description": "正常に処理された場合のレスポンス。",
        }
    },
    "summary": """
    パラメータで与えられた文字列をそのまま返すAPI。
    """,
    "description": """
    パラメータで与えられた文字列をそのまま返します。
    パスパラメータ path_param と クエリパラメータ query_param に対応。
    
    例） http://localhost:8000/returnParameter/hoge?query_param=foobar
     > {"path_param":"hoge","query_param":"foobar"}
    """,
    "tags": ["サンプルAPI"],
}


@router.get("/%s/{path_param}" % API_NAME, **response_definition)
async def return_parameter(req: Request, path_param: str, query_param: Optional[str] = Query(None)):
    return {"path_param": path_param, "query_param": query_param}
