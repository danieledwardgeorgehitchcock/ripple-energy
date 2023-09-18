from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class MonthlySavings(BaseModel):
    monthly_savings_data: Optional["MonthlySavingsMonthlySavingsData"] = Field(
        alias="monthlySavingsData"
    )


class MonthlySavingsMonthlySavingsData(BaseModel):
    currency: "MonthlySavingsMonthlySavingsDataCurrency"
    month: str
    year: str
    savings: float
    referred_savings: Optional[float] = Field(alias="referredSavings")
    generation: float
    co2_saved: float = Field(alias="co2Saved")
    tree_equivalent: int = Field(alias="treeEquivalent")


class MonthlySavingsMonthlySavingsDataCurrency(BaseModel):
    code: str
    precision: int


MonthlySavings.model_rebuild()
MonthlySavingsMonthlySavingsData.model_rebuild()
MonthlySavingsMonthlySavingsDataCurrency.model_rebuild()
