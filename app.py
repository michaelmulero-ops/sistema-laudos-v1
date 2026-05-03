import streamlit as st
from PIL import Image, ImageOps
from fpdf import FPDF
import io
from datetime import datetime

# 1. Configurações de Identidade Visual
st.set_page_config(page_title="Michael Mulero Inspeções Tech V1", layout="wide")

# Estilos CSS
st.markdown("""
    <style>
    .alerta-tecnico { background-color: #ffff00; color: black; padding: 10px; font-weight: bold; border-radius: 5px; border-left: 5px solid red; }
    .narra-sofia { background-color: #f0f2f6; padding: 15px; border-radius: 10px; border-left: 5px solid #007bff; }
    </style>
    """, unsafe_allow_html=True)

# 2. Funções Técnicas
def aplicar_zoom_tecnico(img_input, x, y):
    width, height = img_input.size
    caixa = (max(0, x-200), max(0, y-200), min(width, x+200), min(height, y+200))
    zoom = img_input.crop(caixa).resize((600, 600), Image.LANCZOS)
    zoom = ImageOps.expand(zoom, border=15, fill='red')
    return zoom

def gerar_pdf(projeto, localidade, data, parecer, img_orig, img_zoom):
    pdf = FPDF()
    pdf.add_page()
    
    # Cabeçalho Profissional
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "MICHAEL MULERO INSPEÇÕES - LAUDO TÉCNICO V1", ln=True, align='C')
    pdf.set_font("Arial", '', 10)
    pdf.cell(0, 10, f"Cliente: {projeto} | Localidade: {localidade} | Data: {data}", ln=True, align='C')
    pdf.ln(10)
    
    # Seção de Imagens
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "EVIDÊNCIAS TÉCNICAS (GEOINTELIGÊNCIA):", ln=True)
    
    # Salvar imagens temporariamente para o PDF
    img_orig.save("temp_orig.jpg")
    img_zoom.save("temp_zoom.jpg")
    
    pdf.image("temp_orig.jpg", x=10, y=50, w=90)
    pdf.image("temp_zoom.jpg", x=110, y=50, w=90)
    pdf.ln(75)
    
    # Parecer Técnico
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "PARECER TÉCNICO (AGENTE IA SOFIA):", ln=True)
    pdf.set_font("Arial", '', 11)
    pdf.multi_cell(0, 10, parecer)
    
    return pdf.output(dest='S')

# 3. Interface Principal
st.title("🛡️ Sistema de Laudos V1 - Michael Mulero")
st.write("Independência e automação em inspeções de risco.")

with st.sidebar:
    st.header("Dados da Vistoria")
    cliente = st.selectbox("Seguradora", ["Tokio Marine", "Zurich", "Allianz", "Sompo Seguros", "Sancor"])
    cidade = st.text_input("Cidade", value="Ibiporã")

arquivo_foto = st.file_uploader("Carregue a evidência", type=['jpg', 'png', 'jpeg'])

if arquivo_foto:
    img = Image.open(arquivo_foto).convert("RGB")
    
    # Controles de Zoom
    col_x = st.slider("Ajuste X", 0, img.width, img.width // 2)
    col_y = st.slider("Ajuste Y", 0, img.height, img.height // 2)
    
    # Parecer
    st.subheader("🎙️ Parecer da Sofia")
    texto_narracao = st.text_area("Descrição da Anomalia:", value="Risco crítico detectado. Recomenda-se correção imediata.")
    
    if st.button("🚀 GERAR LAUDO COMPLETO"):
        zoom_img = aplicar_zoom_tecnico(img, col_x, col_y)
        data_atual = datetime.now().strftime("%d/%m/%Y")
        
        # Exibição Visual
        c1, c2 = st.columns(2)
        with c1: st.image(img, caption="Geral")
        with c2: st.image(zoom_img, caption="Destaque Técnico")
        
        # Geração do PDF
        pdf_bytes = gerar_pdf(cliente, cidade, data_atual, texto_narracao, img, zoom_img)
        
        st.success("✅ Laudo gerado com sucesso!")
        st.download_button(
            label="📥 BAIXAR LAUDO EM PDF",
            data=pdf_bytes,
            file_name=f"Laudo_{cliente}_{cidade}.pdf",
            mime="application/pdf"
        )
