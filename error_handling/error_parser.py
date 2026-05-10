"""Error parsing utilities."""

from pydantic import ValidationError
from typing import List, Dict, Any


CUSTOM_MESSAGES = {
    "enum": "Please select a valid value from {expected}",
    "greater_than": "Value must be greater than {limit_value}",
    "less_than": "Value must be less than {limit_value}",
    "decimal_places": "Value must have at most {decimal_places} decimal places",
    "pattern": "Format is invalid. Expected pattern: {pattern}",
    "email": "Invalid email address",
    "age": "Age must be between 18 and 120",
    "string_too_short": "Length must be at least {min_length} characters",
    "string_too_long": "Length must be at most {max_length} characters",
}


def parse_validation_error(error: ValidationError) -> List[Dict[str, Any]]:
    """Convert Pydantic ValidationError into structured, user-friendly list."""
    errors = []
    for err in error.errors():
        loc = " -> ".join(str(l) for l in err["loc"])
        err_type = err["type"]

        # Custom message mapping
        if err_type == "enum":
            allowed = err.get("ctx", {}).get("expected", "")
            msg = f"Please select a valid value from {allowed}"
        elif err_type == "greater_than":
            limit = err.get("ctx", {}).get("gt", err.get("ctx", {}).get("ge"))
            msg = f"Value must be greater than {limit}"
        elif err_type == "decimal_places":
            places = err.get("ctx", {}).get("decimal_places", 2)
            msg = f"Value must have at most {places} decimal places"
        elif err_type == "pattern_mismatch":
            pattern = err.get("ctx", {}).get("pattern", "")
            msg = f"Format is invalid. Expected pattern: {pattern}"
        elif err_type == "value_error":
            # e.g. our custom validator messages
            msg = err.get("msg", "Invalid value")
        else:
            # fallback to original message but cleaned
            msg = err.get("msg", "Invalid input")

        errors.append({"location": loc, "message": msg})
    return errors
