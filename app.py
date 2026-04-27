import streamlit as st

# INICIALIZAÇÃO DE VARIÁVEIS (Para evitar o NameError)
if 'lote_arquivos' not in st.session_state:
    st.session_state.lote_arquivos = None

# MÓDULO DE UPLOAD (A "ÁGUA" DO SISTEMA)
lote_arquivos = st.file_uploader("Upload de Fotos/Vídeos", accept_multiple_files=True, key="inspecao_v17")

# AGORA O IF FUNCIONA SEM ERRO
if lote_arquivos:
    st.session_state.lote_arquivos = lote_arquivos
    st.success(f"✅ {len(lote_arquivos)} arquivos prontos para análise.")
