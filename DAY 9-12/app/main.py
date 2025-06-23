from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from .db import engine
from .models import Base
from .exceptions import custom_exception_handler
from .dependencies import get_db

from app.inventory.router import router as inventory_router
from app.carts.router     import router as carts_router
from app.orders.router    import router as orders_router

# load .env
load_dotenv()

# create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="E-commerce Management API",
    version="1.0.0",
    description="Inventory ↔ Carts ↔ Orders",
)

# CORS (dev only)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_methods=["*"], allow_headers=["*"],
)

# global exception handler
app.add_exception_handler(Exception, custom_exception_handler)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors(), "body": exc.body},
    )

# mount routers
app.include_router(inventory_router)
app.include_router(carts_router)
app.include_router(orders_router)