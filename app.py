import streamlit as st
import plotly.graph_objects as go

# Configuração Michael Mulero Inspeções
st.set_page_config(page_title="Amostra Técnica | Tech V1", layout="wide")

def gerar_amostra_isometrica():
    fig = go.Figure()

    # 1. Volumetria do Galpão (Formato 'H' Industrial)
    fig.add_trace(go.Mesh3d(
        x=[1, 4, 4, 1, 1, 4, 4, 1, 2.5], 
        y=[1, 1, 7, 7, 1, 1, 7, 7, 4], 
        z=[0, 0, 0, 0, 3, 3, 3, 3, 4.5], # Z=Altura e Cumeeira
        color='steelblue', opacity=0.6, name='Estrutura Principal'
    ))

    # 2. Zoneamento de Risco (Padrão Michael Mulero)
    # Piso em Vermelho para indicar área de maior risco
    fig.add_trace(go.Mesh3d(x=[1, 4, 4, 1], y=[1, 1, 3, 3], z=[0.05]*4, color='red', opacity=0.8))

    # 3. Plotagem de Ativos de Segurança
    fig.add_trace(go.Scatter3d(
        x=[1.5, 3.5, 2.5], y=[1.5, 2.5, 4], z=[0.1, 0.1, 4.6],
        mode='markers+text',
        marker=dict(size=10, color='black', symbol='diamond'),
        text=["<b>[RTI]</b>", "<b>[QGBT]</b>", "<b>[SPDA]</b>"],
        textposition="top center"
    ))

    fig.update_layout(
        scene=dict(xaxis=dict(visible=False), yaxis=dict(visible=False), zaxis=dict(visible=False),
        camera=dict(eye=dict(x=1.8, y=1.8, z=1.5))),
        margin=dict(l=0, r=0, b=0, t=0), height=600
    )
    return fig

# Interface de Exibição
st.title("🛡️ Demonstração de Infografia Forense")
st.markdown("---")
st.plotly_chart(gerar_amostra_isometrica(), use_container_width=True)
st.info("Nota: Este modelo integra a volumetria industrial com a localização georreferenciada em Ibiporã/PR.")
