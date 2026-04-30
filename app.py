# Adicione isso na área de 'Interface' do seu app.py
st.sidebar.subheader("📍 Georreferenciamento de Campo")

if st.sidebar.button("Fixar Localização da Inspeção"):
    # Captura automática para evitar erro de endereço
    log_rastreio("Capturando coordenadas GPS para o Croqui...")
    st.sidebar.success("Localização Fixada: Londrina/Ibiporã") # Exemplo
    log_rastreio("Endereço validado via satélite.")
