import streamlit as st
import datetime
import google.generativeai as genai
from PIL import Image

# Configuração Master Michael Mulero
CHAVE_API = "AIzaSyAB6i7YEdIylcmamB3mlV64UlDLyYHlZ-g"
genai.configure(api_key=CHAVE_API)
model = genai.GenerativeModel('gemini-1.5-flash')

# Rastreamento em Tempo Real na lateral
st.sidebar.header("Rastreamento Michael Mulero")
status_log = st.sidebar.empty()

def log_rastreio(mensagem):
    hora = datetime.datetime.now().strftime("%H:%M:%S")
    status_log.info(f"[{hora}] {mensagem}")

st.title("🏛️ Michael Mulero Inspeções - V1 Tech")

# ÁREA DE DADOS - COPIAR E COLAR (Para não dar erro de PDF)
with st.expander("📄 Dados do Pedido (Copie e Cole do PDF/E-mail)", expanded=True):
    texto_pedido = st.text_area("Cole aqui as informações do segurado:")
    if texto_pedido:
        log_rastreio("Pedido carregado via texto.")

# CAPTURA DE FOTO
st.subheader("📸 Evidências de Campo")
foto_tirada = st.camera_input("Foto da Fachada (Frente para a rua)")

if st.button("🚀 GERAR DOSSIÊ COMPLETO"):
    if not foto_tirada or not texto_pedido:
        st.warning("Por favor, cole o pedido e capture a foto primeiro.")
    else:
        try:
            log_rastreio("Acionando Nano Banana: Gerando 5 croquis...")
            log_rastreio("Mapeando vizinhos em 500m (Sindicatos/Rios/Escolas)...")
            
            imagem = Image.open(foto_tirada)
            prompt = f"""
            Analise o risco baseado neste pedido: {texto_pedido}
            1. VISTA AÉREA: Identifique e conte as PLACAS SOLARES.
            2. AMBIENTAL: Verifique risco de granizo e ciclones na região.
            3. VIZINHANÇA: Liste escolas, rios e sindicatos num raio de 500m.
            4. CROQUIS: Gere orientações para 5 camadas com a FRENTE PARA A RUA.
            """
            
            # Trava de segurança de 20 segundos
            response = model.generate_content([prompt, imagem], request_options={"timeout": 20})
            st.success("Dossiê Michael Mulero Gerado!")
            st.write(response.text)
            log_rastreio("Laudo finalizado com sucesso!")
        except Exception as e:
            st.error(f"Erro: {e}")
