import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. IDENTIDADE VISUAL (Michael Mulero Inspeções)
st.set_page_config(page_title="S.I.T. - Michael Mulero", layout="wide")

# 2. CONFIGURAÇÃO DA API COM SUA CHAVE ATUALIZADA
API_KEY = "AIzaSyAB6i7YEdIylcmamB3mlV64UlDLyYHlZ-g" 
genai.configure(api_key=API_KEY)

# 3. DEFINIÇÃO DA INTELIGÊNCIA TÉCNICA (Sênior de Risco)
SYSTEM_PROMPT = """
Você é o motor de IA do Michael Mulero Inspeções.
Sua tarefa é analisar as fotos enviadas e extrair dados para laudos de seguros.
FOCO TÉCNICO:
- INDÚSTRIA: Identifique reatores, tanques e inflamáveis (como D-Limoneno UN 2319).
- LOGÍSTICA: Identifique docas, frotas e armazenamento em CDs ou E-commerce.
- SEGURANÇA: Verifique 9 pontos de SPDA, cercamentos, CFTV e concertinas.
Gere um parágrafo técnico, direto e profissional para o campo 'Processo Operacional'.
"""
model = genai.GenerativeModel(model_name="gemini-1.5-flash", system_instruction=SYSTEM_PROMPT)

# 4. PAINEL DE CONTROLE (BARRA LATERAL)
with st.sidebar:
    st.title("🛡️ Filtros de Vistoria")
    categoria = st.selectbox("Selecione o Nível:", [
        "Indústria", "Transportadora", "E-commerce", "CD de Distribuição", "Comércio", "Residencial"
    ])
    cnpj_input = st.text_input("CNPJ/CPF do Risco:", value="21.203.489/0001-79")
    st.divider()
    st.info("Sistema operando com Gemini 1.5 Flash")

# 5. INTERFACE PRINCIPAL
st.title("🛡️ Painel de Operação - Michael Mulero Inspeções")
st.subheader(f"📋 Análise de Risco: {categoria}")

# Campo para upload das fotos da Solus/Cropfield ou outros clientes
fotos = st.file_uploader("Subir fotos da vistoria (JPG/PNG):", accept_multiple_files=True)

processo_texto = ""

if fotos:
    st.success(f"✅ {len(fotos)} fotos prontas para análise.")
    if st.button("🤖 ANALISAR IMAGENS E GERAR PARECER"):
        with st.spinner("Extraindo inteligência das imagens..."):
            try:
                # Prepara a lista de imagens para a IA
                img_list = [Image.open(f) for f in fotos]
                # Solicita a descrição técnica baseada nas fotos
                response = model.generate_content([
                    f"Analise estas fotos para um laudo de {categoria}. "
                    "Descreva o processo operacional, citando máquinas, inflamáveis e proteções visíveis.", 
                    *img_list
                ])
                processo_texto = response.text
                st.balloons()
            except Exception as e:
                st.error(f"Erro ao processar: {e}")

# 6. CAMPO DE TEXTO DO LAUDO (Editável)
st.subheader("📝 Processo Operacional Extraído")
processo_final = st.text_area(
    "Este texto pode ser copiado para o seu relatório oficial:", 
    value=processo_texto, 
    height=300
)

# 7. FINALIZAÇÃO
if st.button("🚀 FINALIZAR E SALVAR"):
    if not processo_final:
        st.warning("Gere a análise antes de finalizar.")
    else:
        st.success(f"Vistoria da unidade {cnpj_input} concluída com sucesso!")
        st.info("Os dados foram processados seguindo o padrão Michael Mulero Inspeções.")
