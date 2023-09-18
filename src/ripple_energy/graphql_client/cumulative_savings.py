from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class CumulativeSavings(BaseModel):
    cumulative_savings_data: Optional["CumulativeSavingsCumulativeSavingsData"] = Field(
        alias="cumulativeSavingsData"
    )


class CumulativeSavingsCumulativeSavingsData(BaseModel):
    currency: "CumulativeSavingsCumulativeSavingsDataCurrency"
    savings: float
    generation: float
    co2_saved: float = Field(alias="co2Saved")
    last_update: str = Field(alias="lastUpdate")


class CumulativeSavingsCumulativeSavingsDataCurrency(BaseModel):
    code: str
    precision: int


CumulativeSavings.model_rebuild()
CumulativeSavingsCumulativeSavingsData.model_rebuild()
CumulativeSavingsCumulativeSavingsDataCurrency.model_rebuild()
