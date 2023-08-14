"""
Entry point for the Trusted Contract API
"""

from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine

from src.common.settings import AppSettings
from src.data_service.operations.transactionid import (
    check_transaction_id,
    save_transaction_id,
)

app_settings = AppSettings()
mongo_client = AsyncIOMotorClient(app_settings.wallet_db_connection_string)
mongo_engine = AIOEngine(
    client=mongo_client,
    database=app_settings.wallet_db_name,
)

origins = [str(app_settings.primary_origin)]
if app_settings.staging_mode:
    origins.append("http://localhost:4200")

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "HEAD", "DELETE"],
    allow_headers=["*"],
)


@app.get("/")
async def main_route():
    return {"message": "Entry point of Trusted Contract API"}


@app.post("/transacionid/check", response_model=None, status_code=status.HTTP_200_OK)
async def post_check_transaction_id(transaction_id: str) -> None:
    await check_transaction_id(transaction_id)


@app.post("/transacionid/save", response_model=None, status_code=status.HTTP_200_OK)
async def post_save_transaction_id(transaction_id: str) -> None:
    await save_transaction_id(transaction_id)
