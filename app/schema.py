from pydantic import BaseModel

class CustomerData(BaseModel):
    tenure:int
    MonthlyCharges:float
    TotalCharges:float
    SeniorCitizen:float