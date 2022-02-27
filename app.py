#!/usr/bin/env python
# coding: utf-8

# In[11]:


import datetime
import streamlit as st
import pickle
import numpy as np
import pandas as pd
#load the model and dataframe
df = pd.read_csv("df1.csv")
pipe = pickle.load(open("flight_rf.pkl", "rb"))
st.title("Flight fare prediction")
st.subheader("Select Airline")
airline = st.selectbox("  " , ["Air India","GoAir","IndiGo","Jet Airways","Multiple carriers","SpiceJet",
                                    "Vistara","Air Asia"])

if airline == "Jet Airways":
    air_inp = 0
elif airline == "IndiGo":
    air_inp = 1
elif airline == "Air India":
    air_inp = 2
elif airline == "Multiple carriers":
    air_inp = 3
elif airline == "SpiceJet":
    air_inp = 4
elif airline == "Vistara":
    air_inp = 5
elif airline == "Air Asia":
    air_inp = 6
elif airline == "GoAir":
    air_inp = 7

st.write("Airline -- " , airline)

st.subheader("Select Source")
source = st.selectbox(" " , ['Bangalore', 'Mumbai','Delhi','Kolkata',"Chennai"])
if source == "Bangalore":
    source_inp = 0
elif source == "Chennai":
    source_inp = 1
elif source == "Delhi":
    source_inp = 2
elif source == "Kolkata":
    source_inp = 3
elif source == "Mumbai":
    source_inp = 4
    
st.write("Source -- " , source)
    
st.subheader("Select Destination")
dest = st.selectbox("" , ['Bangalore', 'Cochin', 'Hyderabad',"New Delhi",'Delhi','Kolkata'])

if dest == "Bangalore":
    dest_inp = 0
elif dest == "Cochin":
    dest_inp = 1
elif dest == "Delhi":
    dest_inp = 2
elif dest == "Hyderabad":
    dest_inp = 3
elif dest == "Kolkata":
    dest_inp = 4
elif dest == "New Delhi":
    dest_inp = 5
st.write("Destination -- ",dest)

st.subheader("Select Destination")
stops = st.selectbox("" , ['0','1','2','3','4','4'])


if stops == "Bangalore":
    stops_inp = 0
elif dest == "Cochin":
    stops_inp = 1
elif dest == "Delhi":
    stops_inp = 2
elif dest == "Hyderabad":
    stops_inp = 3
elif dest == "Kolkata":
    stops_inp = 4
elif dest == "New Delhi":
    stops_inp = 5
st.write("Number of stops -- ",stops)


st.sidebar.subheader("Select Departure")
m = pd.to_datetime("today").month
d = pd.to_datetime("today").day
y = pd.to_datetime("today").year
    
dep = st.sidebar.date_input("Day" , datetime.date(y,m,d))
if dep is not None:
    mon_d = dep.month
    day_d = dep.day

    hour_1 = st.sidebar.selectbox("Hour", list(range(1,25)))
    minute_1 = st.sidebar.selectbox("Minute", list(range(0,61)))
    
st.subheader("Departure Time :")
x = "2021" + "/"  +str(mon_d) + "/" + str(day_d) + " " + str(hour_1) + ":" + str(minute_1)
if x is not None:
        
    op = pd.to_datetime([x])
    if op is not None:
        st.write(op.item())
st.sidebar.subheader("Select Arrival")
arr = st.sidebar.date_input("Day." , datetime.date(y,m,d+1))
if arr is not None:
    
    mon_a = arr.month
    day_a = arr.day
        
        

    hour_2 = st.sidebar.selectbox("Hour.", list(range(1,25)) ,2)
    minute_2 = st.sidebar.selectbox("Minute.", list(range(0,61)))

st.subheader("Arrival Time :")
x1 = "2021" + "/"  +str(mon_a) + "/" + str(day_a) + " " + str(hour_2) + ":" + str(minute_2)
if x1 is not None:
        
    op1 = pd.to_datetime([x1] )
    if op1 is not None:
        st.write(op1.item())
if st.checkbox("Duration"):
    if op1 is not None:
            
        st.write((op1.item() - op.item()))

    
op2 = str(op1-op)
if op2 is not None:
    hr = int(op2.split(']')[0][-9:-7])
    mini = int(op2.split(']')[0][-6:-4])
    
rfr_model = pickle.load(open("flight_rf.pkl", "rb"))

par = [air_inp , source_inp , dest_inp ,stops , mon_d , day_d , hour_1 , minute_1 , hour_2 ,minute_2 ,hr , mini]

    
    
if st.checkbox("PREDICT"):
    pred = rfr_model.predict([par])
    for i in pred:
        st.write("Your Fare Price is : " , round(i ,3)  , "INR")
        st.write("*Happy and Safe Journey ...*")









    




# In[ ]:




