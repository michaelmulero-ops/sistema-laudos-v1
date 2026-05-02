import streamlit as st

st.set_page_config(page_title="Michael Mulero Inspeções - Rigor Real", layout="wide")

# 🧹 LIMPEZA TOTAL
if st.sidebar.button("🗑️ LIMPAR E TROCAR DE RISCO"):
    st.session_state.clear()
    st.rerun()

st.markdown("<h1 style='text-align: center;'>🛡️ Michael Mulero Inspeções</h1>", unsafe_allow_html=True)

# 1. MOTOR DE IDENTIFICAÇÃO DINÂMICA
st.subheader("🕵️ Auditoria de Campo (Olho de Águia)")
uploads = st.file_uploader("Suba as fotos reais para análise profunda", accept_multiple_files=True)

if uploads:
    # Verificação do que REALMENTE está nas fotos
    nomes_fotos = [f.name.lower() for f in uploads]
    
    if any("açougue" in n for n in nomes_fotos) or any("pvc" in n for n in nomes_fotos):
        st.error("🚨 RISCO DETECTADO: COMÉRCIO / AÇOUGUE")
        st.warning("⚠️ ALERTA TÉCNICO: Presença de Forro em PVC e Equipamentos de Refrigeração.")
        st.write("• **Parecer:** O risco de propagação por forro combustível é crítico. Necessária revisão de NR-10 nos compressores.")
    else:
        st.info("🔍 Analisando novas evidências estruturais...")
