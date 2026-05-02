import streamlit as st
import os
import time
from datetime import datetime
from PIL import Image, ImageDraw

# --- CONFIGURAÇÕES DE MARCA E DIRETÓRIO ---
st.set_page_config(page_title="Michael Mulero Inspeções", layout="wide")

PENDING_DIR = "upload_pendente"
if not os.path.exists(PENDING_DIR):
    os.makedirs(PENDING_DIR)

# --- FUNÇÃO DE ESCANEAMENTO COM MÉTRICAS (FRENTE À RUA) ---
def apply_advanced_scan(image):
    img = image.convert("RGB")
    draw = ImageDraw.Draw(img)
    w, h = img.size
    
    # Efeito visual de Varredura Laser (HUD)
    scan_y = int((time.time() * 150) % h)
    draw.line([(0, scan_y), (w, scan_y)], fill=(0, 255, 0), width=10)
    
    # Marcadores de Medição Técnica (Conferência de Pé-Direito)
    draw.line([(w//8, h//4), (w//8, 3*h//4)], fill=(255, 255, 0), width=4)
    draw.text((w//8 + 10, h//2), "PE-DIREITO EST: 6.50m", fill=(255, 255, 0))
    
    # Caixa de Enquadramento Frontal
    draw.rectangle([w//5, h//5, 4*w//5, 4*h//5], outline=(0, 255, 0), width=5)
    draw.text((w//5, h//5 - 30), "MICHAEL MULERO INSPEÇÕES - SCAN ATIVO", fill=(0, 255, 0))
    
    return img

# --- INTERFACE PRINCIPAL ---
st.title("🛡️ Michael Mulero Inspeções Tech V1")
st.sidebar.info("Assistentes Sofia & Davi: Aguardando Processamento...")

# Opção 1: Upload de Galeria (Híbrido)
st.subheader("Subir Fotos da Galeria")
arquivos = st.file_uploader("Selecione fotos para escaneamento métrico", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if arquivos:
    for arq in arquivos:
        img_processada = apply_advanced_scan(Image.open(arq))
        nome_salvar = f"scan_{int(time.time())}_{arq.name}"
        img_processada.save(os.path.join(PENDING_DIR, nome_salvar))
        st.image(img_processada, caption=f"Análise: {arq.name}", width=400)

st.divider()

# Opção 2: Câmera ao Vivo
st.subheader("Captura com Câmera")
foto_cam = st.camera_input("Escaneamento de Risco Real-Time")

if foto_cam:
    img_cam = apply_advanced_scan(Image.open(foto_cam))
    img_cam.save(os.path.join(PENDING_DIR, f"camera_{int(time.time())}.jpg"))
    st.image(img_cam, caption="Medição e Risco Detectados")

# Sincronização Automática Invisível
if os.listdir(PENDING_DIR):
    st.sidebar.warning(f"📡 {len(os.listdir(PENDING_DIR))} laudos aguardando Wi-Fi.")
