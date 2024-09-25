import re
from pydantic import BaseModel, Field, field_validator


class OrderAddressSchema(BaseModel):
    city: str
    district: str
    street: str


class OrderSchema(BaseModel):
    id: str
    name: str
    address: OrderAddressSchema
    price: float = Field(..., gt=0)
    currency: str

    @field_validator('name')
    def validate_name(cls, value):
        if not re.match("^[A-Za-z ]+$", value):
            raise ValueError("Name contains non-English characters")

        if not all(word[0].isupper() for word in value.split()):
            raise ValueError("Name is not capitalized")

        return value

    @field_validator('price')
    def validate_price(cls, value):
        if value > 2000:
            raise ValueError("Price is over 2000")
        return value

    @field_validator('currency')
    def validate_currency(cls, value):
        if value not in ["TWD", "USD"]:
            raise ValueError("Currency format is wrong")
        return value
