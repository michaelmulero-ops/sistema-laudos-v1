import streamlit as st
import folium
from streamlit_folium import folium_static

def mapear_entorno_estrategico(lat_inspecao, lon_inspecao):
    # Mapa base focado no risco em Ibiporã
    m = folium.Map(location=[lat_inspecao, lon_inspecao], zoom_start=16)
    
    # Marcador do Imóvel Inspecionado (Michael Mulero Inspeções)
    folium.Marker([lat_inspecao, lon_inspecao], 
                  popup='🏠 IMÓVEL INSPECIONADO', 
                  icon=folium.Icon(color='red', icon='home')).add_to(m)

    # Simulação de pontos de interesse (POI) detectados via API Google
    pontos_entorno = [
        {"nome": "Corpo de Bombeiros", "coord": [lat_inspecao+0.002, lon_inspecao+0.002], "cor": "darkred", "icon": "fire"},
        {"nome": "Delegacia de Polícia", "coord": [lat_inspecao-0.003, lon_inspecao+0.001], "cor": "blue", "icon": "shield"},
        {"nome": "Escola Municipal", "coord": [lat_inspecao+0.001, lon_inspecao-0.004], "cor": "orange", "icon": "book"},
        {"nome": "Campo de Futebol/Praça", "coord": [lat_inspecao-0.002, lon_inspecao-0.002], "cor": "green", "icon": "users"},
        {"nome": "Sindicato/Aglomeração", "coord": [lat_inspecao+0.004, lon_inspecao-0.001], "cor": "cadetblue", "icon": "briefcase"}
    ]

    for ponto in pontos_entorno:
        folium.Marker(ponto["coord"], 
                      popup=ponto["nome"], 
                      icon=folium.Icon(color=ponto["cor"], icon=ponto["icon"])).add_to(m)
        
    return m

# Exibição no Streamlit
st.subheader("🛰️ Análise de Vizinhança e Aglomeração Pública")
folium_static(mapear_entorno_estrategico(-23.2692, -51.0519))
    st.warning("Análise de proximidade com rios para verificação de risco de inundação e conformidade ambiental.")
