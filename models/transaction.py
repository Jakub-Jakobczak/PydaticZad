"""Transaction model definition."""

from pydantic import BaseModel, Field, field_validator
from decimal import Decimal
from enum import Enum
from datetime import datetime
from typing import Union


class Currency(str, Enum):
    USD = "USD"
    EUR = "EUR"
    GBP = "GBP"


class TransactionType(str, Enum):
    DEBIT = "DEBIT"
    CREDIT = "CREDIT"


class BankTransaction(BaseModel):
    amount: Decimal = Field(..., gt=0, decimal_places=2)
    currency: Currency
    timestamp: datetime  # auto-parses ISO strings
    transaction_type: TransactionType

    # Coerce stringified numbers to Decimal
    @field_validator("amount", mode="before")
    @classmethod
    def coerce_amount(cls, v):
        if isinstance(v, (int, float, str)):
            return Decimal(str(v))
        return v

    # Enable camelCase input to snake_case fields
    model_config = {
        "alias_generator": lambda s: "".join(
            word.capitalize() if i else word for i, word in enumerate(s.split("_"))
        ),
        "populate_by_name": True,
    }
