from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pickle
import pandas as pd
import pickle
from models.user_input_validation import UserInput




app = FastAPI()


with open("models\\model.pickle",'rb') as f:
    model=pickle.load(f)

 
@app.get("/")
def add():
    return  JSONResponse(content={"desc":"salary predictor api"})


@app.post("/predict")
def predict(data:UserInput):
    
    ip_df=pd.DataFrame([{
        "Age":data.Age,
        "Gender":data.Gender,
        "Education Level":data.Education_Level,
        "Job Title":data.Job_Title,
        "Years of Experience":data.Years_of_Experience
         
    }])
    
    try:
        pred=model.predict(ip_df)[0]
        return  JSONResponse(content={"prediction":pred})
    except Exception as e:
        return  JSONResponse(content={"error":str(e)})
    


 