'''
Author: ChiaEnKang
Date: 2025-06-11 02:28:51
LastEditors: ChiaEnKang
LastEditTime: 2025-06-11 02:28:58
'''
from sqlalchemy import Column, Integer, String
from .base import BaseModel

class User(BaseModel):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(255))
