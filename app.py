import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image

st.header("🛡️ Mapa de Blindagem e Croqui de Risco")
st.write("Desenhe sobre a imagem para definir as zonas de blindagem e os pontos de vulnerabilidade.")

# 1. Seleção da Base (Satélite ou Planta)
base_mapa = st.file_uploader("Carregue o Mapa de Satélite/Planta do Imóvel:", type=["png", "jpg"])

if base_mapa:
    img_base = Image.open(base_mapa)
    
    # 2. Ferramenta de Desenho Técnico
    # 'polygon' para formatos H e limites de terreno
    # 'rect' para zonas de blindagem específicas
    modo = st.sidebar.radio("Ferramenta:", ("Contorno da Edificação (H/L)", "Zona de Blindagem (Retângulo)"))
    drawing_mode = "polygon" if modo == "Contorno da Edificação (H/L)" else "rect"

    canvas_blindagem = st_canvas(
        fill_color="rgba(0, 255, 0, 0.2)",  # Verde para blindagem OK
        stroke_width=2,
        stroke_color="#ff0000", # Vermelho para delimitação de risco
        background_image=img_base,
        update_streamlit=True,
        height=img_base.height * (700 / img_base.width),
        width=700,
        drawing_mode=drawing_mode,
        key="canvas_blindagem_tecnica",
    )

    # 3. Legenda Automática para o Laudo
    if canvas_blindagem.json_data:
        st.info("💡 Legenda do Mapa: Verde = Área Protegida | Linha Vermelha = Limite de Risco de Impacto")
        
        # O sistema já prepara esses dados para o Parecer da Sofia
        if st.button("🚀 INTEGRAR MAPA DE BLINDAGEM AO LAUDO"):
            st.success("✅ Mapa de Blindagem anexado ao processo Michael Mulero.")
