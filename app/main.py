from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from app.routes import order_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


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


app.include_router(order_router, prefix="/api/orders")
