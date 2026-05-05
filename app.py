import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. IDENTIDADE (Michael Mulero Inspeções)
st.set_page_config(page_title="S.I.T. - Michael Mulero", layout="wide")

# 2. CONFIGURAÇÃO DA API
API_KEY = "AIzaSyAB6i7YEdIylcmamB3mlV64UlDLyYHlZ-g" 
genai.configure(api_key=API_KEY)

# 3. DEFINIÇÃO DA INTELIGÊNCIA (Sênior de Risco)
# Foco: Solus/Cropfield, D-Limoneno UN 2319 e 9 pontos de SPDA.
SYSTEM_PROMPT = """
Analise como um inspetor de risco sênior. 
Identifique processos industriais, reatores e inflamáveis. 
Verifique proteções como SPDA (9 pontos), CFTV e perímetros.
Gere um texto técnico para o relatório.
"""

# AJUSTE DE OURO: Usando apenas o nome base para evitar conflito de versão
model = genai.GenerativeModel("gemini-pro-vision") 

# 4. PAINEL LATERAL
with st.sidebar:
    st.title("🛡️ Filtros")
    categoria = st.selectbox("Nível:", ["Indústria", "Transportadora", "E-commerce", "CD"])
    cnpj = st.text_input("CNPJ:", value="21.203.489/0001-79")

# 5. INTERFACE PRINCIPAL
st.title("🛡️ Painel de Operação - Michael Mulero Inspeções")
fotos = st.file_uploader("Subir fotos da vistoria:", accept_multiple_files=True)

processo_texto = ""

if fotos:
    if st.button("🤖 ANALISAR IMAGENS AGORA"):
        with st.spinner("Extraindo dados técnicos..."):
            try:
                img_list = [Image.open(f) for f in fotos]
                # Chamada direta e simplificada
                response = model.generate_content([SYSTEM_PROMPT, *img_list])
                processo_texto = response.text
                st.balloons()
            except Exception as e:
                # Caso o modelo antigo falhe, tentamos o novo automaticamente
                try:
                    model_novo = genai.GenerativeModel("gemini-1.5-flash")
                    response = model_novo.generate_content([SYSTEM_PROMPT, *img_list])
                    processo_texto = response.text
                    st.balloons()
                except:
                    st.error("Erro de conexão com o Google. Verifique se a cota da API não expirou.")

# 6. RESULTADO
st.subheader("📝 Processo Operacional Extraído")
st.text_area("Copie para o laudo:", value=processo_texto, height=300)
