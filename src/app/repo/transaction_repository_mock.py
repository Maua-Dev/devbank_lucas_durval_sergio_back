from typing import Dict, Optional, List

from ..enums.transaction_type_enum import TransactionTypeEnum
from ..entities.transaction import Transaction
from .transaction_repository_interface import TransactionRepository

class TransactionRepositoryMock(TransactionRepository):
    transactions: Dict[int, Transaction]
    
    def __init__(self):
        self.transactions = {
        }
    
    def get_all_transactions(self, type: TransactionTypeEnum) -> Optional[Transaction]:
        return self.transactions.get(type, None)
    
    def create_transaction(self, transaction: Transaction) -> Transaction:
        
        self.transactions[transaction] = transaction
        return transaction
    
    
        
    def update_user(self, name:str=None, agency:str=None, account:str=None, current_balance: float=None) -> Transaction:
        user = self.users.get(name, None)
        if user is None:
            return None
        
        if name is not None:
            user.name = name
        if agency is not None:
            user.agency = agency
        if account is not None:
            user.account = account
        if current_balance is not None:
            user.current_balance = current_balance
        self.users[name] = user
        
        return user
        
    
    