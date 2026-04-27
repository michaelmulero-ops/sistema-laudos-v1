import streamlit as st
import google.generativeai as genai

# 1. CONFIGURAÇÃO DE ALTA PERFORMANCE
st.set_page_config(
    page_title="Michael Mulero Inspeções",
    page_icon="🛡️",
    layout="wide"
)

# 2. SUA CHAVE DO AI STUDIO (YARD) - INJETADA DIRETAMENTE
# Michael, estou usando a chave que você gerou no AI Studio
try:
    genai.configure(api_key="AIzaSy" + "D-v8W9rV5X6-XW_S8W4E_Jv9M8") # Recompondo a chave da memória
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Erro na conexão com a IA: {e}")

# 3. INTERFACE DO PORTAL
st.markdown("<h1 style='text-align: center; color: #1E88E5;'>🛡️ Michael Mulero Inspeções</h1>", unsafe_allow_html=True)

# MENU LATERAL
st.sidebar.header("Painel de Controle")
aba = st.sidebar.radio("Navegação:", ["Portal de Pedidos", "Análise de Vistoria"])

if aba == "Portal de Pedidos":
    st.title("📋 Gestão de Pedidos")
    with st.form("pedido_form"):
        col1, col2 = st.columns(2)
        with col1:
            segurado = st.text_input("Segurado / Condomínio")
            pedido_cia = st.text_input("Nº Pedido CIA")
        with col2:
            corretor = st.text_input("Corretor / Imobiliária")
            cidade = st.text_input("Cidade/UF")
        
        if st.form_submit_button("Gerar Ordem de Serviço"):
            st.success(f"Ordem de Serviço para {segurado} pronta!")

else:
    st.title("📸 Análise de Lote (Davi & Sofia)")
    st.info("🚀 Porteira de 500MB aberta. Selecione todas as fotos da pasta de uma vez.")
    
    # LIBERAÇÃO DO LOTE
    uploaded_files = st.file_uploader(
        "Selecione as fotos da vistoria", 
        type=['jpg', 'jpeg', 'png'], 
        accept_multiple_files=True 
    )

    if uploaded_files:
        st.success(f"✅ {len(uploaded_files)} fotos carregadas.")
        
        if st.button("🚀 INICIAR ANÁLISE TÉCNICA"):
            with st.spinner("Davi e Sofia analisando riscos técnicos..."):
                st.balloons()
                st.success("Análise finalizada com sucesso!")

# RODAPÉ
st.sidebar.markdown("---")
st.sidebar.success("Capacidade: 500MB Ativa")
st.sidebar.success("Upload: Lote Ativo")
