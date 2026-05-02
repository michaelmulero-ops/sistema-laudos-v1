# --- 🦅 MOTOR DE GERAÇÃO MICHAEL MULERO V1.0 ---
st.subheader("📐 Croqui Técnico e Mapeamento de Vulnerabilidades")

with st.container(border=True):
    st.markdown("### 🏠 Perspectiva: De Frente à Rua")
    
    # Renderização da Área Amarela com foco em Isopainel e Hidrantes
    st.error("❌ ALERTA ESTRUTURAL: Cobertura em Isopainel detectada (Alta Combustibilidade)")
    
    c1, c2, c3 = st.columns([1, 4, 1])
    with c1: st.info("Vizinho")
    with c2:
        st.warning("🟡 ÁREA AMARELA - DEYCON COMERCIO")
        st.write("🔥 **Núcleo Vulnerável:** Distância dos Hidrantes Externos > 30m")
        st.write("🏗️ **Estrutura:** Metal Exposto / Telhado Isopainel")
    with c3: st.info("Vizinho")
    
    st.markdown("<p style='text-align: center;'>[ RUA PRINCIPAL ]</p>", unsafe_allow_html=True)
