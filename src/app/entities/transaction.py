from typing import Tuple
from ..errors.entity_errors import ParamNotValidated
from ..enums.transaction_type_enum import TransactionTypeEnum

class Transaction:
    type: TransactionTypeEnum
    value: float
    current_balance: float
    timestamp : float
    
    def __init__(self, type: TransactionTypeEnum=None, value: float=None, current_balance: float=None, timestamp: float=None):
        validation_type = self.validate_type(type)
        if validation_type[0] is False:
            raise ParamNotValidated("type", validation_type[1])
        self.type = type
        validation_value = self.validate_value(value)
        if validation_value[0] is False:
            raise ParamNotValidated("value", validation_value[1])
        self.value = value
        validation_current_balance = self.validate_current_balance(current_balance)
        if validation_current_balance[0] is False:
            raise ParamNotValidated("current_balance", validation_current_balance[1])
        self.current_balance = current_balance
        validation_timestamp = self.validate_timestamp(timestamp)
        if validation_timestamp[0] is False:
            raise ParamNotValidated("timestamp", validation_timestamp[1])
        self.timestamp = timestamp

    @staticmethod   
    def validation_type(type: TransactionTypeEnum) -> Tuple[bool, str]:
        if type is None:
            return (False, "Type is required")
        if type(type) != TransactionTypeEnum:
            return (False, "Type must be TransactionTypeEnum")
        return (True, "")
    
    @staticmethod 
    def validation_value(value: float) -> Tuple[bool, str]:
        if value is None:
            return (False, "Value is required")
        if type(value) != float:
            return (False, "Value must be a float")
        if value < 0:
            return (False,"Value must be positive")
        return (value)
        

    @staticmethod   
    def validation_current_balance(current_balance: float) -> Tuple[bool, str]:
        if current_balance is None:
            return (False, "Current balance is required")
        if type(current_balance) != float:
            return (False, "Current balance must be a float")
        if current_balance < 0:
            return (False, "Current balance must be positive")
        return (True, "")
    
    @staticmethod 
    def validation_timestamp(timestamp: float) -> Tuple[bool, str]:
        if timestamp is None:
            return (False, "Timestamp is required")
        if type(timestamp) != float:
            return (False, "Value must be a float")
        return (True, "")
    
    
    def to_dict(self):
        return {
            "type": self.type,
            "value": self.value,
            "current_balance": self.current_balance,
            "timestamp": self.timestamp
        }
    
    def __eq__(self,other):
        return self.type == other.type and self.value == other.value and self.current_balance == other.current_balance and self.timestamp == other.timestamp
    
    def __repr__(self):
        return f"Transaction(type={self.type}, value={self.value}, current_balance={self.current_balance}, timestamp={self.timestamp})"