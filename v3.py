GEMINI_API_KEY
import streamlit as st
import google.generativeai as genai
from datetime import datetime

# 1. Configuração de Segurança (Lê as chaves que você salvou no Secrets)
try:
    gemini_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=gemini_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("Erro: A chave GEMINI_API_KEY não foi encontrada nos Secrets.")

st.set_page_config(page_title="Michael Mulero Inspeções", layout="wide")
st.title("🏭 Fábrica de Laudos - Michael Mulero")

# 2. Formulário de Vistoria
with st.form("form_vistoria"):
    col1, col2 = st.columns(2)
    with col1:
        cliente = st.text_input("Nome do Cliente/Seguradora")
        cidade = st.text_input("Cidade da Vistoria")
    with col2:
        inspetor = st.text_input("Inspetor Responsável", value="Michael Mulero")
        data = st.date_input("Data da Vistoria", datetime.now())

    st.subheader("Análise Técnica de Campo")
    obs_eletrica = st.text_area("Observações sobre a Elétrica (ex: fios expostos, quadro antigo)")
    obs_entorno = st.text_area("Observações sobre o Entorno (ex: vizinhos, mato alto)")

    submit = st.form_submit_button("GERAR LAUDO PROFISSIONAL")

# 3. A Mágica da Inteligência Artificial
if submit:
    with st.spinner("O Gemini está analisando os riscos e escrevendo o laudo..."):
        # Aqui o sistema pede para a IA escrever o texto profissional
        prompt = f"Aja como um Inspetor de Riscos Sênior. Com base nestas notas de campo: '{obs_eletrica}', escreva um parágrafo técnico e formal para um laudo de seguro sobre o risco elétrico."
        
        response = model.generate_content(prompt)
        texto_eletrica = response.text

        st.success("Laudo Gerado com Sucesso!")
        st.subheader("Resultado da Análise Técnica:")
        st.write(f"**BOX ELÉTRICA:** {texto_eletrica}")
        
        # Aqui você teria o botão de baixar o PDF pronto
        
