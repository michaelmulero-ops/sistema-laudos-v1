import streamlit as st
import plotly.graph_objects as go
import folium
from streamlit_folium import folium_static

# Configuração Michael Mulero
st.set_page_config(page_title="Michael Mulero Inspeções Tech V1", layout="wide")

def gerar_croqui_infra(tipo):
    """Gera croquis técnicos de infraestrutura sem erros de sintaxe"""
    fig = go.Figure()
    
    if tipo == "Transporte e Aerovias":
        # Rota Aérea (Aproximação) - Corrigido sem conflito de opacity
        fig.add_trace(go.Scatter(x=[0, 10], y=[8, 9], mode='lines', 
                                 line=dict(color='rgba(255, 165, 0, 0.3)', width=15), 
                                 name='Aerovia / Rota Aérea'))
        # Linha de Trem
        fig.add_trace(go.Scatter(x=[0, 10], y=[2, 2], mode='lines+markers', 
                                 line=dict(color='black', width=3, dash='dash'), name='Malha Ferroviária'))
        # Rodovias de Grande Movimento
        fig.add_trace(go.Scatter(x=[5, 5], y=[0, 10], mode='lines', 
                                 line=dict(color='gray', width=10), name='Via Arterial / Rodovia'))

    elif tipo == "Hidrografia e Riscos":
        # Rios e Lagos (Polígono Fechado)
        fig.add_trace(go.Scatter(x=[1, 3, 7, 9, 1], y=[1, 4, 3, 1, 1], fill='toself', 
                                 fillcolor='rgba(0, 0, 255, 0.2)', line=dict(color='blue'), 
                                 name='Corpo d\'Água / Rio / APP'))

    # Ponto Central (O Risco)
    fig.add_trace(go.Scatter(x=[5], y=[5], mode='markers+text', 
                             marker=dict(size=15, color='red', symbol='cross'),
                             text=["📍 RISCO INSPECIONADO"], textposition="top center"))

    fig.update_layout(template="plotly_white", height=450, margin=dict(l=20, r=20, b=20, t=50))
    return fig

# --- Interface Principal ---
st.title("🛡️ Michael Mulero Inspeções Tech V1")
st.sidebar.markdown(f"**Inspetor:** Michael Giovanni Mulero\n**Local:** Ibiporã, PR")

# 1. Mapa de Segurança e Serviços Públicos
st.subheader("🛰️ Mapeamento de Serviços e Segurança (Ibiporã/PR)")
m = folium.Map(location=[-23.2692, -51.0519], zoom_start=15)

# Pontos de Interesse Estratégicos
pontos = [
    {"n": "Corpo de Bombeiros", "c": [-23.267, -51.050], "i": "fire", "color": "darkred"},
    {"n": "Delegacia de Polícia", "c": [-23.271, -51.053], "i": "shield", "color": "blue"},
    {"n": "Escola / Aglomeração", "c": [-23.265, -51.055], "i": "book", "color": "orange"},
    {"n": "Sindicato / Praça", "c": [-23.273, -51.049], "i": "users", "color": "green"}
]

for p in pontos:
    folium.Marker(p["c"], popup=p["n"], icon=folium.Icon(color=p["color"], icon=p["i"])).add_to(m)

folium.Marker([-23.2692, -51.0519], popup="RISCO", icon=folium.Icon(color='red', icon='home')).add_to(m)
folium_static(m)

# 2. Croquis de Infraestrutura (Lógica corrigida)
st.divider()
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(gerar_croqui_infra("Transporte e Aerovias"), use_container_width=True)
with col2:
    st.plotly_chart(gerar_croqui_infra("Hidrografia e Riscos"), use_container_width=True)
