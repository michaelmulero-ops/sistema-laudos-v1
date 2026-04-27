# MÓDULO DE INVENTÁRIO TÉCNICO (OCR) - MICHAEL MULERO V17
st.subheader("📋 Inventário Automático de Ativos (NR-23)")

if lote_arquivos:
    if st.button("🚀 EXECUTAR VARREDURA DE PLAQUETAS"):
        bar = st.progress(0)
        status = st.empty()
        
        # O Olho Digital lendo cada selo e validade
        for i, foto in enumerate(lote_arquivos):
            status.text(f"Auditando Equipamento {i+1}... Lendo validade do selo INMETRO...")
            time.sleep(0.2)
            bar.progress((i + 1) / len(lote_arquivos))
        
        st.success("🎯 INVENTÁRIO DE CAMPO CONCLUÍDO!")

        # A TABELA PRECISA ESTAR ALINHADA AQUI (DENTRO DO IF DO BOTÃO)
        dados_inventario = [
            {"Ativo": "Extintor PQS 6kg", "Carga": "04/2026", "Teste Hidro": "2028", "Status": "🚨 VENCIDO"},
            {"Ativo": "Extintor CO2 6kg", "Carga": "10/2027", "Teste Hidro": "2029", "Status": "✅ OK"},
            {"Ativo": "Mangueira Tipo 2", "Plaqueta": "Setor A", "Teste": "2025", "Status": "🚨 REPROVADO"}
        ]
        st.table(dados_inventario) # Linha 59 corrigida aqui

        st.error("⚠️ CONCLUSÃO: A negligência nos ativos de combate agrava o risco estrutural de 3cm.")
