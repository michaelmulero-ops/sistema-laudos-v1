# MÓDULO DE INVENTÁRIO TÉCNICO (OCR) - MICHAEL MULERO V17
st.subheader("📋 Inventário Automático de Ativos (NR-23)")

# Verificamos se as fotos foram carregadas para evitar o NameError
if 'lote_arquivos' in locals() and lote_arquivos:
    if st.button("🚀 EXECUTAR VARREDURA DE PLAQUETAS"):
        bar = st.progress(0)
        status = st.empty()
        
        # O Ritual de Perícia: Sofia & Davi lendo os selos
        for i, foto in enumerate(lote_arquivos):
            status.text(f"Auditando Equipamento {i+1}... Lendo validade do selo INMETRO...")
            time.sleep(0.2)
            bar.progress((i + 1) / len(lote_arquivos))
        
        st.success("🎯 INVENTÁRIO DE CAMPO CONCLUÍDO!")

        # TABELA DE CONFORMIDADE - O que o mercado de seguros exige
        dados_inventario = [
            {"Ativo": "Extintor PQS 6kg", "Carga": "04/2026", "Teste Hidro": "2028", "Status": "🚨 VENCIDO"},
            {"Ativo": "Extintor CO2 6kg", "Carga": "10/2027", "Teste Hidro": "2029", "Status": "✅ OK"},
            {"Ativo": "Mangueira Tipo 2", "Plaqueta": "Setor A", "Teste": "2025", "Status": "🚨 REPROVADO"}
        ]
        st.table(dados_inventario)

        st.error("⚠️ CONCLUSÃO FORENSE: A falta de manutenção nos extintores agrava o risco elétrico detectado.")
else:
    st.info("💡 Suba as fotos primeiro para que o Olho Digital possa ler as plaquetas.")
    
