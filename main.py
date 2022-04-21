from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Rota Raiz
@app.get('/')
def root():
    return {'Hello': 'World'}