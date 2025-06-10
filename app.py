from fastapi import FastAPI
from fastapi.responses import JSONResponse
from typing import Literal, Annotated,Union
import pickle
import pandas as pd
from pydantic import BaseModel, Field
import pickle
from ui import UserInput




app = FastAPI()


with open("models\\model.pickle",'rb') as f:
    model=pickle.load(f)



# usein=UserInput(Age=25,Gender="Male",Education_Level="Bachelor's",Job_Title="Data Analyst",Years_of_Experience=1)



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
    


 