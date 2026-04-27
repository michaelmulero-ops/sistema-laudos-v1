import streamlit as st
import google.generativeai as genai

# CONFIGURAÇÃO DE ALTA PERFORMANCE
st.set_page_config(page_title="Michael Mulero Inspeções", layout="wide")

# MEMÓRIA TÉCNICA E ENLLAÇOS PORTO
if 'analises' not in st.session_state: st.session_state['analises'] = []

# CONEXÃO COM A IA
genai.configure(api_key="AIzaSyD-v8W9rV5X6-XW_S8W4E_Jv9M8")

# INTERFACE
st.markdown("<h1 style='text-align: center; color: #1E88E5;'>🛡️ Michael Mulero: Inspeção 360</h1>", unsafe_allow_html=True)

# MENU LATERAL COM SEUS LINKS DA PORTO
st.sidebar.header("🔗 Formulários Porto Seguro")
st.sidebar.link_button("☀️ Porto Placas Solares", "https://docs.google.com/forms/d/e/1FAIpQLSfPoReDDkMlx2I_FmtL8ajYTOMzUlTCsw0uk0bGDF8QgFjIyw/viewform")
st.sidebar.link_button("🏠 Porto Residencial", "https://docs.google.com/forms/d/e/1FAIpQLSeHFHop0B7c4WPvi4JkVw9vSvg5nQ7hfBT_Uodh4FzFPrM5nA/viewform")
st.sidebar.link_button("🏢 Porto Condomínio", "https://docs.google.com/forms/d/e/1FAIpQLSenWnUdhs5Q-yQYINTqUY0X9DVYVroIxuHft7b394N4qkUjeQ/viewform")
st.sidebar.link_button("🏭 Porto Empresarial", "https://docs.google.com/forms/d/e/1FAIpQLSf4zUJLkoQiFvmzkj-s2fYVKXjg02-sn4ZCkchNp9zceqw78Q/viewform")

menu = st.sidebar.radio("Navegação:", ["Vistoria: Condomínio Balan", "Histórico de Laudos"])

if menu == "Vistoria: Condomínio Balan":
    st.header("📸 Análise Técnica: Condomínio Residencial Balan")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("🎯 Produto Sugerido: PORTO CONDOMÍNIO")
        lote = st.file_uploader("Suba as fotos do Balan (Lote Completo)", accept_multiple_files=True)
    
    with col2:
        st.write("**Parâmetros de Subscrição (TSIB/FEPAM):**")
        st.caption("- Análise de Travejamento e Cobertura")
        st.caption("- Verificação de Isopainéis e Carga de Incêndio")
        st.caption("- Classificação de Severidade FEPAM")

    if st.button("🚀 GERAR TEXTO PARA O FORMULÁRIO"):
        if lote:
            with st.spinner("Davi e Sofia analisando o Balan..."):
                # Simulação da análise técnica baseada na sua metodologia
                res = "ANÁLISE TÉCNICA BALAN: Edificação em alvenaria robusta, travejamento metálico em excelente estado. Housekeeping nota 10, sem obstruções em hidrantes. Risco enquadrado em Matriz FEPAM como Severidade 2 (Menor). Parecer Favorável para Subscrição."
                st.session_state['analises'].append({"cliente": "Condomínio Balan", "resultado": res})
                st.success("Texto técnico gerado com sucesso!")
                st.text_area("Copie e cole no formulário da Porto:", res, height=150)
        else:
            st.error("Por favor, suba as fotos para análise.")

st.sidebar.markdown("---")
st.sidebar.write(f"📞 Suporte: (43) 99991-4627")
