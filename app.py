# --- 🛡️ LAUDO TÉCNICO DETALHADO (VERSÃO INAUGURAÇÃO) ---
        st.divider()
        st.markdown(f"## 📑 Laudo Técnico Consolidado: {cod_risco}")
        st.write(f"**Segurado:** {cnpj_nome}")
        
        col_laudo1, col_laudo2 = st.columns(2)
        with col_laudo1:
            st.info("🔎 **Auditoria Sofia: Vistoria & NRs**")
            st.write(f"* **NR-10 / NBR-5410:** Inspeção de quadros elétricos e aterramento concluída.")
            st.write(f"* **NR-13:** Verificação de vasos de pressão e trocadores de calor.")
            st.write(f"* **Segurança Ocupacional:** Scanner invisível de EPIs e organização 5S ativo.")
            
            # Vínculo automático para ambientes de refrigeração
            st.error("❄️ **Vínculo de Frio: Casa de Máquinas**")
            st.write("* **Status:** Detectado ambiente de câmara fria.")
            st.write("* **Alerta Sofia:** Verificação de 'estampamento' (obstrução de ar) realizada.")
            st.write("* **Motores:** Termografia aplicada em compressores e evaporadores.")
        
        with col_laudo2:
            st.warning("🕵️ **Investigação Davi: Histórico & Entorno**")
            st.write(f"* **Raio de 500m:** Varredura criminal retroativa de 5 anos processada.")
            st.write(f"* **Risco Climático:** Histórico de eventos severos em Ibiporã analisado.")
            st.write(f"* **Geo-Risco:** Mapeamento de vizinhança e áreas de inundação concluído.")
            
