# Função para gerar o Croqui 1: Mapeamento Regional e Blindagem Perimetral
def gerar_mapa_blindagem():
    # Coordenadas base da unidade em Apucarana/região
    # O sistema usará o georreferenciamento para plotar os 9 pontos de SPDA
    m = folium.Map(location=[-23.5505, -51.4614], zoom_start=18, tiles='OpenStreetMap')
    
    # Marcação da área de Inflamáveis (D-Limonene UN 2319)
    folium.Marker(
        [-23.5506, -51.4615], 
        popup="Setor de Inflamáveis - Blindagem Reforçada",
        icon=folium.Icon(color='red', icon='fire')
    ).add_to(m)

    # Marcação dos 9 Pontos de Descida do SPDA
    for i in range(9):
        folium.CircleMarker(
            location=[-23.5504 + (i*0.00005), -51.4613],
            radius=5, color='blue', fill=True, popup=f"Ponto SPDA {i+1}"
        ).add_to(m)
        
    return m

# No corpo do Streamlit, adicione a visualização:
st.subheader("🗺️ Visualização da Blindagem e Georreferenciamento")
mapa = gerar_mapa_blindagem()
st_folium(mapa, width=700, height=450)
