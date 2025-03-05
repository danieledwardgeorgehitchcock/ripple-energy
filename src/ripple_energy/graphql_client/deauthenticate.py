from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class Deauthenticate(BaseModel):
    auth_logout_session: Optional["DeauthenticateAuthLogoutSession"] = Field(
        alias="authLogoutSession"
    )
    delete_token_cookie: Optional["DeauthenticateDeleteTokenCookie"] = Field(
        alias="deleteTokenCookie"
    )
    delete_refresh_token_cookie: Optional["DeauthenticateDeleteRefreshTokenCookie"] = (
        Field(alias="deleteRefreshTokenCookie")
    )


class DeauthenticateAuthLogoutSession(BaseModel):
    logout_successful: Optional[bool] = Field(alias="logoutSuccessful")


class DeauthenticateDeleteTokenCookie(BaseModel):
    deleted: bool


class DeauthenticateDeleteRefreshTokenCookie(BaseModel):
    deleted: bool


Deauthenticate.model_rebuild()
