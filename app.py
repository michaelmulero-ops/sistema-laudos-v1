import streamlit as st
import plotly.graph_objects as go
import folium
from streamlit_folium import folium_static

def gerar_croqui_seguranca_entorno(tipo_mapeamento):
    """Gera visualização técnica de riscos externos (Aerovias, Rios e Acessos)"""
    fig = go.Figure()
    
    # Simulação de camadas de geoprocessamento
    if "Aviões" in tipo_mapeamento:
        # Rota de Aproximação (Cone de pouso/decolagem)
        fig.add_trace(go.Scatter(x=[0, 10], y=[0, 5], mode='lines', 
                                 line=dict(color='yellow', width=10, dash='dot'), name='Aerovia Londrina/Ibiporã'))
        fig.add_annotation(x=5, y=3, text="✈️ Rota de Baixa Altitude", showarrow=True)
    
    elif "Rios" in tipo_mapeamento:
        # Mapeamento de Hidrografia e APP (Área de Preservação)
        fig.add_trace(go.Scatter(x=[0, 2, 5, 8, 10], y=[2, 3, 2, 4, 3], 
                                 fill='toself', color='blue', name='Corpo d\'Água / Rio'))
        fig.add_annotation(x=5, y=2, text="🌊 Risco de Inundação/APP", showarrow=False)

    # Localização do Imóvel (O Alvo da Inspeção)
    fig.add_trace(go.Scatter(x=[5], y=[5], mode='markers+text', 
                             marker=dict(size=15, color='red', symbol='square'),
                             text=["📍 Imóvel Inspecionado"], textposition="top center"))

    fig.update_layout(title=f"Análise de Entorno: {tipo_mapeamento}", 
                      xaxis_title="Distância (km)", yaxis_title="Distância (km)",
                      template="plotly_white", height=400)
    return fig

# --- Interface Michael Mulero ---
st.divider()
st.header("📐 Croquis de Localização e Segurança Perimetral")
st.write("Análise macro do risco: Impactos de aerovias, hidrografia e acessos logísticos em Ibiporã/PR.")

col_entorno1, col_entorno2 = st.columns(2)

with col_entorno1:
    st.subheader("✈️ Espaço Aéreo e Logística")
    st.plotly_chart(gerar_croqui_seguranca_entorno("Rota de Aviões"), use_container_width=True)
    st.info("Verificação de zona de ruído e riscos de queda de objetos/aeronaves conforme proximidade com aeródromo.")

with col_entorno2:
    st.subheader("🌊 Hidrografia e Relevo")
    st.plotly_chart(gerar_croqui_seguranca_entorno("Rios e Escoamento"), use_container_width=True)
    st.warning("Análise de proximidade com rios para verificação de risco de inundação e conformidade ambiental.")
