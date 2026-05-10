"""Settings and configuration models."""

from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Literal


class GlobalConfig(BaseSettings):
    validation_mode: Literal["strict", "lax"] = Field(default="lax", env="VALIDATION_MODE")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
