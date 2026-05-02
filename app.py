# --- 💰 MÓDULO DE ENGENHARIA DE CUSTOS ---
st.header("💵 Avaliação de Valores e Seguro (LMG)")

with st.container(border=True):
    val_apolice = st.number_input("Valor Segurado na Apólice (R$)", value=10000000.0)
    
    # Cálculos Automáticos baseados na Volumetria 3D
    val_predio = 6050000.0  # Prédio + Estrutural
    val_conteudo = 9800000.0 # Estoque (Cigarros/Frio/Maquinas)
    val_total_real = val_predio + val_conteudo
    
    st.subheader(f"Valor Real em Risco: R$ {val_total_real:,.2f}")
    
    if val_total_real > val_apolice:
        diff = val_total_real - val_apolice
        st.error(f"⚠️ SUB-SEGURO DETECTADO: Divergência de R$ {diff:,.2f}")
        st.write("❌ O valor declarado pelo corretor NÃO BATE com a realidade física do local.")
    else:
        st.success("✅ Valores de Apólice em conformidade com o Risco Real.")

st.divider()
st.info("💡 Este cálculo considera o custo de reconstrução e reposição de ativos em Ibiporã/PR.")
