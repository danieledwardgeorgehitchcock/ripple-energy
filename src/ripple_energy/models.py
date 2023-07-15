from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from typing import Dict, List, Optional

class GenerationPeriod(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    date_from: datetime = Field(alias="from")
    date_to: datetime = Field(alias="to")
    contains_estimate: bool
    generated: float
    earned: float

class Generation(BaseModel):
    generation_unit: str
    latest_telemetry: Optional[Dict] #This is empty with proposed sites - Need real usage data
    latest: Optional[Dict] #This is empty with proposed sites - Need real usage data
    today: GenerationPeriod
    yesterday: GenerationPeriod
    this_week: GenerationPeriod
    last_week: GenerationPeriod
    this_month: GenerationPeriod
    last_month: GenerationPeriod
    this_year: GenerationPeriod
    last_year: GenerationPeriod
    total: GenerationPeriod

class GenerationAsset(BaseModel):
    name: str
    type: str
    status: str
    total_capacity: float
    total_capacity_units: str
    member_capacity: float
    member_capacity_units: str
    member_expected_annual_generation: float
    member_expected_annual_generation_units: str
    generation: Generation
    forecast: Optional[List] #This is empty with proposed sites - Need real usage data

class EnergyGeneration(BaseModel):
    email: str
    copyright_notice: str
    generation_assets: List[GenerationAsset]
