# REMOVA ESTA LINHA (Ela causa o erro no Streamlit):
# from google.colab import userdata 

# USE ESTA NO LUGAR (Padrão Streamlit):
import streamlit as st
api_key = st.secrets["GOOGLE_API_KEY"]
