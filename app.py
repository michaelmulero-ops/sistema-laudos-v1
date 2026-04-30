import streamlit as st
import datetime
import google.generativeai as genai
import json
from PIL import Image

# 1. CONFIGURAÇÃO DA CHAVE (LIGAÇÃO DIRETA)
# COLOQUE SUA CHAVE ABAIXO ENTRE AS ASPAS
CHAVE_API = "COLE_SUA_CHAVE_AQUI"
genai.configure(api_key=CHAVE_API)
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. SISTEMA DE RASTREAMENTO E SEGURANÇA
st.sidebar.header("Rastreamento Michael Mulero")
status_log = st.sidebar.empty()

def log_rastreio(mensagem):
    hora = datetime.datetime.now().strftime("%H:%M:%S")
    status_log.info(f"[{hora}] {mensagem}")

# 3. CLASSE DE INSPEÇÃO (LÓGICA DE DECISÃO)
class SistemaInspecao:
    def __init__(self, projeto_id):
        self.projeto_id = projeto_id
        self.itens = []

    def adicionar_item(self, nome, severidade, conforme, evidencia_foto):
        self.itens.append({
            "item": nome,
            "severidade": severidade,
            "conforme": conforme,
            "foto": evidencia_foto
        })
        log_rastreio(f"Item adicionado: {nome} (Severidade {severidade})")

    def processar_laudo(self):
        log_rastreio("Processando laudo final e verificando riscos nível 5...")
        aprovado = True
        motivos_reprovacao = []

        for item in self.itens:
            if item['severidade'] == 5 and not item['conforme']:
                aprovado = False
                motivos_reprovacao.append(f"Risco Crítico identificado: {item['item']}")
        
        status = "APROVADO" if aprovado else "DESAPROVADO"
        log_rastreio(f"Resultado final calculado: {status}")
        return {"Status_Final": status, "Motivos": motivos_reprovacao}

# 4. INTERFACE DO SISTEMA
st.title("Michael Mulero Inspeções Tech V1")
st.write("---")

# Campo para subir a foto
foto_carregada = st.file_uploader("Selecione a foto da inspeção", type=['jpg', 'jpeg', 'png'])

if foto_carregada is not None:
    imagem = Image.open(foto_carregada)
    st.image(imagem, caption="Foto carregada", use_column_width=True)
    
    if st.button("Analisar Risco na Foto"):
        try:
            log_rastreio("Enviando foto para análise da IA...")
            
            # Timeout de 20s para evitar travamento (Loop)
            prompt = "Analise esta foto de inspeção técnica. Identifique riscos conforme NRs brasileiras."
            response = model.generate_content([prompt, imagem], request_options={"timeout": 20})
            
            st.write("### Relatório da IA:")
            st.write(response.text)
            log_rastreio("Análise da IA concluída!")
            
        except Exception as e:
            log_rastreio("ERRO: O processamento demorou demais ou falhou.")
            st.error("Tempo esgotado ou falha na conexão. Tente novamente.")
