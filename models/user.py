"""User model definition."""

from pydantic import BaseModel, Field, EmailStr, field_validator
from uuid import UUID
import re
from typing import Optional


class Address(BaseModel):
    street: str
    city: str
    zip_code: str = Field(..., pattern=r"^\d{5}$")  # 5-digit zip


class User(BaseModel):
    user_id: str = Field(..., description="UUID or ACC-XXXX format")
    email: EmailStr
    age: int = Field(..., ge=18, le=120)
    address: Address
    social_security_number: Optional[str] = None

    # Custom validator for user_id format
    @field_validator("user_id")
    @classmethod
    def validate_user_id(cls, v: str) -> str:
        # Check if it's a valid UUID
        try:
            UUID(v)
            return v
        except ValueError:
            pass
        # Check ACC-XXXX pattern (X = digit or letter, but example says XXXX, let's do 4 alphanum)
        if re.match(r"^ACC-[A-Z0-9]{4}$", v):
            return v
        raise ValueError("user_id must be a UUID or follow pattern 'ACC-XXXX' where XXXX are 4 alphanumeric characters")

    # Exclude SSN from serialization
    def model_dump(self, **kwargs):
        kwargs.setdefault("exclude", set()).add("social_security_number")
        return super().model_dump(**kwargs)

    def model_dump_json(self, **kwargs):
        kwargs.setdefault("exclude", set()).add("social_security_number")
        return super().model_dump_json(**kwargs)
