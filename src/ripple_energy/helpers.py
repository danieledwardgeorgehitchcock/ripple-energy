from exceptions import RippleEnergyTokenExpiredException
from datetime import datetime
from constants import JWT_HEADER_PREFIX
from pydantic import validate_call

@validate_call
def generate_jwt_header(token: str | None = None) -> dict[str, str]:
    return {"Authorization": f"{JWT_HEADER_PREFIX}{token}"}

@validate_call
def check_date(expiry_date: datetime, auto_auth_deauth: bool) -> bool:
    expired = expiry_date < datetime.now()

    if expired and not auto_auth_deauth:
        raise RippleEnergyTokenExpiredException

    return expired
