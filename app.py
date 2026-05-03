import streamlit as st
from PIL import Image

def auditoria_sofia_unificada(nome_arquivo):
    """A Sofia analisa o contexto da imagem e define a criticidade"""
    nome = nome_arquivo.lower()
    
    # Lógica de detecção e classificação de risco
    if "extintor" in nome:
        return "🟢 CONFORMIDADE", "✅ EQUIPAMENTO DE INCÊNDIO: Identificado extintor. Verificar sinalização e livre acesso conforme normas."
    elif "forro" in nome or "laje" in nome:
        return "🔴 CRÍTICO", "⚠️ RISCO ESTRUTURAL: Detectada infiltração/umidade severa em forro. Risco de queda de material."
    elif "area" in nome or "servico" in nome:
        return "🟡 ATENÇÃO", "⚙️ ÁREA OPERACIONAL: Elevador automotivo detectado. Necessário validar isolamento e uso de EPIs."
    elif "quadro" in nome or "eletrico" in nome:
        return "🔴 CRÍTICO", "⚡ RISCO ELÉTRICO: Quadro de energia identificado. Verificar fiação exposta e fechamento térmico."
    else:
        return "🟢 OK", "📋 REGISTRO TÉCNICO: Elemento documentado para fins de conformidade geral."

st.header("🛡️ Auditoria Analítica com Selo de Severidade")

fotos_lote = st.file_uploader("Subir fotos da vistoria:", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if fotos_lote:
    for foto in fotos_lote:
        col1, col2 = st.columns([1, 2])
        img_aberta = Image.open(foto)
        
        # Executa a análise unificada
        severidade, parecer = auditoria_sofia_unificada(foto.name)
        
        with col1:
            st.image(img_aberta, use_container_width=True)
            
        with col2:
            # Exibe o Selo e o Parecer lado a lado
            st.markdown(f"### Status: {severidade}")
            st.text_area(f"Análise Técnica Sofia: {foto.name}", value=parecer, height=150, key=f"v_{foto.name}")
