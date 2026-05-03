import streamlit as st
import plotly.graph_objects as go

# Configuração Michael Mulero Inspeções - Qualidade Absoluta
st.set_page_config(page_title="Michael Mulero | Auditoria Tech V1", layout="wide")

def gerar_isometria_residencial_elite(setor, ativos_selecionados):
    fig = go.Figure()
    
    # 1. Modelagem Isométrica de Alto Padrão (Corte Técnico)
    if setor == "Residência de Luxo":
        # Desenho da residência com telhado e varandas
        fig.add_trace(go.Mesh3d(
            x=[1, 5, 5, 1, 1, 5, 5, 1, 3], y=[1, 1, 4, 4, 1, 1, 4, 4, 2.5], z=[0, 0, 0, 0, 2.5, 2.5, 2.5, 2.5, 4],
            color='peru', opacity=0.7, name='Residência'
        ))
    elif setor == "Condomínio":
        # Desenho da portaria e áreas sociais
        fig.add_trace(go.Mesh3d(
            x=[1, 9, 9, 1]*2, y=[1, 1, 3, 3]*2, z=[0]*4+[2]*4, color='silver', opacity=0.5, name='Portaria/Muro'
        ))

    # 2. Plotagem de Ativos de Segurança (Ícones Técnicos)
    for ativo in ativos_selecionados:
        # Posições simuladas conforme a planta real de Ibiporã
        fig.add_trace(go.Scatter3d(
            x=[2], y=[2], z=[0.2], mode='markers+text',
            marker=dict(size=10, symbol='diamond', color='black'),
            text=[f"<b>{ativo}</b>"], textposition="top center"
        ))

    fig.update_layout(
        scene=dict(xaxis=dict(visible=False), yaxis=dict(visible=False), zaxis=dict(visible=False),
        camera=dict(eye=dict(x=1.8, y=1.8, z=1.5))), # Ângulo Isométrico Profissional
        margin=dict(l=0, r=0, b=0, t=0), height=650
    )
    return fig

# --- Interface Michael Mulero ---
st.title("🛡️ Sistema de Auditoria Forense Tech V1")
st.sidebar.markdown(f"**Inspetor:** Michael Giovanni Mulero")
st.sidebar.markdown(f"**Local:** Ibiporã, PR")

setor = st.sidebar.selectbox("Gaveta de Risco:", 
                             ["Residência de Luxo", "Condomínio", "Shopping Center", "Transportadora Logística", "Comércio"])

with st.expander("⚙️ Engrenagens de Ativos e Zoneamento", expanded=True):
    ativos = st.multiselect("Sinalizar no Croqui:", 
                            ["🔥 [RTI] Hidrantes", "⚡ [QGBT] Elétrica", "🛡️ Cerca Elétrica", "🚨 Portaria 24h"])

st.subheader(f"📐 Croqui Isométrico HD - Setor: {setor}")
st.plotly_chart(gerar_isometria_residencial_elite(setor, ativos), use_container_width=True)
