"""Test script to validate all models."""

from models.user import User, Address
from models.transaction import BankTransaction, Currency, TransactionType
from models.insurance import InsurancePolicy, PolicyStatus
from models.account import Account
from models.settings import GlobalConfig
from datetime import date, datetime
from decimal import Decimal

def test_models():
    print("Testing PydaticZad models...")

    # Test User model
    addr = Address(street='123 Main St', city='Anytown', zip_code='12345')
    user = User(user_id='ACC-ABCD', email='test@example.com', age=30, address=addr)
    print('✓ User model created successfully')

    # Test Transaction model
    txn = BankTransaction(amount=Decimal('100.50'), currency=Currency.USD, timestamp=datetime.now(), transactionType='CREDIT')
    print('✓ Transaction model created successfully')

    # Test Insurance model
    policy = InsurancePolicy(policyNumber='ABC1234567', startDate=date.today(), endDate=date.today().replace(day=date.today().day + 60), status=PolicyStatus.ACTIVE)
    print('✓ Insurance model created successfully')

    # Test Account model
    account = Account(user=user, transactions=[txn])
    print(f'✓ Account created with portfolio value: {account.total_portfolio_value}')
    print(f'✓ Risk score: {account.risk_score}')

    # Test SSN exclusion
    user_dict = user.model_dump()
    assert 'social_security_number' not in user_dict
    print('✓ SSN properly excluded from serialization')

    print('All models working correctly!')

if __name__ == "__main__":
    test_models()