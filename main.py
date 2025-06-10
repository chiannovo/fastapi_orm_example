'''
Author: ChiaEnKang
Date: 2025-06-11 02:27:06
LastEditors: ChiaEnKang
LastEditTime: 2025-06-11 03:07:34
'''
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine
import models
from routers.users import router as users_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router, prefix="/api/users")

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Project"}
