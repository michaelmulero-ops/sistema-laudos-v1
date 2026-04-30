import streamlit as st
import datetime
import google.generativeai as genai
from PIL import Image
from pypdf import PdfReader
import io

# Configuração Michael Mulero Inspeções
CHAVE_API = "AIzaSyAB6i7YEdIylcmamB3mlV64UlDLyYHlZ-g"
genai.configure(api_key=CHAVE_API)
model = genai.GenerativeModel('gemini-1.5-flash')

st.sidebar.header("Rastreamento Michael Mulero")
status_log = st.sidebar.empty()

def log_rastreio(mensagem):
    hora = datetime.datetime.now().strftime("%H:%M:%S")
    status_log.info(f"[{hora}] {mensagem}")

st.title("Michael Mulero Inspeções Tech V1 📱")

# ABA DE UPLOAD DO PDF
with st.expander("📄 Subir Pedido de Vistoria (PDF)", expanded=True):
    arquivo_pdf = st.file_uploader("Arraste o PDF do pedido aqui", type=['pdf'])
    texto_extraido = ""
    
    if arquivo_pdf:
        try:
            reader = PdfReader(arquivo_pdf)
            for page in reader.pages:
                texto_extraido += page.extract_text()
            st.success("Pedido carregado com sucesso!")
            log_rastreio("Dados extraídos via PDF.")
        except Exception as e:
            st.error(f"Erro ao ler o PDF: {e}")

# DADOS ADICIONAIS
with st.expander("🔍 Informações do Risco"):
    cnpj_cliente = st.text_input("CNPJ (Se não estiver no PDF)")

st.subheader("📸 Captura de Evidências")
foto_tirada = st.camera_input("Foto da Fachada (Frente para a rua)")

if st.button("🚀 GERAR DOSSIÊ COMPLETO"):
    if not foto_tirada or (not texto_extraido and not cnpj_cliente):
        st.warning("Por favor, suba o pedido e capture a foto da fachada.")
    else:
        try:
            log_rastreio("Nano Banana: Desenhando 5 croquis automáticos...")
            log_rastreio("Mapeando vizinhos em 500m (Sindicatos/Rios/Escolas)...")
            
            imagem = Image.open(foto_tirada)
            prompt = f"""
            Analise o risco baseado neste pedido: {texto_extraido[:2000]}
            1. VISTA AÉREA: Identifique e conte as PLACAS SOLARES.
            2. AMBIENTAL: Risco de granizo e ciclones em Londrina/Ibiporã.
            3. VIZINHANÇA: Liste escolas, rios e sindicatos num raio de 500m.
            4. ORIENTAÇÃO: 5 croquis sempre com a FRENTE PARA A RUA.
            5. NORMAS: Aplique NR-10, 11 e 13.
            """
            
            response = model.generate_content([prompt, imagem], request_options={"timeout": 60})
            st.success("Dossiê Michael Mulero Gerado!")
            st.write(response.text)
            log_rastreio("Laudo finalizado com sucesso!")
        except Exception as e:
            st.error(f"Erro no processamento: {e}")
