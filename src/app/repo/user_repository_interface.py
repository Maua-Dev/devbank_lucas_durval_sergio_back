from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from ..entities.user import User


class IUserRepository(ABC):

    @abstractmethod
    def get_user(self) -> User:
        '''
        Returns the User with the given name.
        If the User does not exist, returns None
        '''
        pass

    
    