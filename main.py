from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "테스트입니다"}

@app.get("/ping")
def ping():
    return {"message": "pong!"}