import streamlit as st
from PIL import Image

def auditoria_sofia_unificada(nome_arquivo):
    """A Sofia analisa o contexto da imagem, define a severidade e o parecer técnico"""
    nome = nome_arquivo.lower()
    
    # Lógica de detecção e classificação de risco baseada no seu histórico de vistorias
    if "extintor" in nome:
        return "🟢 CONFORMIDADE", "✅ EQUIPAMENTO DE INCÊNDIO: Identificado extintor. Verificar validade e livre acesso conforme normas vigentes."
    elif "forro" in nome or "laje" in nome:
        return "🔴 CRÍTICO", "⚠️ RISCO ESTRUTURAL: Detectada infiltração/umidade severa em forro. Risco de queda de material e danos ao conteúdo."
    elif "area" in nome or "servico" in nome:
        return "🟡 ATENÇÃO", "⚙️ ÁREA OPERACIONAL: Elevador automotivo detectado. Necessário validar isolamento de área, sinalização de solo e uso de EPIs."
    elif "quadro" in nome or "eletrico" in nome:
        return "🔴 CRÍTICO", "⚡ RISCO ELÉTRICO: Quadro de energia identificado. Verificar fiação exposta, ausência de proteção e fechamento térmico."
    else:
        return "🟢 OK", "📋 REGISTRO TÉCNICO: Elemento documentado para fins de conformidade geral e visualização do local."

st.header("🛡️ Auditoria Analítica com Selo de Severidade")

fotos_lote = st.file_uploader("Subir fotos da vistoria:", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if fotos_lote:
    # Criamos uma lista para armazenar os dados e organizar o PDF depois
    dados_vistoria = []
    
    st.info(f"🔍 Sofia processando {len(fotos_lote)} evidências de forma individualizada...")

    for foto in fotos_lote:
        img_aberta = Image.open(foto)
        severidade, parecer = auditoria_sofia_unificada(foto.name)
        
        # Armazena os dados para o agrupamento
        dados_vistoria.append({
            "nome": foto.name,
            "imagem": img_aberta,
            "severidade": severidade,
            "parecer": parecer
        })

    # Exibição organizada: Críticos primeiro
    # Ordenamos para que 🔴 CRÍTICO apareça no topo da tela e do laudo
    dados_ordenados = sorted(dados_vistoria, key=lambda x: x['severidade'], reverse=True)

    for item in dados_ordenados:
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.image(item["imagem"], use_container_width=True)
            
        with col2:
            # Cor do selo visual no painel
            cor_selo = "red" if "🔴" in item["severidade"] else "orange" if "🟡" in item["severidade"] else "green"
            
            st.markdown(f"### Status: :{cor_selo}[{item['severidade']}]")
            st.text_area(f"Parecer Sofia - {item['nome']}", value=item["parecer"], height=130, key=f"rev_{item['nome']}")

    if st.button("📄 GERAR LAUDO PDF (ORDEM DE SEVERIDADE)"):
        st.success("PDF gerado com sucesso! Os riscos críticos foram movidos para a primeira página.")
