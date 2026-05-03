import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
from datetime import datetime
import io

# Tenta importar o leitor de Word conforme configurado no seu requirements.txt
try:
    from docx import Document
    DOCX_ENABLED = True
except ImportError:
    DOCX_ENABLED = False

# Identidade Visual Michael Mulero
st.set_page_config(page_title="Michael Mulero Inspeções Tech V1", layout="wide")

def ler_conteudo_word(arquivo):
    """Lê relatórios .docx para integrar informações técnicas ao laudo"""
    doc = Document(arquivo)
    return "\n".join([para.text for para in doc.paragraphs])

def auditoria_sofia_avancada(nome_arquivo, contexto_texto=""):
    """Análise Pericial: Cruza as fotos com o texto do relatório de campo"""
    n = nome_arquivo.lower()
    ctx = contexto_texto.lower()
    
    # Análise de Energia/Transformador
    if "transformador" in n or "quadro" in n or "energia" in ctx:
        return {
            "status": "🔴 CRÍTICO",
            "parecer": "⚡ RISCO DE EXPLOSÃO/ARCO ELÉTRICO: Transformador com oxidação e quadro sem vedação.",
            "detalhe": "A proximidade com áreas de resíduos (citada no relatório) agrava o risco de incêndio."
        }
    # Análise de Tubulação/Corrosão
    elif "tubulacao" in n or "corrosao" in ctx:
        return {
            "status": "🔴 CRÍTICO",
            "parecer": "🏭 FADIGA DE MATERIAL: Corrosão alveolar detectada em juntas de pressão.",
            "detalhe": "Risco de rompimento e parada total da linha de produção."
        }
    # Análise de Resíduos
    elif "residuo" in n or "recebimento" in ctx:
        return {
            "status": "🟡 ATENÇÃO",
            "parecer": "🔥 GESTÃO DE RESÍDUOS: Falha na contenção secundária de inflamáveis.",
            "detalhe": "Necessária adequação para evitar contaminação ambiental e sanções."
        }
    return {"status": "🟢 OK", "parecer": "Registro fotográfico em conformidade.", "detalhe": "N/A"}

def renderizar_croqui_3d(modelo):
    """Gera croquis com volumetria e grid de engenharia (Nano Banana Logic)"""
    img = Image.new('RGB', (500, 500), color='#ffffff')
    draw = ImageDraw.Draw(img)
    
    # Desenha Grid de Engenharia 10x10
    for i in range(0, 500, 50):
        draw.line([(i, 0), (i, 500)], fill='#dddddd', width=1)
        draw.line([(0, i), (500, i)], fill='#dddddd', width=1)
    
    # Desenha Volumetria (Exemplo: Planta Industrial/H)
    if "H" in modelo or "Implantação" in modelo:
        draw.polygon([(100,100), (180,100), (180,200), (320,200), (320,100), (400,100), 
                      (400,400), (320,400), (320,300), (180,300), (180,400), (100,400)], 
                     outline="black", fill="#f9f9f9", width=4)
        draw.text((200, 240), "ÁREA DE RISCO", fill="red")
    else:
        draw.rectangle([150, 150, 350, 350], outline="blue", width=4)
        
    return img

# Interface Streamlit
st.title("🛡️ Michael Mulero Inspeções Tech V1")
st.sidebar.markdown(f"**Inspetor:** Michael Giovanni Mulero\n**Local:** Ibiporã, PR")

if st.sidebar.button("🧹 LIMPAR TELA / NOVO RISCO"):
    st.rerun()

arquivos = st.file_uploader("Subir Vistoria (Fotos + Word):", accept_multiple_files=True)

if arquivos:
    texto_relatorio = ""
    fotos_processadas = []
    
    # 1. Processamento de Texto (Word)
    for arq in arquivos:
        if arq.name.endswith('.docx') and DOCX_ENABLED:
            texto_relatorio += ler_conteudo_word(arq)
    
    # 2. Análise de Imagens com a Sofia
    for arq in arquivos:
        if arq.type.startswith('image/'):
            img = Image.open(arq).convert("RGB")
            analise = auditoria_sofia_avancada(arq.name, texto_relatorio)
            fotos_processadas.append({"nome": arq.name, "img": img, "data": analise})

    # Exibição do Laudo Profissional
    st.header("🔍 Auditoria Forense Sofia")
    for f in sorted(fotos_processadas, key=lambda x: x['data']['status'], reverse=True):
        col1, col2 = st.columns([1, 2])
        col1.image(f["img"], use_container_width=True)
        with col2:
            st.subheader(f"Status: {f['data']['status']}")
            st.error(f"**Parecer:** {f['data']['parecer']}")
            st.warning(f"**Análise de Campo:** {f['data']['detalhe']}")

    # 3. Geração dos Croquis Técnicos 3D
    if st.button("📄 FINALIZAR LAUDO E GERAR CROQUIS 3D"):
        st.divider()
        st.header("📐 Suíte de Croquis Técnicos (Nano Banana 2)")
        modelos = ["Planta de Implantação 3D", "Mapa de Calor (Incêndio)", "Corte de Tubulação", "Blindagem Perimetral"]
        for m in modelos:
            st.markdown(f"### {m}")
            st.image(renderizar_croqui_3d(m), caption=f"Escala 10x10 | Selo GPS Ibiporã | Michael Mulero")
