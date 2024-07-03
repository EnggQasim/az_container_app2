from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"Hello": "World1"}

@app.get("/about")
def index():
    return {"Institute Name": "PIAIC"}