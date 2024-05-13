from typing import Dict, Optional, List

from ..enums.transaction_type_enum import TransactionTypeEnum
from ..entities.user import User
from .user_repository_interface import UserRepository


class UserRepositoryMock(UserRepository):
    users: Dict[int, User]
    
    def __init__(self):
        self.users = {
            1: User(name="Vitor Soller", agency="0000", account="00000-0", current_balance= 1000.0)

        }
    
    def get_user(self, name: str) -> Optional[User]:
        return self.users.get(name, None)
    
    def create_user(self, user: User) -> User:
        
        self.users[user] = user
        return user
    
    def delete_item(self, name: str) -> Optional[User]:
        user= self.users.pop(name, None)
        return user
        
        
    def update_user(self, name:str=None, agency:str=None, account:str=None, current_balance: float=None) -> User:
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
        
    
    