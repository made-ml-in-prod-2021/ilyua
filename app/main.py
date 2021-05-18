from fastapi import FastAPI
import pickle
from pydantic import BaseModel
import numpy as np

app = FastAPI()
with open('model.pkl','rb') as f:
    model=pickle.load(f)

@app.get("/")
async def root():
    return {"message": "Hello World! Use /predict to inference my model!"}

class Request(BaseModel):
    f1: float
    f2: float
    f3: float
    f4: float

from fastapi.responses import PlainTextResponse
from fastapi.exceptions import RequestValidationError

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)

@app.post("/predict/")
async def create_item(request:Request):
    data=np.array(list(request.dict().values())).reshape(-1,4)
    print(data)
    return {'scores':model.predict_proba(data).tolist(),'prediction':model.predict(data).tolist()}
