import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. IDENTIDADE VISUAL
st.set_page_config(page_title="S.I.T. - Michael Mulero", layout="wide")

# 2. CONFIGURAÇÃO DA API (Google AI Studio)
API_KEY = "SUA_CHAVE_AQUI" 
genai.configure(api_key=API_KEY)

# 3. DEFINIÇÃO DA INTELIGÊNCIA TÉCNICA
SYSTEM_PROMPT = """
Você é o motor de IA do Michael Mulero Inspeções.
Analise as fotos enviadas e identifique:
- INDÚSTRIA: Reatores, GLP e inflamáveis (D-Limoneno UN 2319).
- LOGÍSTICA: Docas, frotas e carga de incêndio em CDs e E-commerce.
- ENGENHARIA: Verifique 9 pontos de SPDA, CFTV e perímetros.
Gere um texto técnico para o campo 'Processo Operacional'.
"""
model = genai.GenerativeModel(model_name="gemini-1.5-flash", system_instruction=SYSTEM_PROMPT)

# 4. PAINEL DE CONTROLE (BARRA LATERAL)
with st.sidebar:
    st.title("🛡️ Filtros de Vistoria")
    categoria = st.selectbox("Selecione o Nível:", [
        "Indústria", "Transportadora", "E-commerce", "CD de Distribuição", "Comércio", "Residencial"
    ])
    cnpj = st.text_input("CNPJ do Risco:", value="21.203.489/0001-79")

# 5. INTERFACE DE OPERAÇÃO
st.title("🛡️ Painel de Operação - Michael Mulero Inspeções")
st.info(f"Categoria Selecionada: {categoria}")

# CAMPO DE UPLOAD
fotos = st.file_uploader("Subir fotos da vistoria:", accept_multiple_files=True)

# LÓGICA DE PROCESSAMENTO (O QUE ESTAVA FALTANDO)
processo_texto = ""
if fotos:
    st.success(f"{len(fotos)} fotos carregadas com sucesso!")
    if st.button("🤖 ANALISAR IMAGENS E GERAR PARECER"):
        with st.spinner("Girando o programa e extraindo dados técnicos..."):
            try:
                img_list = [Image.open(f) for f in fotos]
                # Envia as fotos para a IA analisar
                response = model.generate_content(["Descreva detalhadamente o processo desta unidade:", *img_list])
                processo_texto = response.text
                st.balloons()
            except Exception as e:
                st.error(f"Erro ao processar imagens: {e}")

# 6. RESULTADO FINAL (O QUE VAI PARA O SEU RELATÓRIO)
st.subheader("📝 Processo Operacional Extraído")
processo_final = st.text_area("Texto Técnico:", value=processo_texto, height=300)

if st.button("🚀 FINALIZAR E SALVAR LAUDO"):
    st.success(f"Laudo de {categoria} pronto para envio!")
