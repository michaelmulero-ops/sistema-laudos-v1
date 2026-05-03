import streamlit as st
import plotly.graph_objects as go

def desenhar_modelo(tipo, key):
    fig = go.Figure()
    # Lógica de renderização específica para cada um dos 6 tipos
    if "H" in tipo:
        fig.add_trace(go.Mesh3d(x=[1,2,2,3,3,4,4,1]*2, y=[1,1,2,2,1,1,4,4]*2, z=[0]*8+[1.5]*8, color='steelblue'))
    elif "Entorno" in tipo:
        fig.add_trace(go.Scatter(x=[5], y=[5], mode='markers+text', text=["📍 RISCO"]))
        fig.add_trace(go.Scatter(x=[2, 8], y=[2, 8], mode='markers', name='Bombeiros/Polícia'))
    # ... demais modelos ...
    fig.update_layout(title=tipo, margin=dict(l=0,r=0,b=0,t=30), height=250)
    return fig

st.header("📐 Galeria de Modelos de Croquis - Michael Mulero Tech V1")

# Grade de 3x2 para visualização completa
col1, col2 = st.columns(2)
modelos = [
    "Planta Baixa (H)", "Entorno Estratégico", 
    "Hidrografia/Rios", "Logística/Trens", 
    "Realidade Aumentada", "Aglomeração Pública"
]

for i, m in enumerate(modelos):
    with (col1 if i % 2 == 0 else col2):
        st.plotly_chart(desenhar_modelo(m, i), use_container_width=True, key=f"croqui_{i}")
