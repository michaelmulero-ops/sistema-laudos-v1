# --- NOVO CAMPO PARA SUBIR FOTOS DA GALERIA/PC ---
st.subheader("Subir Fotos da Galeria")
arquivos_subidos = st.file_uploader(
    "Selecione as fotos da inspeção (Híbrido)", 
    type=["jpg", "png", "jpeg"], 
    accept_multiple_files=True
)

if arquivos_subidos:
    for arquivo in arquivos_subidos:
        img_galeria = Image.open(arquivo)
        img_com_scan_galeria = apply_scanner_hud(img_galeria)
        
        # Salva na fila para sincronização automática
        nome_arq_galeria = f"galeria_{int(time.time())}_{arquivo.name}"
        caminho_galeria = os.path.join(PENDING_DIR, nome_arq_galeria)
        img_com_scan_galeria.save(caminho_galeria)
        
        st.image(img_com_scan_galeria, caption=f"Escaneando: {arquivo.name}", width=300)

st.divider() # Separa a Galeria da Câmera ao vivo)
if arquivos_na_fila:
    st.info(f"Existem {len(arquivos_na_fila)} inspeções aguardando sinal de Wi-Fi.")
