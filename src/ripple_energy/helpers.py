from exceptions import RippleEnergyMissingTokenException
from constants import JWT_HEADER_PREFIX


def generate_jwt_header(token: str | None = None) -> dict[str, str]:
    if not token:
        raise RippleEnergyMissingTokenException
    return {"Authorization": f"{JWT_HEADER_PREFIX}{token}"}
