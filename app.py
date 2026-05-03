# Verifique se 'st' foi importado corretamente no topo do arquivo
import streamlit as st

# ... seu código anterior ...

# Linha que causou o erro no seu print
st.markdown("---") # Usar markdown como alternativa segura ao divider
st.subheader("📊 Painel de Inteligência Regional")

# Resto do código do Dashboard...
