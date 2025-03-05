from typing import Optional

from .base_model import BaseModel
from .enums import CoopCoopStatusChoices


class ActiveCoopStatus(BaseModel):
    coop: Optional["ActiveCoopStatusCoop"]


class ActiveCoopStatusCoop(BaseModel):
    id: str
    status: CoopCoopStatusChoices


ActiveCoopStatus.model_rebuild()
