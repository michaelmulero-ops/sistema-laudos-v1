import streamlit as st

# --- PAINEL DE CONTROLE (BOTÕES DE COMANDO) ---
with st.sidebar:
    st.markdown("### 🕹️ Painel de Operação")
    
    # Botão de Injeção de Dados (Processar Auditoria)
    if st.button("🚀 INJETAR DADOS NO LAUDO", use_container_width=True, type="primary"):
        st.session_state['processar'] = True
        st.success("Dados injetados com sucesso!")
    
    st.markdown("---")
    
    # Botão de Reset (Limpar para o Próximo Risco)
    if st.button("♻️ LIMPAR TELA / NOVO RISCO", use_container_width=True):
        # Limpa o cache e reinicia as variáveis do sistema Michael Mulero
        for key in st.session_state.keys():
            del st.session_state[key]
        st.rerun()

# --- LÓGICA DE EXIBIÇÃO ---
if st.session_state.get('processar'):
    st.info("🛠️ **Status:** Sofia processando croquis isométricos e compliance...")
    # Aqui o sistema renderiza os 6 croquis que você definiu
else:
    st.warning("Aguardando comando para injetar dados da inspeção em Ibiporã...")
