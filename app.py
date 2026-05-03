import streamlit as st
import plotly.graph_objects as go

# Configuração Michael Mulero Inspeções
st.set_page_config(page_title="Michael Mulero | Tech V1", layout="wide")

def gerar_isometria_premium(zona_a, zona_b, zona_c, ativos):
    """Gerador de Infográficos Isométricos Nível Auditoria"""
    fig = go.Figure()

    # 1. Base Isométrica do Terreno
    fig.add_trace(go.Mesh3d(
        x=[0, 10, 10, 0, 0, 10, 10, 0], y=[0, 0, 10, 10, 0, 0, 10, 10],
        z=[0, 0, 0, 0, 0.1, 0.1, 0.1, 0.1], color='lightgray', opacity=0.4
    ))

    # 2. Renderização das Zonas (Carga de Incêndio/Risco)
    # ZONA A (Vermelho)
    fig.add_trace(go.Mesh3d(x=[1, 4, 4, 1]*2, y=[1, 1, 4, 4]*2, z=[0.1]*4+[2]*4, color=zona_a, opacity=0.8))
    # ZONA B (Amarelo)
    fig.add_trace(go.Mesh3d(x=[4, 8, 8, 4]*2, y=[1, 1, 5, 5]*2, z=[0.1]*4+[1.5]*4, color=zona_b, opacity=0.7))
    # ZONA C (Verde)
    fig.add_trace(go.Mesh3d(x=[1, 8, 8, 1]*2, y=[5, 5, 9, 9]*2, z=[0.1]*4+[1]*4, color=zona_c, opacity=0.6))

    # 3. Plotagem de Ativos de Segurança (Ícones Técnicos)
    posicoes = {"[RTI]": [2.5, 2.5, 2.2], "[QGBT]": [6, 3, 1.7], "Rota de Fuga": [4.5, 7, 1.1]}
    for ativo in ativos:
        if ativo in posicoes:
            p = posicoes[ativo]
            fig.add_trace(go.Scatter3d(
                x=[p[0]], y=[p[1]], z=[p[2]], mode='markers+text',
                marker=dict(size=10, symbol='diamond', color='black'),
                text=[f"<b>{ativo}</b>"], textposition="top center"
            ))

    fig.update_layout(
        scene=dict(
            xaxis=dict(visible=False), yaxis=dict(visible=False), zaxis=dict(visible=False),
            camera=dict(eye=dict(x=1.8, y=1.8, z=1.5)) # Ângulo Forense
        ),
        margin=dict(l=0, r=0, b=0, t=0), height=600, paper_bgcolor='rgba(0,0,0,0)'
    )
    return fig

# --- Interface Principal ---
st.title("🛡️ Michael Mulero Inspeções Tech V1")
st.sidebar.info(f"Inspetor: Michael Giovanni Mulero\nBase: Ibiporã, PR")

col_dados, col_viz = st.columns([1, 2])

with col_dados:
    st.subheader("📋 Dados do Laudo")
    with st.expander("⚙️ Engrenagens de Zoneamento", expanded=True):
        z_a = st.color_picker("Zona A (Alto Risco)", "#FF0000")
        z_b = st.color_picker("Zona B (Médio Risco)", "#FFFF00")
        z_c = st.color_picker("Zona C (Baixo Risco)", "#00FF00")
        ativos_sel = st.multiselect("Ativos Identificados:", ["[RTI]", "[QGBT]", "Rota de Fuga"])

with col_viz:
    st.subheader("📐 Croqui de Implantação e Zoneamento 3D")
    st.plotly_chart(gerar_isometria_premium(z_a, z_b, z_c, ativos_sel), use_container_width=True)
