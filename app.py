import streamlit as st
import pandas as pd
from datetime import datetime

def investigar_entidade(documento):
    """Simula consulta de compliance e saúde financeira do risco"""
    # Lógica de simulação de consulta (em produção, conectaria a uma API de birô)
    if len(documento) > 11:  # CNPJ
        return {
            "Tipo": "Jurídica",
            "Situação": "ATIVA",
            "CNAE Principal": "Comércio Varejista",
            "Risco Financeiro": "Baixo",
            "Apontamentos": "Nenhum histórico de sinistro grave."
        }
    else:  # CPF
        return {
            "Tipo": "Física",
            "Situação": "REGULAR",
            "Risco Financeiro": "Moderado",
            "Apontamentos": "Pequena divergência cadastral de endereço."
        }

# --- Interface Michael Mulero ---
st.divider()
st.header("🔍 Investigação de Compliance e Risco Cadastral")
st.write("Validação de dados junto à Receita Federal e análise de histórico de sinistralidade.")

doc_input = st.text_input("Digite o CNPJ ou CPF do Risco para investigação:")

if doc_input:
    with st.spinner("Sofia consultando bases de compliance..."):
        dados = investigar_entidade(doc_input)
        
        col_inf1, col_inf2, col_inf3 = st.columns(3)
        col_inf1.metric("Situação Cadastral", dados["Situação"])
        col_inf2.metric("Risco Financeiro", dados["Risco Financeiro"])
        col_inf3.metric("Tipo de Entidade", dados["Tipo"])

        st.subheader("📋 Relatório Detalhado de Compliance")
        df_cadastral = pd.DataFrame([dados])
        st.table(df_cadastral)
        
        if dados["Risco Financeiro"] == "Baixo":
            st.success("✅ **Veredito Sofia:** O segurado apresenta baixo risco moral. Prosseguir com a emissão da apólice.")
        else:
            st.warning("⚠️ **Atenção Pericial:** Verificar histórico detalhado de pagamentos e endereços anteriores.")
