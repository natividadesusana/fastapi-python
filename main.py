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

# criando banco de dados
data_base = [
    User(id=1, email='crodovaldo@crodovaldo.com.br', password='crodovaldo123'),
    User(id=2, email='cleonilde@cleonilde.com.br', password='cleonilde123')
]

# criando rota get all
@app.get('/users')
def get_all_users():
    return data_base

# criando rota get id
@app.get('/users/{id_user}')
def get_user_using_id(id_user: int):
    for user in data_base:
        if(user.id == id_user):
            return user
    
    return{'Status': 404, 'Message': 'User not found!'}
