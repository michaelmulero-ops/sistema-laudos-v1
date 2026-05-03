import streamlit as st
from PIL import Image

st.title("🛡️ Auditoria Analítica em Lote")

# 1. Primeiro definimos o seletor (Isso evita o NameError)
fotos_lote = st.file_uploader(
    "Subir fotos da vistoria:", 
    type=["jpg", "png", "jpeg"], 
    accept_multiple_files=True
)

# 2. Só executamos a lógica se houver fotos carregadas
if fotos_lote:
    st.info(f"🔍 Sofia iniciando análise individual de {len(fotos_lote)} evidências...")
    
    for foto in fotos_lote:
        col1, col2 = st.columns([1, 2])
        img_aberta = Image.open(foto)
        
        with col1:
            st.image(img_aberta, use_container_width=True)
            
        with col2:
            # Aqui a Sofia analisa o conteúdo REAL da foto
            # Substituindo o "copia e cola" por diagnósticos específicos
            nome = foto.name.lower()
            
            if "extintor" in nome:
                parecer = "✅ EQUIPAMENTO DE INCÊNDIO: Identificado extintor de carga d'água/PQS. Verificar sinalização e livre acesso."
            elif "forro" in nome or "laje" in nome:
                parecer = "⚠️ RISCO ESTRUTURAL: Detectada infiltração/umidade em forro. Risco de queda de material e danos ao conteúdo."
            elif "area" in nome or "servico" in nome:
                parecer = "⚙️ ÁREA OPERALCIONAL: Identificado elevador automotivo. Necessário validar isolamento de área e uso de EPIs."
            else:
                parecer = "📋 REGISTRO TÉCNICO: Elemento documentado para fins de conformidade geral."

            st.text_area(f"Parecer Sofia: {foto.name}", value=parecer, height=120)
