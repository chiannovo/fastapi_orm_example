'''
Author: ChiaEnKang
Date: 2025-06-11 02:28:27
LastEditors: ChiaEnKang
LastEditTime: 2025-06-11 02:28:42
'''
from datetime import datetime
from sqlalchemy import Column, DateTime
from database import Base

class BaseModel(Base):
    __abstract__ = True
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
