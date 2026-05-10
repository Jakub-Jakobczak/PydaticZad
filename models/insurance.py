"""Insurance model definition."""

from pydantic import BaseModel, Field, field_validator
from datetime import date, timedelta
from enum import Enum


class PolicyStatus(str, Enum):
    ACTIVE = "ACTIVE"
    ELAPSED = "ELAPSED"
    PENDING = "PENDING"


class InsurancePolicy(BaseModel):
    policy_number: str = Field(..., min_length=10, max_length=10, pattern=r"^[A-Z0-9]{10}$")
    start_date: date
    end_date: date
    status: PolicyStatus

    @field_validator("policy_number")
    @classmethod
    def uppercase_policy_number(cls, v: str) -> str:
        return v.upper()

    @field_validator("end_date")
    @classmethod
    def end_date_after_start(cls, v: date, info) -> date:
        start = info.data.get("start_date")
        if start and v < start + timedelta(days=30):
            raise ValueError("end_date must be at least 30 days after start_date")
        return v

    model_config = {
        "alias_generator": lambda s: "".join(
            word.capitalize() if i else word for i, word in enumerate(s.split("_"))
        ),
        "populate_by_name": True,
    }
