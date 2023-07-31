from typing import Union

import conexao
 
import json 

from fastapi import FastAPI

app = FastAPI()

@app.get("/recomendacoes")
def getTeste():
 return {"teste":"teste"}

@app.get("/recomendacoes")
def getRecomendacoes():
    recomendacoes = []
    for recomendacao in conexao.collection.find():
        recomendacoes.append({"nome":recomendacao['nome'],
                              "tipo":recomendacao['tipo']})
    return recomendacoes
