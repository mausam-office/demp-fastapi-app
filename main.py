from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/msg")
def some_msg():
    return {'msg': "Some important message on this request."}