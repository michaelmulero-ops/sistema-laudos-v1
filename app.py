import streamlit as st
from streamlit_js_eval import get_geolocation

st.subheader("📡 GPS em Tempo Real - Michael Mulero")

# Captura as coordenadas reais do seu celular no campo
loc = get_geolocation()

if loc:
    lat = loc['coords']['latitude']
    lon = loc['coords']['longitude']
    st.success(f"📍 Ponto de Inspeção Detectado: {lat}, {lon}")
    # O mapa agora carregará automaticamente nesta posição
else:
    st.info("Aguardando sinal de GPS para alinhar o satélite...")
