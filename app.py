import streamlit as st
import datetime
import google.generativeai as genai
from PIL import Image

# 1. CONFIGURAÇÃO DA CHAVE (LIGAÇÃO DIRETA)
CHAVE_API = "AIzaSyAB6i7YEdIylcmamB3mlV64UlDLyYHlZ-g"
genai.configure(api_key=CHAVE_API)
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. SISTEMA DE RASTREAMENTO E SEGURANÇA
st.sidebar.header("Rastreamento Michael Mulero")
status_log = st.sidebar.empty()

def log_rastreio(mensagem):
    hora = datetime.datetime.now().strftime("%H:%M:%S")
    status_log.info(f"[{hora}] {mensagem}")

# 3. INTERFACE DE VISTORIA
st.title("Michael Mulero Inspeções 📱")

# Captura direta pela câmera
foto_tirada = st.camera_input("Capturar evidência agora")

if foto_tirada is not None:
    imagem = Image.open(foto_tirada)
    
    if st.button("🚀 ANALISAR RISCO"):
        try:
            log_rastreio("Iniciando análise técnica de campo...")
            
            # Timeout de 20 segundos contra loops infinitos
            prompt = "Analise esta imagem de inspeção técnica. Identifique riscos conforme as NRs brasileiras (NR-10, 11, 13) e sugira ações corretivas."
            response = model.generate_content([prompt, imagem], request_options={"timeout": 20})
            
            st.success("Análise Finalizada")
            st.write("### Relatório de Campo:")
            st.write(response.text)
            log_rastreio("Laudo técnico gerado com sucesso!")
            
        except Exception as e:
            log_rastreio("ERRO: A conexão falhou ou o tempo esgotou.")
            st.error(f"Ocorreu um problema: {e}")
            
