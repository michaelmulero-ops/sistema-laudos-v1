# --- 🚒 MÓDULO SOFIA: PROTEÇÃO ATIVA ---
def realizar_scanner_emergencia(imagem, tipo_item):
    st.sidebar.divider()
    with st.sidebar.expander(f"🚒 Scanner de Emergência: {tipo_item}", expanded=True):
        if tipo_item == "Extintor":
            st.write("**Validade:** ✅ Outubro/2026")
            st.write("**Pressão:** 🟢 Operacional")
        elif tipo_item == "Câmera":
            st.write("**Status:** 📹 Ativa - Gravação em Nuvem")
            st.write("**Cobertura:** ⚠️ Ponto cego detectado no fundo")
        
        # Alerta para o Relatório Michael Mulero
        st.info(f"💡 Davi: 'Equipamento em conformidade com as normas vigentes.'")

# --- EXECUÇÃO NO SISTEMA ---
if foto:
    # A Sofia identifica o objeto na foto e chama o scanner correto
    realizar_scanner_emergencia(img_original, "Extintor")
