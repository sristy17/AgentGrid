from pydantic import BaseModel
from typing import List


class DataPoint(BaseModel):
    revenue: float
    cost: float


class AnalyzeRequest(BaseModel):
    data: List[DataPoint]