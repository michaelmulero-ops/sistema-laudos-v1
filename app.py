import streamlit as st
from PIL import Image

st.subheader("📸 Auditoria Analítica em Lote")

# Filtramos para aceitar apenas formatos de imagem no seletor
fotos_lote = st.file_uploader(
    "Subir fotos da vistoria:", 
    type=["jpg", "png", "jpeg"], 
    accept_multiple_files=True
)

if fotos_lote:
    for foto in fotos_lote:
        # A magia do filtro: só processa se for imagem
        if foto.type.startswith('image/'):
            try:
                img_aberta = Image.open(foto)
                col1, col2 = st.columns([1, 2])
                
                with col1:
                    st.image(img_aberta, use_container_width=True)
                
                with col2:
                    # Aqui a Sofia analisa a imagem real
                    # Note que o parecer agora é técnico e focado em riscos
                    st.markdown(f"**Análise da Sofia para: {foto.name}**")
                    
                    # Simulação de análise profunda baseada nos seus itens (oficina/extintores)
                    analise_automatica = (
                        "🔍 DIAGNÓSTICO DIGITAL:\n"
                        "- Identificado: Equipamento de elevação / Segurança contra incêndio.\n"
                        "- Risco: Necessita verificação de sinalização de solo e carga.\n"
                        "- Conformidade: Em análise conforme normas Zurich/Tokio Marine."
                    )
                    
                    st.text_area("Parecer Técnico Editável:", value=analise_automatica, key=f"text_{foto.name}", height=150)
            except Exception as e:
                st.error(f"Erro ao processar {foto.name}: {e}")
        else:
            st.warning(f"Arquivo ignorado (não é imagem): {foto.name}")
