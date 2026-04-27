import streamlit as st
from datetime import date

# MÓDULO DE COMPLIANCE DOCUMENTAL (Michael Mulero V17)
st.subheader("📁 Central de Documentos e Alvarás")

# Lista de documentos padrão para o mercado de seguros
docs_necessarios = [
    "AVCB / CLCB (Corpo de Bombeiros)",
    "Alvará de Funcionamento",
    "Laudo de SPDA (Para-raios)",
    "Certificado de Brigada de Incêndio",
    "Plano de Emergência / PAPI",
    "Prontuário das Instalações Elétricas (NR-10)"
]

col_doc, col_status, col_validade = st.columns([2, 1, 1])

# Dicionário para armazenar o status
status_docs = {}

for doc in docs_necessarios:
    with col_doc:
        st.write(f"**{doc}**")
        st.file_uploader(f"Anexar {doc}", label_visibility="collapsed", key=f"file_{doc}")
        
    with col_status:
        status = st.selectbox("Status", ["Pendente", "Apresentado", "Não Possui"], key=f"status_{doc}")
        status_docs[doc] = status
        
    with col_validade:
        validade = st.date_input("Validade", value=None, key=f"val_{doc}")

# VEREDITO DOCUMENTAL
if st.button("🚀 VALIDAR COMPLIANCE"):
    st.markdown("---")
    st.subheader("⚖️ Análise de Risco Jurídico")
    
    docs_faltantes = [d for d, s in status_docs.items() if s != "Apresentado"]
    
    if docs_faltantes:
        st.error(f"⚠️ **ALERTA CRÍTICO:** Empresa operando sem {len(docs_faltantes)} documentos essenciais.")
        for d in docs_faltantes:
            st.write(f"❌ Ausência de: {d}")
    else:
        st.success("✅ Compliance Documental em conformidade com as exigências Allianz/Sancor.")
