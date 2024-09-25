import re
from pydantic import BaseModel, Field, validator


class OrderAddress(BaseModel):
    city: str
    district: str
    street: str


class Order(BaseModel):
    id: str
    name: str
    address: OrderAddress
    price: float = Field(..., gt=0)
    currency: str

    @validator('name')
    def validate_name(cls, value):
        if not re.match("^[A-Za-z ]+$", value):
            raise ValueError("Name contains non-English characters")

        if not all(word[0].isupper() for word in value.split()):
            raise ValueError("Name is not capitalized")

        return value

    @validator('price')
    def validate_price(cls, value):
        if value > 2000:
            raise ValueError("Price is over 2000")
        return value

    @validator('currency')
    def validate_currency(cls, value, values):
        if value not in ["TWD", "USD"]:
            raise ValueError("Currency format is wrong")

        if value == "USD":
            price_in_usd = values.get("price")
            if price_in_usd is not None:
                values["price"] = price_in_usd * 31
                value = "TWD"

        return value
