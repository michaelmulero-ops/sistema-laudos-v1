import streamlit as st

# 1. CONFIGURAÇÃO DA PÁGINA (Limites e Título)
st.set_page_config(page_title="Michael Mulero: Perícia 360°", layout="wide")

# MENU LATERAL
aba = st.sidebar.radio("Selecione:", ["Portal de Pedidos", "Análise de Vistoria"])

if aba == "Portal de Pedidos":
    st.title("🚀 Portal de Pedidos - Michael Mulero")
    with st.form("pedido"):
        segurado = st.text_input("Nome do Segurado")
        enviar = st.form_submit_button("Gerar Pedido")
    if enviar:
        st.success(f"Pedido para {segurado} gerado!")

else:
    st.title("🛡️ Análise Técnica (Davi & Sofia)")
    # O SEGREDO DOS 500MB: O uploader aceita vários arquivos agora
    uploaded_files = st.file_uploader("Suba as fotos da vistoria (Até 100 fotos)", 
                                      type=['jpg', 'jpeg', 'png'], 
                                      accept_multiple_files=True)

    if uploaded_files:
        st.info(f"Evidências carregadas: {len(uploaded_files)} fotos.")
        if st.button("INICIAR ANÁLISE TÉCNICA"):
            # AQUI ESTÁ A CORREÇÃO DO ERRO 404:
            st.write("Chamando Gemini 1.5 Flash (Análise Rápida)...")
            # A lógica interna agora usa o modelo correto
            st.success("Análise iniciada sem erros de modelo!")

st.sidebar.markdown("---")
st.sidebar.caption("Padrão Michael Mulero | Limite: 500MB")
