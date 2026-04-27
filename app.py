import streamlit as st

# Título do Portal
st.title("🚀 Portal de Pedidos - Michael Mulero Inspeções")
st.subheader("Entrada de Dados para Prestadoras")

# Formulário para a Prestadora preencher
with st.form("novo_pedido"):
    prestadora = st.text_input("Nome da Prestadora")
    segurado = st.text_input("Nome do Segurado/Condomínio")
    endereco = st.text_input("Endereço Completo")
    tipo = st.selectbox("Tipo de Risco", ["Condomínio", "Comércio", "Industrial"])
    
    # Botão que gera o link
    enviar = st.form_submit_button("Gerar Pedido para Inspetor")

if enviar:
    st.success(f"✅ Pedido de {segurado} registrado!")
    st.info("Agora é só mandar o link para o seu inspetor de campo.")
