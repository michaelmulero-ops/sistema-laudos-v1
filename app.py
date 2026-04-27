
import streamlit as st
import google.generativeai as genai
import time

# CONFIGURAÇÃO DE ALTA FIDELIDADE
st.set_page_config(page_title="Michael Mulero | Engenharia 360", layout="wide")
genai.configure(api_key="AIzaSyD-v8W9rV5X6-XW_S8W4E_Jv9M8")

# --- MEMÓRIA DO PASSEIO (TRACKING) ---
if 'checklist' not in st.session_state:
    st.session_state['checklist'] = {
        "Fachada/Portaria": {},
        "Produção/Área Técnica": {},
        "Utilidades/Elétrica": {},
        "Segurança/CFTV": {}
    }

st.markdown("<h1 style='text-align: center; color: #0D47A1;'>🛡️ Michael Mulero: Mapeamento Digital 3D</h1>", unsafe_allow_html=True)

# MENU LATERAL: O PASSO A PASSO DO INSPETOR
st.sidebar.header("📍 Roteiro de Inspeção")
fase = st.sidebar.radio("Onde você está agora?", ["1. Fachada e Portaria", "2. Quadros e Elétrica", "3. Combate a Incêndio", "4. CFTV e Sensores", "5. Gerar Relatório Nível A"])

if fase == "1. Fachada e Portaria":
    st.header("🏢 Mapeamento de Perímetro")
    col1, col2 = st.columns(2)
    with col1:
        st.session_state['checklist']["Fachada/Portaria"]["cameras"] = st.number_input("Quantidade de Câmeras Externas", min_value=0)
        st.session_state['checklist']["Fachada/Portaria"]["estado_portao"] = st.selectbox("Estado da Portaria", ["Excelente", "Bom", "Precário"])
    with col2:
        foto_fachada = st.file_uploader("Foto da Fachada (Georreferenciada)", type=['jpg', 'jpeg', 'png'])
        st.info("💡 Cada foto aqui alimenta o ponto zero do seu Croqui Digital.")

elif fase == "2. Quadros e Elétrica":
    st.header("⚡ Inventário de Utilidades: Elétrica")
    with st.expander("Detalhamento de Quadros Elétricos"):
        qnt_quadros = st.number_input("Quantos quadros analisados?", min_value=0)
        obs_eletrica = st.text_area("Observações Técnicas (Fiação, Termografia, Identificação)")
        fotos_eletrica = st.file_uploader("Fotos dos Quadros", accept_multiple_files=True)

elif fase == "5. Gerar Relatório Nível A":
    st.header("📊 Consolidação de Dados para Seguradora")
    st.write("Aqui o Davi e a Sofia cruzam os dados do seu 'passeio' com a Matriz FEPAM/TSIB.")
    
    if st.button("🚀 GERAR RELATÓRIO E CROQUI 3D"):
        with st.spinner("Construindo inteligência do laudo..."):
            st.balloons()
            st.success("Relatório de Alta Fidelidade Gerado!")
            # Simulação do Relatório Integrado
            st.markdown("""
            ### PARECER TÉCNICO FINAL
            - **Estrutura:** Identificada conformidade em 95% da planta.
            - **Segurança Eletrônica:** Sistema robusto com monitoramento ativo.
            - **Elétrica:** Recomendado reaperto de conexões no quadro secundário.
            - **Status do Croqui:** Pontos de controle exportados para renderização 3D.
            """)

st.sidebar.markdown("---")
st.sidebar.warning("📱 Sincronizado com Celular do Inspetor")
