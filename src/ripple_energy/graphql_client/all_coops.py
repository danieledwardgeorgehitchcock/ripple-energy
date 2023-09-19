from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel
from .fragments import CoopFragment


class AllCoops(BaseModel):
    all_coops: Optional[List["AllCoopsAllCoops"]] = Field(alias="allCoops")


class AllCoopsAllCoops(CoopFragment):
    pass


AllCoops.model_rebuild()
AllCoopsAllCoops.model_rebuild()
