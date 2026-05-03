import streamlit as st
import plotly.graph_objects as go

def gerar_ar_3d(tipo_risco):
    """Gera um modelo 3D interativo para visualização de perícia"""
    fig = go.Figure()

    # Define a volumetria baseada no seu padrão de inspeção (Ex: Formato H)
    if "H" in tipo_risco:
        # Coordenadas do polígono em H
        x = [1, 2, 2, 3, 3, 4, 4, 3, 3, 2, 2, 1, 1]
        y = [1, 1, 2, 2, 1, 1, 4, 4, 3, 3, 4, 4, 1]
        z = [0] * 13
        h = 1.5  # Altura do pé direito
    else:
        # Bloco comercial padrão
        x, y = [1, 4, 4, 1, 1], [1, 1, 4, 4, 1]
        z, h = [0] * 5, 1.2

    # Renderiza as paredes (Realidade Volumétrica)
    fig.add_trace(go.Mesh3d(
        x=x*2, y=y*2, z=z + [h]*len(z), 
        color='lightblue', opacity=0.5, name='Estrutura 3D'
    ))

    # Marcação de Risco (Ex: Ponto Crítico de Infiltração ou Elétrica)
    fig.add_trace(go.Scatter3d(
        x=[2.5], y=[2.5], z=[h],
        mode='markers+text',
        marker=dict(size=10, color='red', symbol='diamond'),
        text=["🔴 RISCO CRÍTICO"],
        name='Alerta Sofia'
    ))

    fig.update_layout(
        margin=dict(l=0, r=0, b=0, t=30),
        scene=dict(xaxis_title='X (m)', yaxis_title='Y (m)', zaxis_title='Z (m)'),
        height=500
    )
    return fig

# Interface do Sistema
st.header("📐 Inspeção em Realidade Aumentada 3D")
st.write("Interaja com o modelo para explorar as vulnerabilidades detectadas em Ibiporã.")

escolha = st.selectbox("Selecione o Croqui para Visualização:", 
                      ["Planta Baixa (Formato H)", "Área Operacional", "Implantação Geral"])

# Renderização do gráfico interativo
st.plotly_chart(gerar_ar_3d(escolha), use_container_width=True)
