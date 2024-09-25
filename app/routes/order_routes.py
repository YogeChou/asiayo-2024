from fastapi import APIRouter, Depends
from app.schema import OrderSchema
from app.service import CurrencyService


order_router = APIRouter(tags=['Order'])


@order_router.post("/", status_code=201)
async def validate_order(order: OrderSchema, currency_service: CurrencyService = Depends(CurrencyService)):
    order.price *= currency_service.get_rate(order.currency)
    order.currency = "TWD"
    return order
