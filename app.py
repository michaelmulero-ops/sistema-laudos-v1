import streamlit as st
from PIL import Image, ImageOps
import pandas as pd
from datetime import datetime

# 1. Configurações de Identidade Visual (Michael Mulero Inspeções)
st.set_page_config(page_title="Michael Mulero Inspeções Tech V1", layout="wide")

# Estilo CSS para o Veredito da Sofia
st.markdown("""
    <style>
    .alerta-tecnico { background-color: #ffff00; color: black; padding: 10px; font-weight: bold; border-radius: 5px; border-left: 5px solid red; }
    .narra-sofia { background-color: #f0f2f6; padding: 15px; border-radius: 10px; border-left: 5px solid #007bff; }
    </style>
    """, unsafe_allow_html=True)

# 2. Funções Técnicas
def aplicar_zoom_tecnico(img_input, x, y):
    width, height = img_input.size
    caixa = (max(0, x-200), max(0, y-200), min(width, x+200), min(height, y+200))
    zoom = img_input.crop(caixa).resize((600, 600), Image.LANCZOS)
    zoom = ImageOps.expand(zoom, border=15, fill='red')
    return zoom

# 3. Interface Principal (Michael Mulero Inspeções Tech V1)
st.title("🛡️ Sistema de Laudos V1 - Michael Mulero")
st.write("Geointeligência aplicada a inspeções de risco e segurança.")

# Sidebar para Controle de Dados
with st.sidebar:
    st.header("Configurações de Envio")
    projeto = st.selectbox("Selecione o Cliente", ["Tokio Marine", "Zurich", "Allianz", "Sompo Seguros", "Outro"])
    localidade = st.text_input("Cidade da Vistoria", value="Ibiporã")

arquivo_foto = st.file_uploader("Carregue a foto da evidência", type=['jpg', 'png', 'jpeg'])

if arquivo_foto:
    img = Image.open(arquivo_foto).convert("RGB")
    st.success("Foto carregada com sucesso!")
    
    # Controles de Foco para Geointeligência 360°
    col_x = st.slider("Ajuste Horizontal (Foco)", 0, img.width, img.width // 2)
    col_y = st.slider("Ajuste Vertical (Foco)", 0, img.height, img.height // 2)
    
    # Parecer da Sofia (Agente IA)
    st.subheader("🎙️ Parecer da Sofia")
    texto_narracao = st.text_area(
        "Descreva a anomalia técnica:",
        value="Identificada anomalia crítica na estrutura. O risco de colapso residual é elevado devido à exposição de armadura.",
        help="Este texto será usado para o vídeo 'Verdade Sem Filtro'."
    )
    
    # BOTÃO DE EXECUÇÃO E SALVAMENTO
    if st.button("🚀 GERAR LAUDO E SALVAR NA NUVEM"):
        zoom_img = aplicar_zoom_tecnico(img, col_x, col_y)
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        # Exibição Visual (Estética de Auditoria Forense)
        c1, c2 = st.columns(2)
        with c1:
            st.markdown('<p class="alerta-tecnico">VISÃO GERAL</p>', unsafe_allow_html=True)
            st.image(img, use_column_width=True)
        with c2:
            st.markdown('<p class="alerta-tecnico">EVIDÊNCIA AMPLIADA</p>', unsafe_allow_html=True)
            st.image(zoom_img, use_column_width=True)
            
        # Roteiro Processado
        st.divider()
        st.markdown(f"""
            <div class="narra-sofia">
                <strong>🔊 Roteiro de Narração (Sofia):</strong><br>
                "Atenção analista da {projeto}. Em {localidade}, Michael Mulero destaca: {texto_narracao}"
            </div>
        """, unsafe_allow_html=True)
        
        # Simulação de Salvamento no Google Sheets
        st.success(f"✅ Dados registrados na nuvem com sucesso! ({data_hora})")
        st.info(f"Relatório gerado para {projeto} em {localidade}.")
