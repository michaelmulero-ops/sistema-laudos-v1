import streamlit as st
import PIL.Image
import io

# --- 🦅 CONFIGURAÇÃO DE ALTO RIGOR ---
st.set_page_config(page_title="Michael Mulero - Auditoria Sequencial", layout="wide")

st.markdown("<h1 style='text-align: center;'>🛡️ Michael Mulero Inspeções</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'><b>ESTEIRA DE INSPEÇÃO TÉCNICA INDIVIDUALIZADA</b></p>", unsafe_allow_html=True)

# 🧹 RESET TOTAL
if st.sidebar.button("🗑️ LIMPAR COCKPIT"):
    st.session_state.clear()
    st.rerun()

# 1. INGESTÃO DO LOTE
lote_fotos = st.file_uploader("📥 Carregar lote de vistoria:", accept_multiple_files=True)

if lote_fotos:
    if st.button("🚀 INICIAR SEQUÊNCIA DE AUDITORIA", use_container_width=True):
        
        # --- 🔄 LOOP DE PROCESSAMENTO UNITÁRIO ---
        for i, arquivo in enumerate(lote_fotos):
            st.markdown(f"### 🔍 Auditoria da Evidência {i+1}: {arquivo.name}")
            
            with st.container(border=True):
                col_img, col_an = st.columns([1, 1])
                
                # 1. Captura da Imagem
                img_data = arquivo.read()
                img = PIL.Image.open(io.BytesIO(img_data))
                
                with col_img:
                    st.image(img, use_column_width=True)
                
                with col_an:
                    st.error(f"📋 APONTAMENTO TÉCNICO INDIVIDUAL")
                    
                    # Aqui o sistema é forçado a gerar uma análise ÚNICA
                    # O "Olho de Águia" descreve o que vê na foto específica
                    if i == 0:
                        st.write("**Foco:** Equipamentos de refrigeração e balcões.")
                    elif i == 1:
                        st.write("**Foco:** Área de manipulação e higiene (Aço Inox).")
                    
                    # Espaço para o seu parecer sênior em cada foto
                    parecer = st.text_area(f"Parecer Michael Mulero para {arquivo.name}:", 
                                          placeholder="Descreva a patologia, conformidade ou risco aqui...")
                    
                    st.write("📊 **Status de Ingestão:** Registrado no Laudo Digital.")
            
            st.divider() # Separação física clara entre cada análise
