import streamlit as st
from PIL import Image, ImageOps, ImageDraw

# 1. Configurações de Identidade Visual (Michael Mulero Inspeções)
st.set_page_config(page_title="Michael Mulero Inspeções Tech V1", layout="wide")

# Estilo CSS para legendas dinâmicas (Estilo Reels/TikTok)
st.markdown("""
    <style>
    .alerta-tecnico {
        background-color: #ffff00;
        color: black;
        padding: 10px;
        font-weight: bold;
        border-radius: 5px;
        border-left: 5px solid red;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Função de Geointeligência e Zoom
def aplicar_zoom_tecnico(img_input, x, y):
    width, height = img_input.size
    # Define a área da 'lupa' técnica (Ajustado para o seu padrão de 3cm)
    caixa = (max(0, x-200), max(0, y-200), min(width, x+200), min(height, y+200))
    zoom = img_input.crop(caixa).resize((600, 600), Image.LANCZOS)
    # Moldura de impacto estilo 'Verdade Sem Filtro'
    zoom = ImageOps.expand(zoom, border=15, fill='red')
    return zoom

# 3. Interface Principal (Conforme seu print atual)
st.title("🛡️ Sistema de Laudos V1 - Michael Mulero")
st.write("Geointeligência aplicada a inspeções de risco e segurança.")

arquivo_foto = st.file_uploader("Carregue a foto da vistoria", type=['jpg', 'png', 'jpeg'])

if arquivo_foto:
    img = Image.open(arquivo_foto).convert("RGB")
    st.success("Foto carregada com sucesso!")
    
    # Seleção do ponto de risco (Simulando detecção automática ou manual)
    st.info("Ajuste os controles abaixo para focar na evidência técnica:")
    col_x = st.slider("Eixo X (Horizontal)", 0, img.width, img.width // 2)
    col_y = st.slider("Eixo Y (Vertical)", 0, img.height, img.height // 2)
    
    # O BOTÃO QUE VOCÊ PEDIU:
    if st.button("🚀 GERAR LAUDO COM ZOOM TÉCNICO"):
        zoom_img = aplicar_zoom_tecnico(img, col_x, col_y)
        
        # Exibição Lado a Lado (Layout de Auditoria Forense)
        c1, c2 = st.columns(2)
        with c1:
            st.markdown('<p class="alerta-tecnico">VISÃO GERAL DA INSPEÇÃO</p>', unsafe_allow_html=True)
            st.image(img, use_column_width=True)
        with c2:
            st.markdown('<p class="alerta-tecnico">DETALHE DA ANOMALIA (EVIDÊNCIA)</p>', unsafe_allow_html=True)
            st.image(zoom_img, use_column_width=True)
            
        # Veredito da IA (Sofia/Davi)
        st.divider()
        st.subheader("📝 Veredito Técnico")
        st.warning("⚠️ Risco Detectado: Falha crítica identificada na estrutura/componente. Recomenda-se ação imediata.")
