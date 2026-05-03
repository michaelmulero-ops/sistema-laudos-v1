import streamlit as st

# Função para limpar a tela e o cache
def limpar_sessao():
    for key in st.session_state.keys():
        del st.session_state[key]
    st.rerun()

# Interface do Sistema
st.title("🛡️ Michael Mulero Inspeções Tech V1")

# Botão de Limpeza na Barra Lateral
if st.sidebar.button("🧹 LIMPAR TELA / NOVO RISCO"):
    limpar_sessao()

st.sidebar.markdown(f"**Inspetor:** Michael Giovanni Mulero\n\n**Local:** Ibiporã, PR")

# Upload de novo pacote
pacote = st.file_uploader("Subir NOVO Pacote de Vistoria:", accept_multiple_files=True, key="novo_upload")

if pacote:
    st.info("🔄 Sistema pronto. Sofia aguardando as novas evidências para análise profunda.")
