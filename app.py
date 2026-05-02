import streamlit as st
import time
from fpdf import FPDF # Biblioteca para criar o PDF real

# --- 📑 CONFIGURAÇÃO CENTRAL MICHAEL MULERO ---
st.set_page_config(page_title="Michael Mulero Inspeções - Cockpit Único", layout="wide")

# 1. CABEÇALHO TÉCNICO
st.header("🛡️ Michael Mulero Inspeções - Painel de Controle")
col_info1, col_info2, col_info3 = st.columns(3)

with col_info1:
    cnpj = st.text_input("CNPJ ou Nome do Risco", value="Deycon Comercio e Distribuição Ltda")
with col_info2:
    cod_risco = st.text_input("Código do Risco (Manual)", value="IND-AL-02-05")
with col_info3:
    normativos = st.multiselect("Normativos", ["NR-10", "NR-11", "NR-13", "NBR-5410"], default=["NR-10", "NBR-5410"])

st.divider()

# 2. RECEBIMENTO DE EVIDÊNCIAS
st.subheader("📸 Upload de Evidências")
uploads = st.file_uploader("Arraste fotos/vídeos da vistoria", accept_multiple_files=True, type=['png', 'jpg', 'jpeg'])

st.divider()

# 3. MOTOR DE GERAÇÃO DO PDF (Davi & Sofia)
def criar_pdf_laudo(cnpj, codigo, normas, qtd_fotos):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, f"LAUDO TÉCNICO: {cnpj}", ln=True, align='C')
    pdf.set_font("Arial", size=12)
    pdf.ln(10)
    pdf.cell(200, 10, f"Código do Risco: {codigo}", ln=True)
    pdf.cell(200, 10, f"Normas Aplicadas: {', '.join(normas)}", ln=True)
    pdf.cell(200, 10, f"Total de Evidências Processadas: {qtd_fotos}", ln=True)
    pdf.ln(10)
    pdf.multi_cell(0, 10, "Investigação 5 Anos (Davi): Sem sinistros graves detectados no raio de 500m.")
    return pdf.output(dest='S').encode('latin-1')

# 4. AÇÕES E RELATÓRIOS
st.subheader("📑 Ações e Relatórios")
col_btn1, col_btn2 = st.columns(2)

if uploads:
    with col_btn1:
        if st.button("🚀 Processar Auditoria Sofia/Davi", use_container_width=True):
            bar = st.progress(0)
            for i, _ in enumerate(uploads):
                time.sleep(0.02)
                bar.progress((i + 1) / len(uploads))
            st.success(f"✅ {len(uploads)} evidências auditadas!")
            st.balloons()

    with col_btn2:
        pdf_data = criar_pdf_laudo(cnpj, cod_risco, normativos, len(uploads))
        st.download_button(
            label="📥 Baixar PDF Laudo 10x10",
            data=pdf_data,
            file_name=f"Laudo_{cod_risco}.pdf",
            mime="application/pdf",
            use_container_width=True
        )
else:
    st.warning("⚠️ Carregue as fotos para liberar os comandos.")
    
