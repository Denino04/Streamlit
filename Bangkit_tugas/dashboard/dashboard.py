import numpy as np
import pandas as pd
import matplotlib as plt
import matplotlib.pyplot as mat
import seaborn as sea
import streamlit as lit

bikehour = pd.read_csv("https://raw.githubusercontent.com/Denino04/Streamlit/main/Bangkit_tugas/dashboard/Main%20Data%20(hour).csv")
bikehour = pd.DataFrame(bikehour)

lit.title("Analisis Penggunaan Sepeda")

tab1, tab2, tab3, tab4 = lit.tabs(["Temperature", "Weather", "Hour", "Air Quality"])

with tab1:
    lit.header("Temperature Graph")
    col1, col2 = lit.columns(2)
    
    with col1:
        fig = mat.figure(figsize=(20,8))
        ax = fig.add_subplot(1,1,1)

        ax.scatter(x=bikehour['cnt'], y=bikehour['temp'], color='blue')
        ax.set_xlabel('Bike Counts',size=15)
        ax.set_ylabel('Temperatures',size=15)
        lit.pyplot(fig)
        
    with col2:
        fig = mat.figure(figsize=(20,8))
        ax = fig.add_subplot(1,1,1)

        ax.scatter(x=bikehour['cnt'], y=bikehour['atemp'], color='Red')
        ax.set_xlabel('Bike Counts',size=15)
        ax.set_ylabel('A-Temperatures',size=15)
        lit.pyplot(fig)
    
with tab2:
    lit.header("Weather Graph")
    
    fig = mat.figure(figsize=(20,8))
    ax = fig.add_subplot(1,1,1)

    ax.scatter(x=bikehour['cnt'], y=bikehour['weathersit'], color='green')
    ax.set_xlabel('Bike Counts',size=15)
    ax.set_ylabel('Weather Situations',size=15)
    lit.pyplot(fig)
    
with tab3:
    lit.header("Hour Graph")
    
    fig = mat.figure(figsize=(20,8))
    ax = fig.add_subplot(1,1,1)

    ax.scatter(x=bikehour['cnt'], y=bikehour['hr'], color='black')
    ax.set_xlabel('Bike Counts',size=15)
    ax.set_ylabel('Hour',size=15)
    lit.pyplot(fig)
    
with tab4:
    lit.header("Air Quality Graph")
    
    col1, col2 = lit.columns(2)
    
    with col1:
        fig = mat.figure(figsize=(20,8))
        ax = fig.add_subplot(1,1,1)

        ax.scatter(x=bikehour['cnt'], y=bikehour['hum'], color='cyan')
        ax.set_xlabel('Bike Counts',size=15)
        ax.set_ylabel('Humidity',size=15)
        lit.pyplot(fig)
        
    with col2:
        fig = mat.figure(figsize=(20,8))
        ax = fig.add_subplot(1,1,1)

        ax.scatter(x=bikehour['cnt'], y=bikehour['windspeed'], color='lime')
        ax.set_xlabel('Bike Counts',size=15)
        ax.set_ylabel('Wind Speed',size=15)
        lit.pyplot(fig)
    
