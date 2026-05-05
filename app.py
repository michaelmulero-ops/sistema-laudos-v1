import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. IDENTIDADE VISUAL
st.set_page_config(page_title="S.I.T. - Michael Mulero", layout="wide")

# 2. CONFIGURAÇÃO DA API (Sua chave atualizada)
API_KEY = "AIzaSyAB6i7YEdIylcmamB3mlV64UlDLyYHlZ-g" 
genai.configure(api_key=API_KEY)

# 3. DEFINIÇÃO DA INTELIGÊNCIA TÉCNICA
# O foco continua em D-Limoneno, reatores e os 9 pontos de SPDA
SYSTEM_PROMPT = """
Você é o motor de IA do Michael Mulero Inspeções.
Analise as fotos enviadas e extraia dados para laudos de seguros.
FOCO TÉCNICO:
- INDÚSTRIA: Reatores, tanques e inflamáveis (D-Limoneno UN 2319).
- LOGÍSTICA: Docas, frotas e armazenamento em CDs ou E-commerce.
- SEGURANÇA: Verifique 9 pontos de SPDA, cercamentos e CFTV.
Gere um parágrafo técnico e profissional para o campo 'Processo Operacional'.
"""

# AJUSTE PARA EVITAR O ERRO 404: Nome do modelo sem o prefixo de versão beta
model = genai.GenerativeModel('gemini-1.5-flash')

# 4. PAINEL DE CONTROLE (BARRA LATERAL)
with st.sidebar:
    st.title("🛡️ Filtros de Vistoria")
    categoria = st.selectbox("Selecione o Nível:", [
        "Indústria", "Transportadora", "E-commerce", "CD de Distribuição", "Comércio", "Residencial"
    ])
    cnpj_input = st.text_input("CNPJ/CPF do Risco:", value="21.203.489/0001-79")

# 5. INTERFACE PRINCIPAL
st.title("🛡️ Painel de Operação - Michael Mulero Inspeções")
st.subheader(f"📋 Análise de Risco: {categoria}")

fotos = st.file_uploader("Subir fotos da vistoria (JPG/PNG):", accept_multiple_files=True)

processo_texto = ""

if fotos:
    st.success(f"✅ {len(fotos)} fotos prontas para análise.")
    if st.button("🤖 ANALISAR IMAGENS E GERAR PARECER"):
        with st.spinner("Extraindo inteligência das imagens..."):
            try:
                img_list = [Image.open(f) for f in fotos]
                # Chamada com o prompt de sistema reforçado aqui para garantir a precisão
                response = model.generate_content([
                    SYSTEM_PROMPT, 
                    "Baseado nas fotos, descreva o processo operacional detalhado:", 
                    *img_list
                ])
                processo_texto = response.text
                st.balloons()
            except Exception as e:
                st.error(f"Erro ao processar: {e}")

# 6. CAMPO DE TEXTO DO LAUDO
st.subheader("📝 Processo Operacional Extraído")
processo_final = st.text_area(
    "Este texto pode ser copiado para o seu relatório oficial:", 
    value=processo_texto, 
    height=300
)

if st.button("🚀 FINALIZAR E SALVAR"):
    st.success(f"Vistoria da unidade {cnpj_input} concluída!")
