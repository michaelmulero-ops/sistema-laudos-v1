import streamlit as st
import plotly.graph_objects as go
import folium
from streamlit_folium import folium_static

# Configuração de Elite - Michael Mulero
st.set_page_config(page_title="Michael Mulero Inspeções Tech V1", layout="wide")

def gerar_ar_3d(tipo):
    """Gera Realidade Aumentada com identificador único"""
    fig = go.Figure()
    if "H" in tipo:
        x, y = [1, 2, 2, 3, 3, 4, 4, 3, 3, 2, 2, 1, 1], [1, 1, 2, 2, 1, 1, 4, 4, 3, 3, 4, 4, 1]
        z, h = [0]*13, 1.5
    else:
        x, y, z, h = [1, 4, 4, 1, 1], [1, 1, 4, 4, 1], [0]*5, 1.2

    fig.add_trace(go.Mesh3d(x=x*2, y=y*2, z=z+[h]*len(z), color='lightblue', opacity=0.5))
    fig.update_layout(margin=dict(l=0, r=0, b=0, t=30), height=350)
    return fig

# --- Interface Principal ---
st.title("🛡️ Dashboard Mestre: Michael Mulero Inspeções Tech V1")
st.sidebar.markdown(f"**Inspetor:** Michael Giovanni Mulero\n**Local:** Ibiporã, PR")

tab1, tab2, tab3, tab4 = st.tabs(["📸 Evidências & Sofia", "📐 Realidade Aumentada (AR)", "🛤️ Entorno & Infraestrutura", "📄 Laudo Final"])

with tab1:
    st.subheader("⚙️ Engrenagem: Processamento de Fotos e Word")
    st.file_uploader("Arraste fotos e relatórios:", accept_multiple_files=True, key="upload_evidencias")

with tab2:
    st.subheader("🧊 Gaveta: Visualização 3D Volumétrica")
    col_ar1, col_ar2 = st.columns(2)
    with col_ar1:
        # A 'key' resolve o erro de DuplicateElementId
        st.plotly_chart(gerar_ar_3d("H"), use_container_width=True, key="grafico_ar_h")
    with col_ar2:
        st.plotly_chart(gerar_ar_3d("Bloco"), use_container_width=True, key="grafico_ar_bloco")

with tab3:
    st.subheader("🛰️ Gaveta: Mapa de Segurança e Infraestrutura")
    # Mapa de Ibiporã consolidado
    m = folium.Map(location=[-23.2692, -51.0519], zoom_start=16)
    folium.Marker([-23.2692, -51.0519], popup="Local do Risco", icon=folium.Icon(color='red')).add_to(m)
    folium_static(m)

with tab4:
    st.subheader("📝 Gaveta: Parecer e Emissão")
    if st.button("GERAR LAUDO FINAL"):
        st.success("Laudo Pericial Consolidado com Sucesso!")
