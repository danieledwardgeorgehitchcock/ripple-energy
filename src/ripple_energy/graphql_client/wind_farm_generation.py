from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import GenerationDataTitle, GenerationGenerationFarmOperationalStatusChoices


class WindFarmGeneration(BaseModel):
    member: Optional["WindFarmGenerationMember"]


class WindFarmGenerationMember(BaseModel):
    id: str
    memberships: List["WindFarmGenerationMemberMemberships"]


class WindFarmGenerationMemberMemberships(BaseModel):
    id: str
    capacity: Any
    coop: "WindFarmGenerationMemberMembershipsCoop"


class WindFarmGenerationMemberMembershipsCoop(BaseModel):
    id: str
    first_year_estimated_bill_savings_per_watt_hour: float = Field(
        alias="firstYearEstimatedBillSavingsPerWattHour"
    )
    currency: "WindFarmGenerationMemberMembershipsCoopCurrency"
    generationfarm: "WindFarmGenerationMemberMembershipsCoopGenerationfarm"


class WindFarmGenerationMemberMembershipsCoopCurrency(BaseModel):
    precision: int
    code: str
    symbol: str


class WindFarmGenerationMemberMembershipsCoopGenerationfarm(BaseModel):
    id: str
    name: str
    capacity: Any
    operational_status: GenerationGenerationFarmOperationalStatusChoices = Field(
        alias="operationalStatus"
    )
    generation_data: List[
        "WindFarmGenerationMemberMembershipsCoopGenerationfarmGenerationData"
    ] = Field(alias="generationData")


class WindFarmGenerationMemberMembershipsCoopGenerationfarmGenerationData(BaseModel):
    title: GenerationDataTitle
    data_set: List[
        "WindFarmGenerationMemberMembershipsCoopGenerationfarmGenerationDataDataSet"
    ] = Field(alias="dataSet")


class WindFarmGenerationMemberMembershipsCoopGenerationfarmGenerationDataDataSet(
    BaseModel
):
    net_power_output_kwh: float = Field(alias="netPowerOutputKwh")
    date_time: str = Field(alias="dateTime")
    is_forecast_data: bool = Field(alias="isForecastData")
    savings_for_period: float = Field(alias="savingsForPeriod")


WindFarmGeneration.model_rebuild()
WindFarmGenerationMember.model_rebuild()
WindFarmGenerationMemberMemberships.model_rebuild()
WindFarmGenerationMemberMembershipsCoop.model_rebuild()
WindFarmGenerationMemberMembershipsCoopGenerationfarm.model_rebuild()
WindFarmGenerationMemberMembershipsCoopGenerationfarmGenerationData.model_rebuild()
