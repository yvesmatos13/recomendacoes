from typing import Union

import conexao
 
import json 

from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

class Recomendacao(BaseModel):
    nome: str
    tipo: str

@app.get("/recomendacoes")
def getRecomendacoes():
    recomendacoes = []
    for recomendacao in conexao.collection.find():
        recomendacoes.append({"nome":recomendacao['nome'],
                              "tipo":recomendacao['tipo']})
    return recomendacoes

@app.post("/recomendacoes")
def postRecomendacoes(recomendacao: Recomendacao):
    recomendacao = recomendacao.dict()
    conexao.collection.insert_one({"nome":recomendacao["nome"],"tipo":recomendacao["tipo"]})
    return recomendacao
