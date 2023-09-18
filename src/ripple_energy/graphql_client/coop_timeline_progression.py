from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class CoopTimelineProgression(BaseModel):
    coop_timeline_progression: "CoopTimelineProgressionCoopTimelineProgression" = Field(
        alias="coopTimelineProgression"
    )


class CoopTimelineProgressionCoopTimelineProgression(BaseModel):
    timeline_progression: Optional[int] = Field(alias="timelineProgression")


CoopTimelineProgression.model_rebuild()
CoopTimelineProgressionCoopTimelineProgression.model_rebuild()
