from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class Authenticate(BaseModel):
    token_auth: "AuthenticateTokenAuth" = Field(alias="tokenAuth")


class AuthenticateTokenAuth(BaseModel):
    token: Optional[str]


Authenticate.model_rebuild()
