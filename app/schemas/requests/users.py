# pylint: disable=all

import re
from typing import Annotated

from pydantic import BaseModel, field_validator, Field, constr

Username = Annotated[
    str,
    Field(
        min_length=4,
        max_length=64,
        description="Username field",
        # regex=re.compile(r"[^a-zA-Z0-9]"),  # Optional regex pattern
    ),
    lambda value: value.strip().lower(),
]


class RegisterUserRequest(BaseModel):
    email: str
    password: constr(min_length=8, max_length=64)
    username: Username

    @field_validator("password")
    def validate_password(cls, value):
        if not re.search(r"[^a-zA-Z0-9]", value):
            raise ValueError("Password must contain special characters")

        if not re.search(r"[0-9]", value):
            raise ValueError("Password must contain numbers")

        if not re.search(r"[A-Z]", value):
            raise ValueError("Password must contain uppercase characters")

        if not re.search(r"[a-z]", value):
            raise ValueError("Password must contain lowercase characters")
        return value

    @field_validator("username")
    def validate_username(cls, value):
        if re.search(r"[^a-zA-Z0-9]", value):
            raise ValueError("Username must not contain special characters")
        return value


class LoginUserRequest(BaseModel):
    email: str
    password: str

    class Config:
        schema_extra = {"example": {"email": "abc@example.com", "password": "abc123@"}}
