import streamlit as st
from streamlit_folium import folium_static
import folium

# 1. Mapa Real de Ibiporã para o Croqui de Implantação
def gerar_mapa_contexto(lat=-23.2692, lon=-51.0519):
    m = folium.Map(location=[lat, lon], zoom_start=18, tiles='Stamen Terrain')
    # Marcação do Risco Crítico (ex: Transformador)
    folium.Marker([lat, lon], popup='Área Crítica: Transformador', icon=folium.Icon(color='red')).add_to(m)
    return m

st.subheader("📍 Contexto Geográfico Forense (Ibiporã/PR)")
st.write("Visão de satélite integrada para validação de confrontantes e logística.")
folium_static(gerar_mapa_contexto())

# 2. Espaço para Vídeo Analítico
video_file = st.file_uploader("Subir Vídeo da Vistoria para Análise Sofia:", type=['mp4', 'mov', 'avi'])
if video_file:
    st.video(video_file)
    st.info("🎥 Sofia analisando frames para detecção de anomalias estruturais e térmicas.")
    
