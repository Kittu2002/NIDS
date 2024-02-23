# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 10:03:08 2024

@author: Balaji Kukkapalli
"""
#import warnings
#from sklearn.exceptions import InconsistentVersionWarning
#warnings.filterwarnings("ignore", category=InconsistentVersionWarning)
#import numpy as np
import pandas as pd
import streamlit as st
import pickle 

#loading saved model

loaded_model1=pickle.load(open("project_model_final.sav","rb"))
label_1=pickle.load(open("label_final_1.pkl","rb"))
label_2=pickle.load(open("label_final_2.pkl","rb"))
label_3=pickle.load(open("label_final_3.pkl","rb"))
loaded_model3=pickle.load(open("stand_final123.pkl","rb"))

#creating prediction

def network_intrusion(input_data1):
    
    #print(input_data1)
    #columns=["protocol_type","service","flag"]
    
    input_data1['protocol_type'] = label_1.transform(input_data1['protocol_type'])
    input_data1['service'] = label_2.transform(input_data1['service'])
    input_data1['flag'] = label_3.transform(input_data1['flag'])   
    
    #print(input_data1)
    
    #input_data2=np.asarray(input_data1)
    
    input_data3=loaded_model3.transform(input_data1)
    
    #print(input_data3)
    prediction = loaded_model1.predict(input_data3)
    #print(prediction)

    if (prediction[0] == 1):
      return '✅ This Network is safe to use ✅'
    else:
      return ' ❌ This Network is not Safe ❌ '
  
  
def main():
    
    
    # giving a title
    st.title('NETWORK INTRUSION DETECTION SYSTEM')
    
    
    # getting the input data from the user
    
    Protocol = st.text_input('Protocol Type')
    Service = st.text_input('Service')
    Flag = st.text_input('Flag')
    Source_Bytes = st.text_input('Source Bytes')
    Destination_Bytes = st.text_input('Destination Bytes')
    Count = st.text_input('Count')
    Same_srv_rate = st.text_input('Same srv rate')
    Different_srv_rate = st.text_input('Different srv rate')
    Dest_host_srv_count = st.text_input('Destination host srv count')
    Dest_host_same_srv_rate = st.text_input('Destination host same srv rate')
    input_data=pd.DataFrame({"protocol_type":[Protocol],"service":[Service],"flag":[Flag],"src_bytes":[Source_Bytes],"dst_bytes":[Destination_Bytes],"count":[Count],"same_srv_rate":[Same_srv_rate],"diff_srv_rate":[Different_srv_rate],"dst_host_srv_count":[Dest_host_srv_count],"dst_host_same_srv_rate":[Dest_host_same_srv_rate]})
    #input_data=pd.DataFrame({"protocol_type":["tcp"],"service":["remote_job"],"flag":["S0"],"src_bytes":[0],"dst_bytes":[0],"count":[270],"same_srv_rate":[0.09],"diff_srv_rate":[0.05],"dst_host_srv_count":[23],"dst_host_same_srv_rate":[0.09]})
    Intrusion = ''
     
    # creating a button for Prediction
    
    if st.button('Network Intrusion Detection Result'):
        Intrusion = network_intrusion(input_data)
    #print(Intrusion)
    st.success(Intrusion)
    
    
    
    
    
if __name__ == '__main__':
    main()
