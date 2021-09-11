# BasicFastAPI-MySQL

A virtual environment must be previously created, in this case it was created with conda and named: fastapi-mysql


## Activate the virtual environment:

```console
conda activate fastapi-mysql
```


## Install critical dependencies

```console
pip install fastapi uvicorn
```


## Run the project with uvicorn

This means, run app function in app module

```console
uvicorn app:app --reload
```



