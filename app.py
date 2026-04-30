import streamlit as st
import datetime
import google.generativeai as genai
from PIL import Image

# 1. CONFIGURAÇÃO DA CHAVE
CHAVE_API = "COLE_SUA_CHAVE_AQUI"
genai.configure(api_key=CHAVE_API)
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. SISTEMA DE RASTREAMENTO (RASTREIO ANTES DA CÂMERA)
st.sidebar.header("Rastreamento Michael Mulero")
status_log = st.sidebar.empty()

def log_rastreio(mensagem):
    hora = datetime.datetime.now().strftime("%H:%M:%S")
    status_log.info(f"[{hora}] {mensagem}")[cite: 1]

# 3. INTERFACE MOBILE
st.title("Vistoria Michael Mulero 📱")

# Captura de imagem direta pelo celular
foto_tirada = st.camera_input("Capturar evidência agora")[cite: 1]

if foto_tirada is not None:
    imagem = Image.open(foto_tirada)
    
    if st.button("🚀 ANALISAR RISCO"):
        try:
            log_rastreio("Iniciando análise de campo...")[cite: 1]
            
            # Timeout de 20 segundos para não travar o celular no 4G
            prompt = "Analise esta imagem de inspeção. Identifique riscos críticos nível 5 e normas NR relacionadas."
            response = model.generate_content([prompt, imagem], request_options={"timeout": 20})
            
            st.success("Análise Concluída")
            st.write(response.text)
            log_rastreio("Laudo gerado com sucesso!")[cite: 1]
            
        except Exception as e:
            log_rastreio("ERRO: A conexão falhou ou demorou demais.")[cite: 1, 2]
            st.error("Tempo esgotado. Tente novamente.")
