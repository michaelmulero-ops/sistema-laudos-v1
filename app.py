import streamlit as st
import google.generativeai as genai
from PIL import Image
from pypdf import PdfReader
import datetime
import io

# --- CONFIGURAÇÃO MASTER MICHAEL MULERO ---
st.set_page_config(page_title="Michael Mulero Inspeções Tech", layout="wide")

# Barra Lateral com Rastreamento
st.sidebar.header("Rastreamento Michael Mulero")
status_log = st.sidebar.empty()

def log_rastreio(mensagem):
    hora = datetime.datetime.now().strftime("%H:%M:%S")
    status_log.info(f"[{hora}] {mensagem}")

# Substitua pela sua chave API
genai.configure(api_key="AIzaSyAB6i7YEdIylcmamB3mlV64UlDLyYHlZ-g")
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🏛️ Michael Mulero Inspeções - Tecnologia 360")

# --- IMPORTAÇÃO DE DADOS (PDF) ---
with st.expander("📄 1. Importar Pedido de Vistoria (PDF)", expanded=True):
    pdf_dados = st.file_uploader("Suba o PDF com os dados do Segurado", type=['pdf'])
    dados_contexto = ""
    if pdf_dados:
        try:
            reader = PdfReader(pdf_dados)
            for page in reader.pages:
                dados_contexto += page.extract_text()
            st.success("✅ Dados do Segurado Importados!")
            log_rastreio("PDF lido com sucesso.")
        except:
            st.error("Erro ao ler o PDF.")

# --- CAPTURA DE CAMPO ---
st.subheader("📸 2. Evidências e Fotos")
arquivos = st.file_uploader("Suba as Fotos da Vistoria", accept_multiple_files=True)

# --- MOTOR DE ANÁLISE ---
if arquivos and st.button("🚀 CONSOLIDAR RELATÓRIO E GERAR CROQUIS"):
    col_a, col_b = st.columns(2)
    log_rastreio("Iniciando integração de dados...")
    
    with st.spinner("Analisando imagens e gerando camadas..."):
        setores = {
            "ANÁLISE DE RISCO": "Conte as PLACAS SOLARES e avalie o telhado.",
            "ARREDORES 500M": "Identifique Escolas, Rios e Sindicatos próximos.",
            "CLIMÁTICO": "Avalie histórico de Granizo e Ciclones em Ibiporã/Londrina.",
            "CROQUIS 360": "Gere 5 camadas técnicas com FRENTE PARA A RUA."
        }

        for i, (titulo, diretriz) in enumerate(setores.items()):
            target_col = col_a if i % 2 == 0 else col_b
            with target_col:
                st.subheader(f"📍 {titulo}")
                prompt_mestre = f"DADOS DO PEDIDO: {dados_contexto}\nDIRETRIZ: {diretriz}\nAnalise a imagem técnica."
                
                # Pega a primeira imagem para a análise geral
                img = Image.open(arquivos[0])
                # Configuração de timeout de 20s para não travar
                res = model.generate_content([prompt_mestre, img], request_options={"timeout": 20})
                st.info(res.text)
                log_rastreio(f"Setor {titulo} concluído.")

st.caption("Michael Mulero Inspeções | Ibiporã-PR")
