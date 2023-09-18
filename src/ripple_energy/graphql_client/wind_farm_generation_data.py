from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import GenerationDataTitle, GenerationGenerationFarmOperationalStatusChoices


class WindFarmGenerationData(BaseModel):
    member: Optional["WindFarmGenerationDataMember"]


class WindFarmGenerationDataMember(BaseModel):
    id: str
    memberships: List["WindFarmGenerationDataMemberMemberships"]


class WindFarmGenerationDataMemberMemberships(BaseModel):
    id: str
    capacity: Any
    coop: "WindFarmGenerationDataMemberMembershipsCoop"


class WindFarmGenerationDataMemberMembershipsCoop(BaseModel):
    id: str
    first_year_estimated_bill_savings_per_watt_hour: float = Field(
        alias="firstYearEstimatedBillSavingsPerWattHour"
    )
    currency: "WindFarmGenerationDataMemberMembershipsCoopCurrency"
    generationfarm: "WindFarmGenerationDataMemberMembershipsCoopGenerationfarm"


class WindFarmGenerationDataMemberMembershipsCoopCurrency(BaseModel):
    precision: int
    code: str
    symbol: str


class WindFarmGenerationDataMemberMembershipsCoopGenerationfarm(BaseModel):
    id: str
    name: str
    capacity: Any
    operational_status: GenerationGenerationFarmOperationalStatusChoices = Field(
        alias="operationalStatus"
    )
    generation_data: List[
        "WindFarmGenerationDataMemberMembershipsCoopGenerationfarmGenerationData"
    ] = Field(alias="generationData")


class WindFarmGenerationDataMemberMembershipsCoopGenerationfarmGenerationData(
    BaseModel
):
    title: GenerationDataTitle
    data_set: List[
        "WindFarmGenerationDataMemberMembershipsCoopGenerationfarmGenerationDataDataSet"
    ] = Field(alias="dataSet")


class WindFarmGenerationDataMemberMembershipsCoopGenerationfarmGenerationDataDataSet(
    BaseModel
):
    net_power_output_kwh: float = Field(alias="netPowerOutputKwh")
    date_time: str = Field(alias="dateTime")
    is_forecast_data: bool = Field(alias="isForecastData")
    savings_for_period: float = Field(alias="savingsForPeriod")


WindFarmGenerationData.model_rebuild()
WindFarmGenerationDataMember.model_rebuild()
WindFarmGenerationDataMemberMemberships.model_rebuild()
WindFarmGenerationDataMemberMembershipsCoop.model_rebuild()
WindFarmGenerationDataMemberMembershipsCoopCurrency.model_rebuild()
WindFarmGenerationDataMemberMembershipsCoopGenerationfarm.model_rebuild()
WindFarmGenerationDataMemberMembershipsCoopGenerationfarmGenerationData.model_rebuild()
WindFarmGenerationDataMemberMembershipsCoopGenerationfarmGenerationDataDataSet.model_rebuild()
