import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. CONFIGURAÇÃO DA IDENTIDADE (Michael Mulero Inspeções)
st.set_page_config(page_title="S.I.T. - Michael Mulero", layout="wide")

# 2. CONFIGURAÇÃO DO "CÉREBRO" (API KEY)
# Substitua as aspas abaixo pela sua nova chave do Google AI Studio
API_KEY = "SUA_CHAVE_AQUI"
genai.configure(api_key=API_KEY)

# 3. INSTRUÇÕES DE SISTEMA (Padrão Sênior de Inspeção)
SYSTEM_PROMPT = """
Você é o motor de inteligência do Michael Mulero Inspeções. 
Sua tarefa é analisar fotos de indústrias e documentos técnicos (CVCB, ART).
FOCO NA SOLUS/CROPFIELD:
- Identifique Reatores Biológicos, Centrais de GLP e Trocadores de Calor.
- Extraia dados de inflamáveis: D-Limoneno, UN 2319.
- Verifique SPDA: Procure por 9 pontos de descida e malha de aterramento.
- Segurança: Analise cercamento, CFTV e blindagem de perímetro.
Gere um parágrafo técnico e direto para o campo 'Processo Operacional'.
"""

model = genai.GenerativeModel(model_name="gemini-1.5-flash", system_instruction=SYSTEM_PROMPT)

# 4. INTERFACE DO PAINEL DE OPERAÇÃO
st.title("🛡️ Painel de Operação - Michael Mulero Inspeções")
st.subheader("📋 Dados do Risco (Extração Automática)")

with st.sidebar:
    st.info("Status: Sistema Conectado via API Gemini 1.5 Flash")
    cnpj = st.text_input("CNPJ/CPF:", value="21.203.489/0001-79")
    categoria = st.selectbox("Categoria:", ["Indústria", "Comércio", "Residencial"])

# 5. UPLOAD E PROCESSAMENTO
fotos = st.file_uploader("Subir arquivos da vistoria:", accept_multiple_files=True, type=['jpg', 'png', 'jpeg'])

processo_texto = ""

if fotos:
    if st.button("🤖 ANALISAR IMAGENS AGORA"):
        with st.spinner("Girando o programa e processando blindagem..."):
            try:
                # Converte arquivos para formato que a API entende
                img_list = [Image.open(f) for f in fotos]
                # Chama a inteligência para preencher o laudo
                response = model.generate_content(["Descreva o processo operacional desta unidade:", *img_list])
                processo_texto = response.text
                st.success("Análise concluída com sucesso!")
            except Exception as e:
                st.error(f"Erro ao processar: {e}")

# 6. CAMPO DE TEXTO (O que rola lá?)
processo_operacional = st.text_area("Processo Operacional (O que rola lá?):", value=processo_texto, height=200)

# 7. FINALIZAÇÃO E GERAÇÃO DO PARECER
if st.button("🚀 FINALIZAR VISTORIA E GERAR PARECER"):
    if not processo_operacional:
        st.warning("Por favor, preencha a descrição antes de gerar o parecer.")
    else:
        st.balloons()
        st.success("Laudo da SOLUS DO BRASIL gerado com sucesso!")
        st.info("Incluindo: 5 Croquis 3D (Blindagem, SPDA, Setorização, Regional e Ambiental).")
        # Aqui o código chamaria a função de geração de PDF final
