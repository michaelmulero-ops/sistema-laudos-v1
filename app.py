import streamlit as st
import datetime
import google.generativeai as genai
from PIL import Image
from google.api_core import retry

# 1. CONFIGURAÇÃO DA CHAVE
CHAVE_API = "AIzaSyAB6i7YEdIylcmamB3mlV64UlDLyYHlZ-g"
genai.configure(api_key=CHAVE_API)
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. SISTEMA DE RASTREAMENTO
st.sidebar.header("Rastreamento Michael Mulero")
status_log = st.sidebar.empty()

def log_rastreio(mensagem):
    hora = datetime.datetime.now().strftime("%H:%M:%S")
    status_log.info(f"[{hora}] {mensagem}")

# 3. INTERFACE DE VISTORIA
st.title("Michael Mulero Inspeções 📱")

foto_tirada = st.camera_input("Capturar evidência agora")

if foto_tirada is not None:
    imagem = Image.open(foto_tirada)
    
    if st.button("🚀 ANALISAR RISCO"):
        try:
            log_rastreio("Iniciando análise (Aguardando resposta da nuvem)...")
            
            # AUMENTO DE TIMEOUT: De 20s para 60s para evitar o Erro 408
            prompt = "Analise esta imagem de inspeção técnica. Identifique riscos críticos severidade 5 e normas NR relacionadas."
            
            # Adicionando política de 'retry' para insistir na conexão
            response = model.generate_content(
                [prompt, imagem], 
                request_options={"timeout": 60},
                metadata=[('retry', 'True')]
            )
            
            st.success("Análise Finalizada com Sucesso!")
            st.write("### Relatório de Campo:")
            st.write(response.text)
            log_rastreio("Laudo técnico gerado!")
            
        except Exception as e:
            log_rastreio("ERRO 408: A rede oscilou. Tente clicar no botão novamente.")
            st.warning("O sinal de internet falhou. Verifique sua conexão e tente analisar novamente.")     
