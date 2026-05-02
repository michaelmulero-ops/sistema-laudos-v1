import streamlit as st
import PIL.Image
import io

# --- 🦅 SISTEMA MICHAEL MULERO INSPEÇÕES V14.0 (CONTROLE MANUAL SÊNIOR) ---
st.set_page_config(page_title="Michael Mulero - Auditoria Digital", layout="wide")

# 🧹 BOTÃO DE LIMPEZA PARA O DESCANSO
if st.sidebar.button("🗑️ LIMPAR E ENCERRAR EXPEDIENTE"):
    st.session_state.clear()
    st.rerun()

st.markdown("<h1 style='text-align: center;'>🛡️ Michael Mulero Inspeções</h1>", unsafe_allow_html=True)

# 1. CARREGAMENTO DO LOTE
lote_fotos = st.file_uploader("📥 Arraste o lote de evidências aqui:", accept_multiple_files=True)

if lote_fotos:
    st.success(f"📊 {len(lote_fotos)} arquivos carregados no sistema.")
    
    if st.button("🚀 ABRIR ESTEIRA DE PARECERES", use_container_width=True):
        
        for i, arquivo in enumerate(lote_fotos):
            # 2. FILTRO DE ARQUIVOS (Imagens vs Documentos)
            if arquivo.name.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
                st.markdown(f"### 🔍 Evidência {i+1}: {arquivo.name}")
                
                with st.container(border=True):
                    col_img, col_input = st.columns([1, 1])
                    
                    try:
                        img_data = arquivo.read()
                        img = PIL.Image.open(io.BytesIO(img_data))
                        
                        with col_img:
                            st.image(img, use_column_width=True)
                        
                        with col_input:
                            st.info("📋 PARECER TÉCNICO MICHAEL MULERO")
                            # Campo em branco para você preencher com sua expertise
                            st.text_area(f"Análise da foto {arquivo.name}:", 
                                        key=f"input_{i}", 
                                        height=250,
                                        placeholder="Digite aqui os apontamentos de NRs, patologias e riscos...")
                            
                    except Exception:
                        st.warning(f"⚠️ Erro ao visualizar imagem: {arquivo.name}")
            
            else:
                # Registro automático de documentos sem travar o app
                st.markdown(f"### 📄 Documento: {arquivo.name}")
                st.info("Este arquivo foi indexado como documento complementar ao laudo.")
            
            st.divider()

        st.success("✅ Esteira de laudo finalizada. Todos os dados estão prontos para consolidação.")
