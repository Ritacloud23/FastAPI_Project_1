from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field, field_validator
import re

app = FastAPI()


class UserRegistration(BaseModel):
    username: str = Field(min_length=3, max_length=20)
    email: EmailStr
    password: str = Field(min_length=8)

    @field_validator("password")
    @classmethod
    def validate_password(cls, password):
        if not re.search(r"[A-Z]", password):
            raise ValueError("Password must contain an uppercase letter")

        if not re.search(r"[a-z]", password):
            raise ValueError("Password must contain a lowercase letter")

        if not re.search(r"\d", password):
            raise ValueError("Password must contain a number")

        if not re.search(r"[!@#$%^&*]", password):
            raise ValueError(
                "Password must contain a special character"
            )

        return password


@app.post("/register")
def register_user(user: UserRegistration):
    return {
        "message": "User registered successfully",
        "username": user.username,
        "email": user.email
    }