def aplicar_zoom_tecnico(img_input, coords, texto="ALERTA DE RISCO"):
    # Coordenadas do ponto crítico (x, y)
    x, y = coords
    
    # Cria a "Lupa" de 400x400 pixels
    box = (x-200, y-200, x+200, y+200)
    zoom = img_input.crop(box).resize((600, 600), Image.LANCZOS)
    
    # Adiciona moldura vermelha (Estilo Auditoria Forense)
    zoom = ImageOps.expand(zoom, border=15, fill='red')
    
    # Cria o layout lado a lado no dashboard
    col1, col2 = st.columns(2)
    with col1:
        st.image(img_input, caption="Visão Geral da Inspeção")
    with col2:
        st.error(f"**{texto}**")
        st.image(zoom, caption="Destaque Técnico da Anomalia")
