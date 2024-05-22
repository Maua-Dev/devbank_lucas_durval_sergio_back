import pytest
from src.app.entities.transaction import Transaction
from src.app.errors.entity_errors import  ParamNotValidated
from src.app.enums.transaction_type_enum import TransactionTypeEnum

class Test_Transaction:
    def test_Transaction(self):
        transaction = Transaction(type=TransactionTypeEnum.DEPOSIT, value = 250.0, current_balance= 1000.0, timestamp= 123456789.0)
        assert transaction.type == TransactionTypeEnum.DEPOSIT
        assert transaction.value == 250.0
        assert transaction.current_balance == 1000.0
        assert transaction.timestamp == 123456789
    
    def test_transaction_dict(self):
       transaction = Transaction(type=TransactionTypeEnum.DEPOSIT, value=250.0, current_balance=1000.0, timestamp=123456789.0)
       assert transaction.to_dict() == {'type': 'DEPOSIT', 'value': 250.0, 'current_balance': 1000.0, 'timestamp': 123456789.0}

    def test_transaction_type_is_none(self):
        with pytest.raises(ParamNotValidated):
            Transaction(value=250.0, current_balance=1000.0, timestamp=123456789.0)
        
    def test_transaction_type_is_not_TransactionTypeEnum(self):
        with pytest.raises(ParamNotValidated):
           Transaction(type = 10,value=250.0, current_balance=1000.0, timestamp=123456789.0)

    def transaction_value_is_not_none(self):
        with pytest.raises(ParamNotValidated):
            Transaction(type=TransactionTypeEnum, current_balance=1000.0, timestamp=123456789.0)

    def test_transaction_value_is_not_float(self):
        with pytest.raises(ParamNotValidated):
            Transaction(type=TransactionTypeEnum.DEPOSIT, value= "oi", current_balance=1000.0, timestamp=123456789.0)

    def test_transaction_value_is_not_positive(self):
        with pytest.raises(ParamNotValidated):
            Transaction(type=TransactionTypeEnum.DEPOSIT, value= -250.0, current_balance=1000.0, timestamp=123456789.0)
    
    def test_transaction_current_balance_is_none(self):
        with pytest.raises(ParamNotValidated):
            Transaction(type=TransactionTypeEnum.DEPOSIT, value=250.0, timestamp=123456789.0)
    
    def test_transaction_current_balance_is_not_float(self):
        with pytest.raises(ParamNotValidated):
            Transaction(type=TransactionTypeEnum.DEPOSIT, value=250.0, current_balance="1000.0", timestamp=123456789.0)
    
    def test_transaction_current_balance_is_not_positive(self):
        with pytest.raises(ParamNotValidated):
            Transaction(type=TransactionTypeEnum.DEPOSIT, value=250.0, current_balance=-1000.0, timestamp=123456789.0)

    def test_transaction_timestamp_is_none(self):
        with pytest.raises(ParamNotValidated):
            Transaction(type=TransactionTypeEnum.DEPOSIT, value=250.0, current_balance=1000.0)
    
    def test_transaction_timestamp_is_not_float(self):
        with pytest.raises(ParamNotValidated):
            Transaction(type=TransactionTypeEnum.DEPOSIT, value=250.0, current_balance=1000.0, timestamp="123456789")






