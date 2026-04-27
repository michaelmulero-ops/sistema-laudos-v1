import streamlit as st
import datetime

st.set_page_config(page_title="Michael Mulero | Compliance & Histórico", layout="wide")

st.markdown("<h1 style='text-align: center; color: #1A237E;'>🛡️ Michael Mulero: Varredura de Sinistralidade 5 Anos</h1>", unsafe_allow_html=True)

# ENTRADA DE DADOS DE COMPLIANCE
st.sidebar.header("🔍 Identificador de Risco")
doc_consulta = st.sidebar.text_input("CPF ou CNPJ para Varredura")
data_limite = datetime.date.today() - datetime.timedelta(days=5*365)

# MENU
aba = st.sidebar.radio("Operação:", ["Varredura 5 Anos", "Auditoria de Nexo", "Relatório Final"])

if aba == "Varredura 5 Anos":
    st.header(f"📅 Histórico Retrospectivo (Desde {data_limite.year})")
    if doc_consulta:
        with st.spinner(f"Consultando sinistros para {doc_consulta}..."):
            # Simulação de base de dados (Ex: casos como Roberta Cardilli ou Nicanor)
            st.subheader("🚩 Registros Encontrados:")
            col1, col2 = st.columns(2)
            with col1:
                st.warning("**Sinistro 113202209... (2022):** Vendaval/Inundação")
                st.info("Status: Indenizado | Valor: R$ 9.000,00")
            with col2:
                st.error("**Inconsistência:** O endereço atual coincide com zona de alagamento reincidente.")
    else:
        st.info("Insira um documento para iniciar a varredura automática.")

elif aba == "Auditoria de Nexo":
    st.header("⚖️ Análise de Nexo Causal")
    st.write("Compare os vestígios atuais com fotos de vistorias antigas do mesmo CPF/CNPJ.")
    st.file_uploader("Upload de Foto Atual para Comparação Digital")
    st.button("🤖 Comparar com Histórico (IA)")

elif aba == "Relatório Final":
    st.header("📋 Veredito de Subscrição")
    st.markdown("""
    | Indicador | Status |
    | :--- | :--- |
    | **Frequência de Sinistros** | Média (2 eventos em 5 anos) |
    | **Risco Moral** | Baixo |
    | **Saúde Financeira** | Regular |
    """)
    st.success("✅ RECOMENDAÇÃO: ACEITAR COM AGRAVAMENTO DE 10% EM VENDAVAL.")
        st.error("❌ VEREDITO: RISCO RECUSADO - Gravidade técnica e moral acima do limite aceitável.")
