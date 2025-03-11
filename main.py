from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "테스트입니다"}

@app.get("/ping")
def ping():
    return {"message": "pong!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
