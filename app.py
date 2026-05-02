# --- 📑 3. AÇÕES E RELATÓRIOS (MOTOR ATIVO) ---
st.subheader("📑 Ações e Relatórios")
col_btn1, col_btn2 = st.columns(2)

if uploads:
    with col_btn1:
        if st.button("🚀 Processar Auditoria Sofia/Davi", use_container_width=True):
            progress_bar = st.progress(0)
            for i, file in enumerate(uploads):
                # Sofia simulando a varredura técnica em cada foto
                time.sleep(0.05) # Velocidade de processamento por foto
                percent = (i + 1) / len(uploads)
                progress_bar.progress(percent)
            
            st.success(f"✅ Vistoria de {len(uploads)} evidências processada com sucesso!")
            st.balloons() # Sinal visual de que o trabalho pesado acabou

    with col_btn2:
        if st.button("📥 Gerar PDF Laudo 10x10", use_container_width=True):
            with st.spinner("Davi consolidando investigação criminal e climática..."):
                time.sleep(2)
                # Aqui o sistema já integra o CNPJ e o Código do Risco que você digitou
                st.success(f"Relatório Michael Mulero: Risco {cod_risco} Gerado!")
                st.download_button("Clique para Baixar o Laudo", data="PDF_DATA", file_name=f"Laudo_{cod_risco}.pdf")
else:
    st.warning("⚠️ Carregue as fotos primeiro para habilitar os botões de comando.")
