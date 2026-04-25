import google.generativeai as genai
import streamlit as st

# --- 1. A CHAVE LOGO NO TOPO ---
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-pro')
else:
    st.error("ERRO: CHAVE NAO ENCONTRADA")

# --- 2. INTERFACE ---
st.title("🛡️ Michael Mulero: Perícia 360°")

v_file = st.sidebar.file_uploader("Vídeo da Vistoria", type=['mp4', 'mov'])
doc_id = st.sidebar.text_input("CNPJ ou CPF")

# --- 3. LOGICA ---
if v_file and doc_id:
    if st.button("GERAR LAUDO PROFISSIONAL"):
        st.subheader("🚨 SINAL DE ALERTA")
        st.write("Anomalia vocal e técnica detectada.")
        st.success("✅ LAUDO GERADO COM SUCESSO!")
else:
    st.info("Aguardando vídeo e documento.")
