# --- 🚀 MÓDULO: FLUXOGRAMA INTELIGENTE 3D ---
def gerar_fluxograma_3d(lista_equipamentos):
    st.subheader("📊 Fluxograma Inteligente de Processo (Visão 3D)")
    
    # Criamos uma representação visual do fluxo
    cols = st.columns(len(lista_equipamentos))
    
    for i, eq in enumerate(lista_equipamentos):
        with cols[i]:
            # Moldura do Equipamento no Fluxo
            st.markdown(f"**Etapa {i+1}**")
            st.image(eq['foto'], caption=eq['nome'], use_container_width=True)
            
            # Dados de Risco integrados ao quadro
            st.caption(f"⚙️ {eq['capacidade']}")
            if eq['risco'] == "Alto":
                st.error(f"⚠️ {eq['norma']}")
            else:
                st.success(f"✅ {eq['norma']}")
            
            # Seta de conexão (exceto no último)
            if i < len(lista_equipamentos) - 1:
                st.write("➡️")

# Exemplo de uso no seu monitor de 27"
equipamentos_teste = [
    {"nome": "Entrada Insumos", "foto": "https://via.placeholder.com/150", "capacidade": "Silo 50t", "norma": "NR-33", "risco": "Baixo"},
    {"nome": "Caldeira", "foto": "https://via.placeholder.com/150", "capacidade": "10 ton/h", "norma": "NR-13", "risco": "Alto"},
    {"nome": "Painel de Controle", "foto": "https://via.placeholder.com/150", "capacidade": "380V", "norma": "NR-10", "risco": "Baixo"}
]

if st.checkbox("Gerar Fluxograma Inteligente"):
    gerar_fluxograma_3d(equipamentos_teste)
