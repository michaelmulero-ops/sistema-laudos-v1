import streamlit as st
from google import genai
from PIL import Image
from fpdf import FPDF
import time
import os

# --- SISTEMA MICHAEL MULERO V14.1: LIMPEZA DE SINTAXE ---
st.set_page_config(page_title="Michael Mulero - Sistema Elite", layout="wide")

CHAVE_GEMINI = "AIzaSyCciPFWs78Ua_NixBYXANA4N6YP0cIj_4Y"

def motor_pericial_v14_1(lote):
    client = genai.Client(api_key=CHAVE_GEMINI)
    banco = []
    barra = st.progress(0)
    for i, arq in enumerate(lote):
        img = Image.open(arq)
        st.write(f"🔄 **Sincronizando Motores na Evidência {i+1}...**")
        prompt = "Aja como Perito Sênior. Leia etiquetas, validades e identifique riscos técnicos NR-10/NR-23."
        try:
            res = client.models.generate_content(model="gemini-1.5-flash", contents=[prompt, img])
            analise = res.text
            col1, col2 = st.columns([1, 2])
            with col1: st.image(img, width=280)
            with col2: st.success(f"DADOS TRAVADOS - PONTO {i+1}:\n{analise}")
            banco.append({"img": img, "texto": analise, "id": i+1})
            time.sleep(4)
        except:
            st.error(f"Sistema ocupado na foto {i+1}. Aguardando...")
            time.sleep(10)
        barra.progress((i + 1) / len(lote))
    return banco

st.title("🛡️ Michael Mulero - V14.1 (Conselho de IAs)")

upload = st.file_uploader("📂 Carregar Lote de Fotos", type=['jpg', 'png', 'jpeg'], accept_multiple_files=True)

if upload and st.button("🚀 ATIVAR MOTORES PARALELOS"):
    st.session_state['dados_v14'] = motor_pericial_v14_1(upload)

if 'dados_v14' in st.session_state:
    if st.button("📄 GERAR LAUDO INTEGRADO"):
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        for item in st.session_state['dados_v14']:
            pdf.add_page()
            pdf.set_font("Arial", 'B', 16)
            pdf.cell(0, 10, f"RELATÓRIO TÉCNICO - EVIDÊNCIA {item['id']}", ln=True, align='C')
            pdf.ln(5)
            tmp = f"img_{item['id']}.jpg"
            item['img'].convert('RGB').save(tmp)
            pdf.image(tmp, x=10, w=130)
            pdf.ln(10)
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(0, 10, "PARECER DO INSPETOR:", ln=True)
            pdf.set_font("Arial", size=11)
            pdf.multi_cell(0, 8, txt=item['texto'].encode('latin-1', 'replace').decode('latin-1'))
            os.remove(tmp)
        
        # --- SEÇÃO DE CROQUIS (CORRIGIDA) ---
        pdf.add_page()
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, "ANEXO: 5 CROQUIS PADRÃO DE QUALIDADE", ln=True, align='C')
        # Aqui estava o erro de sintaxe anterior
        for c in ["Entorno", "Cobertura", "Layout", "Elétrica", "Navegação"]:
            pdf.ln(5)
            pdf.set_font("Arial", 'B', 11)
            pdf.cell(0, 10, f"BOX: {c}", border=1, ln=True)
            pdf.ln(32)

        st.download_button("📥 BAIXAR LAUDO OFICIAL", pdf.output(dest='S').encode('latin-1'), "LAUDO_MULERO_FINAL.pdf")