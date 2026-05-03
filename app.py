import streamlit as st
from PIL import Image, ImageOps, ImageDraw

# Configuração da página para um visual profissional
st.set_page_config(page_title="Michael Mulero Inspeções Tech V1", layout="wide")

def aplicar_zoom_tecnico(img_input, x, y, texto="ANOMALIA DETECTADA"):
    """
    Gera o destaque visual de auditoria forense nas fotos de vistoria.
    """
    width, height = img_input.size
    
    # Define a área da 'lupa' (400x400 pixels)
    caixa = (max(0, x-200), max(0, y-200), min(width, x+200), min(height, y+200))
    zoom = img_input.crop(caixa).resize((600, 600), Image.LANCZOS)
    
    # Moldura de impacto estilo 'Verdade Sem Filtro'
    zoom = ImageOps.expand(zoom, border=15, fill='red')
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📸 Visão Geral")
        st.image(img_input, use_column_width=True)
    with col2:
        st.subheader(f"🔍 {texto}")
        st.image(zoom, use_column_width=True)

# Interface Principal
st.title("🛡️ Sistema de Laudos V1 - Michael Mulero")
st.write("Geointeligência aplicada a inspeções de risco e segurança.")

# Exemplo de fluxo para vistorias em Londrina, Ibiporã e região
arquivo_foto = st.file_uploader("Carregue a foto da vistoria", type=['jpg', 'png', 'jpeg'])

if arquivo_foto:
    imagem = Image.open(arquivo_foto)
    st.success("Foto carregada com sucesso!")
    
    # Slider para simular a marcação de coordenadas na imagem
    col_x = st.slider("Posição Horizontal do Risco (X)", 0, imagem.width, imagem.width // 2)
    col_y = st.slider("Posição Vertical do Risco (Y)", 0, imagem.height, imagem.height // 2)
    
    if st.button("Gerar Zoom de Evidência"):
        aplicar_zoom_tecnico(imagem, col_x, col_y)
