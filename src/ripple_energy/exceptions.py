class RippleEnergyError(Exception):
    """Generic Ripple Energy Exception"""

class RippleEnergyEmailError(RippleEnergyError):
    """Ripple Energy Missing Email Exception"""

class RippleEnergyPasswordError(RippleEnergyError):
    """Ripple Energy Missing Password Exception"""