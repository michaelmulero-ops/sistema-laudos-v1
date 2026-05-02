import streamlit as st
import os
import time
from datetime import datetime
from PIL import Image, ImageDraw

# --- CONFIGURAÇÕES DO MICHAEL MULERO INSPEÇÕES ---
st.set_page_config(page_title="Michael Mulero Inspeções Tech", layout="wide")

# Título Profissional
st.title("🛡️ Michael Mulero Inspeções Tech V1")

# Criar pasta de uploads se não existir
PENDING_DIR = "upload_pendente"
if not os.path.exists(PENDING_DIR):
    os.makedirs(PENDING_DIR)

# --- FUNÇÃO DE ESCANEAMENTO (SOFIA) ---
def aplicar_scanner_sofia(imagem):
    img = imagem.convert("RGB")
    draw = ImageDraw.Draw(img)
    w, h = img.size
    # Efeito visual de scanner HUD
    scan_y = int((time.time() * 150) % h)
    draw.line([(0, scan_y), (w, scan_y)], fill=(0, 255, 0), width=10)
    # Medição de Fachada (Frente à Rua)
    draw.rectangle([w//5, h//5, 4*w//5, 4*h//5], outline=(0, 255, 0), width=5)
    draw.text((w//5, h//5 - 30), "MICHAEL MULERO - SCAN ATIVO", fill=(0, 255, 0))
    return img

# --- INTERFACE ---
st.sidebar.title("Agentes de IA")
st.sidebar.info("Aguardando ativação total dos cérebros Sofia & Davi.")

# Subir Fotos
st.subheader("Subir Fotos da Galeria")
arquivos = st.file_uploader("Selecione as fotos da inspeção", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

# Câmera
st.subheader("Captura ao Vivo")
foto_cam = st.camera_input("Scanner de Risco")

# Processamento
processar = arquivos if arquivos else ([foto_cam] if foto_cam else [])

if processar:
    for item in processar:
        img_original = Image.open(item)
        img_scan = aplicar_scanner_sofia(img_original)
        
        # Salva para o modo híbrido
        nome_arq = f"inspecao_{int(time.time())}.jpg"
        img_scan.save(os.path.join(PENDING_DIR, nome_arq))
        
        st.image(img_scan, caption="Escaneamento de Fachada e Medidas", use_container_width=True)

# Status de Sincronização
fila = os.listdir(PENDING_DIR)
if fila:
    st.sidebar.warning(f"📡 {len(fila)} laudos salvos localmente.")
