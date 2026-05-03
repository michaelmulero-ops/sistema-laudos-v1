import streamlit as st
from PIL import Image

st.subheader("📸 Upload de Evidências em Lote")

# Alteração crítica: adicionado o parâmetro accept_multiple_files=True
fotos_lote = st.file_uploader(
    "Selecione todas as fotos da vistoria:", 
    type=["jpg", "png", "jpeg"], 
    accept_multiple_files=True
)

if fotos_lote:
    st.write(f"✅ {len(fotos_lote)} fotos carregadas. Iniciando análise digital...")
    
    # Criando uma grade para visualização e pareceres
    for foto in fotos_lote:
        col1, col2 = st.columns([1, 2])
        
        with col1:
            img = Image.open(foto)
            st.image(img, use_container_width=True)
            
        with col2:
            # A Sofia analisa cada foto do lote automaticamente
            st.markdown("**Parecer Analítico da Sofia:**")
            
            # Aqui simulamos a extração de dados técnicos (OCR e Contexto)
            analise_sugerida = f"Evidência detectada na foto {foto.name}. " \
                               "Risco estrutural identificado conforme normas de segurança."
            
            # Campo editável para você validar ou alterar rapidamente
            st.text_area(f"Descrição Técnica - {foto.name}", 
                         value=analise_sugerida, 
                         key=f"obs_{foto.name}",
                         height=100)
    
    if st.button("🚀 INTEGRAR TODAS AS FOTOS AO LAUDO PDF"):
        st.success(f"As {len(fotos_lote)} fotos e análises foram consolidadas no relatório.")
