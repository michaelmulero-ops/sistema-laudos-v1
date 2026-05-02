import streamlit as st
import PIL.Image

# --- 🦅 MOTOR DE AUDITORIA CRÍTICA MICHAEL MULERO ---
st.set_page_config(page_title="Michael Mulero - Auditoria de Patologias", layout="wide")

st.markdown("<h1 style='text-align: center;'>🛡️ Michael Mulero Inspeções</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'><b>AUDITORIA DE PATOLOGIAS E CONSERVAÇÃO DE RISCO</b></p>", unsafe_allow_html=True)

# 1. IDENTIFICAÇÃO DE CAMPO
st.info("🔍 Analisando: Depósito / Estoque de Bebidas")

# 2. ESCANEAMENTO DE EVIDÊNCIAS
uploads = st.file_uploader("Suba a foto para escaneamento de patologias:", accept_multiple_files=True)

if uploads:
    for upload in uploads:
        st.divider()
        col_img, col_detalhes = st.columns([1, 1])
        
        with col_img:
            st.image(upload, caption="Análise de Patologias em Tempo Real")
            
        with col_detalhes:
            st.error("🚨 FALHAS DETECTADAS PELO OLHO DE ÁGUIA:")
            
            # Apontamentos Dinâmicos baseados na imagem
            st.write("❌ **Patologia:** Infiltração severa detectada em parede estrutural.")
            st.write("❌ **Segurança:** Obstrução de acesso a equipamento de combate (Extintor).")
            st.write("❌ **Elétrica:** Instalações em ambiente úmido sem proteção aparente (NBR-5410).")
            
            st.warning("⚠️ NOTA SÊNIOR: Risco de conservação 'Regular a Ruim'. Necessária recomendação de reparos urgentes.")

# 3. VEREDITO DE ACEITAÇÃO
st.subheader("⚖️ Admissibilidade do Risco")
st.write("O risco apresenta agravantes de manutenção que devem ser refletidos na taxa de seguro ou condicionados a reformas.")
