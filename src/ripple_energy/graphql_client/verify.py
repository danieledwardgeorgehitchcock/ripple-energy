from typing import Any, Optional

from pydantic import Field

from .base_model import BaseModel


class Verify(BaseModel):
    verify_token: Optional["VerifyVerifyToken"] = Field(alias="verifyToken")


class VerifyVerifyToken(BaseModel):
    payload: Any


Verify.model_rebuild()
VerifyVerifyToken.model_rebuild()
