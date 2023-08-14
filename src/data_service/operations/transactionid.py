from fastapi import HTTPException
from odmantic import ObjectId

from src.data_service.schema.actions import SaveTransactionId
from src.data_service.schema.entities import TransactionId
from src.data_service.schema.types import Engine


async def save_transaction_id(engine: Engine, params: SaveTransactionId) -> TransactionId:
    """
    Save Transaction ID.
    """
    new_transaction_id = TransactionId(
        transaction_id=params.transaction_id)
    await engine.save(new_transaction_id)
    return new_transaction_id


async def check_transaction_id(engine: Engine, transaction_id: str) -> bool:
    """
    Retrieve a Transaction ID if ID exists.
    """

    existing_id = await engine.find(TransactionId, TransactionId.transaction_id == transaction_id)
    if existing_id is None:
        return False
    else:
        return True
