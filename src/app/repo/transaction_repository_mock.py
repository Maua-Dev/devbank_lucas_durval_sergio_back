from typing import Dict, Optional, List

from ..enums.transaction_type_enum import TransactionTypeEnum
from ..entities.transaction import Transaction
from .transaction_repository_interface import TransactionRepository

class TransactionRepositoryMock(TransactionRepository):
    transactions: List[Transaction]
    
    def __init__(self):
        self.transactions = [
        ]
    
    def get_all_transactions(self) -> Optional[Transaction]:
        return self.transactions.values()
    
    def create_transaction(self, transaction: Transaction) -> Transaction:
        self.transactions.append(transaction)
        return transaction
    
    
    