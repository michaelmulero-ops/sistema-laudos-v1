import streamlit as st
import plotly.graph_objects as go
import numpy as np

# Configuração de Perito de Elite
st.set_page_config(page_title="Michael Mulero | Tech V1", layout="wide")

def gerar_isometria_tecnica(tipo_croqui):
    """
    Simula a renderização de infográficos isométricos baseados nos modelos:
    WhatsApp Image 2026-04-17 at 10.23.05.jpeg e 09.07.49.jpeg
    """
    fig = go.Figure()

    # 1. Base do Terreno e Calçadas (Padrão Isométrico)
    fig.add_trace(go.Mesh3d(
        x=[0, 10, 10, 0, 0, 10, 10, 0],
        y=[0, 0, 10, 10, 0, 0, 10, 10],
        z=[0, 0, 0, 0, 0.1, 0.1, 0.1, 0.1],
        color='lightgray', opacity=0.5, name='Base Técnica'
    ))

    # 2. Zoneamento por Cores (Padrão Michael Mulero)
    # Zona A - Vermelho (Alto Risco/Subestação)
    fig.add_trace(go.Mesh3d(x=[1, 4, 4, 1]*2, y=[1, 1, 4, 4]*2, z=[0.1]*4+[2]*4, color='red', opacity=0.7, name='Zona Alto Risco'))
    
    # Zona B - Amarelo (Médio Risco/Produção)
    fig.add_trace(go.Mesh3d(x=[4, 9, 9, 4]*2, y=[1, 1, 6, 6]*2, z=[0.1]*4+[1.5]*4, color='yellow', opacity=0.6, name='Zona Médio Risco'))

    # 3. Plotagem de Ativos (Ícones de Segurança)
    # Hidrantes (H) e Quadros Elétricos (QGBT)
    fig.add_trace(go.Scatter3d(
        x=[2, 5, 8], y=[2, 5, 3], z=[2.1, 1.6, 0.2],
        mode='markers+text',
        marker=dict(size=8, color=['darkred', 'orange', 'green'], symbol='diamond'),
        text=["🔥 [RTI]", "⚡ [QGBT]", "🚶 Rota de Fuga"],
        name='Ativos de Segurança'
    ))

    fig.update_layout(
        scene=dict(
            xaxis=dict(visible=False), yaxis=dict(visible=False), zaxis=dict(visible=False),
            aspectmode='manual', aspectratio=dict(x=1, y=1, z=0.4),
            camera=dict(eye=dict(x=1.5, y=1.5, z=1.2)) # Ângulo Isométrico
        ),
        margin=dict(l=0, r=0, b=0, t=40), height=600,
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)'
    )
    return fig

# --- Interface Estilizada (Digna de Inspeção) ---
st.title("🛡️ Michael Mulero Inspeções | Central de Infografia Forense")
st.markdown("---")

col_info, col_render = st.columns([1, 3])

with col_info:
    st.subheader("📋 Dados do Laudo")
    st.info("**Inspetor:** Michael Giovanni Mulero")
    st.write("**Local:** Ibiporã, PR")
    
    with st.expander("⚙️ Engrenagens de Zoneamento", expanded=True):
        st.color_picker("Zona A (Alto Risco)", "#FF0000")
        st.color_picker("Zona B (Médio Risco)", "#FFFF00")
        st.color_picker("Zona C (Baixo Risco)", "#00FF00")
        st.multiselect("Ativos Identificados:", ["Hidrantes (RTI)", "Para-raios (SPDA)", "Quadros Elétricos", "Depósito Inflamáveis"])

with col_render:
    st.subheader("📐 Croqui de Implantação e Zoneamento 3D")
    st.plotly_chart(gerar_isometria_tecnica("Master"), use_container_width=True)
    st.caption("Visualização Técnica Isométrica conforme NBR 5419 e PAE Rio-Mar.")

# --- Rodapé Técnico ---
st.markdown("---")
st.markdown("#### 📄 Notas Técnicas Forenses")
st.warning("**[RTI]:** Rede de hidrantes verificada em conformidade. **[SPDA]:** Ensaios pendentes conforme norma vigente.")
