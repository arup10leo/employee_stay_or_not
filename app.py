import streamlit as st
import pickle
import numpy as np
from sklearn import *

pipe = pickle.load(open('pipe5.pkl', 'rb'))

df = pickle.load(open('df5.pkl', 'rb'))


st.set_page_config(page_title="Employee Prediction App")


st.title("Will Employee stay or leave?")


#satisfacation
satisfaction = st.number_input('Satisfaction level')

#last evaluation
evaluation = st.number_input('last evaluation')

#projects
project=st.selectbox('No. of project', df['number_project'].unique())

#avg_monthly_hrs
avg_month_hrs=st.slider('Average Monthly Hours',80.0,350.0)

#time_spend
time_spend=st.slider('Time Spent in the company',1.0,12.0)

#work_accident
work_accident=st.selectbox('Work accident', df['Work_accident'].unique())

#promotion_last_5years
promotion_last_5years=st.selectbox('Promotion in last 5 years', df['promotion_last_5years'].unique())


#Department
Department=st.selectbox('Department', df['Department'].unique())


#salary
salary=st.selectbox('salary | 0->Low | 1->Medium | 2->High', df['salary'].unique())



if st.button('Predict whether employee will stay or leave'):
    
    query = np.array([satisfaction,evaluation,project,avg_month_hrs,time_spend,work_accident,promotion_last_5years,Department,salary])

    query = query.reshape(1, 9)
    if(int(pipe.predict(query))==0):
       st.title("The employee will stay")
    else:
       st.title("The employee will not stay")
    
    # print(r)
    # if r==0:
    #     print("The employee will stay")
    # else:
    #     print("The employee will not stay")
# # symboling
# symboling = st.selectbox('Symboling', df['symboling'].unique())

# # aspiration
# aspiration = st.selectbox('aspiration', df['aspiration'].unique())

# # doornumber
# doors = st.selectbox('How many doors want?', df['doornumber'].unique())


# # carbody
# carbody = st.selectbox(
#     'Which type of carbody you are looking for?', df['carbody'].unique())


# # drivewheel
# drivewheel = st.selectbox(
#     'Which type of drivewheel needed?', df['drivewheel'].unique())

# # wheelbase
# wheelbase = st.number_input('wheelbase')

# # curbweight
# curbweight = st.selectbox('curbweight', df['curbweight'].unique())

# # enginetype
# enginetype = st.selectbox('enginetype', df['enginetype'].unique())

# # cylinder
# cylinder = st.selectbox('Number of cylinders', df['cylindernumber'].unique())

# # enginesize
# enginesize = st.slider('Engine Size', 65.0, 326.0)

# # fuel
# fuel = st.selectbox('fuelsystem', df['fuelsystem'].unique())


# # boreratio
# boreratio = st.selectbox('boreratio', df['boreratio'].unique())

# # stroke
# stroke = st.selectbox('stroke', df['stroke'].unique())

# # compressionratio
# compressionratio = st.selectbox(
#     'compressionratio', df['compressionratio'].unique())

# # horsepower
# horsepower = st.number_input('What will be the horsepower?')


# # rpm
# rpm = st.selectbox('RPM', [5000, 5500, 5800, 4250,
#                    5400, 5100, 4800, 6000, 4750, 4650, 4200])

# # citympg
# citympg = st.number_input('What will be the citympg?')

# # highwaympg
# highwaympg = st.number_input('What will be the highwaympg?')


# # volume
# vol = st.slider('Car Volume', 452700.0, 846000.0)

# # brand
# brand = st.selectbox('Prefered Brand', df['CarBrand'].unique())


#if st.button('Predict Price'):

#     query = np.array([])

#     query = query.reshape(1, 20)
#     st.title(np.exp(pipe.predict(query)))