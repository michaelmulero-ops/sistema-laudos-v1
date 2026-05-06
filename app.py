import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. ESSENCIAL: O 'st.title' ou qualquer comando 'st' só funciona DEPOIS do import
st.set_page_config(page_title="Michael Mulero Inspeções Tech V1", layout="wide")

# 2. Configuração de Segurança
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
except Exception as e:
    st.error("Erro de Chave: Verifique os Secrets do Streamlit.")

# 3. Interface do Sistema
st.title("🛡️ Michael Mulero Inspeções - Tech V1")

# 4. Blocos de Funcionalidade
arquivo = st.file_uploader("Suba a foto para análise visual", type=['jpg', 'png', 'jpeg'])

if arquivo:
    img = Image.open(arquivo)
    st.image(img, width=400)
    
    with st.spinner('Analisando com Google Lens...'):
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(["Identifique este equipamento de risco e dados de placa.", img])
        st.write("### Resultado da Análise:")
        st.info(response.text)

# 5. O SEU RODAPÉ (Sempre no final do arquivo)
st.markdown("---")
st.caption("📍 **Padrão Técnico Michael Mulero**")
st.caption("Orientação: Frente-para-Rua | Norte Magnético Ignorado.")
