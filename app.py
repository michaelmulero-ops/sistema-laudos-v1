# MÓDULO DE CAPTURA COM ANÁLISE AUTOMÁTICA
st.subheader("📸 Captura de Evidências (Lote de Fotos e Vídeos)")
lote_arquivos = st.file_uploader("Arraste os arquivos aqui", accept_multiple_files=True, key="v17_upload")

if lote_arquivos:
    st.success(f"✅ {len(lote_arquivos)} arquivos prontos para o Dossiê.")
    
    # BOTÃO PARA Sofia/Davi ANALISAREM O RISCO PESADO
    if st.button("🚀 INICIAR AUDITORIA FORENSE (SOFIA & DAVI)"):
        with st.spinner("Analisando vestígios de sinistros e anomalias térmicas..."):
            # Aqui simulamos a inteligência agindo sobre as 55 fotos
            st.error("🚨 ALERTA DE RISCO PESADO DETECTADO!")
            st.markdown("""
            - **Sofia:** Identificado desvio de finalidade na área fabril.
            - **Davi:** Termografia aponta superaquecimento crítico em 3 painéis.
            - **Veredito:** Sugerida recusa imediata para Allianz.
            """)
            st.session_state.analise_concluida = True
        with col2:
            st.warning("👷 INFRAÇÃO NR-6: Funcionário sem luvas de isolamento.")
