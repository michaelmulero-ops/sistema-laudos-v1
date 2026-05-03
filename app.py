import streamlit as st
import plotly.graph_objects as go

def gerar_croqui_ilustrado(tipo, icone, cor):
    fig = go.Figure()
    
    # 1. O Desenho do Risco (Base do Mapa)
    fig.add_annotation(x=5, y=5, text="🏠", font=dict(size=100), showarrow=False)
    
    # 2. O Desenho do Elemento Externo (Rio, Avião, Trem)
    fig.add_annotation(x=2, y=8, text=icone, font=dict(size=80), showarrow=False)
    
    # 3. Sinalização de Texto Direta para a Analista
    fig.add_trace(go.Scatter(
        x=[2, 5], y=[7.5, 4.5],
        mode='text',
        text=[f"<b>{tipo}</b>", "<b>IMÓVEL</b>"],
        textfont=dict(size=18, color="black")
    ))

    fig.update_layout(
        showlegend=False,
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        plot_bgcolor=cor,
        height=350, margin=dict(l=10, r=10, b=10, t=50)
    )
    return fig

# --- Interface Michael Mulero Tech V1 ---
st.title("🛡️ Michael Mulero | Central de Croquis Ilustrados")

col_a, col_b = st.columns(2)

with col_a:
    st.plotly_chart(gerar_croqui_ilustrado("Rota de Aviões", "✈️", "#fff9c4"), use_container_width=True)
    st.plotly_chart(gerar_croqui_ilustrado("Risco de Inundação", "🌊", "#e3f2fd"), use_container_width=True)
    st.plotly_chart(gerar_croqui_ilustrado("Socorro Emergencial", "🚒", "#ffecb3"), use_container_width=True)

with col_b:
    st.plotly_chart(gerar_croqui_ilustrado("Malha Ferroviária", "🚂", "#f5f5f5"), use_container_width=True)
    st.plotly_chart(gerar_croqui_ilustrado("Aglomeração Pública", "🏟️", "#e8f5e9"), use_container_width=True)
    st.plotly_chart(gerar_croqui_ilustrado("Segurança/Delegacia", "🚓", "#e1f5fe"), use_container_width=True)
