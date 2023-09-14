from typing import Optional

from .base_model import BaseModel
from .enums import CoopCoopStatusChoices


class GetActiveCoopStatus(BaseModel):
    coop: Optional["GetActiveCoopStatusCoop"]


class GetActiveCoopStatusCoop(BaseModel):
    id: str
    status: CoopCoopStatusChoices


GetActiveCoopStatus.update_forward_refs()
GetActiveCoopStatusCoop.update_forward_refs()
