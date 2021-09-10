from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

# meta es una propiedad para que sqlalchemy pueda saber mas propiedades acerca de la tabla
users = Table("users", meta, 
Column("id", Integer, primary_key=True), 
Column("name", String(255)), 
Column("email", String(255)), 
Column("password", String(255)))

#Una vez conectado a mysql (con engine), queremos que cree la tabla con meta.create_all
meta.create_all(engine)  