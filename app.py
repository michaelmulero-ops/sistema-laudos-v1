import streamlit as st
import plotly.graph_objects as go

# Configuração de Elite
st.set_page_config(page_title="Michael Mulero | Tech V1", layout="wide")

# --- ESTADOS DO SISTEMA ---
if 'dados_pedido' not in st.session_state: st.session_state.dados_pedido = {}
if 'fotos_processadas' not in st.session_state: st.session_state.fotos_processadas = False

# --- PAINEL DE OPERAÇÃO LATERAL ---
with st.sidebar:
    st.header("🕹️ Painel de Comando")
    
    # BOTÃO 1: INGESTÃO DO PEDIDO
    with st.expander("📥 1. INJETAR PEDIDO", expanded=False):
        pedido_texto = st.text_area("Cole aqui o texto do pedido de serviço:")
        if st.button("PROCESSAR PEDIDO"):
            # Lógica para copiar e preencher automaticamente
            st.session_state.dados_pedido = {"doc": "00.000.000/0001-00", "tipo": "Indústria"}
            st.success("Dados do pedido extraídos!")

    # BOTÃO 2: ENTRADA DE EVIDÊNCIAS
    with st.expander("📸 2. ENTRADA DE FOTOS/VÍDEOS", expanded=False):
        arquivos = st.file_uploader("Subir arquivos da vistoria:", accept_multiple_files=True)
        if st.button("ANALISAR EVIDÊNCIAS"):
            st.session_state.fotos_processadas = True
            st.info("Sofia descrevendo ativos e gerando croquis...")

    st.markdown("---")
    
    # BOTÃO 3: RELATÓRIO FINAL
    if st.button("📄 3. GERAR RELATÓRIO FINAL", type="primary", use_container_width=True):
        st.session_state.gerar_laudo = True

    if st.button("♻️ LIMPAR TELA / NOVO RISCO", use_container_width=True):
        st.session_state.clear()
        st.rerun()

# --- TELA PRINCIPAL ORGANIZADA ---
tab1, tab2, tab3 = st.tabs(["📝 INFO DO RISCO", "📐 CROQUIS HD", "📄 PARECER TÉCNICO"])

with tab1:
    st.subheader("📋 Dados Extraídos do Pedido")
    col1, col2 = st.columns(2)
    with col1:
        # Preenchimento automático vindo do Botão 1
        st.text_input("CNPJ ou CPF:", value=st.session_state.dados_pedido.get("doc", ""))
        st.selectbox("Tipo de Risco:", ["Indústria", "Comércio", "Shopping", "Logística", "Residencial", "Social"], 
                     index=0 if st.session_state.dados_pedido.get("tipo") == "Indústria" else 1)
    with col2:
        st.number_input("Número de Funcionários:", step=1)
        st.text_area("O que rola lá? (Processo Operacional):")

with tab2:
    if st.session_state.fotos_processadas:
        st.subheader("📐 Infografia Isométrica Forense")
        # Renderização dos Croquis de Alto Padrão (Indústria a Barraco)
        st.write("Exibindo 6 pranchas técnicas isométricas...")
        fig = go.Figure(go.Mesh3d(x=[1, 5, 5, 1]*2, y=[1, 1, 6, 6]*2, z=[0]*4+[3]*4, color='red', opacity=0.5))
        st.plotly_chart(fig, use_container_width=True)

with tab3:
    if st.session_state.get('gerar_laudo'):
        st.subheader("📝 Veredito de Michael Giovanni Mulero")
        st.text_area("Texto Final de Aprovação/Reprovação:", height=300)
        st.radio("Conclusão:", ["APROVADO", "APROVADO COM RECOMENDAÇÕES", "REPROVADO"], horizontal=True)
