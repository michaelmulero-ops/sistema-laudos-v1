import streamlit as st
import os
import time
from datetime import datetime
from PIL import Image, ImageDraw

# --- CONFIGURAÇÕES DO SISTEMA ---
st.set_page_config(page_title="Michael Mulero Inspeções", layout="wide")

PENDING_DIR = "upload_pendente"
if not os.path.exists(PENDING_DIR):
    os.makedirs(PENDING_DIR)

def apply_scanner_hud(image):
    """Cria o efeito visual de scanner (estilo HUD)"""
    img = image.convert("RGB")
    draw = ImageDraw.Draw(img)
    w, h = img.size
    scan_y = int((time.time() * 150) % h)
    draw.line([(0, scan_y), (w, scan_y)], fill=(0, 255, 0), width=10)
    draw.rectangle([w//5, h//5, 4*w//5, 4*h//5], outline=(0, 255, 0), width=5)
    return img

# --- INTERFACE ---
st.title("Michael Mulero Inspeções Tech V1 🛡️")

# 1. Campo para subir fotos da Galeria (O que você pediu agora)
st.subheader("Subir Fotos da Galeria")
arquivos_subidos = st.file_uploader(
    "Selecione as fotos da inspeção (Híbrido)", 
    type=["jpg", "png", "jpeg"], 
    accept_multiple_files=True
)

if arquivos_subidos:
    for arquivo in arquivos_subidos:
        img_galeria = Image.open(arquivo)
        img_com_scan = apply_scanner_hud(img_galeria)
        
        # Salva na fila automática para modo offline
        nome_arq = f"galeria_{int(time.time())}_{arquivo.name}"
        img_com_scan.save(os.path.join(PENDING_DIR, nome_arq))
        st.image(img_com_scan, caption=f"Escaneando: {arquivo.name}", width=300)

st.divider()

# 2. Campo para Foto ao Vivo
st.subheader("Captura com Câmera")
foto = st.camera_input("Escaneamento de Risco em Tempo Real")

if foto:
    img_camera = Image.open(foto)
    img_scan_cam = apply_scanner_hud(img_camera)
    nome_cam = f"camera_{int(time.time())}.jpg"
    img_scan_cam.save(os.path.join(PENDING_DIR, nome_cam))
    st.image(img_scan_cam, caption="Análise de Campo Ativa")
