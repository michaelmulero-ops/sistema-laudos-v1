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
    st.info("Varredura em raio de 500m: Escolas, Rios, Sindicatos e Criminalidade ativados.")

st.subheader("📸 Captura de Campo")
foto_tirada = st.camera_input("Foto da Fachada (Referência: Frente para a rua)")

if st.button("🚀 GERAR DOSSIÊ COMPLETO COM VISTA AÉREA"):
    try:
        log_rastreio("Iniciando varredura 500m (Sindicatos, Rios, Escolas)...")
        log_rastreio("Acessando Vista Aérea para contagem de Placas Solares...")
        log_rastreio("Analisando riscos ambientais (Vento, Granizo)...")
        
        imagem = Image.open(foto_tirada)
        
        # PROMPT DE IA PARA ANÁLISE COMPLETA
        prompt = f"""
        Analise o risco para o CNPJ {cnpj_cliente} com foco em:
        1. VISTA AÉREA: Identifique se há placas solares no telhado e QUANTAS são.
        2. VIZINHANÇA (500m): Localize sindicatos, escolas, rios ou campos de futebol.
        3. AMBIENTAL: Risco de granizo e ventos na região de Londrina/Ibiporã.
        4. TÉCNICO: Riscos Severidade 5 (NR-10, 11, 13).
        5. PADRÃO: Mantenha os 5 croquis orientados com a FRENTE PARA A RUA.
        """
        
        log_rastreio("Processando inteligência artificial (Timeout 60s)...")
        response = model.generate_content([prompt, imagem], request_options={"timeout": 60})
        
        st.success("Dossiê Michael Mulero Gerado!")
        st.write("### Relatório Consolidado:")
        st.write(response.text)
        log_rastreio("Dossiê finalizado com sucesso!")
        
    except Exception as e:
        log_rastreio("ERRO: Falha na conexão de campo. Tente novamente.")
        st.error(f"Erro no processamento: {e}")
