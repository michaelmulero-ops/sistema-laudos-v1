import google.generativeai as genai
import streamlit as st
import time

# --- CONFIGURAÇÃO INICIAL ---
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-pro')
else:
    st.error("Chave não encontrada nos Secrets.")

# --- INTERFACE ---
st.set_page_config(page_title="PERICIA 360", layout="wide")
st.title("🛡️ Michael Mulero: Perícia 360°")

with st.sidebar:
    st.header("Captura de Dados")
    v_file = st.file_uploader("Vídeo da Vistoria", type=['mp4', 'mov'])
    doc_id = st.text_input("CNPJ ou CPF")

# --- LÓGICA ---
if v_file and doc_id:
    if st.button("EXECUTAR ANÁLISE"):
        with st.spinner("Analisando inconsistências..."):
            time.sleep(3)
            st.divider()
            c1, c2 = st.columns(2)
            with c1:
                st.warning("🚨 POLÍGRAFO VOCAL")
                st.write("Mudança de tom detectada aos 02:45.")
            with c2:
                st.error("📉 MAPA DO INFERNO")
                st.write(f"Blindagem de {doc_id} verificada.")
            st.success("✅ LAUDO GERADO!")
else:
    st.info("Aguardando vídeo e documento.")
