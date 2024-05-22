from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from ..enums.transaction_type_enum import TransactionTypeEnum

from ..entities.transaction import Transaction


class ITransactionRepository(ABC):
    
    
    @abstractmethod
    def get_all_transactions(self) -> List[Transaction]:
        '''
        Returns all the itens in the database 
        '''
        pass
    
    @abstractmethod
    def create_transaction(self, transaction: Transaction) -> Transaction:
        '''
        Creates a new Transaction in the database
        '''
        pass

    