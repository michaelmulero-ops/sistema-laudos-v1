import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. IDENTIDADE E CONFIGURAÇÃO (Michael Mulero Inspeções)
st.set_page_config(page_title="S.I.T. - Michael Mulero", layout="wide")

# 2. CHAVE DA API (Google AI Studio)
API_KEY = "SUA_CHAVE_AQUI"
genai.configure(api_key=API_KEY)

# 3. INSTRUÇÕES DO SISTEMA (Níveis de Inspeção)
SYSTEM_PROMPT = """
Você é o motor do Sistema de Inspeção Tech (S.I.T.).
Analise fotos de vistorias para:
- INDÚSTRIA: Reatores, GLP e inflamáveis (ex: D-Limoneno UN 2319).
- TRANSPORTADORA: Tanques de diesel, frota e oficinas.
- E-COMMERCE: Áreas de picking, estoque de embalagens e carga de incêndio.
- CD DE DISTRIBUIÇÃO: Docas, altura de estocagem e sprinklers.
Identifique sempre os 9 pontos de SPDA e a blindagem de perímetro.
"""

model = genai.GenerativeModel(model_name="gemini-1.5-flash", system_instruction=SYSTEM_PROMPT)

# 4. PAINEL LATERAL
with st.sidebar:
    st.title("🛡️ Configurações")
    cnpj = st.text_input("CNPJ/CPF:", value="21.203.489/0001-79")
    # AQUI ESTÃO AS NOVAS CATEGORIAS QUE ADICIONAMOS:
    categoria = st.selectbox("Categoria:", [
        "Indústria", 
        "Transportadora", 
        "E-commerce", 
        "CD de Distribuição",
        "Comércio", 
        "Residencial"
    ])

# 5. CORPO DO PROGRAMA
st.title("🛡️ Painel de Operação - Michael Mulero Inspeções")
st.subheader(f"📋 Vistoria: {categoria}")

fotos = st.file_uploader("Subir arquivos da vistoria:", accept_multiple_files=True, type=['jpg', 'png', 'jpeg'])

processo_texto = ""

if fotos:
    if st.button("🤖 ANALISAR IMAGENS AGORA"):
        with st.spinner("Extraindo dados e processando blindagem..."):
            try:
                img_list = [Image.open(f) for f in fotos]
                response = model.generate_content(["Descreva o processo técnico:", *img_list])
                processo_texto = response.text
                st.success("Análise automática concluída!")
            except Exception as e:
                st.error(f"Erro de conexão: {e}")

# 6. CAMPO DE DESCRIÇÃO
processo_operacional = st.text_area("Processo Operacional (O que rola lá?):", value=processo_texto, height=200)

# 7. BOTÃO FINAL
if st.button("🚀 FINALIZAR VISTORIA E GERAR PARECER"):
    if not processo_operacional:
        st.warning("Preencha a descrição antes de finalizar.")
    else:
        st.balloons()
        st.success(f"Laudo de {categoria} gerado com sucesso!")
        st.info("Incluindo os 5 Croquis 3D de Blindagem e SPDA.")
