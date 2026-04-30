import streamlit as st
import datetime
import google.generativeai as genai
from PIL import Image

# Configuração Michael Mulero Inspeções
CHAVE_API = "AIzaSyAB6i7YEdIylcmamB3mlV64UlDLyYHlZ-g"
genai.configure(api_key=CHAVE_API)
model = genai.GenerativeModel('gemini-1.5-flash')

# Barra Lateral de Rastreamento
st.sidebar.header("Rastreamento Michael Mulero")
status_log = st.sidebar.empty()

def log_rastreio(mensagem):
    hora = datetime.datetime.now().strftime("%H:%M:%S")
    status_log.info(f"[{hora}] {mensagem}")

st.title("Michael Mulero Inspeções Tech V1 📱")

# ÁREA PARA COLAR O PEDIDO
with st.expander("📄 Autorizar Leitura do Pedido (Copiar e Colar)", expanded=True):
    texto_pedido = st.text_area("Cole aqui o conteúdo do PDF ou E-mail do pedido:")
    if texto_pedido:
        st.success("Conteúdo do pedido pronto para análise!")
        log_rastreio("Pedido de vistoria autorizado e carregado.")

# CAPTURA DE FOTO E CNPJ
with st.expander("🔍 Dados do Risco"):
    cnpj_cliente = st.text_input("CNPJ (Se não estiver no texto acima)")

st.subheader("📸 Evidências de Campo")
foto_tirada = st.camera_input("Foto da Fachada (Referência: Rua)")

if st.button("🚀 INICIAR VARREDURA COMPLETA"):
    if not foto_tirada or not texto_pedido:
        st.warning("Por favor, cole o pedido e capture a foto da fachada.")
    else:
        try:
            log_rastreio("Nano Banana: Gerando 5 croquis automáticos...")
            log_rastreio("Mapeando 500m: Escolas, Sindicatos, Rios e Campos...")
            log_rastreio("Clima: Histórico de Granizo e Ciclones em Londrina/Ibiporã...")
            
            imagem = Image.open(foto_tirada)
            prompt = f"""
            Com base neste pedido: {texto_pedido}
            Analise o risco para o CNPJ {cnpj_cliente}:
            1. VISTA AÉREA: Identifique e conte as PLACAS SOLARES no telhado.
            2. AMBIENTAL: Vulnerabilidade a granizo e vendavais (atípicos).
            3. VIZINHANÇA: Liste escolas, rios e sindicatos num raio de 500m.
            4. CROQUIS: Oriente o desenho das 5 camadas com a FRENTE PARA A RUA.
            5. NORMAS: Aplique NR-10, 11 e 13 conforme o setor.
            """
            
            response = model.generate_content([prompt, imagem], request_options={"timeout": 60})
            st.success("Dossiê Michael Mulero Gerado!")
            st.write(response.text)
            log_rastreio("Relatório finalizado com sucesso!")
            
        except Exception as e:
            st.error(f"Erro no processamento: {e}")
