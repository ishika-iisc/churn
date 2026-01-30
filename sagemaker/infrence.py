import joblib
import json
import os
import pandas as pd

def model_fn(model_dir):
    model_path = os.path.join(model_dir,"model.pkl")
    model = joblib.load(model_path)
    return model

def input_fn(request_body, request_content_type):
    if request_content_type == "application/json":
        data = json.load(request_body)
        return pd.DataFrame([data])
    
    raise ValueError(f"Unsupported content type:{request_content_type}")

def predict_fn(input_data,model):
    prediction = model.predict(input_data)
    return prediction[0]

def output_fn(prediction,response_content_type):
    result = "Yes" if prediction == 1 else "No"
    return json.dumps({"churn_prediction":result})