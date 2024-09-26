from fastapi import APIRouter
from app.schema import OrderSchema
from app.service import CurrencyServiceFactory, CurrencyConverter


order_router = APIRouter(tags=['Order'])


@order_router.post("/", status_code=200)
async def validate_order(order: OrderSchema):
    base_currency_service = CurrencyServiceFactory.get_currency_service(order.currency)
    converter = CurrencyConverter(base_currency_service)

    twd_price = converter.convert(order.price, "TWD")
    order.price = twd_price
    order.currency = "TWD"
    return order
