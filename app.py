import streamlit as st
import datetime
import google.generativeai as genai
from google.api_core import retry

# 1. CONFIGURAÇÃO DA CHAVE (LIGAÇÃO DIRETA)
# Substitua o texto abaixo pela sua chave que começa com 'AIza...'
CHAVE_API = "COLE_SUA_CHAVE_AQUI"
genai.configure(api_key=CHAVE_API)
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. CONFIGURAÇÃO CONTRA LOOPS
# Se a IA demorar mais de 20 segundos, o sistema corta a conexão.
config_segura = {"request_options": {"timeout": 20}}

# 3. INTERFACE E RASTREAMENTO
st.title("Michael Mulero Inspeções Tech V1")

st.sidebar.header("Rastreamento em Tempo Real")
status_log = st.sidebar.empty()

def log_rastreio(mensagem):
    hora = datetime.datetime.now().strftime("%H:%M:%S")
    status_log.info(f"[{hora}] {mensagem}")[cite: 1]

# 4. ÁREA DE TESTE DO SISTEMA
pergunta = st.text_input("O que você deseja analisar agora? (Ex: Risco NR-10)")

if st.button("Executar Análise"):
    try:
        log_rastreio("Iniciando contato com o cérebro da IA...")[cite: 1]
        
        # Chamada segura com o 'disjuntor' de 20 segundos[cite: 2]
        response = model.generate_content(pergunta, request_options={"timeout": 20})
        
        st.write("### Resultado da Inspeção:")
        st.write(response.text)
        log_rastreio("Análise finalizada com sucesso!")[cite: 1]
        
    except Exception as e:
        log_rastreio("ERRO: O sistema parou para evitar um travamento.")[cite: 1, 2]
        st.error(f"Ocorreu um problema ou lentidão. Detalhe: {e}")
