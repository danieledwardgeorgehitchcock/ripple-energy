from typing import Optional

from .base_model import BaseModel


class Version(BaseModel):
    version: Optional[str]


Version.model_rebuild()
