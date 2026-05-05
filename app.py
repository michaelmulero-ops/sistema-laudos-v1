import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. IDENTIDADE (Michael Mulero Inspeções)
st.set_page_config(page_title="S.I.T. - Michael Mulero", layout="wide")

# 2. CONFIGURAÇÃO DA API
# Cole sua chave aqui dentro das aspas
API_KEY = "AIzaSyAB6i7YEdIylcmamB3mlV64UlDLyYHlZ-g" 
genai.configure(api_key=API_KEY)

# 3. CONFIGURAÇÃO DO MODELO (Correção do erro da imagem image_2d8c95.png)
model = genai.GenerativeModel("gemini-1.5-flash")

# 4. PAINEL LATERAL
with st.sidebar:
    st.title("🛡️ Filtros")
    categoria = st.selectbox("Nível:", ["Indústria", "Transportadora", "E-commerce", "CD"])

# 5. INTERFACE PRINCIPAL
st.title("🛡️ Painel de Operação - Michael Mulero Inspeções")
fotos = st.file_uploader("Subir fotos da vistoria:", accept_multiple_files=True)

if fotos:
    if st.button("🤖 ANALISAR IMAGENS AGORA"):
        with st.spinner("Extraindo dados técnicos..."):
            try:
                img_list = [Image.open(f) for f in fotos]
                response = model.generate_content([
                    "Identifique reatores, inflamáveis como D-Limoneno e pontos de SPDA:", 
                    *img_list
                ])
                st.subheader("📝 Processo Operacional Extraído")
                st.write(response.text)
                st.balloons()
            except Exception as e:
                st.error(f"Erro: {e}")
