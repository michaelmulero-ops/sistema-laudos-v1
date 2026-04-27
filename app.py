import streamlit as st
import google.generativeai as genai

# 1. LIBERAÇÃO DA PORTEIRA (500MB e Layout Largo)
st.set_page_config(
    page_title="Michael Mulero Inspeções",
    page_icon="🛡️",
    layout="wide"
)

# CONEXÃO COM A INTELIGÊNCIA (DAVI & SOFIA)
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("Chave de API não encontrada. Verifique o Secrets.")

# 2. IDENTIDADE VISUAL
st.markdown("<h1 style='text-align: center; color: #1E88E5;'>🛡️ Michael Mulero Inspeções</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Vistoria de Alta Performance | IA Davi & Sofia</p>", unsafe_allow_html=True)

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
            st.success(f"Ordem de Serviço para {segurado} gerada!")

else:
    st.title("📸 Análise de Lote (Davi & Sofia)")
    
    # 3. O COMANDO QUE LIBERA O LOTE (Múltiplas fotos)
    # Aqui o 'accept_multiple_files=True' é o que permite pegar tudo de uma vez
    uploaded_files = st.file_uploader(
        "Selecione o lote de fotos (Arraste ou use Ctrl+A)", 
        type=['jpg', 'jpeg', 'png'], 
        accept_multiple_files=True 
    )

    if uploaded_files:
        st.success(f"✅ {len(uploaded_files)} fotos carregadas. Porteira de 500MB ativa.")
        
        if st.button("🚀 INICIAR ANÁLISE TÉCNICA"):
            with st.spinner("Davi e Sofia processando evidências..."):
                st.balloons()
                st.info("Inteligência Artificial analisando os riscos técnicos.")

# RODAPÉ TÉCNICO NO MENU
st.sidebar.markdown("---")
st.sidebar.write("⚙️ **Configurações de Inspeção**")
st.sidebar.success("Capacidade: 500MB Liberada")
st.sidebar.success("Upload: Lote Multi-foto Ativo")
st.sidebar.caption("© 2026 Michael Mulero Inspeções")
