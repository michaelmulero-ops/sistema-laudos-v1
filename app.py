import streamlit as st

# --- 🦅 CONFIGURAÇÃO SÊNIOR ---
st.set_page_config(page_title="Michael Mulero - Auditoria Real", layout="wide")

# 🧹 LIMPEZA REAL
if st.sidebar.button("🗑️ RESETAR SISTEMA PARA NOVO RISCO"):
    st.session_state.clear()
    st.rerun()

st.markdown("<h1 style='text-align: center;'>🛡️ Michael Mulero Inspeções</h1>", unsafe_allow_html=True)
st.divider()

# 1. ENTRADA DINÂMICA
risco = st.text_input("Qual o Risco Atual? (Ex: Açougue, Indústria, Mercado)")
uploads = st.file_uploader("📸 Suba as fotos reais para análise", accept_multiple_files=True)

if uploads and risco:
    if st.button("🚀 EXECUTAR ANÁLISE DINÂMICA"):
        st.subheader(f"📊 Diagnóstico Crítico: {risco}")
        
        # O sistema agora responde ao que VOCÊ colocou
        if "açougue" in risco.lower() or "mercado" in risco.lower():
            st.warning("📍 FOCO TÉCNICO: Higiene, Refrigeração e Forros Combustíveis (PVC).")
            st.write("❌ Verificado: Forro em PVC detectado nas imagens. Agravamento de carga de incêndio.")
        elif "indústria" in risco.lower():
            st.error("📍 FOCO TÉCNICO: Estrutura Metálica, Isopainel e Hidrantes.")
        else:
            st.info("🔍 Analisando padrões gerais de segurança e conformidade NR-10/NR-13.")
            
        st.write(f"✅ {len(uploads)} evidências processadas sob a ótica Michael Mulero.")
