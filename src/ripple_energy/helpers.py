from .exceptions import RippleEnergyTokenExpiredException
from .constants import JWT_HEADER_PREFIX
from datetime import datetime
from pydantic import validate_call


@validate_call
def generate_jwt_header(token: str | None = None) -> dict[str, str]:
    return {"Authorization": f"{JWT_HEADER_PREFIX}{token}"}


@validate_call
def check_date(date: datetime, auto_auth_deauth: bool) -> bool:
    expired = date < datetime.now()

    if expired and not auto_auth_deauth:
        raise RippleEnergyTokenExpiredException

    return expired
