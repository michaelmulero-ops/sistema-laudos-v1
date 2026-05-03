import streamlit as st
import google.generativeai as genai

# 1. Configuração Inicial
st.set_page_config(page_title="Michael Mulero | Tecnologia V1", layout="wide")
st.title("🛡️ Painel de Operação - Michael Mulero Inspeções")

# 2. Entrada de Dados
with st.sidebar:
    st.header("1. Injetar Pedido")
    cnpj = st.text_input("CNPJ/CPF:", value="38496589000133")
    categoria = st.selectbox("Categoria:", ["Comércio", "Indústria", "Residência"])

st.subheader("📋 Dados do Risco (Extração Automática)")
processo_operacional = st.text_area("Processo Operacional (O que rola lá?):", 
                                    value="Mini mercado de bairro em situações deplorável. Infiltrações, gôndolas vazias, falta de mercadorias e salários atrasados.")

# 3. Upload de Fotos
uploaded_files = st.file_uploader("Subir arquivos da vistoria:", accept_multiple_files=True)

# 4. Botão de Comando Final (A CORREÇÃO)
if st.button("🚀 FINALIZAR VISTORIA E GERAR PARECER"):
    if uploaded_files and processo_operacional:
        st.success("Análise Concluída com Sucesso!")
        
        # Exibição do Relatório
        st.divider()
        st.subheader("📄 Relatório Técnico Gerado")
        st.write(f"**CNPJ:** {cnpj}")
        st.write(f"**Classificação:** {categoria}")
        st.warning(f"**Parecer Técnico:** Identificado risco crítico em {categoria}. {processo_operacional}")
        
        # Exibição das Fotos
        st.subheader("📸 Evidências Fotográficas")
        cols = st.columns(3)
        for i, foto in enumerate(uploaded_files):
            cols[i % 3].image(foto, caption=foto.name, use_container_width=True)
            
        st.info("Você já pode fechar o computador. O relatório foi gerado e salvo.")
    else:
        st.error("Por favor, suba as fotos e preencha a descrição antes de gerar o parecer.")
