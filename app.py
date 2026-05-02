# --- 📐 MÓDULO DE CROQUIS MICHAEL MULERO ---
        st.divider()
        st.subheader("📐 Croquis Técnicos e Mapeamento Setorial")
        
        col_croqui1, col_croqui2 = st.columns(2)
        
        with col_croqui1:
            st.info("🖼️ **Perspectiva: De Frente à Rua**")
            # Simulação do Croqui 2D/3D (Página 02 do Laudo)
            st.code("""
            _________________________________________
            |           TERRENO VIZINHO             |
            |_______________________________________|
            |   [ ÁREA AMARELA - TERRENO CLIENTE ]  |
            |       (Delimitado por Sofia)          |
            |_______________________________________|
            | [FACHADA] [PORTARIA] [ESTACIONAMENTO] |
            |_______________________________________|
                        [ RUA PRINCIPAL ]
            """, language="text")
            st.caption("Visualização técnica priorizando o acesso principal (Não utiliza Norte Magnético).")

        with col_croqui2:
            st.warning("📍 **Georeferenciamento e Geo-Risco**")
            # Representação do mapeamento de raio de 500m do Davi
            st.write(f"* **Localização:** Ibiporã - PR")
            st.write("* **Mapeamento:** Raio de 500m processado para riscos criminais.")
            st.write("* **Satélite:** Vínculo com coordenadas GPS das fotos concluído.")
            
        # --- 🛡️ EXIBIÇÃO DO LAUDO CONSOLIDADO (NRs e Parecer) ---
        st.divider()
        st.markdown(f"## 📑 Laudo Técnico Consolidado: {cod_risco}")
        
        if observacoes:
            st.warning(f"**PARECER DO INSPETOR SÊNIOR:** {observacoes}")
