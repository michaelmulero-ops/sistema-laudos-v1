# --- 📑 3. CHECKLIST DE CONFORMIDADE (RIGOR MICHAEL MULERO) ---
st.subheader("🛡️ Verificação de Proteção e Setorização")
col_check1, col_check2 = st.columns(2)

with col_info1:
    extintores = st.radio("Sinalização de Extintores/Hidrantes Detectada?", ("Sim", "Não / Inexistente"), index=1)
    setorizacao = st.radio("Setorização de Risco Definida?", ("Sim", "Não / Áreas Misturadas"), index=1)

with col_info2:
    itbi = st.checkbox("Possui AVCB/CLCB Vigente?", value=False)
    estampamento = st.checkbox("Alerta de Estampamento em Câmaras?", value=True)

st.divider()

# --- 🚀 COMANDO DE AUDITORIA COM ALERTA DE FALHAS ---
if uploads:
    if st.button("🚀 PROCESSAR AUDITORIA COMPLETA", use_container_width=True):
        # ... (barra de progresso da Sofia)
        
        st.error("⚠️ FALHAS DE SEGURANÇA DETECTADAS")
        if extintores == "Não / Inexistente":
            st.write("❌ **CRÍTICO:** Ausência de sinalização fotoluminescente e marcação de solo para equipamentos de combate.")
        if setorizacao == "Não / Áreas Misturadas":
            st.write("❌ **ALERTA:** Ausência de setorização física. Risco de propagação rápida de sinistro entre áreas de estoque e operação.")
        
        # O Laudo agora sai com o Parecer Sênior Automático baseado nas falhas
        if extintores == "Não / Inexistente" or setorizacao == "Não / Áreas Misturadas":
            status_risco = "⚠️ RISCO AGRAVADO / RECOMENDAÇÕES URGENTES"
        else:
            status_risco = "✅ RISCO CONTROLADO"

        st.divider()
        st.markdown(f"## 📑 Laudo Consolidado: {cod_risco}")
        st.subheader(f"Status: {status_risco}")
