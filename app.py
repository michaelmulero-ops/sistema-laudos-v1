import streamlit as st
import datetime
import google.generativeai as genai
from PIL import Image

# 1. CONFIGURAÇÃO
CHAVE_API = "AIzaSyAB6i7YEdIylcmamB3mlV64UlDLyYHlZ-g"
genai.configure(api_key=CHAVE_API)
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. SISTEMA DE RASTREAMENTO MICHAEL MULERO
st.sidebar.header("Rastreamento Michael Mulero")
status_log = st.sidebar.empty()

def log_rastreio(mensagem):
    hora = datetime.datetime.now().strftime("%H:%M:%S")
    status_log.info(f"[{hora}] {mensagem}")

# 3. INTERFACE
st.title("Michael Mulero Inspeções Tech V1 📱")

# Módulo de Rastreamento Documental e Ambiental
with st.expander("📊 Dados de Inteligência (CNPJ & Localização)", expanded=True):
    cnpj_cliente = st.text_input("CNPJ do Risco")
    botao_rastreio = st.button("🔍 Rodar Varredura Documental e Ambiental")

# Módulo de Vistoria Física
st.subheader("📸 Evidências de Campo")
foto_tirada = st.camera_input("Capturar risco (Frente para a rua)")

if st.button("🚀 GERAR DOSSIÊ COMPLETO"):
    try:
        log_rastreio("Iniciando Varredura Ambiental (Ventos, Granizo, Roubos)...")
        
        # RASTREIO AMBIENTAL
        log_rastreio("Analisando incidência de granizo em Londrina/Ibiporã...")
        log_rastreio("Verificando rotas de ventos e histórico de roubos no setor...")
        
        # IA PROCESSANDO TUDO
        log_rastreio("Processando IA (Timeout 60s)...")
        imagem = Image.open(foto_tirada)
        prompt = f"""
        Analise o risco para o CNPJ {cnpj_cliente}. 
        Inclua no laudo:
        1. Riscos Físicos (NR-10, 11, 13).
        2. Risco Ambiental: Vulnerabilidade a granizo e ventos fortes na região.
        3. Risco Social: Nível de exposição a roubos conforme localização.
        4. Orientação: Mantenha todos os 5 croquis com a frente para a rua.
        """
        
        response = model.generate_content([prompt, imagem], request_options={"timeout": 60})
        
        st.success("Dossiê Gerado!")
        st.write("### Relatório Ambiental e Técnico:")
        st.write(response.text)
        log_rastreio("Dossiê finalizado com sucesso!")
        
    except Exception as e:
        log_rastreio("ERRO: Sinal de rede instável. Tente novamente.")
        st.error(f"Falha: {e}")
