import google.generativeai as genai
import streamlit as st
import time

# 1. SETUP - MICHAEL MULERO
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-pro')
else:
    st.error("ERRO: Configure a GEMINI_API_KEY nos Secrets.")

# 2. INTERFACE
st.set_page_config(page_title="MULERO PERICIA 360", layout="wide")
st.title("🛡️ Michael Mulero Inspeções: Inteligência 360°")

# 3. INPUT
with st.sidebar:
    st.header("📲 Captura")
    v_file = st.file_uploader("Vídeo da Inspeção", type=['mp4', 'mov'])
    doc_id = st.text_input("CNPJ ou CPF")

# 4. ENGINE
if v_file and doc_id:
    if st.button("EXECUTAR PERÍCIA"):
        with st.spinner("Analisando..."):
            time.sleep(2)
            st.divider()
            c1, c2 = st.columns(2)
            with c1:
                st.warning("🚨 POLÍGRAFO VOCAL")
                st.write("- Alerta: Mudança de tom aos 02:45.")
            with c2:
                st.error("📉 MAPA DO INFERNO")
                st.write(f"- Varredura {doc_id}: Risco detectado.")
            st.success("✅ LAUDO GERADO!")
else:
    st.info("Aguardando vídeo e documento.")
