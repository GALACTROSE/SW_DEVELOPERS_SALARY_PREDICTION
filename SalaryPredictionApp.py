import streamlit as st
from predict_page_is import model_dt,model_linear,model_gradient
from explore_page import show_explore
from annotated_text import annotated_text

def annotated_message():
    annotated_text(
        ("🔵", "", ""),
        ("Hey there,", " ", "#063"),
        (" we developed ", " ", "#063"),
        ("Software Developers", " ", "#217"),
        ("Salary Predictor !", " ", "#217"),
    )

# Usage
annotated_message()



explore = st.sidebar.selectbox("Choose your option:",("Explore Data","Predict"))

if(explore=="Predict"):
    selection = st.sidebar.selectbox("Regression Model",("Decision Tree Regressor","Linear Regressor","Gradient Regressor"))
    if(selection=="Decision Tree Regressor"):
        model_dt()
    if(selection=="Linear Regressor"):
        model_linear()
    if(selection=="Gradient Regressor"):
        model_gradient()

if(explore=="Explore Data"):
    show_explore()
