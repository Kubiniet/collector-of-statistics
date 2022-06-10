from datetime import date
from typing import Optional

from pydantic import BaseModel, condecimal


class StatsModelDTO(BaseModel):
    """
    DTO for stats models.

    It returned when accessing stats models from the API.
    """

    id: int
    date: date
    views: Optional[int]
    clicks: Optional[int]
    cost: Optional[condecimal(decimal_places=2)]
    cpc: Optional[float]
    cpn: Optional[float]

    class Config:
        orm_mode = True


class StatsModelInputDTO(BaseModel):
    """DTO for creating new stats model."""

    date: date
    views: Optional[int]
    clicks: Optional[int]
    cost: Optional[condecimal(decimal_places=2)]
