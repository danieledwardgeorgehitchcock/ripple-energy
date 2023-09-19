class RippleEnergyException(Exception):
    """Generic Ripple Energy Exception"""


class RippleEnergyMissingAuthorizationHeaderException(RippleEnergyException):
    """Ripple Energy Missing Authorization Header Exception"""


class RippleEnergyAuthenticationException(RippleEnergyException):
    """Ripple Energy Authentication Exception"""


class RippleEnergyDeauthenticationException(RippleEnergyException):
    """Ripple Energy Deauthentication Exception"""


class RippleEnergyTokenDestroyException(RippleEnergyException):
    """Ripple Energy Unable To Destroy Token Exception"""


class RippleEnergyTokenExpiredException(RippleEnergyException):
    """Ripple Energy Token Expired Exception"""
