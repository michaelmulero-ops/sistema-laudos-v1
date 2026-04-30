import streamlit as st
import datetime
from google.api_core import retry

# --- CONFIGURAÇÃO DE SEGURANÇA CONTRA LOOPS ---
# Se a IA demorar mais de 20 segundos, o sistema corta a conexão para não travar.
config_segura = {"request_options": {"timeout": 20}}

# --- FUNÇÃO DE RASTREAMENTO (BARRA LATERAL) ---
# Isso cria o "diário de bordo" na lateral do seu sistema.
st.sidebar.header("Rastreamento Michael Mulero")
status_log = st.sidebar.empty()

def log_rastreio(mensagem):
    hora = datetime.datetime.now().strftime("%H:%M:%S")
    # Atualiza o status na tela em tempo real[cite: 1].
    status_log.info(f"[{hora}] {mensagem}")

# --- EXEMPLO DE COMO USAR DENTRO DO SEU PROCESSO ---
# Quando você for gerar o laudo, use este bloco:
# try:
#     log_rastreio("Iniciando análise técnica...")[cite: 1]
#     response = model.generate_content(prompt, **config_segura)[cite: 2]
#     log_rastreio("Laudo gerado com sucesso!")[cite: 1]
# except Exception as e:
#     log_rastreio(f"ERRO: O sistema pulou uma etapa para evitar loop.")[cite: 1, 2]
