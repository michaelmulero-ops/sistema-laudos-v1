# --- 🛡️ MOTOR DE AUDITORIA CRÍTICA ---
if uploads:
    if st.button("🚀 PROCESSAR AUDITORIA COMPLETA", use_container_width=True):
        # Sofia e Davi iniciam a varredura técnica
        bar = st.progress(0)
        for i, _ in enumerate(uploads):
            time.sleep(0.01)
            bar.progress((i + 1) / len(uploads))
        
        st.divider()
        
        # VERIFICAÇÃO DE PENDÊNCIAS GRAVES
        if extintores == "Não / Inexistente" or setorizacao == "Não / Áreas Misturadas":
            st.error("🚨 FALHAS CRÍTICAS DE SEGURANÇA DETECTADAS")
            st.markdown("### 📋 Recomendações Obrigatórias para o Laudo:")
            
            # As 10 Recomendações Padrão Michael Mulero
            recomendacoes = [
                "1. Executar marcação de solo (quadrado vermelho/borda amarela) em todos os extintores/hidrantes.",
                "2. Instalar sinalização fotoluminescente superior conforme NPT-020.",
                "3. Fixar Mapa de Riscos visível em cada entrada setorial.",
                "4. Certificar Brigada de Incêndio com 100% do operacional.",
                "5. Estabelecer cronograma mensal de inspeção de lacres e carga.",
                "6. Delimitar áreas de estoque/expedição com faixas amarelas no piso (Organização 5S).",
                "7. Isolar riscos especiais (Carga de baterias/Inflamáveis) com barreiras físicas.",
                "8. Identificar quadros elétricos (NR-10) por setor alimentado.",
                "9. Garantir rotas de fuga desobstruídas com largura mínima de 1,20m.",
                "10. Implementar retirada diária de descartes combustíveis (papelão/plástico)."
            ]
            for rec in recomendacoes:
                st.write(rec)
            
            status_final = "⚠️ RISCO AGRAVADO - NECESSITA ADEQUAÇÃO"
        else:
            st.success("✅ CONFORMIDADE TÉCNICA DETECTADA")
            status_final = "✅ RISCO CONTROLADO"

        # EXIBIÇÃO DO LAUDO FINAL NA TELA DO MONITOR DE 27"
        st.divider()
        st.header(f"📑 Status Final do Risco: {status_final}")
        if observacoes:
            st.warning(f"**PARECER DO INSPETOR SÊNIOR:** {observacoes}")
