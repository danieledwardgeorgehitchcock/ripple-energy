from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import GenerationGenerationFarmOperationalStatusChoices


class InsightsChartData(BaseModel):
    member: Optional["InsightsChartDataMember"]


class InsightsChartDataMember(BaseModel):
    id: str
    memberships: List["InsightsChartDataMemberMemberships"]


class InsightsChartDataMemberMemberships(BaseModel):
    id: str
    coop: "InsightsChartDataMemberMembershipsCoop"


class InsightsChartDataMemberMembershipsCoop(BaseModel):
    id: str
    name: str
    generationfarm: "InsightsChartDataMemberMembershipsCoopGenerationfarm"


class InsightsChartDataMemberMembershipsCoopGenerationfarm(BaseModel):
    id: str
    name: str
    operational_status: GenerationGenerationFarmOperationalStatusChoices = Field(
        alias="operationalStatus"
    )
    insights_chart_data: (
        "InsightsChartDataMemberMembershipsCoopGenerationfarmInsightsChartData"
    ) = Field(alias="insightsChartData")


class InsightsChartDataMemberMembershipsCoopGenerationfarmInsightsChartData(BaseModel):
    chart_data: Optional[
        List[
            "InsightsChartDataMemberMembershipsCoopGenerationfarmInsightsChartDataChartData"
        ]
    ] = Field(alias="chartData")
    cumulative_data: Optional[
        "InsightsChartDataMemberMembershipsCoopGenerationfarmInsightsChartDataCumulativeData"
    ] = Field(alias="cumulativeData")
    user_errors: List[
        "InsightsChartDataMemberMembershipsCoopGenerationfarmInsightsChartDataUserErrors"
    ] = Field(alias="userErrors")


class InsightsChartDataMemberMembershipsCoopGenerationfarmInsightsChartDataChartData(
    BaseModel
):
    wind_speed_mph: Optional[float] = Field(alias="windSpeedMph")
    generation_kwh: Optional[float] = Field(alias="generationKwh")
    savings: Optional[float]
    from_time: Any = Field(alias="fromTime")
    to_time: Any = Field(alias="toTime")


class InsightsChartDataMemberMembershipsCoopGenerationfarmInsightsChartDataCumulativeData(
    BaseModel
):
    average_wind_speed_mph: Optional[float] = Field(alias="averageWindSpeedMph")
    cumulative_generation_kwh: float = Field(alias="cumulativeGenerationKwh")
    cumulative_savings: float = Field(alias="cumulativeSavings")


class InsightsChartDataMemberMembershipsCoopGenerationfarmInsightsChartDataUserErrors(
    BaseModel
):
    field: str
    message: str


InsightsChartData.model_rebuild()
InsightsChartDataMember.model_rebuild()
InsightsChartDataMemberMemberships.model_rebuild()
InsightsChartDataMemberMembershipsCoop.model_rebuild()
InsightsChartDataMemberMembershipsCoopGenerationfarm.model_rebuild()
InsightsChartDataMemberMembershipsCoopGenerationfarmInsightsChartData.model_rebuild()
