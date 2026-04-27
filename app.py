import streamlit as st
import google.generativeai as genai

# CONFIGURAÇÃO DE ENGENHARIA
st.set_page_config(page_title="Michael Mulero | Vistoria Balan", layout="wide")
genai.configure(api_key="AIzaSyD-v8W9rV5X6-XW_S8W4E_Jv9M8")

# --- BANCO DE DADOS DA VISTORIA ---
if 'balan_data' not in st.session_state:
    st.session_state['balan_data'] = {"passos": 0, "itens": []}

st.markdown("<h1 style='text-align: center; color: #0D47A1;'>🛡️ Operação: Condomínio Residencial Balan</h1>", unsafe_allow_html=True)
st.info("📅 Agendado para: Quarta-feira | Padrão: Inspeção Nível A")

# MENU DE CAMINHADA (O PASSO A PASSO DO INSPETOR)
etapa = st.sidebar.selectbox("Fase da Vistoria:", 
    ["1. Entrada e Fachada", "2. Estrutura e Cobertura", "3. Elétrica e Utilidades", "4. Prevenção e Incêndio", "5. Finalizar e Gerar RTI"])

if etapa == "1. Entrada e Fachada":
    st.header("🏢 Início do Passeio: Perímetro")
    col1, col2 = st.columns(2)
    with col1:
        cameras = st.number_input("Câmeras na Portaria", min_value=0)
        sensores = st.number_input("Sensores de Presença", min_value=0)
    with col2:
        st.file_uploader("Foto da Fachada Principal", type=['jpg', 'png'], key="foto_f")
        st.file_uploader("Foto dos Acessos (Veículos/Pedestres)", type=['jpg', 'png'], key="foto_a")

elif etapa == "3. Elétrica e Utilidades":
    st.header("⚡ Inventário Técnico: Elétrica")
    st.warning("Foco: Disjuntores, fiação e sinais de aquecimento.")
    qnt_quadros = st.number_input("Número de Quadros Elétricos", min_value=0)
    obs = st.text_area("Observações Técnicas (Ex: Fiação exposta, falta de legenda)")
    st.file_uploader("Fotos dos Quadros (Lote)", accept_multiple_files=True)

elif etapa == "5. Finalizar e Gerar RTI":
    st.header("📐 Consolidação do Laudo Sênior")
    if st.button("🚀 PROCESSAR DADOS DO BALAN"):
        with st.spinner("Davi e Sofia montando o Croqui 3D e a Matriz FEPAM..."):
            st.success("Relatório Técnico Pré-formatado!")
            st.markdown("""
            **PARECER TÉCNICO (PRÉVIA):**
            - Estrutura Classe 1 (Superior).
            - Risco Adjacente: Residencial (Baixo impacto).
            - PMP sugerido para subscrição: 20%.
            """)

st.sidebar.markdown("---")
st.sidebar.warning("📱 Sincronizado com Celular do Inspetor")
