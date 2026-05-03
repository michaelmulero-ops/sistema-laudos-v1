import streamlit as st
import plotly.graph_objects as go

# Configuração de Perito de Elite
st.set_page_config(page_title="Michael Mulero | Auditoria Tech V1", layout="wide")

def gerar_croqui_forense_3d(tipo_risco, ativos_identificados):
    """
    Renderiza infográficos isométricos de alta complexidade.
    Padrão: WhatsApp Image 2026-04-17 at 14.48.34.jpeg
    """
    fig = go.Figure()

    # 1. Estrutura Isométrica do Imóvel (Corte Técnico)
    # Definindo as paredes e telhado com volumetria real
    fig.add_trace(go.Mesh3d(
        x=[1, 5, 5, 1, 1, 5, 5, 1, 3], # Coordenadas X
        y=[1, 1, 6, 6, 1, 1, 6, 6, 3.5], # Coordenadas Y
        z=[0, 0, 0, 0, 3, 3, 3, 3, 4.5], # Z (Altura + Cumeeira)
        i=[7, 0, 0, 0, 4, 4, 2, 6, 4, 5, 6, 7], # Índices para faces
        j=[0, 1, 2, 3, 5, 6, 7, 4, 5, 6, 7, 4],
        k=[1, 2, 3, 0, 1, 2, 3, 0, 8, 8, 8, 8],
        color='steelblue', opacity=0.5, name='Estrutura Principal'
    ))

    # 2. Zoneamento de Risco por Cores (Padrão Michael Mulero)
    # Chão colorido para indicar carga de incêndio (Vermelho/Amarelo/Verde)
    fig.add_trace(go.Mesh3d(
        x=[1, 5, 5, 1], y=[1, 1, 4, 4], z=[0.05, 0.05, 0.05, 0.05],
        color='red', opacity=0.8, name='Zona A: Alta Carga'
    ))

    # 3. Plotagem de Ativos de Segurança (Ícones Técnicos HD)
    # RTI, QGBT, SPDA conforme fotos de referência
    posicoes = {
        "🔥 [RTI]": [2, 2, 0.1], 
        "⚡ [QGBT]": [4, 2, 0.1], 
        "⚡ [SPDA]": [3, 3.5, 4.6],
        "🚶 Rota de Fuga": [1, 5, 0.1]
    }
    
    for nome, coord in posicoes.items():
        if nome in ativos_identificados:
            fig.add_trace(go.Scatter3d(
                x=[coord[0]], y=[coord[1]], z=[coord[2]],
                mode='markers+text',
                marker=dict(size=8, color='black', symbol='diamond'),
                text=[f"<b>{nome}</b>"],
                textposition="top center"
            ))

    # Configuração de Câmera e Estética Forense
    fig.update_layout(
        scene=dict(
            xaxis=dict(visible=False), yaxis=dict(visible=False), zaxis=dict(visible=False),
            aspectmode='data',
            camera=dict(eye=dict(x=1.8, y=1.8, z=1.5)) # Ângulo Isométrico Técnico
        ),
        margin=dict(l=0, r=0, b=0, t=30), height=650,
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)'
    )
    return fig

# --- Interface Michael Mulero ---
st.title("🛡️ Michael Mulero Inspeções | Central de Auditoria Forense")
st.sidebar.info(f"Inspetor: Michael Giovanni Mulero\nBase: Ibiporã, PR")

col_config, col_viz = st.columns([1, 2])

with col_config:
    st.subheader("📋 Parâmetros da Inspeção")
    with st.expander("⚙️ Engrenagens de Zoneamento", expanded=True):
        st.write("**Localização:** Ibiporã, Paraná")
        tipo = st.selectbox("Tipo de Edificação", ["Indústria", "Condomínio de Alto Padrão", "Residência de Luxo"])
        ativos = st.multiselect("Ativos Identificados no Campo:", 
                                ["🔥 [RTI]", "⚡ [QGBT]", "⚡ [SPDA]", "🚶 Rota de Fuga"],
                                default=["🔥 [RTI]", "⚡ [QGBT]"])

with col_viz:
    st.subheader(f"📐 Croqui de Implantação e Zoneamento 3D - {tipo}")
    st.plotly_chart(gerar_croqui_forense_3d(tipo, ativos), use_container_width=True)
    st.caption("Visualização Técnica Isométrica em Conformidade com Normas NBR.")
