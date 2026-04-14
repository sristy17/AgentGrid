from pydantic import BaseModel
from typing import List, Optional


class Problem(BaseModel):
    type: str
    description: str


class Reason(BaseModel):
    problem: str
    reason: str


class StrategyItem(BaseModel):
    strategy: str
    description: Optional[str] = None
    impact: Optional[str] = None


class Strategy(BaseModel):
    pricing: List[StrategyItem]
    growth: List[StrategyItem]
    cost_cutting: List[StrategyItem]


class AnalyzeResponse(BaseModel):
    data: list
    analytics: dict
    insights: dict
    strategy: Strategy