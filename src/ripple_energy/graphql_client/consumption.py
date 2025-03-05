from typing import Optional

from .base_model import BaseModel
from .fragments import ConsumptionFragment


class Consumption(BaseModel):
    consumption: Optional["ConsumptionConsumption"]


class ConsumptionConsumption(ConsumptionFragment):
    pass


Consumption.model_rebuild()
