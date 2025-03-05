from typing import Any, Optional

from pydantic import Field

from .base_model import BaseModel


class RefreshToken(BaseModel):
    refresh_token: Optional["RefreshTokenRefreshToken"] = Field(alias="refreshToken")


class RefreshTokenRefreshToken(BaseModel):
    payload: Any
    refresh_expires_in: int = Field(alias="refreshExpiresIn")
    token: str


RefreshToken.model_rebuild()
