from langchain_groq import ChatGroq
import os
import base64
import streamlit as st

# Directly assign API key here for testing
groq_api_key = st.secrets["general"]["GROQ_API_KEY"]

llm= ChatGroq(groq_api_key=groq_api_key, model_name="llama-3.2-90b-vision-preview")

if __name__=="__main__":
    response=llm.invoke("How do I build a neural network in python? provide code")
    print(response.content)
