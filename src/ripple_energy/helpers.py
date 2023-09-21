from datetime import datetime
from typing import Any

from pydantic import validate_call

from .constants import JWT_HEADER_PREFIX
from .exceptions import RippleEnergyTokenExpiredException


@validate_call
def generate_jwt_header(token: str | None = None) -> dict[str, str]:
    return {"Authorization": f"{JWT_HEADER_PREFIX}{token}"}


@validate_call
def check_date(date: datetime, auto_auth_deauth: bool) -> bool:
    expired = date < datetime.now()

    if expired and not auto_auth_deauth:
        raise RippleEnergyTokenExpiredException

    return expired


def check_expiry(function: Any):  # type: ignore
    """Ripple Energy decorator function to check JWT token expiry"""

    async def wrapper(*args, **kwargs):  # type: ignore
        if check_date(args[0].token_expires, args[0].auto_auth_deauth):
            await args[0].refresh_token()

        return await function(*args, **kwargs)

    return wrapper
