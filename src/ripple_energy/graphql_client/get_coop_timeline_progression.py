from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class GetCoopTimelineProgression(BaseModel):
    coop_timeline_progression: "GetCoopTimelineProgressionCoopTimelineProgression" = (
        Field(alias="coopTimelineProgression")
    )


class GetCoopTimelineProgressionCoopTimelineProgression(BaseModel):
    timeline_progression: Optional[int] = Field(alias="timelineProgression")


GetCoopTimelineProgression.model_rebuild()
GetCoopTimelineProgressionCoopTimelineProgression.model_rebuild()
