from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# criando rota raiz
@app.get('/')
def root():
    return {'Hello': 'World'}

# criando modelo
class User(BaseModel):
    id: int
    email: str
    password: str


