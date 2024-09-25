from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from app.schemas import Order

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def custom_http_exception_handler(request: Request, exc: RequestValidationError):
    msg = exc.errors()[0].get("msg", "")
    for error in exc.errors():
        if error["type"] == "value_error":
            msg = ",".join(error["msg"].split(",")[1:]).strip()
            break

    return JSONResponse(
        status_code=400,
        content={"msg": msg}
    )


@app.post("/api/orders", status_code=201)
def validate_order(order: Order):
    return order
