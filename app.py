import streamlit as st
from streamlit_folium import folium_static
import folium

def gerar_mapa_contexto(lat=-23.2692, lon=-51.0519):
    # Usando OpenStreetMap para evitar o erro de atribuição do Stamen
    m = folium.Map(
        location=[lat, lon], 
        zoom_start=18, 
        tiles='OpenStreetMap'
    )
    
    # Adicionando o Marcador de Risco com Selo Michael Mulero
    folium.Marker(
        [lat, lon], 
        popup='📍 Ponto de Inspeção: Transformador/Risco Elétrico', 
        icon=folium.Icon(color='red', icon='info-sign')
    ).add_to(m)
    
    return m

# Interface do Laudo
st.subheader("📍 Geolocalização e Contexto do Risco (Ibiporã/PR)")
try:
    folium_static(gerar_mapa_contexto())
except Exception as e:
    st.error(f"Erro ao carregar mapa: {e}")
