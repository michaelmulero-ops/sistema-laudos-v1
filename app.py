import streamlit as st  # Esta linha resolve o NameError
import google.generativeai as genai
import hashlib
from datetime import datetime

# Configuração de Identidade visual - Michael Mulero Inspeções
st.set_page_config(page_title="Michael Mulero Tech V1", layout="wide")

# Interface de Blindagem Industrial - USITRORG AMBIENTAL
with st.expander("🛡️ Painel de Blindagem Industrial - USITRORG AMBIENTAL"):
    col1, col2, col3 = st.columns(3)
    col1.metric("IS Total Gerenciada", "R$ 47M")
    col2.metric("Fotos Rastreadas", "347")
    col3.metric("Alertas Pendentes", "3")
