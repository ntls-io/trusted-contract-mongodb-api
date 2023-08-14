from pydantic import BaseModel


class CheckTransactionId(BaseModel):
    """
    Check Transaction ID parameters
    """

    transaction_id: str


class SaveTransactionId(BaseModel):
    """
    Save Transaction ID parameters
    """

    transaction_id: str
