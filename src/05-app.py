# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 10:24:41 2022

@author: amado
"""

import streamlit as st
import numpy as np
import joblib 
import warnings




warnings.filterwarnings("ignore")






st.write(""" ## Car Evaluation""")

st.image("""img.jpg""")


st.write(""" ### User Inputs """)


def UserInputs():
    
    buyingPrice = st.selectbox("Buying Price",("Low","Medium","Hight","Very Hight"))
    maintenanceCost = st.selectbox("Maintenance Cost",("Low","Medium","Hight","Very Hight"))
    numberDors = st.radio("Numbers of Doors",(2,4,5))
    numberPersons =  st.radio("Numbers of Persons",(2,4,"More"))
    lugBoot = st.selectbox("Lug Boot",("Low","Medium","Hight"))
    safety = st.selectbox("Safety",("Low","Medium","Hight"))
    
    return buyingPrice,maintenanceCost,numberDors,numberPersons,lugBoot,safety
    
    

def preprocess():
    
    buyingPrice,maintenanceCost,numberDors,numberPersons,lugBoot,safety = UserInputs()
    
    buyingPrice = np.where(buyingPrice == "Low",0,buyingPrice)
    buyingPrice = np.where(buyingPrice == "Medium",1,buyingPrice)
    buyingPrice = np.where(buyingPrice == "Hight",2,buyingPrice)
    buyingPrice = np.where(buyingPrice == "Very Hight",3,buyingPrice)
    
    maintenanceCost = np.where(maintenanceCost == "Low",0,buyingPrice)
    maintenanceCost = np.where(maintenanceCost == "Medium",1,buyingPrice)
    maintenanceCost = np.where(maintenanceCost == "Hight",2,buyingPrice)
    maintenanceCost = np.where(maintenanceCost == "Very Hight",3,buyingPrice)
    
    
    numberPersons = np.where(numberPersons == "More",5,numberPersons)
    
    
    lugBoot = np.where(lugBoot == "Low",0,lugBoot)
    lugBoot = np.where(lugBoot == "Medium",1,lugBoot)
    lugBoot = np.where(lugBoot == "Hight",2,lugBoot)
    
    
    safety = np.where(safety == "Low",0,safety)
    safety = np.where(safety == "Medium",1,safety)
    safety = np.where(safety == "Hight",2,safety)
    
    
    
    inputs = [[buyingPrice,maintenanceCost,numberDors,numberPersons,lugBoot,safety]]
    inputs = np.array(inputs).astype(np.int64)
    
    
    
    return inputs
    
    



def predict():
    
    newData = preprocess()
    
    
    url = "car_evaluation_model.pkl"
    model = joblib.load(url)
    pred = model.predict(newData)
    
    if pred == 0:
        pred = "Unacceptable"
        
    if pred == 1:
        pred = "Acceptable"
        
    if pred == 2:
        pred = "Good"
        
    if pred == 3:
        pred = "Very Good"
        
        
    
    if st.button(label='Predicted'):
        
        st.success(f'Recomendation : {pred} ')
        
        
    

    
if __name__ == '__main__':
    
    predict()
