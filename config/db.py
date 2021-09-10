from sqlalchemy import create_engine, MetaData

#mysql+pymysql://user:password@localhost:3306/database

engine = create_engine("mysql+pymysql://root:password@localhost:3306/storedb") #Se guarda la conexion en engine

meta = MetaData()

conn = engine.connect()  #Metodo connect devuelve un objeto de conexion, cuando queramos interactuar con la db llamamos a la funcion conn

