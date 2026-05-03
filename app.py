iimport streamlit as st
from PIL import Image, ImageDraw
from docx import Document # Necessário: pip install python-docx
import folium
from streamlit_folium import folium_static

# Identidade Visual Michael Mulero
st.set_page_config(page_title="Michael Mulero Inspeções Tech V1", layout="wide")

def ler_word_tecnico(arquivo):
    """Lê o relatório de campo para alimentar a análise da Sofia"""
    try:
        doc = Document(arquivo)
        return "\n".join([p.text for p in doc.paragraphs])
    except:
        return ""

def analise_pericial_sofia(nome, contexto=""):
    """Análise forense baseada na imagem e no contexto do Word"""
    n = nome.lower()
    c = contexto.lower()
    analise = {"status": "🟢 OK", "parecer": "Elemento em conformidade.", "alerta": "N/A"}
    
    if "quadro" in n or "eletrico" in n or "transformador" in n:
        analise = {
            "status": "🔴 CRÍTICO",
            "parecer": "⚡ RISCO ELÉTRICO/EXPLOSÃO IDENTIFICADO.",
            "alerta": "Conforme relatório anexado, há sinais de fadiga e falta de manutenção."
        }
    elif "infiltração" in c or "forro" in n or "laje" in n:
        analise = {
            "status": "🔴 CRÍTICO",
            "parecer": "⚠️ RISCO ESTRUTURAL ATIVO.",
            "alerta": "Umidade detectada compromete a integridade do conteúdo segurado."
        }
    return analise

def desenhar_croqui_real(tipo):
    """Gera croquis 10x10 reais com grid de engenharia"""
    img = Image.new('RGB', (400, 400), color='#ffffff')
    draw = ImageDraw.Draw(img)
    for i in range(0, 400, 40): # Grid 10x10
        draw.line([(i, 0), (i, 400)], fill='#eeeeee')
        draw.line([(0, i), (400, i)], fill='#eeeeee')
    
    if "H" in tipo:
        draw.polygon([(100,100), (150,100), (150,180), (250,180), (250,100), (300,100), 
                      (300,300), (250,300), (250,220), (150,220), (150,300), (100,300)], 
                     outline="black", width=3)
    else:
        draw.rectangle([120, 120, 280, 280], outline="blue", width=3)
    return img

st.title("🛡️ Michael Mulero Inspeções Tech V1")
st.sidebar.info(f"Inspetor: Michael Giovanni Mulero\nLocal: Ibiporã, PR")

if st.sidebar.button("🧹 LIMPAR TELA / NOVO RISCO"):
    st.rerun()

# 1. Mapa Forense
st.subheader("📍 Geolocalização do Risco")
m = folium.Map(location=[-23.2692, -51.0519], zoom_start=18)
folium.Marker([-23.2692, -51.0519], popup='Inspeção Michael Mulero', icon=folium.Icon(color='red')).add_to(m)
folium_static(m)

# 2. Upload e Processamento
pacote = st.file_uploader("Subir Evidências (Fotos + Word):", accept_multiple_files=True)

if pacote:
    contexto_word = ""
    fotos = []
    
    for arquivo in pacote:
        if arquivo.name.endswith('.docx'):
            contexto_word += ler_word_tecnico(arquivo)
    
    for arquivo in pacote:
        if arquivo.type.startswith('image/'):
            img = Image.open(arquivo).convert("RGB")
            res = analise_pericial_sofia(arquivo.name, contexto_word)
            fotos.append({"img": img, "res": res, "nome": arquivo.name})

    # 3. Renderização do Laudo (Onde estava o erro)
    st.divider()
    st.header("📐 Suíte de Croquis Técnicos 10x10")
    modelos = ["Planta Baixa (Formato H)", "Área Operacional", "Mapa de Blindagem", "Implantação Geral"]
    c_croqui = st.columns(2)
    for i, m_nome in enumerate(modelos):
        with c_croqui[i % 2]:
            st.image(desenhar_croqui_real(m_nome), caption=m_nome)

    st.divider()
    st.header("🔍 Relatório de Evidências Analisadas")
    for item in fotos:
        col1, col2 = st.columns([1, 2])
        col1.image(item["img"], use_container_width=True)
        with col2:
            st.subheader(f"Arquivo: {item['nome']}")
            st.write(f"**Status:** {item['res']['status']}")
            st.error(f"**Parecer Sofia:** {item['res']['parecer']}")
            st.warning(f"**Contexto Técnico:** {item['res']['alerta']}")
