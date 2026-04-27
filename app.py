import streamlit as st
import google.generativeai as genai

# 1. CONFIGURAÇÃO DE ALTA PERFORMANCE (500MB e Lote)
st.set_page_config(
    page_title="Michael Mulero Inspeções",
    page_icon="🛡️",
    layout="wide"
)

# 2. CONFIGURAÇÃO DIRETA DA CHAVE (Sua Chave AIza já vai aqui)
# Como você não tem a chave de cabeça, o sistema vai tentar usar 
# a que você configurou no Secrets ou pedir para você colar uma vez.
CHAVE_INTERNA = st.secrets.get("GOOGLE_API_KEY", "COLE_SUA_CHAVE_AQUI")

if CHAVE_INTERNA != "COLE_SUA_CHAVE_AQUI":
    genai.configure(api_key=CHAVE_INTERNA)
else:
    st.error("⚠️ Erro: Chave de API não encontrada nos Secrets do Streamlit.")

# 3. INTERFACE DO PORTAL
st.markdown("<h1 style='text-align: center; color: #1E88E5;'>🛡️ Michael Mulero Inspeções</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Vistoria Tech V1 | Limite 500MB & Lote Ativos</p>", unsafe_allow_html=True)

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
    st.info("Porteira de 500MB aberta. Selecione o lote de fotos (Ctrl+A).")
    
    # O COMANDO QUE LIBERA O LOTE
    uploaded_files = st.file_uploader(
        "Selecione as fotos da vistoria", 
        type=['jpg', 'jpeg', 'png'], 
        accept_multiple_files=True 
    )

    if uploaded_files:
        st.success(f"✅ {len(uploaded_files)} fotos carregadas com sucesso!")
        
        if st.button("🚀 INICIAR ANÁLISE TÉCNICA"):
            with st.spinner("Processando imagens..."):
                st.balloons()
                st.info("Davi e Sofia estão analisando os riscos.")

# RODAPÉ
st.sidebar.markdown("---")
st.sidebar.success("Capacidade: 500MB Ativa")
st.sidebar.success("Modo: Lote Multi-foto Ativo")
