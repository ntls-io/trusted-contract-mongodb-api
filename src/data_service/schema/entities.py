from odmantic import Model


class TransactionId(Model):
    """
    Transaction ID.
    """

    transaction_id: str
