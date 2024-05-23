from urllib import response
from fastapi.exceptions import HTTPException
import pytest
from src.app import repo
from src.app.entities.user import User
from src.app.entities.transaction import Transaction
from src.app.enums.transaction_type_enum import TransactionTypeEnum
from src.app.main import get_user, create_deposit, create_withdraw, get_all_transactions
from src.app.repo.user_repository_mock import UserRepositoryMock
from src.app.repo.transaction_repository_mock import TransactionRepositoryMock

class Test_Main:
    # def test_get_all_items(self):
    #     repo = ItemRepositoryMock()
    #     response = get_all_items()
    #     assert all([item_expect.to_dict() == item for item_expect, item in zip(repo.items.values(), response.get("items"))]) 
        
    def test_get_user(self):
        repo = UserRepositoryMock()
        response = get_user()
        assert response == {
            'user': repo.users[0].to_dict()
        }
        
#     def test_get_user_id_is_none(self):
        
#         item_id = None
#         with pytest.raises(HTTPException) as err:
#             get_item(item_id=item_id)
    
#     def test_get_item_id_is_not_int(self):
#         item_id = '1'
#         with pytest.raises(HTTPException) as err:
#             get_item(item_id=item_id)
            
#     def test_get_item_id_is_not_positive(self):
#         item_id = -1
#         with pytest.raises(HTTPException) as err:
#             get_item(item_id=item_id)
            
    def test_create_deposit(self):
        repo = TransactionRepositoryMock()
        
        body = {
            "2": 1,
            "5": 1,
            "10": 1,
            "20": 1,
            "50": 1,
            "100": 1,
            "200": 1
        }
        response = create_deposit(request=body)
        print(response)
        assert response == {'transaction': {'type': 'DEPOSIT', 'value': 387.0, 'current_balance': 1000.0, 'timestamp': 1.0}}

    def test_create_deposit_suspect(self):
        repo = TransactionRepositoryMock()

        body = {
            "2": 1,
            "5": 1,
            "10": 1,
            "20": 1,
            "50": 1,
            "100": 1,
            "200": 100
        }
        response = create_deposit(request=body)
        with pytest.raises(HTTPException) as err:
            assert response == {'transaction': {'type': 'DEPOSIT', 'value': 387.0, 'current_balance': 1000.0, 'timestamp': 1.0}}


    def test_create_withdraw(self):
        repo = TransactionRepositoryMock()
        
        body = {
            "2": 1,
            "5": 1,
            "10": 1,
            "20": 1,
            "50": 1,
            "100": 1,
            "200": 1
        }
        response = create_withdraw(request=body)
        print(response)
        assert response == {'withdraw': {'type': 'WITHDRAW', 'value': 387.0, 'current_balance': 1000.0, 'timestamp': 1.0}}
 
#     def test_create_item_conflict(self):
#         repo = ItemRepositoryMock()
        
#         body = {
#             'item_id': 1,
#             'name': 'test',
#             'price': 1.0,
#             'item_type': 'TOY',
#             'admin_permission': False
#         }
#         with pytest.raises(HTTPException) as err:
#             create_item(request=body)
    
#     def test_create_item_missing_id(self):
#         body = {
#             'name': 'test',
#             'price': 1.0,
#             'item_type': 'TOY',
#             'admin_permission': False
#         }
#         with pytest.raises(HTTPException) as err:
#             create_item(request=body)
        
#     def test_create_item_id_is_not_int(self):
#         body = {
#             'item_id': '0',
#             'name': 'test',
#             'price': 1.0,
#             'item_type': 'TOY',
#             'admin_permission': False
#         }
#         with pytest.raises(HTTPException) as err:
#             create_item(request=body)
    
#     def test_create_item_id_is_not_positive(self):
#         body = {
#             'item_id': -1,
#             'name': 'test',
#             'price': 1.0,
#             'item_type': 'TOY',
#             'admin_permission': False
#         }
#         with pytest.raises(HTTPException) as err:
#             create_item(request=body)
            
#     def test_create_item_missing_type(self):
#         body = {
#             'item_id': 1,
#             'name': 'test',
#             'price': 1.0,
#             'admin_permission': False
#         }
#         with pytest.raises(HTTPException) as err:
#             create_item(request=body)
            
#     def test_create_item_item_type_is_not_string(self):
#         body = {
#             'item_id': 1,
#             'name': 'test',
#             'price': 1.0,
#             'item_type': 1,
#             'admin_permission': False
#         }
#         with pytest.raises(HTTPException) as err:
#             create_item(request=body)
            
#     def test_create_item_item_type_is_not_valid(self):
#         body = {
#             'item_id': 1,
#             'name': 'test',
#             'price': 1.0,
#             'item_type': 'test',
#             'admin_permission': False
#         }
#         with pytest.raises(HTTPException) as err:
#             create_item(request=body)
            
#     def test_create_item_param_not_validated(self):
#         body = {
#             'item_id': 1,
#             'name': '',
#             'price': 1.0,
#             'item_type': 'TOY',
#             'admin_permission': False,
#         }
#         with pytest.raises(HTTPException) as err:
#             create_item(request=body)
            
#     def test_delete_item(self):
#         body = {
#             "item_id": 1
#         }
#         response = delete_item(request=body)
#         assert response == {'item_id': 1, 'item': {'name': 'Barbie', 'price': 48.9, 'item_type': 'TOY', 'admin_permission': False}}
        
#     def test_delete_item_missing_id(self):
#         with pytest.raises(HTTPException) as err:
#             delete_item(request={})
            
#     def test_delete_item_id_is_not_int(self):
#         body = {
#             "item_id": '1'
#         }
#         with pytest.raises(HTTPException) as err:
#             delete_item(request=body)
            
#     def test_delete_item_id_not_found(self):
#         body = {
#             "item_id": 100
#         }
#         with pytest.raises(HTTPException) as err:
#             delete_item(request=body)
            
#     def test_delete_item_id_not_positive(self):
#         body = {
#             "item_id": -100
#         }
#         with pytest.raises(HTTPException) as err:
#             delete_item(request=body)
            
#     def test_delete_item_without_admin_permission(self):
#         body = {
#             "item_id": 4
#         }
#         with pytest.raises(HTTPException) as err:
#             delete_item(request=body)
            
#     def test_update_item(self):
#         body = {
#             "item_id": 2,
#             "name": "test",
#             "price": 1.0,
#             "item_type": "TOY",
#             "admin_permission": False
#         }
#         response = update_item(request=body)
#         assert response == {'item_id': 2, 'item': {'name': 'test', 'price': 1.0, 'item_type': 'TOY', 'admin_permission': False}}
        
#     def test_update_item_missing_id(self):
#         body = {
#             "name": "test",
#             "price": 1.0,
#             "item_type": "TOY",
#             "admin_permission": False
#         }
#         with pytest.raises(HTTPException) as err:
#             update_item(request=body)
    
#     def test_update_item_id_is_not_int(self):
#         body = {
#             "item_id": "1",
#             "name": "test",
#             "price": 1.0,
#             "item_type": "TOY",
#             "admin_permission": False
#         }
#         with pytest.raises(HTTPException) as err:
#             update_item(request=body)
            
#     def test_update_item_not_positive(self):
#         body = {
#             "item_id": -1,
#             "name": "test",
#             "price": 1.0,
#             "item_type": "test",
#             "admin_permission": False
#         }
#         with pytest.raises(HTTPException) as err:
#             update_item(request=body)
            
#     def test_update_item_not_found(self):
#         body = {
#             "item_id": 1,
#             "name": "test",
#             "price": 1.0,
#             "item_type": "test",
#             "admin_permission": False
#         }
#         with pytest.raises(HTTPException) as err:
#             update_item(request=body)
            
#     def test_update_item_without_admin_permission(self):
#         body = {
#             "item_id": 4,
#             "name": "test",
#             "price": 1.0,
#             "item_type": "TOY",
#             "admin_permission": False
#         }
#         with pytest.raises(HTTPException) as err:
#             update_item(request=body)
    
#     def test_update_item_type_not_string(self):
#         body = {
#             "item_id": 1,
#             "name": "test",
#             "price": 1.0,
#             "item_type": 1,
#             "admin_permission": False
#         }
#         with pytest.raises(HTTPException) as err:
#             update_item(request=body)
            
#     def test_update_item_type_not_valid(self):
        
#         body = {
#             "item_id": 1,
#             "name": "test",
#             "price": 1.0,
#             "item_type": "test",
#             "admin_permission": False
#         }
#         with pytest.raises(HTTPException) as err:
#             update_item(request=body)
            