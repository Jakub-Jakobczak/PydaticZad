"""Main entry point for PydaticZad application."""

from models.user import User, Address
from models.transaction import BankTransaction, Currency, TransactionType
from models.insurance import InsurancePolicy, PolicyStatus
from models.account import Account
from models.settings import GlobalConfig
from error_handling.error_parser import parse_validation_error
from pydantic import ValidationError
from decimal import Decimal
from datetime import datetime, date, timedelta
import json


def main():
    # Load settings (reads VALIDATION_MODE from .env)
    config = GlobalConfig()
    print(f"Running in {config.validation_mode} mode")

    # Example 1: Valid user with camelCase input
    user_data_camel = {
        "userId": "ACC-9A3F",
        "email": "john.doe@example.com",
        "age": 30,
        "address": {
            "street": "123 Main St",
            "city": "Springfield",
            "zipCode": "12345"
        },
        "socialSecurityNumber": "123-45-6789"
    }

    try:
        user = User.model_validate(user_data_camel)
        print("User created:", user.user_id)
        print("Serialized (no SSN):", user.model_dump())
    except ValidationError as e:
        print("User validation errors:", parse_validation_error(e))

    # Example 2: Transaction with stringified amount and camelCase
    tx_data = {
        "amount": "1500.50",
        "currency": "USD",
        "timestamp": "2025-03-15T10:30:00",
        "transactionType": "CREDIT"
    }
    try:
        tx = BankTransaction.model_validate(tx_data)
        print("Transaction amount:", tx.amount, type(tx.amount))  # Decimal
    except ValidationError as e:
        print("Transaction errors:", parse_validation_error(e))

    # Example 3: Insurance policy with date logic
    policy_data = {
        "policyNumber": "POL12345678",   # will be upper-cased
        "startDate": "2025-01-01",
        "endDate": "2025-01-20",         # less than 30 days → error
        "status": "ACTIVE"
    }
    try:
        policy = InsurancePolicy.model_validate(policy_data)
    except ValidationError as e:
        print("Policy errors:", parse_validation_error(e))

    # Example 4: Account with risk score and portfolio value
    user2 = User.model_validate({
        "userId": "550e8400-e29b-41d4-a716-446655440000",
        "email": "jane@example.com",
        "age": 22,
        "address": {"street": "456 Oak Ave", "city": "Metropolis", "zipCode": "90210"},
        "socialSecurityNumber": "987-65-4321"
    })
    transactions = [
        BankTransaction(amount=Decimal("12000"), currency=Currency.USD, timestamp=datetime.now(), transaction_type=TransactionType.CREDIT),
        BankTransaction(amount=Decimal("500"), currency=Currency.USD, timestamp=datetime.now(), transaction_type=TransactionType.DEBIT)
    ]
    account = Account(user=user2, transactions=transactions)
    print(f"Total portfolio: {account.total_portfolio_value}")
    print(f"Risk score: {account.risk_score}")


if __name__ == "__main__":
    main()
