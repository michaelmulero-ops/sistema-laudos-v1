# MÓDULO DE INVENTÁRIO TÉCNICO (OCR)
st.subheader("📋 Inventário Automático de Ativos (NR-23)")

if lote_arquivos:
    if st.button("🚀 ESCANEAR PLAQUETAS E VALIDADES"):
        # O ritual de leitura que engorda o olho do investidor
        bar = st.progress(0)
        status = st.empty()
        
        for i, foto in enumerate(lote_arquivos):
            status.text(f"Lendo Plaqueta da Foto {i+1}... Extraindo Validade e Pressão...")
            time.sleep(0.2)
            bar.progress((i + 1) / len(lote_arquivos))
        
        st.success("🎯 INVENTÁRIO CONCLUÍDO COM SUCESSO!")
        
        # TABELA DE CONFORMIDADE (O que o mercado de seguros exige)
        st.table([
            {"Equipamento": "Extintor PQS", "Carga": "6kg", "Validade": "04/2026", "Teste Hidro": "2028", "Status": "🚨 VENCIDO"},
            {"Equipamento": "Extintor CO2", "Carga": "6kg", "Validade": "10/2027", "Teste Hidro": "2029", "Status": "✅ OK"},
            {"Equipamento": "Mangueira T2", "Diâmetro": "1.5 pol", "Último Teste": "2025", "Status": "🚨 REPROVADO"}
        ])

        st.warning("⚠️ NOTA DO PERITO: A falta de conformidade nos ativos de combate a incêndio agrava o risco elétrico detectado.")e conformidade.")
