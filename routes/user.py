#Nota. En este punto es necesario instalar el package cryptography o tirara error 

from os import name
from fastapi import APIRouter, Response  #Permite definir subrutas por separado
from config.db import conn     #Importamos la conexion a la base datos(Permite interactuar con ella)
from models.user import users
from schemas.user import User
from cryptography.fernet import Fernet   #Con Fernet se puede crear funcion que permite cifrar
from starlette.status import HTTP_204_NO_CONTENT

key = Fernet.generate_key()
f = Fernet(key)              #En f queda una funcion con la que podemos cifrar lo que queramos

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
def update_user(id: str, user_updated: User):
        conn.execute(users.update().values(name = user_updated.name, 
                                           email = user_updated.email, 
                                           password = user_updated.password).where(users.c.id == id))
        return "Updated"
        