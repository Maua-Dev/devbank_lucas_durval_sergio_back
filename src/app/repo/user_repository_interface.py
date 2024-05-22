from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from ..entities.user import User


class IUserRepository(ABC):

    @abstractmethod
    def create_user(self, name: str, agency: str, account: str, current_balance: float) -> User:
        '''
        Creates a new User with the given name.
        If the User already exists, returns None
        '''
        pass
    
    @abstractmethod
    def get_user(self, name: str) -> Optional[User]:
        '''
        Returns the User with the given name.
        If the User does not exist, returns None
        '''
        pass
    
    @abstractmethod
    def delete_user(self, name: str) -> User:
        '''
        Deletes the User with the given name.
        If the User does not exist, returns None
        '''
        
    @abstractmethod
    def update_user(self, name:str=None, agency:str=None, account:str=None, current_balance:float=None) -> User:
        '''
        Updates the User with the given name.
        If the User does not exist, returns None
        '''
        pass
    
    