# --- 🎨 ICONOGRAFIA TÁTICA MICHAEL MULERO ---
def inserir_icones_ra(tipo_risco):
    if tipo_risco == "criminal":
        with st.popover("👮 Ver Ocorrências (500m)"):
            st.error("🚨 2024: Invasão de Perímetro detectada.")
            st.write("**Impacto:** Risco de dano ao patrimônio.")
            st.caption("Investigação Davi: 5 anos retroativos.")
            
    elif tipo_risco == "climatico":
        with st.popover("⛈️ Histórico Climático"):
            st.warning("🌪️ 2023: Vendaval acima de 90km/h.")
            st.write("**Impacto:** Verificadas avarias no telhado.")
            st.caption("Fonte: Radares Meteorológicos PR.")

# --- APLICAÇÃO NAS PÁGINAS 10x10 ---
col_icones = st.columns(3)
with col_icones[0]:
    st.markdown("### 🛡️ Segurança")
    inserir_icones_ra("criminal")

with col_icones[1]:
    st.markdown("### 🌊 Ambiental")
    inserir_icones_ra("climatico")

with col_icones[2]:
    st.markdown("### ⚙️ Industrial")
    # Ícone para o Fluxo 3D
    with st.popover("🚒 Bombeiros"):
        st.success("✅ AVCB regularizado até 2027.")
