from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import GenerationGenerationFarmOperationalStatusChoices


class GetInsightsChartData(BaseModel):
    member: Optional["GetInsightsChartDataMember"]


class GetInsightsChartDataMember(BaseModel):
    id: str
    memberships: List["GetInsightsChartDataMemberMemberships"]


class GetInsightsChartDataMemberMemberships(BaseModel):
    id: str
    coop: "GetInsightsChartDataMemberMembershipsCoop"


class GetInsightsChartDataMemberMembershipsCoop(BaseModel):
    id: str
    name: str
    generationfarm: "GetInsightsChartDataMemberMembershipsCoopGenerationfarm"


class GetInsightsChartDataMemberMembershipsCoopGenerationfarm(BaseModel):
    id: str
    name: str
    operational_status: GenerationGenerationFarmOperationalStatusChoices = Field(
        alias="operationalStatus"
    )
    insights_chart_data: "GetInsightsChartDataMemberMembershipsCoopGenerationfarmInsightsChartData" = Field(
        alias="insightsChartData"
    )


class GetInsightsChartDataMemberMembershipsCoopGenerationfarmInsightsChartData(
    BaseModel
):
    chart_data: Optional[
        List[
            "GetInsightsChartDataMemberMembershipsCoopGenerationfarmInsightsChartDataChartData"
        ]
    ] = Field(alias="chartData")
    cumulative_data: Optional[
        "GetInsightsChartDataMemberMembershipsCoopGenerationfarmInsightsChartDataCumulativeData"
    ] = Field(alias="cumulativeData")
    user_errors: List[
        "GetInsightsChartDataMemberMembershipsCoopGenerationfarmInsightsChartDataUserErrors"
    ] = Field(alias="userErrors")


class GetInsightsChartDataMemberMembershipsCoopGenerationfarmInsightsChartDataChartData(
    BaseModel
):
    wind_speed_mph: Optional[float] = Field(alias="windSpeedMph")
    generation_kwh: Optional[float] = Field(alias="generationKwh")
    savings: Optional[float]
    from_time: Any = Field(alias="fromTime")
    to_time: Any = Field(alias="toTime")


class GetInsightsChartDataMemberMembershipsCoopGenerationfarmInsightsChartDataCumulativeData(
    BaseModel
):
    average_wind_speed_mph: Optional[float] = Field(alias="averageWindSpeedMph")
    cumulative_generation_kwh: float = Field(alias="cumulativeGenerationKwh")
    cumulative_savings: float = Field(alias="cumulativeSavings")


class GetInsightsChartDataMemberMembershipsCoopGenerationfarmInsightsChartDataUserErrors(
    BaseModel
):
    field: str
    message: str


GetInsightsChartData.model_rebuild()
GetInsightsChartDataMember.model_rebuild()
GetInsightsChartDataMemberMemberships.model_rebuild()
GetInsightsChartDataMemberMembershipsCoop.model_rebuild()
GetInsightsChartDataMemberMembershipsCoopGenerationfarm.model_rebuild()
GetInsightsChartDataMemberMembershipsCoopGenerationfarmInsightsChartData.model_rebuild()
GetInsightsChartDataMemberMembershipsCoopGenerationfarmInsightsChartDataChartData.model_rebuild()
GetInsightsChartDataMemberMembershipsCoopGenerationfarmInsightsChartDataCumulativeData.model_rebuild()
GetInsightsChartDataMemberMembershipsCoopGenerationfarmInsightsChartDataUserErrors.model_rebuild()
