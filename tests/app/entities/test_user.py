import pytest
from src.app.entities.user import User
from src.app.errors.entity_errors import  ParamNotValidated

class Test_User:
    def test_User(self):
        user = User(name="test", account="00000-0", agency="1.0", current_balance=1000.0)
        assert user.name == "test"
        assert user.account == "00000-0"
        assert user.agency == "1.0"
        assert user.current_balance == 1000.0
      
    def test_user_dict(self):
        user = User(name="test", account="00000-0", agency="1.0", current_balance=1000.0)
        assert user.to_dict() == {'name': 'test', 'account': '00000-0', 'agency': '1.0', 'current_balance': 1000.0}
  
    def test_user_name_is_none(self):
        with pytest.raises(ParamNotValidated):
            User(account="00000-0", agency="1.0", current_balance=1000.0)
          
    def test_user_name_is_not_string(self):
        with pytest.raises(ParamNotValidated):
            User(name=1.0, account="00000-0", agency=1.0, current_balance=1000.0)
          
    def test_user_account_is_none(self):
        with pytest.raises(ParamNotValidated):
            User(name="test", agency="1.0", current_balance=1000.0)
          
    def test_user_account_is_not_string(self):
        with pytest.raises(ParamNotValidated):
            User(name="test", account=1.0, agency="1.0", current_balance=1000.0)

    def test_user_account_not_in_pattern(self):
        with pytest.raises(ParamNotValidated):
            User(name="test", account="000-0", agency="1.0", current_balance=1000.0)
          
    def test_user_agency_is_none(self):
        with pytest.raises(ParamNotValidated):
            User(name="test", account="00000-0", current_balance=1000.0)
          
    def test_user_agency_is_not_string(self):
        with pytest.raises(ParamNotValidated):
            User(name="test", account="00000-0", agency=1.0, current_balance=1000.0)
          
    def test_user_current_balance_is_none(self):
        with pytest.raises(ParamNotValidated):
            User(name="test", account="00000-0", agency="1.0")
      
    def test_user_current_balance_is_not_float(self):
        with pytest.raises(ParamNotValidated):
            User(name="test", account="00000-0", agency="1.0", current_balance="1000.0")
