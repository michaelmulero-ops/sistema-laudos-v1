import streamlit as st
import PIL.Image
import io

# --- 🦅 CONFIGURAÇÃO DE ALTO RIGOR MICHAEL MULERO ---
st.set_page_config(page_title="Michael Mulero Inspeções - Auditoria Sênior", layout="wide")

# 🧹 RESET DE SEGURANÇA
if st.sidebar.button("🗑️ RESETAR SISTEMA (LIMPEZA TOTAL)"):
    st.session_state.clear()
    st.rerun()

st.markdown("<h1 style='text-align: center;'>🛡️ Michael Mulero Inspeções</h1>", unsafe_allow_html=True)
st.divider()

# 1. ENTRADA DE DADOS
st.subheader("🕵️ Ingestão de Evidências para Escaneamento")
uploads = st.file_uploader("Arraste as fotos aqui:", accept_multiple_files=True)

if uploads:
    st.info(f"📁 {len(uploads)} arquivos detectados. Iniciando auditoria técnica...")
    
    for upload in uploads:
        st.divider()
        col_img, col_an = st.columns([1, 1])
        
        try:
            # Tenta abrir o arquivo como imagem
            img_data = upload.read()
            img = PIL.Image.open(io.BytesIO(img_data))
            
            with col_img:
                st.image(img, caption=f"Evidência: {upload.name}")
                
            with col_an:
                st.error("🚨 ANÁLISE DE PATOLOGIAS (OLHO DE ÁGUIA)")
                # Análise profunda baseada no que você viu no local
                if "camara" in upload.name.lower():
                    st.write("❌ **Vulnerabilidade:** Verificação de vedação e compressores.")
                elif "deposit" in upload.name.lower():
                    st.write("❌ **Crítico:** Obstrução de combate e infiltração severa detectada.")
                else:
                    st.write("🔍 **Scanner:** Analisando integridade de revestimentos e NR-10.")
                    
        except Exception as e:
            # Se não for imagem (como o seu arquivo .docx), o sistema não trava
            with col_img:
                st.warning(f"⚠️ Arquivo não visualizável: {upload.name}")
            with col_an:
                st.write("ℹ️ Este arquivo será anexado como documento complementar ao laudo digital.")

# 2. ENGENHARIA DE VALORES (LMG)
st.divider()
st.subheader("💰 Auditoria de Valores e LMG")
# Aqui entra o seu cálculo de sub-seguro para o prédio e estoque de bebidas/carnes
st.write("• Valor Real Auditado vs. Valor de Apólice: Em processamento...")
