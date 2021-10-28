from flask import Flask,request
import pickle
import pandas
app = Flask(__name__)

@app.route('/', methods=['GET'])
# Function that would be executed when the above URL is hit.

def welcome():
    return f"Hospital Optimization app"

pickled_model = open("Pickle_file_ho.pkl","rb")
model = pickle.load(pickled_model)

# Defining second url
@app.route('/')

# Function that should be executed when this URL is hit
def forecast():
    days = request.args.get("days",type = int)
    netamount = model.forecast(days).sum()
    return f"The forecast of net bill ammount for next {days} days is {netamount}"

if __name__ == "__main__":
    # Use debug only when required. With debug no need to stop the server every time.
    app.run(port=8080,host="0.0.0.0")