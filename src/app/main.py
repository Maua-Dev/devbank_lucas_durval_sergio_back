from fastapi import FastAPI, HTTPException
from mangum import Mangum

from .environments import Environments

from .repo.user_repository_mock import UserRepositoryMock

from .repo.transaction_repository_mock import TransactionRepositoryMock

from .errors.entity_errors import ParamNotValidated

from .enums.transaction_type_enum import TransactionTypeEnum

from .entities.user import User

from .entities.transaction import Transaction

import time

from src.app.enums import transaction_type_enum


app = FastAPI()

repo_user = Environments.get_user_repo()()
repo_transaction = Environments.get_transaction_repo()()

# @app.get("/items/get_all_items")
# def get_all_items():
#     items = repo.get_all_items()
#     return {
#         "items": [item.to_dict() for item in items]
#     }


# @app.post("/items/create_item", status_code=201)
# def create_item(request: dict):
#     item_id = request.get("item_id")
    
#     validation_item_id = Item.validate_item_id(item_id=item_id)
#     if not validation_item_id[0]:
#         raise HTTPException(status_code=400, detail=validation_item_id[1])
    
#     item = repo.get_item(item_id)
#     if item is not None:
#         raise HTTPException(status_code=409, detail="Item already exists")
    
#     name = request.get("name")
#     price = request.get("price")
#     item_type = request.get("item_type")
#     if item_type is None:
#         raise HTTPException(status_code=400, detail="Item type is required")
#     if type(item_type) != str:
#         raise HTTPException(status_code=400, detail="Item type must be a string")
#     if item_type not in [possible_type.value for possible_type in ItemTypeEnum]:
#         raise HTTPException(status_code=400, detail="Item type is not a valid one")
    
#     admin_permission = request.get("admin_permission")
    
#     try:
#         item = Item(name=name, price=price, item_type=ItemTypeEnum[item_type], admin_permission=admin_permission)
#     except ParamNotValidated as err:
#         raise HTTPException(status_code=400, detail=err.message)
    
#     item_response = repo.create_item(item, item_id)
#     return {
#         "item_id": item_id,
#         "item": item_response.to_dict()    
#     }
    
# @app.delete("/items/delete_item")
# def delete_item(request: dict):
#     item_id = request.get("item_id")
    
#     validation_item_id = Item.validate_item_id(item_id=item_id)
#     if not validation_item_id[0]:
#         raise HTTPException(status_code=400, detail=validation_item_id[1])
    
#     item = repo.get_item(item_id)
    
#     if item is None:
#         raise HTTPException(status_code=404, detail="Item Not found")
    
#     if item.admin_permission == True:
#         raise HTTPException(status_code=403, detail="Item Not found")
    
#     item_deleted = repo.delete_item(item_id)
    
#     return {
#         "item_id": item_id,
#         "item": item_deleted.to_dict()    
#     }
    
# @app.put("/items/update_item")
# def update_item(request: dict):
#     item_id = request.get("item_id")
    
#     validation_item_id = Item.validate_item_id(item_id=item_id)
#     if not validation_item_id[0]:
#         raise HTTPException(status_code=400, detail=validation_item_id[1])
    
#     item = repo.get_item(item_id)
    
#     if item is None:
#         raise HTTPException(status_code=404, detail="Item Not found")
    
#     if item.admin_permission == True:
#         raise HTTPException(status_code=403, detail="Item Not found")
    
#     name = request.get("name")
#     price = request.get("price")
#     admin_permission = request.get("admin_permission")
    
#     item_type_value = request.get("item_type")
#     if item_type_value != None:
#         if type(item_type_value) != str:
#             raise HTTPException(status_code=400, detail="Item type must be a string")
#         if item_type_value not in [possible_type.value for possible_type in ItemTypeEnum]:
#             raise HTTPException(status_code=400, detail="Item type is not a valid one")
#         item_type = ItemTypeEnum[item_type_value]
#     else:
#         item_type = None
        
#     item_updated = repo.update_item(item_id, name, price, item_type, admin_permission)
    
#     return {
#         "item_id": item_id,
#         "item": item_updated.to_dict()    
#     }

@app.get("/")
def get_user(user_id: int):
    
    user = repo_user.get_user(user_id)
    
    if user is None:
        raise HTTPException(status_code=404, detail="User Not found")

    return {
        "name": user.name,
        "agency": user.agency.to_dict(),
        "account": user.account.to_dict(),
        "current_balance": user.current_balance.to_dict(),
    }

@app.post("/deposit")
def create_deposit(request: dict):

    # dicionário com os valores
    dois = request.get("2")
    cinco = request.get("5")
    dez = request.get("10")
    vinte = request.get("20")
    cinquenta = request.get("50")
    cem = request.get("100")
    duzentos = request.get("200")

    total_depositado = dois*2 + cinco*5 + dez*10 + vinte*20 + cinquenta*50 + cem*100 + duzentos*200

    if total_depositado > user.current_balance:
        raise HTTPException(status_code=403, detail="Depósito suspeito")
    
    user = get_user(1)

    timestamp = int(time.time() * 1000)
    transaction = Transaction(TransactionTypeEnum.DEPOSIT, total_depositado, user.current_balance, timestamp)

    user.current_balance += total_depositado

@app.post("/withdraw")
def create_withdraw(request: dict):
    
    # dicionário com os valores
    dois = request.get("2")
    cinco = request.get("5")
    dez = request.get("10")
    vinte = request.get("20")
    cinquenta = request.get("50")
    cem = request.get("100")
    duzentos = request.get("200")
    
    total_depositado = dois*2 + cinco*5 + dez*10 + vinte*20 + cinquenta*50 + cem*100 + duzentos*200

    user = get_user(1)

    if user.current_balance < total_depositado:
        raise HTTPException(status_code=403, detail="Saldo insuficiente")

    transaction = Transaction(TransactionTypeEnum.WITHDRAW, request.get("value"))

    user.current_balance -= total_depositado

@app.get("/history")
def get_all_transactions():
    
    transactions = repo_transaction.get_transaction_repo()
    return {
        "all_transactions": [transactions.to_dict() for transaction in transactions]
    }

handler = Mangum(app, lifespan="off")
