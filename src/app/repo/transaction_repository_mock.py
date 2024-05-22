from typing import Dict, Optional, List

from ..enums.transaction_type_enum import TransactionTypeEnum
from ..entities.transaction import Transaction
from .transaction_repository_interface import ITransactionRepository

class TransactionRepositoryMock(ITransactionRepository):
    transactions: List[Transaction]
    
    def __init__(self):
        self.transactions = [
        ]
    
    def get_all_transactions(self) -> List[Transaction]:
        return self.transactions
    
    def create_transaction(self, transaction: Transaction) -> Transaction:
        self.transactions.append(transaction)
        return transaction
    
    
    