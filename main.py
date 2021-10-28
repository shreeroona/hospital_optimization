from flask import Flask, request
import numpy as np
import pandas as pd
import pickle
from flasgger import Swagger
import sklearn


app = Flask(__name__)
Swagger(app)

pickled_model = open("Pickle_file_ho.pkl","rb")
model = pickle.load(pickled_model)

@app.route("/")
def home():
    return "Welcome to Hosptial Optimization App"
@app.route('/predict')



def forecast_netamount():

    """ Forecast the Hospital billing
    ---

    parameters:
     - name: days
       in: query
       type: number
       required: true
    responses:
       200:
            
            description: Result is
    """
    days = request.args.get("days",type = int)
    forecast = model.forecast(days)
    return f"The forecast is {forecast}"



if __name__ == "__main__":
    
    app.run()
