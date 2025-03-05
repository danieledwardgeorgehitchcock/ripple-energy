from typing import Any, Optional

from pydantic import Field

from .base_model import BaseModel


class VerifyToken(BaseModel):
    verify_token: Optional["VerifyTokenVerifyToken"] = Field(alias="verifyToken")


class VerifyTokenVerifyToken(BaseModel):
    payload: Any


VerifyToken.model_rebuild()
