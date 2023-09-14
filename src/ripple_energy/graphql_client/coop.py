from typing import Optional

from .base_model import BaseModel
from .fragments import CoopFragment


class Coop(BaseModel):
    coop: Optional["CoopCoop"]


class CoopCoop(CoopFragment):
    pass


Coop.update_forward_refs()
CoopCoop.update_forward_refs()
