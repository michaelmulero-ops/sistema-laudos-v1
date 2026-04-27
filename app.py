# MÓDULO DE SENSIBILIDADE DE RISCO (Michael Mulero V17)
st.subheader("🎯 Definição de Perfil de Inspeção")

perfil_risco = st.selectbox("Selecione o Porte do Risco:", ["Comércio Local (Pequeno)", "Empresa de Médio Porte", "Grande Indústria/Cooperativa"])

if perfil_risco == "Comércio Local (Pequeno)":
    st.info("💡 Modo Empático Ativo: Foco em Prevenção Básica e Risco Moral.")
    # Checklist reduzido, mas rigoroso no básico (fiação, extintor, estrutura)
elif perfil_risco == "Grande Indústria/Cooperativa":
    st.warning("🚨 Modo Auditoria Total: Exigência Máxima de Compliance e Engenharia.")
    # Libera todos os campos de NR-10, NR-12, SPDA e AVCB completo
