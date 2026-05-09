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

# Estilização CSS para manter o visual moderno do teu app mobile
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stMetric { background-color: #1a1c23; padding: 15px; border-radius: 10px; border: 1px solid #2d2e35; }
    .stProgress > div > div > div > div { background-color: #1D9E75; }
    </style>
    """, unsafe_allow_html=True)

# Configuração da API Gemini (Secrets do Streamlit)
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
except:
    st.warning("⚠️ API Key não detectada. Algumas funções de IA podem estar limitadas.")

# =================================================================
# CLASSE DE INTELIGÊNCIA TÉCNICA (MANDANTE DO LAUDO)
# =================================================================
class AnalisadorVistoria:
    def __init__(self):
        pass

    def _analyze_sharpness(self, gray_image):
        """Analisa a nitidez da imagem usando Variância de Laplacian."""
        if gray_image is None or gray_image.size == 0:
            return 0.0
        return float(cv2.Laplacian(gray_image, cv2.CV_64F).var())

    def _get_risk_level(self, score):
        """Retorna o nível de risco baseado no score (0.0 a 1.0)"""
        if score < 0.3: return "Baixo"
        elif score < 0.6: return "Moderado"
        elif score < 0.8: return "Alto"
        else: return "Crítico"

    def processar_imagem(self, uploaded_file):
        """Executa a blindagem técnica da foto enviada."""
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Cálculo de Nitidez (Blindagem contra fotos borradas)
        sharpness = self._analyze_sharpness(gray)
        
        # Geração de Hash SHA-256 (Autenticidade Michael Mulero)
        hash_auth = hashlib.sha256(file_bytes).hexdigest()
        
        return {
            "nitidez": round(sharpness, 2),
            "hash": hash_auth,
            "status": "Aprovada" if sharpness > 100 else "Rejeitada (Baixa Qualidade)"
        }

analisador = AnalisadorVistoria()

# =================================================================
# INTERFACE PRINCIPAL - PAINEL DE CONTROLE
# =================================================================
st.title("🛡️ Michael Mulero Inspeções")
st.subheader("Sistema de Blindagem Industrial - V1.0")

# Painel de Métricas (Inspirado no teu HTML da USITRORG)
with st.container():
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Inspeções Ativas", "12")
    col2.metric("Fotos Rastreadas", "347")
    col3.metric("Alertas Pendentes", "3")
    col4.metric("IS Gerenciada", "R$ 47M")

st.markdown("---")

# Layout de Colunas: Esquerda (Dados/Vistoria) | Direita (Mapa/Riscos)
col_dados, col_mapa = st.columns([2, 1])

with col_dados:
    st.header("📊 Vistoria: USITRORG AMBIENTAL AS")
    
    # Upload de Fotos com Validação Técnica
    uploaded_file = st.file_uploader("Upload de Evidência (Foto Georeferenciada)", type=['jpg', 'png'])
    
    if uploaded_file:
        resultado = analisador.processar_imagem(uploaded_file)
        if resultado["status"] == "Aprovada":
            st.success(f"✅ Foto Autenticada! Hash SHA-256: {resultado['hash'][:16]}...")
            st.write(f"Nível de Nitidez: {resultado['nitidez']}")
        else:
            st.error(f"❌ {resultado['status']}. Por favor, tire uma nova foto com foco.")

    # Checklist de Blindagem
    st.subheader("📋 Checklist de Conformidade")
    st.checkbox("Vistoria interna — Bloco 01 (Unificado)", value=True)
    st.checkbox("Vistoria interna — Bloco 02 (Unificado)", value=True)
    st.checkbox("Inspeção de transformadores", value=True)
    st.checkbox("Monitoramento de Lagoas de Biogás", value=False)

with col_mapa:
    st.header("📍 Mapa de Blindagem")
    
    # Alerta Climatológico (Padrão do teu HTML)
    st.error("""
        **ALERTA CLIMATOLÓGICO**
        Risco de vendaval detectado no Norte Pioneiro.
        Exigida fixação técnica conforme NBR 5419.
    """)
    
    # Scores de Risco (Progresso)
    st.write("Risco de Incêndio (65%)")
    st.progress(0.65)
    
    st.write("Risco Ambiental (72%)")
    st.progress(0.72)
    
    st.write("Risco Elétrico (55%)")
    st.progress(0.55)

    if st.button("Gerar Laudo Final Blindado"):
        st.info("Compilando dados e gerando Hash de segurança...")
        # Aqui o sistema integraria com a geração de PDF

# Sidebar com Dados de Campo
st.sidebar.image("https://via.placeholder.com/150", caption="Inspetor: Michael Mulero")
st.sidebar.markdown(f"**GPS:** Ativo 📍")
st.sidebar.write(f"**Local:** Jacarezinho - PR")
st.sidebar.write(f"**Data:** {datetime.now().strftime('%d/%m/%Y %H:%M')}")
st.sidebar.button("Sincronizar com Nuvem")
