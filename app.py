import streamlit as st
from PIL import Image, ImageOps, ImageDraw

# 1. Configurações de Identidade Visual (Michael Mulero Inspeções)
st.set_page_config(page_title="Michael Mulero Inspeções Tech V1", layout="wide")

# Estilo CSS para legendas dinâmicas
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
    .narra-sofia {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #007bff;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Função de Zoom Técnico
def aplicar_zoom_tecnico(img_input, x, y):
    width, height = img_input.size
    caixa = (max(0, x-200), max(0, y-200), min(width, x+200), min(height, y+200))
    zoom = img_input.crop(caixa).resize((600, 600), Image.LANCZOS)
    zoom = ImageOps.expand(zoom, border=15, fill='red')
    return zoom

# 3. Interface Principal
st.title("🛡️ Sistema de Laudos V1 - Michael Mulero")
st.write("Geointeligência aplicada a inspeções de risco e segurança.")

arquivo_foto = st.file_uploader("Carregue a foto da vistoria", type=['jpg', 'png', 'jpeg'])

if arquivo_foto:
    img = Image.open(arquivo_foto).convert("RGB")
    st.success("Foto carregada com sucesso!")
    
    # Controles de Foco
    col_x = st.slider("Eixo X (Horizontal)", 0, img.width, img.width // 2)
    col_y = st.slider("Eixo Y (Vertical)", 0, img.height, img.height // 2)
    
    # NOVO: CAMPO DE NARRAÇÃO DA SOFIA
    st.subheader("🎙️ Parecer da Sofia (Agente IA)")
    texto_narracao = st.text_area(
        "O que a Sofia deve dizer sobre esta evidência?",
        value="Identificada anomalia crítica na estrutura. O risco de colapso residual é elevado devido à exposição de armadura.",
        help="Este texto será usado para gerar a narração do vídeo técnico."
    )
    
    # BOTÃO DE EXECUÇÃO
    if st.button("🚀 GERAR LAUDO E ROTEIRO TÉCNICO"):
        zoom_img = aplicar_zoom_tecnico(img, col_x, col_y)
        
        # Layout Lado a Lado
        c1, c2 = st.columns(2)
        with c1:
            st.markdown('<p class="alerta-tecnico">VISÃO GERAL</p>', unsafe_allow_html=True)
            st.image(img, use_column_width=True)
        with c2:
            st.markdown('<p class="alerta-tecnico">EVIDÊNCIA AMPLIADA</p>', unsafe_allow_html=True)
            st.image(zoom_img, use_column_width=True)
            
        # Exibição do Roteiro Processado
        st.divider()
        st.markdown(f"""
            <div class="narra-sofia">
                <strong>🔊 Roteiro de Narração Gerado:</strong><br>
                "Atenção analista. No detalhe à direita, Michael Mulero destaca: {texto_narracao}"
            </div>
        """, unsafe_allow_html=True)
        
        st.info("💡 Este roteiro já está formatado para ser enviado ao gerador de voz da Sofia.")
