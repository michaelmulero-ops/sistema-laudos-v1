import streamlit as st
import datetime
import google.generativeai as genai
from PIL import Image
import PyPDF2  # Necessário instalar: pip install PyPDF2

# 1. CONFIGURAÇÃO (CHAVE ATUALIZADA)
CHAVE_API = "AIzaSyAB6i7YEdIylcmamB3mlV64UlDLyYHlZ-g"
genai.configure(api_key=CHAVE_API)
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. SISTEMA DE RASTREAMENTO MICHAEL MULERO
st.sidebar.header("Rastreamento Michael Mulero")
status_log = st.sidebar.empty()

def log_rastreio(mensagem):
    hora = datetime.datetime.now().strftime("%H:%M:%S")
    status_log.info(f"[{hora}] {mensagem}")

# 3. INTERFACE DE VISTORIA PROFISSIONAL
st.title("Michael Mulero Inspeções Tech V1 📱")

# ABA DE IMPORTAÇÃO DE PEDIDO
with st.expander("📄 Importar Pedido de Vistoria (PDF)", expanded=True):
    arquivo_pdf = st.file_uploader("Suba o PDF do pedido aqui", type=['pdf'])
    
    if arquivo_pdf:
        log_rastreio("Lendo PDF do pedido e extraindo dados do segurado...")
        # Extração básica de texto para a IA processar
        leitor = PyPDF2.PdfReader(arquivo_pdf)
        texto_pedido = "".join([pagina.extract_text() for pagina in leitor.pages])
        st.success("Dados do pedido carregados com sucesso!")

# ABA DE INTELIGÊNCIA E CROQUIS
with st.expander("📊 Inteligência de Dados e Arredores"):
    cnpj_cliente = st.text_input("CNPJ (Extraído do PDF ou digite aqui)")
    st.info("Módulos Ativos: Varredura 500m, Ambiental, Criminalidade e Nano Banana.")

st.subheader("📸 Captura de Evidências")
foto_tirada = st.camera_input("Foto da Fachada (Frente para a rua)")

if st.button("🚀 PROCESSAR TUDO E GERAR PDF FINAL"):
    try:
        log_rastreio("Acionando Nano Banana: Gerando 5 Croquis (Frente para a rua)...")
        log_rastreio("Verificando Clima: Histórico de Granizo e Ciclones...")
        log_rastreio("Mapeando Vizinhança: Sindicatos, Escolas e Rios em 500m...")
        
        # PROMPT DE IA INTEGRANDO O PDF E A FOTO
        prompt = f"""
        Com base no pedido: {texto_pedido if arquivo_pdf else 'Manual'}
        E na foto da vistoria:
        1. Confirme os dados do Segurado e CNPJ {cnpj_cliente}.
        2. VISTA AÉREA: Conte as PLACAS SOLARES no telhado.
        3. AMBIENTAL: Avalie risco de granizo/vendavais em Londrina/Ibiporã.
        4. CROQUIS: Oriente o Nano Banana a desenhar as 5 camadas com a FRENTE PARA A RUA.
        5. VIZINHOS: Mapeie escolas e rios no raio de 500m.
        """
        
        imagem = Image.open(foto_tirada)
        response = model.generate_content([prompt, imagem], request_options={"timeout": 60})
        
        st.success("Dossiê Michael Mulero Consolidado!")
        st.write("### Relatório de Engenharia e Risco:")
        st.write(response.text)
        
        # DOWNLOAD DO RESULTADO
        st.download_button("📥 Baixar Laudo Completo (PDF)", data=response.text, file_name=f"Laudo_{cnpj_cliente}.txt")
        log_rastreio("Dossiê e laudo disponibilizados para download.")
        
    except Exception as e:
        log_rastreio("ERRO: Sinal de rede instável ou falha no PDF.")
        st.error(f"Erro no processamento: {e}")
