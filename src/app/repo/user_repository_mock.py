from typing import Dict, Optional, List

from ..enums.transaction_type_enum import TransactionTypeEnum
from ..entities.user import User
from .user_repository_interface import UserRepository


class UserRepositoryMock(UserRepository):
    users: Dict[int, User]
    
    # creates the users list
    def __init__(self):
        self.users = {
            1: User(name="Vitor Soller", agency="0000", account="00000-0", current_balance= 1000.0)
        }
    
    # creates a new user
    def create_user(self, user_id: int=None, name: str=None, agency:str=None, account:str=None, current_balance: float=None):
        user = User(name=name, agency=agency, account=account, current_balance=current_balance)
        self.users[user_id] = user

    # gets a user in the users list
    def get_user(self, user_id: int) -> Optional[User]:
        return self.users.get(user_id)
    
    # deletes a user in the users list
    def delete_user(self, user_id: int) -> Optional[User]:
        return self.users.pop(user_id, None)
        
    # updates a user in the users list
    def update_user(self, user_id: int=None, name:str=None, agency:str=None, account:str=None, current_balance: float=None) -> User:
        user = self.users.get(user_id)
        if user:
            if agency is not None:
                user.agency = agency
            if account is not None:
                user.account = account
            if current_balance is not None:
                user.current_balance = current_balance
        return user

        
    
    