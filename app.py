# Adicione isso logo abaixo do st.success no seu app.py
st.subheader("📋 Relatório Gerado")
st.write(f"**Análise para:** {processo_operacional}") # Aqui aparece o texto do mini mercado

# Para mostrar as fotos que você subiu
if uploaded_files:
    st.subheader("📸 Evidências Fotográficas")
    for foto in uploaded_files:
        st.image(foto, caption=foto.name, use_column_width=True)
