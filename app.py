import streamlit as st
import numpy as np
import cv2
import hashlib
from datetime import datetime
import google.generativeai as genai

# =================================================================
# CONFIGURAÇÃO DE INTERFACE UNIVERSAL - PADRÃO MICHAEL MULERO
# =================================================================
st.set_page_config(
    page_title="Michael Mulero Multi-Inspeção", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# Estilização Dark Mode para qualquer dispositivo
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stMetric { background-color: #1a1c23; padding: 15px; border-radius: 10px; border: 1px solid #2d2e35; }
    .stProgress > div > div > div > div { background-color: #1D9E75; }
    </style>
    """, unsafe_allow_html=True)

# Inicialização da IA (Para análise de qualquer tipo de risco)
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.warning("⚠️ Chave de API não configurada. O motor de IA está em modo offline.")

# =================================================================
# MOTOR DE PROCESSAMENTO AGNOSTICO (PARA QUALQUER RISCO)
# =================================================================
class EngineInspecao:
    def validar_imagem(self, uploaded_file):
        """Analisa qualidade técnica e gera prova de autenticidade (Hash)"""
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        sharpness = cv2.Laplacian(gray, cv2.CV_64F).var()
        hash_auth = hashlib.sha256(file_bytes).hexdigest()
        
        return {"nitidez": round(sharpness, 2), "hash": hash_auth}

    def sugerir_checklist(self, tipo_risco):
        """Retorna itens de inspeção baseados no tipo de risco selecionado"""
        checklists = {
            "Industrial": ["Cabine Primária/Transformadores", "Carga de Incêndio", "Depósitos de Resíduos", "Linha de Produção"],
            "Residencial/Condomínio": ["Áreas Comuns/Lazer", "SPDA (Pára-raios)", "Bombas de Recalque", "Garagens/Subsolo"],
            "Rural/Agrícola": ["Armazenagem de Grãos/Silos", "Maquinário Agrícola", "Tanques de Combustível", "Sede/Alojamento"],
            "Comercial": ["Saídas de Emergência", "Instalações Elétricas", "Estoque/Almoxarifado", "Acessibilidade"]
        }
        return checklists.get(tipo_risco, ["Inspeção Geral de Perímetro", "Verificação de Cobertura", "Instalações Elétricas"])

engine = EngineInspecao()

# =================================================================
# INTERFACE DINÂMICA
# =================================================================
st.title("🛡️ Michael Mulero Inspeções")
st.caption("Plataforma Universal de Blindagem de Risco Tech V1")

# Seleção do Tipo de Inspeção (O código agora é aberto)
tipo_inspecao = st.selectbox(
    "Selecione o Segmento da Inspeção:",
    ["Industrial", "Residencial/Condomínio", "Rural/Agrícola", "Comercial", "Outros"]
)

# Painel de Métricas Gerais
with st.container():
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Tipo de Risco", tipo_inspecao)
    col2.metric("Status do GPS", "Ativo 📍")
    col3.metric("Segurança", "SHA-256 ON")
    col4.metric("Versão", "Tech V1.2")

st.markdown("---")

col_left, col_right = st.columns([2, 1])

with col_left:
    nome_risco = st.text_input("Identificação do Risco (Ex: Nome da Empresa ou Condomínio)", placeholder="Digite o nome do segurado...")
    
    st.subheader("📸 Captura de Evidências")
    foto = st.file_uploader("Upload de Foto de Campo (Georeferenciada)", type=['jpg', 'png'])
    
    if foto:
        res = engine.validar_imagem(foto)
        if res['nitidez'] > 50:
            st.
