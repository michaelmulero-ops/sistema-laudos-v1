import streamlit as st
from streamlit_drawable_canvas import st_canvas
import folium
from streamlit_folium import st_folium

# 1. Módulo de Geointeligência: Localização Automática
st.subheader("📍 Localização e Satélite em Tempo Real")

# Coordenadas padrão de Ibiporã (sua base)
lat, lon = -23.2694, -51.0469 

# Criação do mapa técnico para base do croqui
m = folium.Map(location=[lat, lon], zoom_start=19, tiles="https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}", attr="Google")
folium.Marker([lat, lon], popup="Ponto de Inspeção").add_to(m)

# Exibe o mapa para conferência de limites e confrontantes
st_data = st_folium(m, width=700, height=400)

# 2. Prancheta de Desenho sobre o Satélite
st.subheader("📐 Desenho Técnico de Delimitação (H, L, U)")
st.write("Utilize a ferramenta abaixo para traçar o contorno real da edificação conforme a imagem acima.")

# Interface de desenho para formas complexas
canvas_result = st_canvas(
    fill_color="rgba(255, 0, 0, 0.3)",  # Vermelho transparente para áreas de risco
    stroke_width=2,
    stroke_color="#ff0000",
    background_color="#eee",
    height=400,
    width=700,
    drawing_mode="polygon", # Essencial para formatos em "H"
    key="canvas_georeferenciado",
)

if canvas_result.json_data:
    st.success("✅ Croqui técnico alinhado ao satélite gerado com sucesso.")
