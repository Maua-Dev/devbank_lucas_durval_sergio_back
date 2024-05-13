from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from ..enums.transaction_type_enum import TransactionTypeEnum

from ..entities.transaction import Transaction


class ITransactionRepository(ABC):
    
    
    @abstractmethod
    def get_all_Transactions(self) -> List[Transaction]:
        '''
        Returns all the itens in the database 
        '''
        pass
    
    @abstractmethod
    def get_Transaction(self, Transaction_id: int) -> Optional[Transaction]:
        '''
        Returns the Transaction with the given id.
        If the Transaction does not exist, returns None
        '''
        pass
    
    @abstractmethod
    def create_Transaction(self, Transaction: Transaction, Transaction_id: int) -> Transaction:
        '''
        Creates a new Transaction in the database
        '''
        pass
    
    @abstractmethod
    def delete_Transaction(self, Transaction_id: int) -> Transaction:
        '''
        Deletes the Transaction with the given id.
        If the Transaction does not exist, returns None
        '''
        
    @abstractmethod
    def update_Transaction(self, Transaction_id:int, name:str=None, price:float=None, Transaction_type:TransactionTypeEnum=None, admin_permission:bool=None) -> Transaction:
        '''
        Updates the Transaction with the given id.
        If the Transaction does not exist, returns None
        '''
        pass
    
    