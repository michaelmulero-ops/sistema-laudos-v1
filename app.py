import streamlit as st

# Configuração Michael Mulero Inspeções
st.set_page_config(page_title="Michael Mulero | Auditoria Tech V1", layout="wide")

# Inicialização de Memória
if 'dados_injetados' not in st.session_state:
    st.session_state.dados_injetados = False

# --- SIDEBAR: COMANDO CENTRAL ---
with st.sidebar:
    st.header("🕹️ Painel de Operação")
    
    # Botão de Ingestão (Só habilita se houver dados)
    btn_injetar = st.button("🚀 INJETAR DADOS NO LAUDO", type="primary", use_container_width=True)
    
    st.markdown("---")
    if st.button("♻️ LIMPAR TELA / NOVO RISCO", use_container_width=True):
        st.session_state.clear()
        st.rerun()

# --- TELA PRINCIPAL: O FLUXO DO JOGO ---
tab1, tab2, tab3, tab4 = st.tabs(["📥 1. INFO & CONVERSA", "📸 2. FOTOS & ANÁLISE", "📐 3. CROQUIS TÉCNICOS", "📄 4. VEREDITO FINAL"])

with tab1:
    st.subheader("📋 Entrevista Técnica e Classificação")
    col1, col2 = st.columns(2)
    with col1:
        st.text_input("CNPJ ou CPF do Risco:", key="doc")
        st.selectbox("Tipo de Risco:", ["Indústria", "Shopping", "Logística", "Comércio", "Residencial Luxo", "Social"], key="tipo")
    with col2:
        st.number_input("Número de Funcionários:", key="func")
        st.text_area("O que rola lá? (Processo Operacional):", key="processo")

with tab2:
    st.subheader("⚙️ Análise Sofia: Fotos e Apontamentos")
    st.file_uploader("Subir Evidências:", accept_multiple_files=True, key="fotos")
    if st.session_state.fotos:
        st.success("Sofia analisando ativos e descrevendo pontos críticos...")

with tab3:
    if btn_injetar or st.session_state.dados_injetados:
        st.session_state.dados_injetados = True
        st.subheader("📐 Infografia Isométrica Forense")
        st.write("Renderizando 6 pranchas técnicas: Isometria, Entorno, Hidrografia, Segurança...")
        # Aqui entram os códigos de Plotly 3D que criamos

with tab4:
    if st.session_state.dados_injetados:
        st.subheader("📝 Parecer Técnico Final")
        st.text_area("Texto de Conclusão:", value="Após auditoria pericial, o risco apresenta...", height=300)
        st.radio("Veredito:", ["APROVADO", "APROVADO COM RECOMENDAÇÕES", "REPROVADO"], horizontal=True)
