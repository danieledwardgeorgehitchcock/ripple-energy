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


class DeauthenticateAuthLogoutSession(BaseModel):
    logout_successful: Optional[bool] = Field(alias="logoutSuccessful")


class DeauthenticateDeleteTokenCookie(BaseModel):
    deleted: bool


Deauthenticate.model_rebuild()
DeauthenticateAuthLogoutSession.model_rebuild()
DeauthenticateDeleteTokenCookie.model_rebuild()
