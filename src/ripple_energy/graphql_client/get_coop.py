from typing import Optional

from .base_model import BaseModel
from .fragments import CoopFragment


class GetCoop(BaseModel):
    coop: Optional["GetCoopCoop"]


class GetCoopCoop(CoopFragment):
    pass


GetCoop.update_forward_refs()
GetCoopCoop.update_forward_refs()
