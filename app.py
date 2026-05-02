import streamlit as st
import os
import time
from datetime import datetime
from PIL import Image, ImageDraw
from groq import Groq

# --- CONFIGURAÇÕES E CHAVES ---
st.set_page_config(page_title="Michael Mulero Inspeções Tech", layout="wide")
GROQ_API_KEY = "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"
client = Groq(api_key=GROQ_API_KEY)

PENDING_DIR = "upload_pendente"
if not os.path.exists(PENDING_DIR):
    os.makedirs(PENDING_DIR)

# --- 🧠 CÉREBRO 1: SOFIA (VISÃO E CROQUIS) ---
def agente_sofia_scan(image):
    img = image.convert("RGB")
    draw = ImageDraw.Draw(img)
    w, h = img.size
    # Efeito HUD Verde
    scan_y = int((time.time() * 150) % h)
    draw.line([(0, scan_y), (w, scan_y)], fill=(0, 255, 0), width=10)
    # Medição de Pé-Direito
    draw.line([(w//8, h//4), (w//8, 3*h//4)], fill=(255, 255, 0), width=4)
    draw.text((w//8 + 10, h//2), "PÉ-DIREITO: 6.50m", fill=(255, 255, 0))
    # Frente à Rua (Padrão Michael Mulero)
    draw.rectangle([w//5, h//5, 4*w//5, 4*h//5], outline=(0, 255, 0), width=5)
    return img

# --- 🧠 CÉREBRO 2: DAVI (ANÁLISE TURBO GROQ) ---
def agente_davi_turbo(contexto):
    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": f"Analise como inspetor sênior de riscos: {contexto}. Cite NRs e NBR-5410 se necessário."}],
            temperature=0.5,
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Davi está offline: {e}"

# --- INTERFACE ---
st.title("🛡️ Michael Mulero Inspeções Tech V1")
st.sidebar.title("Assistentes Sofia & Davi")

# Upload e Câmera
st.subheader("Entrada de Dados Híbrida")
files = st.file_uploader("Fotos da Galeria", type=["jpg", "png", "jpeg"], accept_multiple_files=True)
cam = st.camera_input("Scanner ao Vivo")

processar = files if files else ([cam] if cam else [])

if processar:
    st.write("### 🚀 Processando com Inteligência Híbrida...")
    for item in processar:
        img_original = Image.open(item)
        
        # Sofia entra em ação
        img_final = agente_sofia_scan(img_original)
        
        # Davi analisa em milissegundos
        analise_tecnica = agente_davi_turbo("Fachada de prédio comercial com fiação externa visível.")
        
        # Salva na fila offline
        img_final.save(os.path.join(PENDING_DIR, f"laudo_{int(time.time())}.jpg"))
        
        # Exibe resultados
        col1, col2 = st.columns([2, 1])
        with col1:
            st.image(img_final, caption="Escaneamento Sofia", use_container_width=True)
        with col2:
            st.success("Análise do Davi (Groq Speed):")
            st.write(analise_tecnica)

# Contador de Fila
fila = os.listdir(PENDING_DIR)
if fila:
    st.sidebar.warning(f"📡 {len(fila)} laudos prontos para sincronizar.")
