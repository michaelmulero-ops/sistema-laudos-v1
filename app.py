import streamlit as st
import google.generativeai as genai

# CONFIGURAÇÃO NÍVEL A - MICHAEL MULERO
st.set_page_config(page_title="Michael Mulero | Engenharia de Riscos", layout="wide")
genai.configure(api_key="AIzaSyD-v8W9rV5X6-XW_S8W4E_Jv9M8")

# NAVEGAÇÃO POR CAMADAS DE CROQUI
st.sidebar.title("📊 Painel de Engenharia")
modulo = st.sidebar.radio("Selecione a Camada:", [
    "1. Localização e Vizinhança", 
    "2. Setorização de Risco", 
    "3. Inventário de Proteção", 
    "4. Mapa de Utilidades", 
    "5. Análise de PMP (3D)"
])

st.markdown(f"## 🛡️ Mapeamento Digital: {modulo}")

if modulo == "1. Localização e Vizinhança":
    st.info("Foco: Identificação de Riscos Adjacentes e Coordenadas.")
    col1, col2 = st.columns(2)
    with col1:
        st.text_input("Vizinhança Norte (O que existe?)")
        st.text_input("Vizinhança Sul (O que existe?)")
    with col2:
        st.file_uploader("Upload: Foto Aérea / Drone", key="drone")

elif modulo == "3. Inventário de Proteção":
    st.subheader("🧯 Checkpoint de Equipamentos")
    # Tabela dinâmica para o inventário
    if 'inventario' not in st.session_state: st.session_state.inventario = []
    
    with st.expander("Adicionar Item ao Inventário"):
        tipo = st.selectbox("Equipamento", ["Extintor PQS", "Extintor CO2", "Hidrante", "Câmera CFTV", "Sensor de Fumaça"])
        validade = st.date_input("Validade/Última Manutenção")
        if st.button("Registrar Item"):
            st.session_state.inventario.append({"tipo": tipo, "validade": validade})
    
    st.table(st.session_state.inventario)

elif modulo == "5. Análise de PMP (3D)":
    st.subheader("📐 Cálculo de Perda Máxima Provável")
    st.write("Davi e Sofia calculando o cenário de maior dano material.")
    m_fepam = st.select_slider("Severidade FEPAM", options=["1", "2", "3", "4", "5"])
    st.success(f"Matriz de Risco calibrada para Nível {m_fepam}")

st.sidebar.markdown("---")
st.sidebar.caption("Sincronizado: Padrão Michael Mulero Inspeções")

st.sidebar.markdown("---")
st.sidebar.warning("📱 Sincronizado com Celular do Inspetor")
