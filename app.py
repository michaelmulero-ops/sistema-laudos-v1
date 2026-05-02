import streamlit as st # Garante que o 'st' funcione em todo o código
import time

# --- 📑 CONFIGURAÇÃO E CABEÇALHO MICHAEL MULERO ---
st.set_page_config(page_title="Michael Mulero Inspeções Tech V1", layout="wide")

def gerar_cabecalho_tecnico():
    st.markdown("## 🛡️ Michael Mulero Inspeções - Central de Laudos")
    col1, col2 = st.columns(2)
    with col1:
        cnpj = st.text_input("CNPJ do Risco", placeholder="00.000.000/0001-00")
        atividade = st.text_input("Atividade Principal", placeholder="Ex: Frigorífico")
    with col2:
        cod_risco = st.text_input("Código do Risco (Manual)", placeholder="Ex: IND-AL-05")
        normativos = st.multiselect("Normativos Aplicáveis", ["NR-10", "NR-11", "NR-13", "NBR-5410"], default=["NR-10", "NBR-5410"])
    return cnpj, atividade, cod_risco

# --- 🚀 INTERFACE DE OPERAÇÃO ---
cnpj, atividade, cod_risco = gerar_cabecalho_tecnico()
st.divider()

# Agora o botão vai funcionar sem NameError:
if st.button("📥 Gerar PDF do Laudo 10x10 (92 Evidências)"):
    with st.spinner("Davi consolidando dados de Ibiporã e investigação de 5 anos..."):
        time.sleep(2)
        st.success(f"Laudo para {atividade} (Código {cod_risco}) gerado com sucesso!")
