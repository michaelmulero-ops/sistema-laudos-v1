import streamlit as st
import os
import time
from PIL import Image, ImageDraw, ImageFont
from groq import Groq
import json

# --- CONFIGURAÇÕES MICHAEL MULERO INSPEÇÕES ---
st.set_page_config(page_title="Michael Mulero Inspeções Tech V1", layout="wide")

# Título do Sistema
st.title("🛡️ Michael Mulero Inspeções Tech - Monitoramento Ativo V1")

# Diretório de Trabalho
PENDING_DIR = "upload_pendente"
if not os.path.exists(PENDING_DIR):
    os.makedirs(PENDING_DIR)

# --- 🧠 NÍVEL 1 & 3: SOFIA + NANO BANANA (IDENTIFICAÇÃO E CROQUI) ---
def gerar_interface_monitoramento(imagem):
    """Sofia & Nano Banana: Gera o croqui técnico com alvos inteligentes (Realidade Aumentada)"""
    img = imagem.convert("RGB")
    draw = ImageDraw.Draw(img)
    w, h = img.size
    
    # Simulação de dados de RA (isso virá do Nano Banana + Davi)
    data_points = [
        {"type": "Transformador", "pos": (w//3, h//2), "size": (100, 150), "temp": "55°C", "norm": "NR-10"},
        {"type": "Gerador Fotovoltaico", "pos": (2*w//3, h//4), "size": (150, 100), "temp": "42°C", "norm": "NBR-16690"},
        {"type": "Quadro Elétrico", "pos": (w//2, h//1.5), "size": (80, 120), "temp": "38°C", "norm": "NBR-5410"}
    ]
    
    # 1. Base do Croqui (Calçada/Rua) - Padrão Michael Mulero
    draw.line([(0, 3*h//4), (w, 3*h//4)], fill=(150, 150, 150), width=3)
    draw.text((w//2 - 50, 3*h//4 + 10), "FRENTE À RUA", fill=(255, 255, 255))
    
    hotspots = []
    
    for point in data_points:
        x, y = point["pos"]
        sw, sh = point["size"]
        
        # 2. "Mira" Inteligente (Bounding Box)
        # Borda verde estilo HUD técnica
        rect = [x - sw//2, y - sh//2, x + sw//2, y + sh//2]
        draw.rectangle(rect, outline=(0, 255, 0), width=4)
        
        # Etiqueta de identificação
        draw.rectangle([x - sw//2, y - sh//2 - 25, x - sw//2 + 100, y - sh//2], fill=(0, 255, 0))
        draw.text((x - sw//2 + 5, y - sh//2 - 20), point["type"], fill=(0, 0, 0))
        
        # Ponto central para o Hover (RA)
        draw.ellipse([x - 5, y - 5, x + 5, y + 5], fill=(0, 255, 0), outline=(255, 255, 255), width=2)
        
        # Dados do Hotspot (para o JavaScript do Streamlit)
        hotspots.append({
            "rect": rect,
            "data": f"{point['type']}<br>Temp: {point['temp']}<br>Norma: {point['norm']}"
        })
        
    # 3. HUD de Medição Técnica
    draw.text((10, 10), "MICHAEL MULERO - MONITORAMENTO ATIVO", fill=(0, 255, 0))
    
    return img, hotspots

# --- INTERFACE DE INSPEÇÃO ---
st.sidebar.title("Assistentes Sofia, Davi & Nano Banana")
st.sidebar.success("Sofia: Monitoramento de Alvos Ativo")

# Captura de Dados
st.subheader("Entrada de Imagem para Monitoramento")
foto = st.camera_input("Scanner de Risco")
galeria = st.file_uploader("Fotos da Galeria", type=["jpg", "png", "jpeg"])

item_inspecao = foto if foto else galeria

if item_inspecao:
    with st.spinner("Sofia rastreando alvos técnicos..."):
        img_original = Image.open(item_inspecao)
        croqui_final, hotspots = gerar_interface_monitoramento(img_original)
        
        # Salva o progresso
        img_nome = f"monitoramento_{int(time.time())}.jpg"
        croqui_final.save(os.path.join(PENDING_DIR, img_nome))
        
        # Exibe o resultado com a mira técnica
        st.image(croqui_final, caption="Interface de Monitoramento (Prévia de RA)", use_container_width=True)
        
        # 4. Lógica de Interatividade (Simulação do Hover do Mouse)
        # No seu monitor de 27", você verá esses dados ao passar o mouse (em breve)
        st.write("### Pontos de Risco Detectados (Passe o mouse - Em desenvolvimento)")
        
        for hs in hotspots:
            # Criamos uma região interativa básica (Streamlit puro)
            # Para o Hover total (RA), precisaremos de um módulo JS.
            with st.expander(f"📌 {hs['data'].split('<br>')[0]}"):
                st.write(hs['data'].replace('<br>', '\n'))

# Fila de Sincronização
fila = os.listdir(PENDING_DIR)
if fila:
    st.sidebar.info(f"📋 {len(fila)} laudos em processamento local.")
