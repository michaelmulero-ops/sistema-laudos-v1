import streamlit as st
import plotly.graph_objects as go

# Configuração Michael Mulero Inspeções
st.set_page_config(page_title="Michael Mulero | Auditoria Tech V1", layout="wide")

def gerar_isometria_especializada(setor, ativos):
    fig = go.Figure()
    
    # 1. Base e Volumetria Adaptativa
    # Se for Shopping, a planta é mais espraiada; se Logística, foca em pátios.
    if setor == "Shopping":
        cor_base = "lightgray"
        fig.add_trace(go.Mesh3d(x=[1, 9, 9, 1]*2, y=[1, 1, 9, 9]*2, z=[0, 0, 0, 0, 2, 2, 2, 2], color='silver', opacity=0.4))
    elif setor == "Transportadora/Logística":
        cor_base = "gray"
        fig.add_trace(go.Mesh3d(x=[1, 9, 9, 1]*2, y=[1, 1, 5, 5]*2, z=[0, 0, 0, 0, 3, 3, 3, 3], color='gray', opacity=0.5))
    
    # 2. Zoneamento e Ativos Críticos
    for nome, pos in ativos.items():
        fig.add_trace(go.Scatter3d(
            x=[pos[0]], y=[pos[1]], z=[pos[2]],
            mode='markers+text',
            marker=dict(size=10, symbol='diamond', color='black'),
            text=[f"<b>{nome}</b>"], textposition="top center"
        ))

    fig.update_layout(
        scene=dict(xaxis=dict(visible=False), yaxis=dict(visible=False), zaxis=dict(visible=False),
        camera=dict(eye=dict(x=1.8, y=1.8, z=1.5))),
        margin=dict(l=0, r=0, b=0, t=0), height=600
    )
    return fig

# Interface do Perito
st.title("🛡️ Central de Auditoria Especializada - Michael Mulero")
setor_sel = st.sidebar.selectbox("Setor de Inspeção:", 
                                ["Comércio", "Shopping Center", "Transportadora Logística", "Indústria"])

with st.expander("⚙️ Engrenagens de Risco Local - Ibiporã/PR"):
    ativos_map = {
        "🔥 [RTI]": [2, 2, 0.2], 
        "⚡ [QGBT]": [7, 3, 0.2], 
        "📦 Área de Carga": [5, 8, 0.1]
    }
    st.write(f"Gerando croquis isométricos para o setor de **{setor_sel}**.")

st.plotly_chart(gerar_isometria_especializada(setor_sel, ativos_map), use_container_width=True)
