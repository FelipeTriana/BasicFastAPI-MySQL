from fastapi import FastAPI
from routes.user import user

app = FastAPI()

app.include_router(user)   #Que la aplicacion incluya las rutas que vienen desde user