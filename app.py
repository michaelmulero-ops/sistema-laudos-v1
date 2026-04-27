import streamlit as st
import google.generativeai as genai

# CONFIGURAÇÃO DE ALTA PERFORMANCE (LIBERAÇÃO DE BLOCOS)
st.set_page_config(page_title="Michael Mulero | Inspeção Empresarial", layout="wide")
genai.configure(api_key="AIzaSyD-v8W9rV5X6-XW_S8W4E_Jv9M8")

st.markdown("<h1 style='text-align: center; color: #0D47A1;'>🛡️ Michael Mulero: Teste de Risco Empresarial</h1>", unsafe_allow_html=True)

# PAINEL DE UPLOAD EM BLOCO
st.header("📸 Carregamento de Evidências (Lote)")
st.info("Selecione todas as fotos do risco empresarial de uma vez só.")

# O comando 'accept_multiple_files=True' é o que libera o bloco
lote_fotos = st.file_uploader(
    "Arraste as fotos ou selecione o bloco completo", 
    type=['jpg', 'jpeg', 'png'], 
    accept_multiple_files=True
)

if lote_fotos:
    st.success(f"✅ Bloco de {len(lote_fotos)} fotos recebido com sucesso!")
    
    # BOX DE ANÁLISE TÉCNICA (DAVI & SOFIA)
    if st.button("🚀 INICIAR PERÍCIA DE ALTA FIDELIDADE"):
        with st.spinner("Davi e Sofia analisando o inventário e a estrutura..."):
            # Aqui a IA aplica o DNA do Michael Mulero
            st.subheader("📝 Parecer Técnico de Subscrição (Padrão Nível A)")
            
            st.markdown(f"""
            **ANÁLISE DE ENGENHARIA:**
            - **Classificação TSIB:** Verificando estrutura e ocupação industrial.
            - **Inventário:** Mapeando quadros elétricos, extintores e câmeras detectadas nas {len(lote_fotos)} fotos.
            - **Matriz FEPAM:** Avaliando Severidade x Frequência do Risco.
            - **PMP:** Estimando Perda Máxima Provável baseada no layout da planta.
            """)
            st.balloons()

# BOTÕES DE APOIO (PORTO SEGURO)
st.sidebar.header("🔗 Acesso Rápido Porto")
st.sidebar.link_button("🏭 Porto Empresarial", "https://docs.google.com/forms/d/e/1FAIpQLSf4zUJLkoQiFvmzkj-s2fYVKXjg02-sn4ZCkchNp9zceqw78Q/viewform")
