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

repo_user = Environments.get_user_repo()
repo_transaction = Environments.get_transaction_repo()

@app.get("/")
def get_user():
    
    user = repo_user.get_user()
    
    if user is None:
        raise HTTPException(status_code=404, detail="User Not found")

    return {
        'user': user.to_dict()
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

    user = repo_user.get_user()

    if total_depositado > user.current_balance:
        raise HTTPException(status_code=403, detail="Depósito suspeito")

    timestamp = int(time.time() * 1000)
    transaction = Transaction(TransactionTypeEnum.DEPOSIT, float(total_depositado), user.current_balance, float(timestamp))

    user.current_balance += total_depositado

    return {
        "transaction": transaction.to_dict()
    }

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

    user = get_user()

    if user[0] < total_depositado:
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
