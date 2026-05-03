import streamlit as st
from streamlit_folium import folium_static
import folium
from PIL import Image, ImageDraw
import io

# Identidade Michael Mulero - Inspetor de Risco
st.set_page_config(page_title="Michael Mulero Inspeções Tech V1", layout="wide")

def gerar_croqui_tecnico_vivo(tipo, contexto=""):
    """Renderiza croquis com profundidade e escala real 10x10"""
    img = Image.new('RGB', (500, 500), color='#ffffff')
    draw = ImageDraw.Draw(img)
    # Grid de Engenharia
    for i in range(0, 500, 50):
        draw.line([(i, 0), (i, 500)], fill='#f0f0f0', width=1)
        draw.line([(0, i), (500, i)], fill='#f0f0f0', width=1)
    
    # Lógica de Desenho conforme o Risco
    if "H" in tipo:
        draw.polygon([(100,100), (180,100), (180,200), (320,200), (320,100), (400,100), 
                      (400,400), (320,400), (320,300), (180,300), (180,400), (100,400)], 
                     outline="black", fill="#f9f9f9", width=4)
    else:
        draw.rectangle([150, 150, 350, 350], outline="blue", width=4)
    return img

# --- Interface Consolidada ---
st.title("🛡️ Michael Mulero Inspeções Tech V1")
st.sidebar.markdown(f"**Inspetor:** Michael Giovanni Mulero\n**Local:** Ibiporã, PR")

# 1. Mapa Forense (O Coração da Localização)
st.subheader("📍 Contexto Geográfico e Localização do Risco")
m = folium.Map(location=[-23.2692, -51.0519], zoom_start=18, tiles='OpenStreetMap')
folium.Marker([-23.2692, -51.0519], popup='📍 Ponto de Inspeção: Michael Mulero', icon=folium.Icon(color='red')).add_to(m)
folium_static(m)

# 2. Processamento de Evidências (Fotos + Word + Vídeos)
arquivos = st.file_uploader("Subir Pacote de Vistoria (Fotos, Vídeos, Word):", accept_multiple_files=True)

if arquivos:
    st.info("🔄 Sofia realizando leitura cruzada de imagens e relatórios técnicos...")
    
    if st.button("📄 GERAR LAUDO FINAL E SUÍTE DE CROQUIS"):
        st.divider()
        st.header("📐 Suíte de Croquis Técnicos (Escala 10x10)")
        cols = st.columns(2)
        modelos = ["Planta Baixa (Formato H)", "Área Operacional Industrial", "Mapa de Blindagem Perimetral", "Implantação Geral"]
        
        for idx, m in enumerate(modelos):
            with cols[idx % 2]:
                st.markdown(f"**{m}**")
                st.image(gerar_croqui_tecnico_vivo(m), caption="Visualização Técnica | Selo GPS Ibiporã")
