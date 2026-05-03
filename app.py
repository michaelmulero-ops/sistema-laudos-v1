import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image

# 1. Título do Módulo de Croquis
st.subheader("📐 Módulo de Croquis e Delimitação de Área")
st.write("Desenhe o contorno da edificação (formato H, L, etc.) sobre a imagem de satélite ou planta baixa.")

# 2. Configuração do Canvas (Prancheta Digital)
bg_image = st.file_uploader("Carregue a imagem de base para o Croqui (Satélite/Planta):", type=["png", "jpg"])

if bg_image:
    img_base = Image.open(bg_image)
    
    # Criando a prancheta de desenho sobre a imagem
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",  # Cor de preenchimento (laranja transparente)
        stroke_width=3,
        stroke_color="#ff0000", # Linha vermelha para destaque técnico
        background_image=img_base,
        update_streamlit=True,
        height=img_base.height * (600 / img_base.width), # Mantém a proporção
        width=600,
        drawing_mode="polygon", # Permite criar formas complexas como o "H"
        key="canvas_croqui",
    )

    # 3. Processamento do Desenho Técnico
    if canvas_result.json_data is not None:
        objects = canvas_result.json_data["objects"]
        if objects:
            st.success(f"✅ Croqui gerado com {len(objects)} polígonos de área.")
            st.info("💡 Este desenho será exportado para o PDF final como 'Anexo de Delimitação de Risco'.")
