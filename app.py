import pandas as pd
import plotly.express as px

# Simulando dados de vistorias recentes em Ibiporã/Londrina
data_mapa = {
    'lat': [-23.2694, -23.3103, -23.0519],
    'lon': [-51.0469, -51.1628, -50.2319],
    'Risco': ['Médio', 'Crítico', 'Baixo'],
    'Cidade': ['Ibiporã', 'Londrina', 'Andirá']
}
df_vistorias = pd.DataFrame(data_mapa)

st.divider()
st.subheader("📊 Painel de Inteligência Regional")

col1, col2 = st.columns([2, 1])

with col1:
    # Mapa de calor das inspeções
    fig = px.scatter_mapbox(df_vistorias, lat="lat", lon="lon", hover_name="Cidade", 
                            color="Risco", size_max=15, zoom=9, 
                            mapbox_style="carto-positron")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.write("📈 Resumo da Semana")
    st.metric("Vistorias Realizadas", "12")
    st.metric("Laudos Gerados", "12")
    st.success("✅ Backups 100% Sincronizados")
