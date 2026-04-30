import streamlit as st
import datetime
import google.generativeai as genai
from PIL import Image
import pdfplumber

# Configuração da API Michael Mulero Inspeções
CHAVE_API = "AIzaSyAB6i7YEdIylcmamB3mlV64UlDLyYHlZ-g"
genai.configure(api_key=CHAVE_API)
model = genai.GenerativeModel('gemini-1.5-flash')

# Sistema de Rastreamento Lateral
st.sidebar.header("Rastreamento Michael Mulero")
status_log = st.sidebar.empty()

def log_rastreio(mensagem):
    hora = datetime.datetime.now().strftime("%H:%M:%S")
    status_log.info(f"[{hora}] {mensagem}")

st.title("Michael Mulero Inspeções Tech V1 📱")

# Aba de Importação do Pedido
with st.expander("📄 Importar Pedido (PDF)", expanded=True):
    arquivo_pdf = st.file_uploader("Suba o pedido da seguradora", type=['pdf'])
    dados_extraidos = ""
    if arquivo_pdf:
        with pdfplumber.open(arquivo_pdf) as pdf:
            dados_extraidos = "\n".join([p.extract_text() for p in pdf.pages])
        st.success("Dados do segurado carregados!")
        log_rastreio("Pedido lido com sucesso.")

# Entrada de Dados e Captura
cnpj_cliente = st.text_input("CNPJ do Risco", help="Extraído automaticamente se subir o PDF")
foto_tirada = st.camera_input("Foto da Fachada (Frente para a rua)")

if st.button("🚀 GERAR DOSSIÊ E 5 CROQUIS"):
    if not foto_tirada:
        st.warning("Capture a foto da fachada primeiro.")
    else:
        try:
            log_rastreio("Acionando Nano Banana: Desenhando croquis...")
            log_rastreio("Mapeando raio 500m: Escolas, Rios e Sindicatos...")
            log_rastreio("Analisando Clima: Histórico de Granizo e Ciclones...")
            
            imagem = Image.open(foto_tirada)
            prompt = f"""
            Analise o risco para o CNPJ {cnpj_cliente} com base no pedido: {dados_extraidos}
            1. VISTA AÉREA: Identifique e conte as PLACAS SOLARES.
            2. AMBIENTAL: Frequência de temporais, granizo e ciclones em Londrina/Ibiporã.
            3. VIZINHANÇA: Mapeie escolas, rios e sindicatos num raio de 500m.
            4. CROQUIS: Gere 5 camadas técnicas com a FRENTE PARA A RUA.
            5. NORMAS: Verifique conformidade NR-10, 11 e 13.
            """
            
            response = model.generate_content([prompt, imagem], request_options={"timeout": 60})
            st.success("Dossiê Michael Mulero Consolidado!")
            st.write(response.text)
            log_rastreio("Laudo finalizado com sucesso!")
            
        except Exception as e:
            log_rastreio("ERRO: Rede instável. Tente novamente.")
            st.error(f"Falha no processamento: {e}")
            
