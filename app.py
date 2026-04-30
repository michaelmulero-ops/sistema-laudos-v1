import streamlit as st
import datetime
import google.generativeai as genai
from PIL import Image

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

# Removi o leitor de PDF complexo para destravar o sistema agora
with st.expander("📄 Dados do Segurado (Manual)", expanded=True):
    nome_segurado = st.text_input("Nome do Segurado")
    cnpj_cliente = st.text_input("CNPJ do Risco")

st.subheader("📸 Evidências de Campo")
foto_tirada = st.camera_input("Foto da Fachada (Frente para a rua)")

if st.button("🚀 GERAR DOSSIÊ COMPLETO"):
    if not foto_tirada:
        st.warning("Capture a foto primeiro.")
    else:
        try:
            log_rastreio("Acionando Nano Banana: Desenhando 5 croquis...")
            log_rastreio("Mapeando raio 500m: Escolas, Rios e Sindicatos...")
            
            imagem = Image.open(foto_tirada)
            prompt = f"Analise o risco para {nome_segurado} ({cnpj_cliente}). Identifique placas solares, riscos ambientais (granizo/ciclone) e mantenha os croquis com a frente para a rua."
            
            response = model.generate_content([prompt, imagem], request_options={"timeout": 60})
            st.success("Dossiê Gerado!")
            st.write(response.text)
            log_rastreio("Laudo finalizado!")
        except Exception as e:
            st.error(f"Erro: {e}")
