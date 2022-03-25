import json
from typing import Optional

from api.v1 import API_VERSION
from fastapi import APIRouter, Depends, FastAPI, Form
from pydantic import BaseModel, Field

router = APIRouter()
API_NAME = "user"


class ResponseModelGet(BaseModel):
    user_name: str = Field(
        ...,
        title="ユーザー名",
        description="""
        """,
    )
    age: int = Field(
        ...,
        title="ユーザーの年齢",
        description="""
        """,
    )


response_definition_get = {
    "response_model": ResponseModelGet,
    "responses": {
        200: {
            "model": ResponseModelGet,
            "description": "正常に処理された場合のレスポンス。",
        }
    },
    "summary": """
     パスパラメータuser_idで指定されたユーザーの名前と年齢を返すAPI。
    """,
    "description": """
    
    """,
    "tags": ["サンプルAPI"],
}


@router.get("/v%s/%s/{user_id}" % (API_VERSION, API_NAME), **response_definition_get)
async def user(
    user_id: str,
):
    return {
        "user_name": f"{user_id} 一郎さん",
        "age": 12,
    }


class ResponseModelPost(BaseModel):
    user_id: str = Field(
        ...,
        title="ユーザーID",
        description="""
        """,
    )


response_definition_post = {
    "response_model": ResponseModelPost,
    "responses": {
        200: {
            "model": ResponseModelPost,
            "description": "正常に処理された場合のレスポンス。",
        }
    },
    "summary": """
     パスパラメータuser_idで与えられた文字列をそのまま返すAPI。
    """,
    "description": """
    
    """,
    "tags": ["サンプルAPI"],
}


@router.post("/v%s/%s/{user_id}" % (API_VERSION, API_NAME), **response_definition_post)
async def user(
    # post_params: PostParamsModel = Depends(post_params_model),
    user_id: str,
):
    return {
        # "user_id": post_params.user_id,
        "user_id": user_id,
    }


# HTML <form>からsubmitされたパラメータを取得する場合
class PostParamsModel:
    user_id: str

    def __init__(
        self,
        **kwargs,
    ):
        self.kwargs = kwargs
        for k in kwargs:
            setattr(self, k, kwargs[k])


def post_params_model(
    user_id: str = Form(
        ...,  # 何らかの入力を必須と定義する
        description="""
        ユーザーID
        """,
    ),
):
    return PostParamsModel(
        user_id=user_id,
    )


response_definition_post_by_form = {
    "response_model": ResponseModelPost,
    "responses": {
        200: {
            "model": ResponseModelPost,
            "description": "正常に処理された場合のレスポンス。",
        }
    },
    "summary": """
     POSTパラメータuser_idで与えられた文字列をそのまま返すAPI。
    """,
    "description": """
    
    """,
    "tags": ["サンプルAPI"],
}


@router.post("/v%s/%s" % (API_VERSION, API_NAME), **response_definition_post_by_form)
async def user(
    post_params: PostParamsModel = Depends(post_params_model),
):
    return {
        "user_id": post_params.user_id,
    }
