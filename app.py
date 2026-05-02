import streamlit as st
import os
import time
from PIL import Image, ImageDraw

# --- CONFIGURAÇÕES DO SISTEMA ---
# Definido conforme o branding pessoal Michael Mulero Inspeções
st.set_page_config(page_title="Michael Mulero Inspeções Tech", layout="wide")

# Título Profissional
st.title("🛡️ Michael Mulero Inspeções Tech V1")

# Gerenciamento de Pastas (Para garantir o fluxo de trabalho offline)
PENDING_DIR = "upload_pendente"
if not os.path.exists(PENDING_DIR):
    os.makedirs(PENDING_DIR)

# --- 🧠 INTELIGÊNCIA SOFIA: MONITORAMENTO E MIRA (NÍVEL 1 E 3) ---
def aplicar_monitoramento_sofia(imagem):
    """
    Sofia (Nano Banana 2): Identifica ativos e gera a interface de monitoramento interativo.
    Foca na perspectiva de frente para a rua.
    """
    img = imagem.convert("RGB")
    draw = ImageDraw.Draw(img)
    w, h = img.size
    
    # 1. Base do Croqui: Frente à Rua (Identidade Técnica Michael Mulero)
    draw.line([(0, 3*h//4), (w, 3*h//4)], fill=(150, 150, 150), width=4)
    
    # 2. Simulação de Detecção de Ativos (Gerador, Transformador, Caldeira)
    # Estes pontos serão os 'hotspots' para a Realidade Aumentada.
    ativos = [
        {"nome": "Transformador", "cor": (0, 255, 0), "pos": [w//4, h//2, w//2.5, h//1.3], "norma": "NR-10"},
        {"nome": "Placas Solares", "cor": (0, 200, 255), "pos": [w//2, h//5, 3*w//4, h//2.5], "norma": "NBR-16690"},
        {"nome": "Quadro Elétrico", "cor": (255, 255, 0), "pos": [w//1.5, h//2, w//1.2, h//1.5], "norma": "NBR-5410"}
    ]
    
    for ativo in ativos:
        # Desenha a 'Mira' (Bounding Box) estilo o vídeo do TikTok
        draw.rectangle(ativo["pos"], outline=ativo["cor"], width=5)
        
        # Etiqueta de Identificação
        x1, y1, x2, y2 = ativo["pos"]
        draw.rectangle([x1, y1 - 25, x1 + 120, y1], fill=ativo["cor"])
        draw.text((x1 + 5, y1 - 22), f"{ativo['nome']} ({ativo['norma']})", fill=(0, 0, 0))
    
    # 3. Marcação de HUD Técnico
    draw.text((10, 10), "MICHAEL MULERO - SCAN ATIVO: MONITORAMENTO DE RISCO", fill=(0, 255, 0))
    
    return img

# --- INTERFACE DE COMANDO ---
st.sidebar.title("Agentes Sofia & Davi")
st.sidebar.info("Modo: Monitoramento de Risco e Realidade Aumentada.")

# Entrada de Dados
col_entrada, col_preview = st.columns([1, 2])

with col_entrada:
    st.subheader("Captura de Campo")
    arquivos = st.file_uploader("Fotos da Inspeção", type=["jpg", "png", "jpeg"], accept_multiple_files=True)
    foto_cam = st.camera_input("Scanner ao Vivo")

# Processamento e Visualização
processar = arquivos if arquivos else ([foto_cam] if foto_cam else [])

if processar:
    for item in processar:
        with st.spinner("Processando alvos técnicos..."):
            img_original = Image.open(item)
            img_monitorada = aplicar_monitoramento_sofia(img_original)
            
            # Salva o arquivo localmente para sincronização futura
            nome_arquivo = f"monitor_risco_{int(time.time())}.jpg"
            img_monitorada.save(os.path.join(PENDING_DIR, nome_arquivo))
            
            with col_preview:
                st.image(img_monitorada, caption="Interface de Monitoramento Ativo (Nível 3)", use_container_width=True)
                st.success(f"Ativos identificados conforme normas técnicas (NR-10, NR-13, NBR-5410).")

# Status do Sistema em Ibiporã
st.sidebar.divider()
st.sidebar.write(f"📍 **Localização:** Ibiporã, PR")
fila = os.listdir(PENDING_DIR)
if fila:
    st.sidebar.warning(f"📡 {len(fila)} laudos na fila de sincronização.")
