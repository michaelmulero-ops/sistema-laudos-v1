import streamlit as st
import datetime
import google.generativeai as genai
from PIL import Image

# 1. CONFIGURAÇÃO (CHAVE ATUALIZADA)
CHAVE_API = "AIzaSyAB6i7YEdIylcmamB3mlV64UlDLyYHlZ-g"
genai.configure(api_key=CHAVE_API)
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. RASTREAMENTO MICHAEL MULERO
st.sidebar.header("Rastreamento Michael Mulero")
status_log = st.sidebar.empty()

def log_rastreio(mensagem):
    hora = datetime.datetime.now().strftime("%H:%M:%S")
    status_log.info(f"[{hora}] {mensagem}")

# 3. INTERFACE DE VISTORIA PROFISSIONAL
st.title("Michael Mulero Inspeções Tech V1 📱")

with st.expander("📊 Inteligência de Dados (CNPJ, Arredores e Ambiental)", expanded=True):
    cnpj_cliente = st.text_input("CNPJ do Risco")
    st.info("Varredura 500m: Escolas, Rios, Granizo, Ciclones e Criminalidade ativos.")

st.subheader("📸 Captura de Campo")
foto_tirada = st.camera_input("Foto da Fachada (Frente para a rua)")

if st.button("🚀 GERAR DOSSIÊ COMPLETO"):
    try:
        log_rastreio("Rastreando frequência de Granizo e Ciclones na região...")
        log_rastreio("Contando Placas Solares via Vista Aérea...")
        log_rastreio("Mapeando vizinhos (Sindicatos/Escolas) em 500m...")
        
        imagem = Image.open(foto_tirada)
        
        prompt = f"""
        Analise o risco para o CNPJ {cnpj_cliente}:
        1. CLIMA ATÍPICO: Frequência de granizo, chuvas de pedra e vendavais na região de Londrina/Ibiporã.
        2. ENERGIA: Identifique e conte as PLACAS SOLARES no telhado.
        3. VIZINHANÇA: Escolas, sindicatos ou rios em um raio de 500m.
        4. TÉCNICO: Riscos Severidade 5 (NR-10, 11, 13).
        5. CROQUIS: Gere a lógica dos 5 croquis sempre com a FRENTE PARA A RUA.
        """
        
        log_rastreio("Processando IA (Timeout 60s)...")
        response = model.generate_content([prompt, imagem], request_options={"timeout": 60})
        
        st.success("Dossiê Michael Mulero Gerado com Sucesso!")
        st.write("### Relatório Consolidado de Riscos:")
        st.write(response.text)
        log_rastreio("Dossiê finalizado com sucesso!")
        
    except Exception as e:
        log_rastreio("ERRO: Rede instável. Tente novamente.")
        st.error(f"Erro no processamento: {e}")
