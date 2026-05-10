# PydaticZad

A comprehensive Python project demonstrating advanced Pydantic v2 features for data validation, serialization, and business logic implementation. This project showcases modern Python development practices with type-safe data models for a financial services application.

## 🚀 Features

- **Advanced Pydantic Models**: Demonstrates Pydantic v2 features including custom validators, computed fields, and serialization control
- **Type-Safe Data Validation**: Robust validation with custom error messages and business logic constraints
- **Environment Configuration**: Settings management using pydantic-settings with environment file support
- **User-Friendly Error Handling**: Structured error parsing that converts Pydantic validation errors into readable messages
- **Financial Data Models**: Complete implementation of User, Transaction, Insurance, and Account models
- **CamelCase/SnakeCase Support**: Automatic field aliasing for API compatibility
- **Decimal Precision**: Proper monetary calculations with decimal arithmetic

## 📁 Project Structure

```
PydaticZad/
├── .env                    # Environment variables (copy from .env.example)
├── .env.example           # Environment template
├── .gitignore            # Git ignore rules
├── README.md             # This file
├── requirements.txt      # Python dependencies
├── main.py               # Main demonstration script
├── models/               # Pydantic data models
│   ├── __init__.py
│   ├── user.py           # User and Address models
│   ├── transaction.py    # Bank transaction models
│   ├── insurance.py      # Insurance policy models
│   ├── account.py        # Account with computed fields
│   └── settings.py       # Global configuration
├── error_handling/       # Error processing utilities
│   ├── __init__.py
│   └── error_parser.py   # User-friendly error messages
└── tests/                # Test suite
    ├── __init__.py
    └── test_models.py    # Model tests
```

## 🛠 Installation

### Prerequisites
- Python 3.8+
- pip package manager

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/Jakub-Jakobczak/PydaticZad.git
   cd PydaticZad
   ```

2. **Create virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env file if needed (default VALIDATION_MODE=lax)
   ```

## 🎯 Usage

### Running the Demonstration

Execute the main script to see all models in action:

```bash
python main.py
```

This will demonstrate:
- Settings loading from environment
- User creation with camelCase input
- Transaction processing with automatic type coercion
- Insurance policy validation (with intentional error example)
- Account creation with computed portfolio value and risk assessment

### Expected Output

```
Running in lax mode
User created: ACC-9A3F
Serialized (no SSN): {'user_id': 'ACC-9A3F', 'email': 'john.doe@example.com', 'age': 30, 'address': {'street': '123 Main St', 'city': 'Springfield', 'zip_code': '12345'}}
Transaction amount: 1500.50 <class 'decimal.Decimal'>
Policy errors: [{'location': 'end_date', 'message': 'end_date must be at least 30 days after start_date'}]
Total portfolio: 11500
Risk score: High
```

## 📋 Model Descriptions

### User Model (`models/user.py`)
- **Fields**: user_id, email, age, address, social_security_number
- **Features**:
  - UUID or ACC-XXXX format validation for user_id
  - Email validation using EmailStr
  - Age constraints (18-120)
  - Nested Address model with zip code validation
  - SSN automatically excluded from serialization

### Transaction Model (`models/transaction.py`)
- **Fields**: amount, currency, timestamp, transaction_type
- **Features**:
  - Decimal amount with 2 decimal places precision
  - Currency enum (USD, EUR, GBP)
  - Transaction type enum (DEBIT, CREDIT)
  - Automatic string-to-Decimal coercion
  - CamelCase input support

### Insurance Policy Model (`models/insurance.py`)
- **Fields**: policy_number, start_date, end_date, status
- **Features**:
  - 10-character alphanumeric policy number (auto-uppercase)
  - Date validation ensuring minimum 30-day coverage
  - Policy status enum (ACTIVE, ELAPSED, PENDING)
  - CamelCase input support

### Account Model (`models/account.py`)
- **Fields**: user, transactions
- **Computed Fields**:
  - `total_portfolio_value`: Sum of all transactions (credit +, debit -)
  - `risk_score`: High/Medium/Low based on age and transaction amounts

### Settings Model (`models/settings.py`)
- **Fields**: validation_mode
- **Features**:
  - Environment variable loading
  - Strict/lax validation modes
  - Configurable via .env file

## 🔧 Configuration

### Environment Variables

Create a `.env` file with:

```env
VALIDATION_MODE=lax  # or 'strict'
DATABASE_URL=        # Optional database connection
DEBUG=True          # Debug mode
```

### Validation Modes

- **lax**: More permissive validation (default)
- **strict**: Strict type checking (rejects string numbers as integers)

## 🧪 Testing

Run the test suite:

```bash
python -m pytest tests/
```

Or run specific tests:

```bash
python -m pytest tests/test_models.py -v
```

## 📝 Error Handling

The `error_handling/error_parser.py` module provides user-friendly error messages:

```python
from pydantic import ValidationError
from error_handling.error_parser import parse_validation_error

try:
    # Some invalid model creation
    user = User(user_id="invalid", age=150)
except ValidationError as e:
    errors = parse_validation_error(e)
    for error in errors:
        print(f"{error['location']}: {error['message']}")
```

## 🔍 Key Pydantic Features Demonstrated

- **Custom Validators**: `@field_validator` decorators
- **Computed Fields**: `@computed_field` for dynamic properties
- **Field Constraints**: `ge`, `le`, `min_length`, `pattern`, etc.
- **Model Configuration**: `model_config` for alias generation
- **Serialization Control**: `model_dump()` with exclude parameters
- **Environment Settings**: `BaseSettings` integration
- **Type Coercion**: Automatic type conversion
- **Nested Models**: Complex data structures
- **Enum Validation**: Restricted value sets

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and add tests
4. Run tests: `python -m pytest`
5. Commit changes: `git commit -m "Add feature"`
6. Push to branch: `git push origin feature-name`
7. Create a Pull Request

## 📄 License

This project is for educational purposes. Feel free to use and modify as needed.

## 🆘 Troubleshooting

### Common Issues

1. **Import Errors**: Ensure all dependencies are installed with `pip install -r requirements.txt`

2. **Environment File Not Found**: Copy `.env.example` to `.env`

3. **Validation Too Strict**: Change `VALIDATION_MODE=lax` in `.env`

4. **Python Version**: Requires Python 3.8+ for full Pydantic v2 support

### Getting Help

- Check the [Pydantic Documentation](https://docs.pydantic.dev/)
- Review the code comments for implementation details
- Run `python main.py` to see working examples

---

**Built with ❤️ using Pydantic v2**
