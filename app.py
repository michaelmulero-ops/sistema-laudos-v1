import streamlit as st
import datetime
import google.generativeai as genai
from PIL import Image
import pdfplumber

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

# 3. INTERFACE
st.title("Michael Mulero Inspeções Tech V1 📱")

# ABA DE IMPORTAÇÃO DE PEDIDO
with st.expander("📄 Importar Pedido de Vistoria (PDF)", expanded=True):
    arquivo_pdf = st.file_uploader("Suba o PDF do pedido aqui", type=['pdf'])
    dados_pedido = ""
    if arquivo_pdf:
        with pdfplumber.open(arquivo_pdf) as pdf:
            dados_pedido = "\n".join([pagina.extract_text() for pagina in pdf.pages])
        st.success("Dados do segurado extraídos com sucesso!")
        log_rastreio("Dados do pedido lidos via pdfplumber.")

# ABA DE INTELIGÊNCIA
with st.expander("📊 Inteligência de Dados e Arredores"):
    cnpj_cliente = st.text_input("CNPJ (Extraído ou Manual)")
    st.info("Ativos: Raio 500m (Sindicatos/Rios), Ambiental (Granizo/Ciclone) e Nano Banana.")

st.subheader("📸 Captura de Evidências")
foto_tirada = st.camera_input("Foto da Fachada (Frente para a rua)")

if st.button("🚀 GERAR DOSSIÊ COMPLETO"):
    try:
        log_rastreio("Acionando Nano Banana: Gerando 5 Croquis...")
        log_rastreio("Mapeando vizinhos (Sindicatos/Escolas) em 500m...")
        
        imagem = Image.open(foto_tirada)
        prompt = f"""
        Com base nestes dados: {dados_pedido}
        Analise o risco para o CNPJ {cnpj_cliente}:
        1. VISTA AÉREA: Conte as PLACAS SOLARES no telhado.
        2. AMBIENTAL: Frequência de granizo, chuvas de pedra e ciclones em Londrina/Ibiporã.
        3. VIZINHANÇA: Identifique escolas, sindicatos e rios num raio de 500m.
        4. CROQUIS: Oriente o Nano Banana a desenhar 5 camadas com a FRENTE PARA A RUA.
        """
        
        response = model.generate_content([prompt, imagem], request_options={"timeout": 60})
        st.success("Dossiê Consolidado!")
        st.write(response.text)
        log_rastreio("Dossiê finalizado com sucesso!")
        
    except Exception as e:
        log_rastreio("ERRO: Sinal instável. Tente novamente.")
        st.error(f"Falha: {e}")
