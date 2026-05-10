"""Account model definition."""

from pydantic import BaseModel, computed_field
from typing import List
from .transaction import BankTransaction
from .user import User
from decimal import Decimal


class Account(BaseModel):
    user: User
    transactions: List[BankTransaction] = []

    @computed_field
    @property
    def total_portfolio_value(self) -> Decimal:
        """Sum of all transaction amounts (credit positive, debit negative?)"""
        # According to typical finance: CREDIT adds, DEBIT subtracts.
        total = Decimal("0")
        for t in self.transactions:
            if t.transaction_type == "CREDIT":
                total += t.amount
            else:  # DEBIT
                total -= t.amount
        return total

    @computed_field
    @property
    def risk_score(self) -> str:
        """High/Med/Low based on user age and largest transaction amount"""
        if not self.transactions:
            return "Low"
        max_amount = max(t.amount for t in self.transactions)
        age = self.user.age

        if max_amount > Decimal("10000") or age < 25 or age > 65:
            return "High"
        elif max_amount > Decimal("5000") or 25 <= age <= 35:
            return "Medium"
        else:
            return "Low"
