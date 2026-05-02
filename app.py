# --- 📐 MÓDULO DE ENGENHARIA: CROQUI TÉCNICO V1 ---
        st.divider()
        st.subheader("📐 Croqui de Engenharia - Delimitação e Setorização")
        
        # Container visual para simular a planta baixa de frente para a rua
        with st.container(border=True):
            st.markdown(f"🏠 **Perspectiva Frontal: Rua do Risco {cod_risco}**")
            
            # Divisão do Terreno em Colunas Técnicas
            c_vizin_l, c_centro, c_vizin_r = st.columns([1, 4, 1])
            
            with c_vizin_l:
                st.info("📦 Vizinho Esquerdo")
            
            with c_centro:
                # Delimitação da Área Amarela (Terreno do Cliente)
                st.markdown("<div style='border: 4px solid #FFD700; padding: 20px; background-color: #FFFDE7; text-align: center;'>"
                            "<b>🟡 ÁREA AMARELA - TERRENO CLIENTE (DEYCON)</b><br>"
                            "<small>Setorização de Risco Ativa</small></div>", unsafe_allow_html=True)
                
                # Setores Internos
                s1, s2, s3 = st.columns(3)
                s1.button("🏭 PRODUÇÃO", disabled=True, use_container_width=True)
                s2.button("📦 ESTOQUE", disabled=True, use_container_width=True)
                s3.button("❄️ CÂMARA FRIA", disabled=True, use_container_width=True)
            
            with c_vizin_r:
                st.info("🏢 Vizinho Direito")

        # 🚨 ALERTAS DE INFRAESTRUTURA NO CROQUI
        if extintores == "Não / Inexistente":
            st.error("📍 FALHA NO CROQUI: Ausência de pontos de combate sinalizados nos setores acima.")
