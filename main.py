from flask import Flask, render_template,request
import streamlit as st

import numpy as np
import pandas as pd
import pickle

from streamlit.state.widgets import NoValue

pickled_model = open("Pickle_file_ho.pkl","rb")
model = pickle.load(pickled_model)

def forecast():
    st.title("Hospital Optimization App")
    days = st.number_input("Days for forecast",value=1)
    netamount = model.forecast(days).sum()
    result = ""
    if st.button("Show Result"):
        st.success(f"The forecast of net bill ammount for next {days} days is {netamount}")

if __name__ =="__main__":
    forecast()