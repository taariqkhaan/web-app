# Pydantic data validation

from pydantic import BaseModel
from typing import List

class SubtaskBase(BaseModel):
    subtask_name: str
    labor_amount: float
    expenses_amount: float
    travel_amount: float
    tier_fee: float
    budget_amount: float

class ProjectBase(BaseModel):
    project_name: str
    wo_number: str
    activity_code: str
    total_labor_amount: float
    total_expenses_amount: float
    total_travel_amount: float
    total_tier_fee: float
    total_budget_amount: float
    subtasks: List[SubtaskBase] = []
