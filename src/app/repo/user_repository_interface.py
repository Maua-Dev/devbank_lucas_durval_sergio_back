from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from ..enums.transaction_type_enum import TransactionTypeEnum

from ..entities.user import User


class IUserRepository(ABC):
    
    @abstractmethod
    def get_User(self, name: str) -> Optional[User]:
        '''
        Returns the User with the given name.
        If the User does not exist, returns None
        '''
        pass
    
    @abstractmethod
    def delete_User(self, name: str) -> User:
        '''
        Deletes the User with the given name.
        If the User does not exist, returns None
        '''
        
    @abstractmethod
    def update_User(self, name:str=None, agency:str=None, account:str=None, current_balance:float=None) -> User:
        '''
        Updates the User with the given name.
        If the User does not exist, returns None
        '''
        pass
    
    