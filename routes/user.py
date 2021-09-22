#Nota. En este punto es necesario instalar el package cryptography o tirara error 

from inspect import Arguments
from os import name
from fastapi import APIRouter, Response  #Permite definir subrutas por separado
from config.db import conn     #Importamos la conexion a la base datos(Permite interactuar con ella)
from models.user import users
from schemas.user import User, UserUpdate
from cryptography.fernet import Fernet   #Con Fernet se puede crear funcion que permite cifrar
from starlette.status import HTTP_204_NO_CONTENT
from fastapi.encoders import jsonable_encoder
import http3
import requests

key = Fernet.generate_key()
f = Fernet(key)              #En f queda una funcion con la que podemos cifrar lo que queramos

client = http3.AsyncClient()

async def call_api(url: str):
    r = await client.get(url)
    return r.json()

user = APIRouter()

@user.get("/users")
def get_users():
        return conn.execute(users.select()).fetchall()  #Hace un select y trae todo de la tabla users

@user.post("/users")
def create_user(user: User):
        new_user = {"name": user.name,
                    "email": user.email}
        new_user["password"] = f.encrypt(user.password.encode("utf-8"))
        result = conn.execute(users.insert().values(new_user))
        print(result.lastrowid)
        return conn.execute(users.select().where(users.c.id == result.lastrowid)).first()

@user.get("/users/{id}")
def get_oneuser(id: str):
        return conn.execute(users.select().where(users.c.id == id)).first()

@user.delete("/users/{id}")
def delete_user(id: str):
        conn.execute(users.delete().where(users.c.id == id))
        return Response(status_code=HTTP_204_NO_CONTENT)

@user.put("/users/{id}")
def update_user(id: str, user_updated: UserUpdate):
        print(user_updated)
        update_data = user_updated.dict(exclude_unset=True)
        print(update_data)
        conn.execute(users.update().values(update_data).where(users.c.id == id))
        return "Updated"

@user.get("/")
async def root():
    url = "https://jsonplaceholder.typicode.com/posts"
    result = await call_api(url)
    return result
     

@user.get("/s/")
def root():
    url = "https://jsonplaceholder.typicode.com/users"
    result = requests.get(url)
    return result.json()


@user.post("/s/")
def root():
    url = "https://jsonplaceholder.typicode.com/posts"
    result = requests.post(url)
    return result.json()