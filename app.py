# --- 🧹 COMANDO DE LIMPEZA GERAL ---
if st.sidebar.button("🗑️ LIMPAR TODOS OS DADOS", use_container_width=True):
    for key in st.session_state.keys():
        del st.session_state[key]
    st.rerun()
