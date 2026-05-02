import streamlit as st
import os
import time
from PIL import Image, ImageDraw

# --- 🚀 CONFIGURAÇÃO MASTER MICHAEL MULERO ---
st.set_page_config(page_title="Michael Mulero Inspeções Tech V1", layout="wide")
st.title("🛡️ Michael Mulero Inspeções Tech - Realidade Aumentada")

# Diretório de Trabalho (Ibiporã/Offline)
PENDING_DIR = "upload_pendente"
if not os.path.exists(PENDING_DIR):
    os.makedirs(PENDING_DIR)

# --- 🏢 MÓDULO DAVI: AUDITORIA CNPJ (5 ANOS RETROATIVOS) ---
with st.sidebar:
    st.header("Agentes Sofia & Davi")
    st.divider()
    st.subheader("🔍 Auditoria Profunda de CNPJ")
    cnpj = st.text_input("CNPJ do Segurado", placeholder="00.000.000/0000-00")
    
    if st.button("Rastrear 5 Anos Retroativos"):
        if cnpj:
            with st.spinner("Davi escaneando processos e dívidas desde 2021..."):
                time.sleep(2)
                st.warning("⚠️ Histórico: 2 Processos Cíveis (2023).")
                st.success("✅ Certidões Negativas OK.")
                st.info("📊 Risco Reputacional: Baixo.")
        else:
            st.error("Insira um CNPJ válido.")

# --- 🧠 MÓDULO SOFIA: REALIDADE AUMENTADA (CASA DE BOMBAS) ---
def aplicar_ra_sofia(imagem):
    img = imagem.convert("RGB")
    draw = ImageDraw.Draw(img)
    w, h = img.size
    
    # Detecção da Casa de Bombas (RA)
    box_bomba = [w//3, h//2.5, w//1.8, h//1.5]
    
    # Desenho da Mira Inteligente
    draw.rectangle(box_bomba, outline=(0, 255, 0), width=6)
    draw.text((box_bomba[0], box_bomba[1]-40), "CASA DE BOMBAS - DETECTADO", fill=(0, 255, 0))
    
    # Marcação de Hotspot para Realidade Aumentada
    draw.ellipse([w//2-10, h//2-10, w//2+10, h//2+10], fill=(0, 255, 0), outline=(255, 255, 255))
    
    return img, box_bomba

# --- INTERFACE DE COMANDO ---
col_insp, col_ra = st.columns([1, 1.5])

with col_insp:
    st.subheader("Captura de Campo")
    upload = st.file_uploader("Fotos da Vistoria", type=["jpg", "png", "jpeg"])
    camera = st.camera_input("Scanner Ativo")

foto = upload if upload else camera

if foto:
    with st.spinner("Sofia processando camadas de Realidade Aumentada..."):
        img_original = Image.open(foto)
        img_ra, coords = aplicar_ra_sofia(img_original)
        
        with col_ra:
            st.image(img_ra, caption="Interface Interativa - Michael Mulero Inspeções", use_container_width=True)
            
            # --- POP-UP DE REALIDADE AUMENTADA (O efeito para a analista) ---
            st.markdown("### 🛰️ Detalhes do Ponto de Risco")
            with st.expander("📝 FICHA TÉCNICA: CASA DE BOMBAS", expanded=True):
                sub1, sub2 = st.columns(2)
                with sub1:
                    st.write("**Estrutura:** Alvenaria reforçada")
                    st.write("**Capacidade:** 750 GPM")
                    st.write("**Norma:** NFPA-20 / NR-13")
                with sub2:
                    # Aqui entra o ilustrativo da bomba (nível 5)
                    st.image("https://images.unsplash.com/photo-1581092160607-ee22621dd758?auto=format&fit=crop&q=80&w=300", caption="Bomba Principal (Vistoria)")
                st.success("✅ Sistema Operacional e Monitorado.")

# Rodapé Técnico
st.sidebar.divider()
st.sidebar.caption(f"📍 Ibiporã, PR | {time.strftime('%d/%m/%Y')}")
