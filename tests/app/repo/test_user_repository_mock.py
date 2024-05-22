import pytest
from src.app.entities.user import User
from src.app.repo.user_repository_mock import UserRepositoryMock

class Test_ItemRepositoryMock:
    
    #  def test_get_all_users(self):
    #      repo = UserRepositoryMock()
    #      assert all([item_expect == item for item_expect, item in zip(repo.items.values(), repo.get_all_items())]) 
       
     def test_get_user(self):
         repo = UserRepositoryMock()
         user = repo.get_user(user_id=1)
         assert user == repo.users.get(1)
   
     def test_get_user_not_found(self):
         repo = UserRepositoryMock()
         user = repo.get_user(user_id=10)
         assert user is None
       
     def test_create_user(self):
         repo = UserRepositoryMock()
         len_before = len(repo.users)
         user = User(name="test", agency="0000", account="00000-0", current_balance=1.0)
         repo.create_user(user=user, user_id=0)
         len_after = len(repo.users)
         assert len_after == len_before + 1
         assert repo.users.get(0) == user
       
     def test_delete_user(self):
         repo = UserRepositoryMock()
         user_expected_to_be_deleted = repo.users.get(1)
         len_before = len(repo.users)
       
         user = repo.delete_user(user_id=1)
         len_after = len(repo.users)
         assert len_after == len_before - 1
         assert user == user_expected_to_be_deleted
       
     def test_delete_item_not_found(self):
         repo = UserRepositoryMock()
         user = repo.delete_user(user_id=10)
         assert user is None
       
     def test_update_item(self):
         repo = UserRepositoryMock()
         user = User(name="test", agency="0000", account="00000-0", current_balance=1.0)
         user_updated = repo.update_user(user_id=1, name=user.name, account=user.account, agency=user.agency, current_balance=user.current_balance)
       
         assert user_updated == user
         assert repo.users.get(1) == user
       
     def test_update_user_partial_1(self):
         repo = UserRepositoryMock()
         name = "test"
         user_updated = repo.update_user(user_id=1, name=name)
       
         assert user_updated.name == name
         assert repo.users.get(1).name == name
       
     def test_update_user_partial_2(self):
         repo = UserRepositoryMock()
         account = "0000"
         user_updated = repo.update_user(user_id=1, account=account)
       
         assert user_updated.account == account
         assert repo.users.get(1).account == account