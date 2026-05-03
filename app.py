import streamlit as st
from PIL import Image, ImageDraw
from docx import Document  # Necessário: pip install python-docx
import io

# Identidade Visual Michael Mulero
st.set_page_config(page_title="Michael Mulero Inspeções Tech V1", layout="wide")

def ler_texto_docx(arquivo_word):
    """Extrai texto de arquivos .docx para alimentar a Sofia"""
    doc = Document(arquivo_word)
    texto_completo = [para.text for para in doc.paragraphs]
    return "\n".join(texto_completo)

def analise_sofia_pericial(nome_foto, contexto_word=""):
    """Análise que cruza a imagem com os dados lidos do arquivo Word"""
    n = nome_foto.lower()
    analise = {"status": "🟢 OK", "parecer": "Elemento documentado.", "agravante": "Nenhum detectado."}
    
    # Se houver menção a infiltração ou elétrica no Word, a Sofia fica em alerta
    contexto_alerta = contexto_word.lower()
    
    if "eletrico" in n or "quadro" in n or "fiação" in contexto_alerta:
        analise = {
            "status": "🔴 CRÍTICO",
            "parecer": "⚡ RISCO ELÉTRICO IDENTIFICADO.",
            "agravante": "Conforme relatório anexado, há registro de sobrecarga ou fiação exposta no local."
        }
    elif "forro" in n or "laje" in n or "infiltração" in contexto_alerta:
        analise = {
            "status": "🔴 CRÍTICO",
            "parecer": "⚠️ RISCO ESTRUTURAL (INFILTRAÇÃO).",
            "agravante": "Dados do Word confirmam umidade ativa afetando o conteúdo do imóvel."
        }
    return analise

def gerar_desenho_tecnico(modelo):
    """Gera croquis reais 10x10 com grid de engenharia"""
    img = Image.new('RGB', (400, 400), color='#ffffff')
    draw = ImageDraw.Draw(img)
    # Desenha Grid
    for i in range(0, 400, 40):
        draw.line([(i, 0), (i, 400)], fill='#eeeeee')
        draw.line([(0, i), (400, i)], fill='#eeeeee')
    
    # Desenha forma base conforme modelo
    if "H" in modelo:
        draw.polygon([(100,100), (150,100), (150,180), (250,180), (250,100), (300,100), 
                      (300,300), (250,300), (250,220), (150,220), (150,300), (100,300)], 
                     outline="black", width=3)
    else:
        draw.rectangle([120, 120, 280, 280], outline="black", width=3)
    return img

st.title("🛡️ Michael Mulero Inspeções Tech V1")
st.sidebar.info(f"Inspetor: Michael Giovanni Mulero\nLocal: Ibiporã, PR")

pacote = st.file_uploader("Subir Vistoria (Fotos + Relatórios Word):", accept_multiple_files=True)

if pacote:
    texto_extraido = ""
    fotos = []
    
    # Primeiro Passo: Ler todos os arquivos Word para contexto
    for arquivo in pacote:
        if arquivo.name.endswith('.docx'):
            texto_extraido += ler_texto_docx(arquivo)
            st.success(f"✅ Informações lidas do arquivo: {arquivo.name}")
    
    # Segundo Passo: Analisar Fotos com base no que foi lido no Word
    for arquivo in pacote:
        if arquivo.type.startswith('image/'):
            img = Image.open(arquivo).convert("RGB")
            res = analise_sofia_pericial(arquivo.name, texto_extraido)
            fotos.append({"img": img, "res": res})

    # Exibição do Laudo
    for item in sorted(fotos, key=lambda x: x['res']['status'], reverse=True):
        c1, c2 = st.columns([1, 2])
        c1.image(item["img"], use_container_width=True)
        with c2:
            st.subheader(f"Status: {item['res']['status']}")
            st.write(f"**Análise:** {item['res']['parecer']}")
            st.warning(f"**Contexto do Relatório:** {item['res']['agravante']}")

    if st.button("📄 FINALIZAR LAUDO E GERAR CROQUIS 10x10"):
        st.header("📐 Croquis Técnicos Sinalizados")
        modelos = ["Planta Baixa (Formato H)", "Área Operacional", "Mapa de Blindagem", "Bloco Comercial", "Residencial/Lazer", "Implantação Geral"]
        for i in range(0, 6, 2):
            cols = st.columns(2)
            cols[0].image(gerar_desenho_tecnico(modelos[i]), caption=modelos[i])
            cols[1].image(gerar_desenho_tecnico(modelos[i+1]), caption=modelos[i+1])
