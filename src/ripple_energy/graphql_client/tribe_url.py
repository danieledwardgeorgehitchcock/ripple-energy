from pydantic import Field

from .base_model import BaseModel


class TribeUrl(BaseModel):
    tribe_url: str = Field(alias="tribeUrl")
