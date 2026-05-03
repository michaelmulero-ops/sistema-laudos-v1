import streamlit as st
import plotly.graph_objects as go

def gerar_croqui_infraestrutura(tipo_analise):
    """Gera croquis técnicos de infraestrutura: Rios, Trens, Aerovias e Rodovias"""
    fig = go.Figure()
    
    # Simulação de Eixos de Risco e Logística
    if tipo_analise == "Transporte e Aerovias":
        # Linha de Trem (Malha Ferroviária)
        fig.add_trace(go.Scatter(x=[0, 10], y=[2, 2], mode='lines+markers', 
                                 line=dict(color='black', width=3, dash='dash'), name='Linha Férrea'))
        # Aeroporto / Rota de Aviões (Cone de Aproximação)
        fig.add_trace(go.Scatter(x=[0, 10], y=[8, 9], mode='lines', 
                                 line=dict(color='orange', width=15, opacity=0.3), name='Rota Aérea (Aproximação)'))
        # Vias de Grande Movimento (Rodovias/Avenidas)
        fig.add_trace(go.Scatter(x=[5, 5], y=[0, 10], mode='lines', 
                                 line=dict(color='gray', width=8), name='Rodovia / Via Arterial'))

    elif tipo_analise == "Hidrografia e Lagos":
        # Rios e Lagos (Corpos d'Água)
        fig.add_trace(go.Scatter(x=[1, 3, 7, 9, 1], y=[1, 4, 3, 1, 1], 
                                 fill='toself', fillcolor='rgba(0, 0, 255, 0.3)', 
                                 line=dict(color='blue'), name='Rio / Lago / APP'))

    # Ponto Central: O Risco Inspecionado
    fig.add_trace(go.Scatter(x=[5], y=[5], mode='markers+text', 
                             marker=dict(size=18, color='red', symbol='cross'),
                             text=["📍 IMÓVEL INSPECIONADO"], textposition="top center"))

    fig.update_layout(
        title=f"Croqui de Segurança: {tipo_analise}",
        xaxis=dict(title="Distância Relativa (km)", range=[0, 10]),
        yaxis=dict(title="Distância Relativa (km)", range=[0, 10]),
        margin=dict(l=20, r=20, b=20, t=50),
        template="plotly_white",
        height=500
    )
    return fig

# --- Interface Michael Mulero ---
st.header("📐 Mapeamento Geográfico de Riscos Externos")
st.write("Análise técnica de proximidade com infraestruturas críticas e recursos hídricos em Ibiporã/PR.")

col_infra1, col_infra2 = st.columns(2)

with col_infra1:
    st.plotly_chart(gerar_croqui_infraestrutura("Transporte e Aerovias"), use_container_width=True)
    st.info("⚠️ **Análise de Logística:** Avaliação de vibração (trens), ruído/queda (aviões) e acessibilidade (vias).")

with col_infra2:
    st.plotly_chart(gerar_croqui_infraestrutura("Hidrografia e Lagos"), use_container_width=True)
    st.warning("🌊 **Análise Hídrica:** Verificação de inundação, áreas de preservação permanente (APP) e solo.")
