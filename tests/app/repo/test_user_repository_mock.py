import pytest
from src.app.entities.user import User
from src.app.repo.user_repository_mock import UserRepositoryMock

class Test_ItemRepositoryMock:
    
    #  def test_get_all_users(self):
    #      repo = UserRepositoryMock()
    #      assert all([item_expect == item for item_expect, item in zip(repo.items.values(), repo.get_all_items())]) 
       
     def test_get_user(self):
         repo = UserRepositoryMock()
         user = repo.get_user()
         assert user == repo.users[0]
         assert user.name == "Vitor Soller"

       