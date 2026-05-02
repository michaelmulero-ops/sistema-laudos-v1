import streamlit as st
import os
import time
from PIL import Image, ImageDraw

# --- CONFIGURAÇÕES MICHAEL MULERO INSPEÇÕES ---
st.set_page_config(page_title="Michael Mulero Inspeções Tech", layout="wide")

# Título do Sistema
st.title("🛡️ Michael Mulero Inspeções Tech V1")

# Diretório de Trabalho
PENDING_DIR = "upload_pendente"
if not os.path.exists(PENDING_DIR):
    os.makedirs(PENDING_DIR)

# --- 🧠 NÍVEL 1: CROQUI DE FRENTE PARA A RUA ---
def gerar_croqui_nivel_1(imagem):
    img = imagem.convert("RGB")
    draw = ImageDraw.Draw(img)
    w, h = img.size
    
    # 1. Base do Croqui (Calçada/Rua)
    draw.line([(0, 3*h//4), (w, 3*h//4)], fill=(200, 200, 200), width=5)
    
    # 2. Fachada Principal (Perspectiva Frontal)
    draw.rectangle([w//4, h//3, 3*w//4, 3*h//4], outline=(0, 255, 0), width=8)
    
    # 3. Identificação Técnica
    draw.text((w//4, h//3 - 40), "NÍVEL 1: CROQUI DE LOCALIZAÇÃO", fill=(0, 255, 0))
    draw.text((w//2 - 50, 3*h//4 + 10), "FRENTE À RUA", fill=(255, 255, 255))
    
    return img

# --- INTERFACE DE INSPEÇÃO ---
st.sidebar.title("Assistentes Sofia & Davi")
st.sidebar.success("Sofia: Pronta para Croqui Nível 1")

# Captura de Dados
st.subheader("Entrada de Imagem para Croqui")
foto = st.camera_input("Escaneamento de Fachada")
galeria = st.file_uploader("Fotos da Galeria", type=["jpg", "png", "jpeg"])

item_inspecao = foto if foto else galeria

if item_inspecao:
    with st.spinner("Sofia gerando croqui nível 1..."):
        img_original = Image.open(item_inspecao)
        croqui_final = gerar_croqui_nivel_1(img_original)
        
        # Salva o progresso
        img_nome = f"nivel1_{int(time.time())}.jpg"
        croqui_final.save(os.path.join(PENDING_DIR, img_nome))
        
        # Exibe o resultado
        st.image(croqui_final, caption="Croqui Nível 1: Localização Frontal", use_container_width=True)

# Fila de Sincronização
fila = os.listdir(PENDING_DIR)
if fila:
    st.sidebar.info(f"📋 {len(fila)} laudos em processamento.")
