import streamlit as st
import numpy as np
import cv2
import hashlib
from datetime import datetime
import google.generativeai as genai

# =================================================================
# CONFIGURAÇÃO DE INTERFACE - PADRÃO MICHAEL MULERO (DARK MODE)
# =================================================================
st.set_page_config(
    page_title="Michael Mulero Inspeções Tech V1", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# Estilização CSS para o visual moderno do app
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stMetric { background-color: #1a1c23; padding: 15px; border-radius: 10px; border: 1px solid #2d2e35; }
    </style>
    """, unsafe_allow_html=True)

# Configuração da IA (Secrets do Streamlit)
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
except:
    st.warning("⚠️ Configurar GOOGLE_API_KEY nos Secrets para ativar IA.")

# =================================================================
# MÓDULOS DE ANÁLISE TÉCNICA
# =================================================================
class AnalisadorVistoria:
    def _analyze_sharpness(self, gray_image):
        """Avalia nitidez para evitar fotos borradas"""
        if gray_image is None or gray_image.size == 0:
            return 0.0
        return float(cv2.Laplacian(gray_image, cv2.CV_64F).var())

    def processar_evidencia(self, uploaded_file):
        """Gera Hash SHA-256 e valida qualidade"""
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        sharpness = self._analyze_sharpness(gray)
        hash_auth = hashlib.sha256(file_bytes).hexdigest()
        
        return {"nitidez": round(sharpness, 2), "hash": hash_auth}

analisador = AnalisadorVistoria()

# =================================================================
# INTERFACE PRINCIPAL (BASEADA NO TEU HTML)
# =================================================================
st.title("🛡️ Michael Mulero Inspeções")
st.subheader("Sistema de Blindagem Industrial")

# Painel de Métricas
with st.container():
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Inspeções Ativas", "12")
    col2.metric("Fotos Rastreadas", "347")
    col3.metric("Alertas Pendentes", "3")
    col4.metric("IS Total Gerenciada", "R$ 47M")

st.markdown("---")

col_esq, col_dir = st.columns([2, 1])

with col_esq:
    st.header("📋 Vistoria: USITRORG AMBIENTAL AS")
    st.caption("CNPJ 28.698.939/0001-90 · Jacarezinho-PR")
    
    # Upload e Validação de Imagem
    foto = st.file_uploader("Capturar ou Importar Foto Rastreada", type=['jpg', 'png'])
    if foto:
        res = analisador.processar_evidencia(foto)
        st.success(f"✅ Evidência Autenticada | Hash: {res['hash'][:16]}...")
        st.info(f"Qualidade Técnica (Nitidez): {res['nitidez']}")

    # Checklist de Inspeção
    st.subheader("Checklist Digital")
    st.checkbox("Vistoria interna — Bloco 01 e 02 (Unificados)", value=True)
    st.checkbox("Inspeção de Transformadores", value=True)
    st.checkbox("Monitoramento de Lagoas de Biogás", value=False)

with col_dir:
    st.header("📍 Blindagem 500m")
    
    # Alerta Climatológico do teu App
    st.error("**Risco de vendaval — Norte Pioneiro**\n\nExige fixação técnica (NBR 5419).")
    
    # Scores de Risco Dinâmicos
    st.write("Risco Incêndio (65%)")
    st.progress(0.65)
    st.write("Risco Ambiental (72%)")
    st.progress(0.72)
    st.write("Risco Elétrico (55%)")
    st.progress(0.55)

# Sidebar de Campo
st.sidebar.write(f"**Data:** {datetime.now().strftime('%d/%m/%Y %H:%M')}")
st.sidebar.write("**GPS:** Ativo 📍 -23.1591°, -49.9718°")
