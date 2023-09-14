from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class TokenAuth(BaseModel):
    token_auth: "TokenAuthTokenAuth" = Field(alias="tokenAuth")


class TokenAuthTokenAuth(BaseModel):
    token: Optional[str]


TokenAuth.update_forward_refs()
TokenAuthTokenAuth.update_forward_refs()
