from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator
from datetime import datetime
import re

app = FastAPI()


class Payment(BaseModel):
    amount: float = Field(gt=0)
    card_number: str = Field(min_length=16, max_length=16)
    card_expiry: str
    card_cvc: str = Field(min_length=3, max_length=3)

    @field_validator("card_number")
    @classmethod
    def validate_card_number(cls, card_number):
        if not card_number.isdigit():
            raise ValueError("Card number must contain only numbers")

        return card_number

    @field_validator("card_cvc")
    @classmethod
    def validate_card_cvc(cls, card_cvc):
        if not card_cvc.isdigit():
            raise ValueError("CVC must contain only numbers")

        return card_cvc

    @field_validator("card_expiry")
    @classmethod
    def validate_card_expiry(cls, card_expiry):
        if not re.match(r"^(0[1-9]|1[0-2])/\d{4}$", card_expiry):
            raise ValueError("Card expiry must be in MM/YYYY format")

        expiry = datetime.strptime(card_expiry, "%m/%Y")
        current_date = datetime.now()

        if expiry.year < current_date.year or (
            expiry.year == current_date.year
            and expiry.month < current_date.month
        ):
            raise ValueError("Card has expired")

        return card_expiry


class PaymentProcessing:
    def process_payment(
        self,
        amount: float,
        card_number: str,
        card_expiry: str,
        card_cvc: str
    ):
        # Simulate payment processing logic
        return {
            "status": "success",
            "amount": amount,
            "card_number": card_number,
            "card_expiry": card_expiry,
            "card_cvc": card_cvc
        }


payment_processor = PaymentProcessing()


@app.post("/payments")
def process_payment(payment: Payment):

    result = payment_processor.process_payment(
        payment.amount,
        payment.card_number,
        payment.card_expiry,
        payment.card_cvc
    )

    return result