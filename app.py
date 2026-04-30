import streamlit as st
import datetime
import google.generativeai as genai
from PIL import Image

# 1. CONFIGURAÇÃO DA CHAVE (LIGAÇÃO DIRETA)
# Coloque sua chave entre as aspas abaixo
CHAVE_API = "COLE_SUA_CHAVE_AQUI"
genai.configure(api_key=CHAVE_API)
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. SISTEMA DE RASTREAMENTO E SEGURANÇA
st.sidebar.header("Rastreamento Michael Mulero")
status_log = st.sidebar.empty()

def log_rastreio(mensagem):
    hora = datetime.datetime.now().strftime("%H:%M:%S")
    status_log.info(f"[{hora}] {mensagem}")[cite: 1]

# 3. INTERFACE DE USUÁRIO
st.title("Sistema de Inspeção Tech V1")
st.write("---")

# Campo para subir a foto da inspeção (padarias, fábricas, fiações, etc)
foto_carregada = st.file_uploader("Selecione a foto da inspeção", type=['jpg', 'jpeg', 'png'])

if foto_carregada is not None:
    imagem = Image.open(foto_carregada)
    st.image(imagem, caption="Foto carregada para análise", use_column_width=True)
    
    if st.button("Analisar Risco na Foto"):
        try:
            log_rastreio("Enviando foto para análise da IA...")[cite: 1]
            
            # O 'timeout' de 20s impede que o sistema trave se a imagem for pesada
            prompt = "Analise esta foto de inspeção técnica. Identifique riscos conforme as NRs brasileiras e sugira ações corretivas."
            
            response = model.generate_content(
                [prompt, imagem], 
                request_options={"timeout": 20}
            )
            
            st.success("Análise concluída!")
            st.write("### Relatório Técnico Preliminar:")
            st.write(response.text)
            log_rastreio("Laudo da foto gerado com sucesso!")[cite: 1]
            
        except Exception as e:
            log_rastreio("ERRO: A análise da foto demorou demais e foi interrompida.")[cite: 1, 2]
            st.error(f"Falha ao processar imagem: {e}")
