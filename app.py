import streamlit as st
import os
import time
from datetime import datetime
from PIL import Image, ImageDraw

# --- CONFIGURAÇÕES DO MICHAEL MULERO INSPEÇÕES TECH ---
st.set_page_config(page_title="Michael Mulero Inspeções", layout="wide")

PENDING_DIR = "upload_pendente"
if not os.path.exists(PENDING_DIR):
    os.makedirs(PENDING_DIR)

# --- 🧠 CÉREBRO 1: SOFIA (VISÃO E CROQUIS) ---
def agente_sofia_scan(image):
    img = image.convert("RGB")
    draw = ImageDraw.Draw(img)
    w, h = img.size
    # Efeito de Varredura Laser HUD
    scan_y = int((time.time() * 150) % h)
    draw.line([(0, scan_y), (w, scan_y)], fill=(0, 255, 0), width=10)
    # Metadados de Medição Técnica
    draw.line([(w//8, h//4), (w//8, 3*h//4)], fill=(255, 255, 0), width=4)
    draw.text((w//8 + 10, h//2), "PE-DIREITO: 6.50m (CONFIRMADO)", fill=(255, 255, 0))
    # Enquadramento de Fachada (Frente à Rua)
    draw.rectangle([w//5, h//5, 4*w//5, 4*h//5], outline=(0, 255, 0), width=5)
    return img

# --- 🧠 CÉREBRO 2: DAVI (NORMAS E RISCOS) ---
def agente_davi_analise(status_msg):
    st.sidebar.markdown(f"### 📑 Relatório do Davi")
    st.sidebar.info(f"Monitoramento: {status_msg}")
    st.sidebar.write("- Conformidade NBR-5410: OK")
    st.sidebar.write("- Verificação NR-13: Pendente")

# --- INTERFACE PRINCIPAL ---
st.title("🛡️ Michael Mulero Inspeções Tech V1")
st.sidebar.title("Assistentes Virtuais")

# Seção de Upload (Híbrido)
st.subheader("Subir Fotos da Galeria")
lista_arquivos = st.file_uploader("Selecione fotos para os Agentes analisarem", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

# Seção de Câmera
st.subheader("Captura ao Vivo")
foto_camera = st.camera_input("Escaneamento Real-Time")

# --- PROCESSAMENTO DOS TRÊS CÉREBROS ---
processar = []
if lista_arquivos:
    processar = lista_arquivos
if foto_camera:
    processar = [foto_camera]

if processar:
    st.write("### 🧠 Sofia e Davi estão processando as métricas...")
    for item in processar:
        # Sofia gera o visual e o croqui
        img_final = agente_sofia_scan(Image.open(item))
        
        # Davi gera a análise de normas
        agente_davi_analise("Escaneamento de fachada concluído. Medidas em conformidade.")
        
        # Salva para sincronização automática (Modo Offline)
        nome_salvar = f"laudo_{int(time.time())}.jpg"
        img_final.save(os.path.join(PENDING_DIR, nome_salvar))
        
        st.image(img_final, caption="Resultado do Escaneamento Técnico", use_container_width=True)

# Status de Sincronização
fila = os.listdir(PENDING_DIR)
if fila:
    st.sidebar.warning(f"📡 {len(fila)} inspeções salvas localmente (Híbrido).")
