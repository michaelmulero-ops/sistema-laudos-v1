import streamlit as st
import os
import time
from PIL import Image, ImageDraw

# --- CONFIGURAÇÃO MICHAEL MULERO INSPEÇÕES ---
st.set_page_config(page_title="Michael Mulero Inspeções Tech V1", layout="wide")
st.title("🛡️ Inventário de Ativos - Michael Mulero (Padrão Lens)")

# Pastas para Funcionamento Offline
PENDING_DIR = "upload_pendente"
PROCESSED_DIR = "inventario_concluido"
for folder in [PENDING_DIR, PROCESSED_DIR]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# --- 🧠 MOTOR DE VISÃO (SIMULAÇÃO LENS/NANO BANANA) ---
def realizar_inventario_lens(imagem):
    img = imagem.convert("RGB")
    draw = ImageDraw.Draw(img)
    w, h = img.size
    
    # Simulação de Identificação de Ativo Industrial
    # O sistema detecta o equipamento e extrai dados para o inventário
    ativo_detectado = {
        "tipo": "Gerador Fotovoltaico",
        "marca": "WEG",
        "capacidade": "500kWp",
        "norma": "NBR-16690",
        "box": [w//4, h//4, 3*w//4, 2*h//3]
    }
    
    # Desenho da Mira Estilo Google Lens
    draw.rectangle(ativo_detectado["box"], outline=(0, 255, 0), width=8)
    draw.text((w//4, h//4 - 30), f"LENS: {ativo_detectado['tipo']} IDENTIFICADO", fill=(0, 255, 0))
    
    return img, ativo_detectado

# --- INTERFACE DE CAMPO ---
with st.sidebar:
    st.header("Status de Sincronização")
    fila_off = os.listdir(PENDING_DIR)
    st.info(f"📁 Fotos aguardando análise: {len(fila_off)}")
    if st.button("Sincronizar e Gerar Inventário") and fila_off:
        st.success("Davi processando dados técnicos e NRs...")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Captura Lens (Offline/Online)")
    foto = st.camera_input("Bater Foto do Equipamento")
    
if foto:
    with st.spinner("Analisando especificações do ativo..."):
        img_original = Image.open(foto)
        img_inventario, dados = realizar_inventario_lens(img_original)
        
        # Salva para garantir que não se perca (Lógica Offline)
        save_path = os.path.join(PENDING_DIR, f"ativo_{int(time.time())}.jpg")
        img_inventario.save(save_path)
        
        with col2:
            st.image(img_inventario, caption="Ativo Identificado via Lens", use_container_width=True)
            st.markdown("### 📋 Ficha de Inventário")
            st.write(f"**Equipamento:** {dados['tipo']}")
            st.write(f"**Fabricante:** {dados['marca']}")
            st.write(f"**Capacidade Técnica:** {dados['capacidade']}")
            st.success(f"Análise de Conformidade: {dados['norma']} (OK)")
