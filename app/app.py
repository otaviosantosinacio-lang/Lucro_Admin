from fastapi import FastAPI

app = FastAPI

@app.get("/")
def home():
    boas_vindas = {'Olá usuário, seja bem-vindo ao Lucro Admin, um sistema financeiro Albha Store'}
    return boas_vindas