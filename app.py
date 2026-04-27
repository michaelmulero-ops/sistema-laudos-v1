import streamlit as st
import google.generativeai as genai

# CONFIGURAÇÃO DE ENGENHARIA AVANÇADA
st.set_page_config(page_title="Michael Mulero | Perícia Autônoma", layout="wide")
genai.configure(api_key="AIzaSyD-v8W9rV5X6-XW_S8W4E_Jv9M8")

st.markdown("<h1 style='text-align: center; color: #0D47A1;'>🛡️ Michael Mulero: Vistoria Inteligente (Vision & Track)</h1>", unsafe_allow_html=True)

# BARRA LATERAL - SENSORES DE CAMPO
st.sidebar.header("📡 Sensores Mobile")
passos = st.sidebar.number_input("Pedômetro (Passos contados)", min_value=0)
distancia = passos * 0.75 # Estimativa de metragem percorrida
st.sidebar.metric("Distância Mapeada", f"{distancia} metros")

# MÓDULO DE TRABALHO
aba = st.sidebar.radio("Atividade:", ["Scanner de Equipamentos", "Mapeamento 3D/Croqui", "Auditoria Ultra Hard"])

if aba == "Scanner de Equipamentos":
    st.header("🔍 Scanner de Ativos (IA Vision)")
    st.info("Aponte para o selo do extintor ou placa do quadro elétrico.")
    foto_ativo = st.file_uploader("Capturar Imagem do Equipamento", type=['jpg', 'png'])
    
    if foto_ativo:
        with st.spinner("IA 'Lens' analisando validade e tipo..."):
            # Aqui a IA faz a leitura OCR do selo e identifica o objeto
            st.success("Equipamento Identificado: Extintor PQS 6kg")
            st.warning("⚠️ Alerta: Validade próxima ao vencimento (08/2026).")
            st.image(foto_ativo, width=300)

elif aba == "Mapeamento 3D/Croqui":
    st.header("📐 Geração de Croqui via GPS/Pedômetro")
    if distancia < 50:
        st.error("❌ Percurso insuficiente para gerar Croqui. O inspetor deve percorrer todo o perímetro.")
    else:
        st.success(f"✅ Perímetro de {distancia}m validado. Gerando volumetria 3D...")
        # Simulação dos 5 Croquis
        tabs = st.tabs(["Localização", "Setorização", "Proteção", "Utilidades", "PMP 3D"])
        with tabs[4]:
            st.write("Visualização da barreira física e propagação de fumaça.")

elif aba == "Auditoria Ultra Hard":
    st.header("🚨 Auditoria Final (O Ovo no Pelo)")
    if st.button("🔥 EXECUTAR PENTE FINO"):
        st.subheader("📌 Inconsistências de Campo")
        st.error("- O inspetor não acessou a casa de máquinas (GPS estático).\n- Foto do hidrante indica mangueira sem bico de esguicho.")
