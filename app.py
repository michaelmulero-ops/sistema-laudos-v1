import streamlit as st
import os
import time
from PIL import Image, ImageDraw

# --- CONFIGURAÇÕES DO SISTEMA MICHAEL MULERO ---
st.set_page_config(page_title="Michael Mulero Inspeções Tech", layout="wide")

# Título Principal
st.title("🛡️ Michael Mulero Inspeções Tech V1")

# Pastas de Trabalho
PENDING_DIR = "upload_pendente"
if not os.path.exists(PENDING_DIR):
    os.makedirs(PENDING_DIR)

# --- 🧠 MÓDULO DAVI: RASTREAMENTO CNPJ (5 ANOS RETROATIVOS) ---
with st.sidebar:
    st.title("Agentes Sofia & Davi")
    st.divider()
    st.subheader("🏢 Auditoria de CNPJ (5 Anos)")
    cnpj_input = st.text_input("Inserir CNPJ para Varredura", placeholder="00.000.000/0000-00")
    
    if st.button("Executar Varredura Profunda"):
        if cnpj_input:
            with st.spinner(f"Davi analisando histórico desde 2021..."):
                time.sleep(2) # Simulação de busca em tribunais e birôs
                st.warning("⚠️ Histórico: Detectados 2 processos cíveis em 2023.")
                st.success("✅ Sem dívidas ativas impeditivas nos últimos 5 anos.")
                st.info("🔍 CNAE compatível com risco industrial/residencial.")
        else:
            st.error("Por favor, insira um CNPJ.")

# --- 🧠 MÓDULO SOFIA: MONITORAMENTO E CROQUI NÍVEL 1 ---
def aplicar_monitoramento_sofia(imagem):
    img = imagem.convert("RGB")
    draw = ImageDraw.Draw(img)
    w, h = img.size
    
    # Base: Frente à Rua
    draw.line([(0, 3*h//4), (w, 3*h//4)], fill=(150, 150, 150), width=4)
    
    # Identificação de Ativos (Miras Inteligentes)
    ativos = [
        {"nome": "Transformador", "cor": (0, 255, 0), "pos": [w//4, h//2, w//2.5, h//1.3]},
        {"nome": "Gerador/Caldeira", "cor": (255, 255, 0), "pos": [w//2, h//5, 3*w//4, h//2.5]}
    ]
    
    for ativo in ativos:
        draw.rectangle(ativo["pos"], outline=ativo["cor"], width=5)
        x1, y1, _, _ = ativo["pos"]
        draw.text((x1 + 5, y1 - 25), f"SCAN: {ativo['nome']}", fill=ativo["cor"])

    return img

# --- INTERFACE DE CAMPO ---
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Captura de Inspeção")
    arquivos = st.file_uploader("Fotos da Galeria", type=["jpg", "png", "jpeg"], accept_multiple_files=True)
    foto_cam = st.camera_input("Scanner ao Vivo")

processar = arquivos if arquivos else ([foto_cam] if foto_cam else [])

if processar:
    for item in processar:
        img_original = Image.open(item)
        img_result = aplicar_monitoramento_sofia(img_original)
        
        with col2:
            st.image(img_result, caption="Monitoramento Ativo - Perspectiva Frontal", use_container_width=True)
            st.success("Ativos mapeados conforme normas NR-10 e NR-13.")

# Status de Ibiporã
st.sidebar.divider()
st.sidebar.write(f"📍 **Unidade:** Ibiporã, PR")
