from typing import Dict, Optional, List

from ..enums.transaction_type_enum import TransactionTypeEnum
from ..entities.user import User
from .user_repository_interface import IUserRepository


class UserRepositoryMock(IUserRepository):
    users: List[User]
    
    # creates the users list
    def __init__(self):
        self.users = [
            User(name="Vitor Soller", agency="0000", account="00000-0", current_balance= 1000.0)
        ]

    # gets a user in the users list
    def get_user(self) -> User:
        return self.users[0]

        
    
    