import streamlit as st
import pickle
import numpy as np
from sklearn import *

pipe = pickle.load(open('pipe5.pkl', 'rb'))

df = pickle.load(open('df5.pkl', 'rb'))


st.set_page_config(page_title="Employee Prediction App")


st.title("Will Employee stay or leave?")

col1, col2, col3 = st.columns(3)

with col1:
#satisfacation
    satisfaction = st.number_input('Satisfaction level')
with col1:
#last evaluation
    evaluation = st.number_input('last evaluation')
with col1:
#projects
    project=st.selectbox('No. of project', df['number_project'].unique())
with col2:
#avg_monthly_hrs
    avg_month_hrs=st.slider('Average Monthly Hours',80.0,350.0)
with col2:
#time_spend
    time_spend=st.slider('Time Spent in the company',1.0,12.0)
with col2:
#work_accident
    work_accident=st.selectbox('Work accident', df['Work_accident'].unique())
with col3:
#promotion_last_5years
    promotion_last_5years=st.selectbox('Promotion in last 5 years', df['promotion_last_5years'].unique())

with col3:
#Department
    Department=st.selectbox('Department', df['Department'].unique())

with col3:
#salary
    salary=st.selectbox('salary | 0->Low | 1->Medium | 2->High', df['salary'].unique())



if st.button('Predict whether employee will stay or leave'):
    
    query = np.array([satisfaction,evaluation,project,avg_month_hrs,time_spend,work_accident,promotion_last_5years,Department,salary])

    query = query.reshape(1, 9)
    if(int(pipe.predict(query))==0):
       st.title("The employee will stay")
    else:
       st.title("The employee will not stay")
    
    



