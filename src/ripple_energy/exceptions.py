class RippleEnergyException(Exception):
    """Generic Ripple Energy Exception"""

class RippleEnergyMissingCredentialsOrTokenException(RippleEnergyException):
    """Ripple Energy Missing Email / Password Or Token Exception"""

class RippleEnergyMissingAuthorizationHeaderException(RippleEnergyException):
    """Ripple Energy Missing Authorization Header Exception"""

class RippleEnergyMissingTokenException(RippleEnergyException):
    """Ripple Energy Missing Authorization Header Exception"""

class RippleEnergyEmailException(RippleEnergyException):
    """Ripple Energy Missing Email Exception"""

class RippleEnergyPasswordException(RippleEnergyException):
    """Ripple Energy Missing Password Exception"""

class RippleEnergyAuthenticationException(RippleEnergyException):
    """Ripple Energy Authentication Exception"""

class RippleEnergyDeauthenticationException(RippleEnergyException):
    """Ripple Energy Deauthentication Exception"""

class RippleEnergyTokenDestroyException(RippleEnergyException):
    """Ripple Energy Unable To Destroy Token Exception"""