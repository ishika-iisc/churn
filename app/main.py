from fastapi import FastAPI
from app.schema import CustomerData
from app.model_loader import predict_churn

app = FastAPI(title="Churn Prediction API")

@app.get("/")
def home():
    return {"status":"API is running"}

@app.post("/predict")
def predict(data: CustomerData):
    result = predict_churn(data.dict())
    return {"churn_prediction": result}