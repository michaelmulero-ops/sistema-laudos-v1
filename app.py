# --- 🛡️ ANÁLISE TÉCNICA ESTRUTURAL ---
        st.error("🚨 ALERTAS DE ENGENHARIA DE RISCO DETECTADOS")
        
        col_eng1, col_eng2 = st.columns(2)
        with col_eng1:
            st.warning("🏗️ **Estrutura e Vedações**")
            st.write("❌ **ISOPAINEL:** Detectada presença de isopainel em divisórias internas. Alto potencial de propagação vertical/horizontal.")
            st.write("❌ **SETORIZAÇÃO:** Ausência de paredes corta-fogo entre áreas administrativas e operacionais.")
            
        with col_info2:
            st.warning("🔥 **Combate a Incêndio**")
            st.write("❌ **HIDRANTES:** Proteção restrita à área externa. Vulnerabilidade total do núcleo do depósito.")
            st.write("❌ **SINALIZAÇÃO:** Ausência de demarcação de solo e placas fotoluminescentes.")

        # --- 📐 RECOMENDAÇÕES DE IMPACTO (O QUE O CLIENTE DEVE FAZER) ---
        st.subheader("📋 Recomendações Prioritárias")
        recs_senhor = [
            "1. Substituir divisórias de isopainel por materiais incombustíveis ou instalar sprinkler específico.",
            "2. Estender a rede de hidrantes para o interior do pavilhão, garantindo cobertura total.",
            "3. Isolar a área de carga de baterias com barreira física de alvenaria.",
            "4. Implementar sinalização de emergência conforme NBR-13434."
        ]
        for r in recs_senhor: st.write(r)
