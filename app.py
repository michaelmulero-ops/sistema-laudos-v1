import streamlit as st

# 1. CONFIGURAÇÃO DA PÁGINA E MEMÓRIA
# O limite de 500MB é reforçado aqui e no arquivo config.toml que você criou
st.set_page_config(page_title="Michael Mulero Inspeções", layout="wide")

# ESTILO PARA O TÍTULO
st.markdown("<h1 style='text-align: center; color: #1E88E5;'>🛡️ Michael Mulero Inspeções</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Sistema de Alta Performance para Laudos e Vistorias</p>", unsafe_allow_html=True)

# 2. MENU LATERAL
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/1063/1063374.png", width=100)
aba = st.sidebar.radio("Navegação:", ["Portal de Pedidos", "Análise de Vistoria"])

if aba == "Portal de Pedidos":
    st.title("📋 Portal de Pedidos")
    with st.form("pedido_form"):
        col1, col2 = st.columns(2)
        with col1:
            segurado = st.text_input("Nome do Segurado / Condomínio")
            pedido_cia = st.text_input("Nº Pedido CIA")
        with col2:
            corretor = st.text_input("Corretor")
            cidade = st.text_input("Cidade/UF")
        
        enviar = st.form_submit_button("Gerar Ordem de Serviço")
    
    if enviar:
        st.success(f"Ordem de Serviço para {segurado} gerada com sucesso!")

else:
    st.title("📸 Análise de Vistoria (Davi & Sofia)")
    st.info("A porteira está aberta! Você pode selecionar até 100 fotos de uma vez.")

    # 3. O SEGREDO DO LOTE (accept_multiple_files=True)
    uploaded_files = st.file_uploader(
        "Selecione o lote de fotos da vistoria", 
        type=['jpg', 'jpeg', 'png'], 
        accept_multiple_files=True  # <-- ISSO LIBERA O LOTE
    )

    if uploaded_files:
        st.success(f"✅ {len(uploaded_files)} fotos carregadas com sucesso!")
        
        if st.button("🚀 INICIAR ANÁLISE TÉCNICA"):
            with st.spinner("Analisando evidências e mapeando riscos..."):
                # Aqui entra a inteligência que usa a sua GOOGLE_API_KEY
                st.write("Davi e Sofia estão processando as imagens...")
                st.balloons()

# RODAPÉ DE CONTROLE
st.sidebar.markdown("---")
st.sidebar.write("⚙️ **Status do Sistema**")
st.sidebar.info("Limite: 500MB Liberado")
st.sidebar.info("Upload: Múltiplos Arquivos Ativo")
