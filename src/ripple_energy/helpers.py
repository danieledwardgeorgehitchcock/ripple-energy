import logging
from datetime import datetime
from typing import Awaitable, Callable

from pydantic import validate_call

from .constants import JWT_HEADER_PREFIX, PARAM, TYPE
from .exceptions import RippleEnergyTokenExpiredException

logger = logging.getLogger(__name__)


@validate_call
def generate_jwt_header(token: str | None = None) -> dict[str, str]:
    return {"Authorization": f"{JWT_HEADER_PREFIX}{token}"}


@validate_call
def check_date(date: datetime, auto_auth_deauth: bool) -> bool:
    now = datetime.now()
    expired = date < now

    logger.info(f"Checked Token Expiry: {date} Against Now: {now}. Result: {expired}")

    if expired and not auto_auth_deauth:
        raise RippleEnergyTokenExpiredException

    return expired


def check_expiry(
    function: Callable[PARAM, Awaitable[TYPE]]
) -> Callable[PARAM, Awaitable[TYPE]]:
    async def wrapper(*args: PARAM.args, **kwargs: PARAM.kwargs) -> TYPE:
        if (
            hasattr(args[0], "token_expires")
            and hasattr(args[0], "auto_auth_deauth")
            and hasattr(args[0], "refresh_token")
        ):
            if check_date(args[0].token_expires, args[0].auto_auth_deauth):
                await args[0].refresh_token()
        return await function(*args, **kwargs)

    return wrapper
