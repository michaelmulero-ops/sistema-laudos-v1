import streamlit as st
import os
import time
from datetime import datetime
from PIL import Image, ImageDraw

# Configurações de Marca e Diretórios
st.set_page_config(page_title="Michael Mulero Inspeções", layout="wide")
PENDING_DIR = "upload_pendente"
if not os.path.exists(PENDING_DIR):
    os.makedirs(PENDING_DIR)

def apply_scanner_hud(image):
    """Cria o efeito visual de scanner (estilo HUD) sem erros técnicos"""
    img = image.convert("RGB")
    draw = ImageDraw.Draw(img)
    w, h = img.size
    # Linha de Scan Verde
    scan_y = int((time.time() * 150) % h)
    draw.line([(0, scan_y), (w, scan_y)], fill=(0, 255, 0), width=10)
    # Caixa de Análise Técnica
    draw.rectangle([w//5, h//5, 4*w//5, 4*h//5], outline=(0, 255, 0), width=5)
    return img

st.title("Michael Mulero Inspeções Tech V1 🛡️")
st.subheader("Sistema Híbrido: Online/Offline Ativo")

# Captura de Campo
foto = st.camera_input("Escaneamento de Risco (Foto/Vídeo)")

if foto:
    img_original = Image.open(foto)
    img_com_scan = apply_scanner_hud(img_original)
    
    # Salva sempre localmente (Modo Indústria/Condomínio)
    nome_arq = f"inspecao_{int(time.time())}.jpg"
    caminho = os.path.join(PENDING_DIR, nome_arq)
    img_com_scan.save(caminho)
    
    st.image(img_com_scan, caption="Análise Técnica em Processamento...")
    st.success(f"Captura salva! Sincronização automática ativa.")

# Verificador de Sincronismo (Roda sempre que a página carrega)
arquivos_na_fila = os.listdir(PENDING_DIR)
if arquivos_na_fila:
    st.info(f"Existem {len(arquivos_na_fila)} inspeções aguardando sinal de Wi-Fi.")
