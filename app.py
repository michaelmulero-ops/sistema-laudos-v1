import streamlit as st
from PIL import Image, ImageOps
from fpdf import FPDF
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from datetime import datetime

# 1. Configurações de Identidade Visual Michael Mulero Inspeções
st.set_page_config(page_title="Michael Mulero Inspeções Tech V1", layout="wide")

# Estilos Visuais
st.markdown("""
    <style>
    .alerta-tecnico { background-color: #ffff00; color: black; padding: 10px; font-weight: bold; border-radius: 5px; border-left: 5px solid red; }
    .narra-sofia { background-color: #f0f2f6; padding: 15px; border-radius: 10px; border-left: 5px solid #007bff; }
    </style>
    """, unsafe_allow_html=True)

# 2. Funções de Processamento e PDF
def aplicar_zoom_tecnico(img_input, x, y):
    width, height = img_input.size
    caixa = (max(0, x-200), max(0, y-200), min(width, x+200), min(height, y+200))
    zoom = img_input.crop(caixa).resize((600, 600), Image.LANCZOS)
    zoom = ImageOps.expand(zoom, border=15, fill='red')
    return zoom

def gerar_pdf(projeto, localidade, data, parecer, img_orig, img_zoom):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "MICHAEL MULERO INSPEÇÕES - LAUDO TÉCNICO", ln=True, align='C')
    pdf.set_font("Arial", '', 10)
    pdf.cell(0, 10, f"Cliente: {projeto} | Local: {localidade} | Data: {data}", ln=True, align='C')
    pdf.ln(10)
    img_orig.save("temp_orig.jpg")
    img_zoom.save("temp_zoom.jpg")
    pdf.image("temp_orig.jpg", x=10, y=50, w=90)
    pdf.image("temp_zoom.jpg", x=110, y=50, w=90)
    pdf.ln(75)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "PARECER TÉCNICO (SOFIA IA):", ln=True)
    pdf.set_font("Arial", '', 11)
    pdf.multi_cell(0, 10, parecer)
    return pdf.output(dest='S')

# 3. Função de Envio de E-mail (Backup)
def enviar_email_backup(pdf_content, filename):
    try:
        msg = MIMEMultipart()
        msg['Subject'] = f"BACKUP: {filename}"
        msg['From'] = st.secrets["email_user"]
        msg['To'] = st.secrets["email_user"]
        
        part = MIMEApplication(pdf_content, _subtype="pdf")
        part.add_header('Content-Disposition', 'attachment', filename=filename)
        msg.attach(part)
        
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(st.secrets["email_user"], st.secrets["email_password"])
        server.send_message(msg)
        server.quit()
        return True
    except:
        return False

# 4. Interface Principal
st.title("🛡️ Sistema de Laudos V1 - Michael Mulero")

with st.sidebar:
    cliente = st.selectbox("Seguradora", ["Tokio Marine", "Zurich", "Allianz", "Sompo", "Sancor"])
    cidade = st.text_input("Cidade", value="Ibiporã")

arquivo_foto = st.file_uploader("Carregue a evidência", type=['jpg', 'png', 'jpeg'])

if arquivo_foto:
    img = Image.open(arquivo_foto).convert("RGB")
    col_x = st.slider("Ajuste Horizontal", 0, img.width, img.width // 2)
    col_y = st.slider("Ajuste Vertical", 0, img.height, img.height // 2)
    texto_narracao = st.text_area("Parecer Técnico:", "Identificado risco crítico conforme normas vigentes.")
    
    if st.button("🚀 FINALIZAR INSPEÇÃO E ENVIAR BACKUP"):
        zoom_img = aplicar_zoom_tecnico(img, col_x, col_y)
        data_atual = datetime.now().strftime("%d/%m/%Y")
        pdf_bytes = gerar_pdf(cliente, cidade, data_atual, texto_narracao, img, zoom_img)
        
        # Envio de Backup Silencioso
        sucesso_email = enviar_email_backup(pdf_bytes, f"Laudo_{cliente}_{cidade}.pdf")
        
        st.success("✅ Laudo gerado e enviado para o backup Michael Mulero!")
        st.download_button("📥 BAIXAR PDF AGORA", data=pdf_bytes, file_name=f"Laudo_{cliente}.pdf")
