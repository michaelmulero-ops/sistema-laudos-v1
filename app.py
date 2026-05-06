import streamlit as st

st.title("Gerador de Laudos - Michael Mulero Inspeções")

with st.sidebar:
    st.header("Dados do Risco")
    endereco = st.text_input("Endereço Completo", "Rua Alexander Graham Bell, 255")
    lmi = st.number_input("Importância Segurada (R$)", value=107000000.0)
    processar = st.button("Gerar Infográficos")

if processar:
    # Aqui o sistema chama a função de imagem e atualiza os dados
    img_path = gerar_infografico_localizacao(endereco, "Londrina/PR", "temp_infografico.png")
    st.image(img_path, caption="Infográfico de Localização Gerado")
    
    with open(img_path, "rb") as file:
        st.download_button("Baixar para o Relatório", file, "infografico_final.png")
