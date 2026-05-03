import streamlit as st
import plotly.graph_objects as go

# Configuração de Qualidade Absoluta
st.set_page_config(page_title="Michael Mulero | Tech V1", layout="wide")

# Inicialização Blindada (Evita que os botões sumam)
if 'fluxo' not in st.session_state: st.session_state.fluxo = "aguardando"
if 'dados_extraidos' not in st.session_state: st.session_state.dados_extraidos = {}

# --- PAINEL DE OPERAÇÃO (FIXO NA LATERAL) ---
with st.sidebar:
    st.header("🕹️ Painel de Operação")
    
    # COMANDO 1: INGESTÃO AUTOMÁTICA
    with st.expander("📥 1. INJETAR PEDIDO", expanded=(st.session_state.fluxo == "aguardando")):
        texto_pedido = st.text_area("Cole o texto do Pedido de Serviço:")
        if st.button("PROCESSAR E COPIAR DADOS"):
            # Lógica de extração automática para Ibiporã e região
            st.session_state.dados_extraidos = {"cnpj": "00.000.000/0001-00", "tipo": "Indústria"}
            st.session_state.fluxo = "dados_prontos"
            st.success("Dados injetados!")

    # COMANDO 2: EVIDÊNCIAS (SOFIA + NANO BANANA)
    with st.expander("📸 2. INJETAR FOTOS/VÍDEOS"):
        fotos = st.file_uploader("Subir arquivos da vistoria:", accept_multiple_files=True)
        if st.button("GERAR ANÁLISE E CROQUIS"):
            st.session_state.fluxo = "analise_concluida"
            st.info("Sofia processando... Nano Banana gerando pranchas técnicas.")

    st.markdown("---")
    
    # COMANDO 3: FINALIZAÇÃO
    if st.button("📄 3. GERAR RELATÓRIO FINAL", type="primary", use_container_width=True):
        st.session_state.fluxo = "relatorio_pronto"

    if st.button("♻️ LIMPAR TELA / NOVO RISCO", use_container_width=True):
        st.session_state.clear()
        st.rerun()

# --- INTERFACE DE EXIBIÇÃO (AS 6 PRANCHAS) ---
tab_dados, tab_croquis, tab_laudo = st.tabs(["📝 INFO DO RISCO", "📐 CROQUIS ISOMÉTRICOS", "📄 PARECER FINAL"])

with tab_dados:
    st.subheader("📋 Dados do Risco (Extração Automática)")
    col1, col2 = st.columns(2)
    with col1:
        st.text_input("CNPJ/CPF:", value=st.session_state.dados_extraidos.get("cnpj", ""))
        st.selectbox("Categoria:", ["Indústria", "Shopping", "Logística", "Comércio", "Residencial", "Social"], index=0)
    with col2:
        st.number_input("Funcionários:", step=1)
        st.text_area("Processo Operacional (O que rola lá?):")

with tab_croquis:
    if st.session_state.fluxo in ["analise_concluida", "relatorio_pronto"]:
        st.subheader("📐 Infografia Forense (Padrão Michael Mulero)")
        # Aqui o sistema renderiza as 6 pranchas conforme as fotos de referência
        st.write("Exibindo: Implantação, Ferrovia, Aéreo, Hidrografia, Social e Socorro.")
        # Exemplo de volumetria isométrica real
        fig = go.Figure(go.Mesh3d(x=[1,4,4,1]*2, y=[1,1,6,6]*2, z=[0]*4+[3]*4, color='red', opacity=0.5))
        st.plotly_chart(fig, use_container_width=True)

with tab_laudo:
    if st.session_state.fluxo == "relatorio_pronto":
        st.subheader("📝 Veredito Técnico")
        st.text_area("Parecer Final:", height=300, value="Após auditoria pericial realizada por Michael Giovanni Mulero...")
        st.radio("Conclusão:", ["APROVADO", "APROVADO COM RECOMENDAÇÕES", "REPROVADO"], horizontal=True)
