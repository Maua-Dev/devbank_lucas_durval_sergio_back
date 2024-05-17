from typing import Tuple
from ..errors.entity_errors import ParamNotValidated
import re

class User:
    name: str
    account: str
    agency: str
    current_balance: float
    user_id: int
    
    def __init__(self, name: str=None, account: str=None, agency: str=None, current_balance: float=None, user_id: int=None):
        validation_name = self.validate_name(name)
        if validation_name[0] is False:
            raise ParamNotValidated("name", validation_name[1])
        self.name = name
        
        validation_account = self.validate_account(account)
        if validation_account[0] is False:
            raise ParamNotValidated("account", validation_account[1])
        self.account = account

        validation_agency = self.validate_agency(agency)
        if validation_agency[0] is False:
            raise ParamNotValidated("agency", validation_agency[1])
        self.agency = agency
        
        validation_current_balance = self.validate_current_balance(current_balance)
        if validation_current_balance[0] is False:
            raise ParamNotValidated("current_balance", validation_current_balance[1])
        self.current_balance = current_balance
        
    @staticmethod
    def validate_name(name: str) -> Tuple[bool, str]:
        if name is None:
            return (False, "Name is required")
        if type(name) != str:
            return (False, "Name must be a string")
        if len(name) < 3:
            return (False, "Name must be at least 3 characters long")
        return (True, "")
        
    @staticmethod
    def validate_account(account: str) -> Tuple[bool, str]:
        if account is None:
            return (False, "Account is required")
        if type(account) != str:
            return (False, "Account must be a string")
        pattern = r"^\d{5}-\d$"
        if not re.match(pattern, account):
            return (False, "Account format is invalid. It must have exactly 6 digits followed by a '-'")
        return (True, "")
    
    @staticmethod
    def validate_agency(agency: str) -> Tuple[bool, str]:
        if agency is None:
            return (False, "Agency type is required")
        if type(agency) != str:
            return (False, "Agency type must be a str")
        return (True, "")
    
    @staticmethod
    def validate_current_balance(current_balance: float) -> Tuple[bool, str]:
        if current_balance is None:
            return (False, "Current balance is required")
        if type(current_balance) != float:
            return (False, "Current balance must be a float")
        if current_balance < 0:
            return (False, "Current balance must be positive")
        return (True, "")
    

    def to_dict(self):
        return {
            "name": self.name,
            "account": self.account,
            "agency": self.agency,
            "current_balance": self.current_balance
        }
    
    def __eq__(self,other):
        return self.user_id == other.user_id and self.name == other.name and self.account == other.account and self.agency == other.agency and self.current_balance == other.current_balance 
    
    def __repr__(self):
        return f"User(name={self.name}, account={self.account}, agency={self.agency}, current_balance={self.current_balance})"