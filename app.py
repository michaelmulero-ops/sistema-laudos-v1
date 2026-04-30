import streamlit as st
import datetime
import google.generativeai as genai
import json

# 1. CONFIGURAÇÃO DE SEGURANÇA E CHAVE
CHAVE_API = "COLE_SUA_CHAVE_AQUI"
genai.configure(api_key=CHAVE_API)
config_segura = {"request_options": {"timeout": 20}} # Impede o travamento do sistema

# 2. RASTREAMENTO EM TEMPO REAL
st.sidebar.header("Rastreamento Michael Mulero")
status_log = st.sidebar.empty()

def log_rastreio(mensagem):
    hora = datetime.datetime.now().strftime("%H:%M:%S")
    status_log.info(f"[{hora}] {mensagem}")[cite: 1]

# 3. SUA CLASSE DE INSPEÇÃO (Lógica de Decisão)
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
        log_rastreio(f"Item adicionado: {nome} (Severidade {severidade})")[cite: 1]

    def processar_laudo(self):
        log_rastreio("Processando laudo final e verificando riscos nível 5...")[cite: 1]
        aprovado = True
        motivos_reprovacao = []

        for item in self.itens:
            # Regra de Ouro contra loops e riscos críticos
            if item['severidade'] == 5 and not item['conforme']:
                aprovado = False
                motivos_reprovacao.append(f"Risco Crítico identificado: {item['item']}")
        
        status = "APROVADO" if aprovado else "DESAPROVADO"
        log_rastreio(f"Resultado final calculado: {status}")[cite: 1]
        return {"Status_Final": status, "Motivos": motivos_reprovacao}

# 4. INTERFACE STREAMLIT
st.title("Michael Mulero Inspeções - Análise de Risco")

# Exemplo de teste no sistema
if st.button("Simular Processamento do Laudo"):
    try:
        # Iniciando a classe para o projeto de hoje
        inspecao = SistemaInspecao("Projeto_Teste_Hoje")
        
        # Simulando os itens que você e a Taís vão coletar
        inspecao.adicionar_item("Instalação Elétrica (NR 10)", 5, False, "evidencia_01.jpg")
        inspecao.adicionar_item("Extintores (NR 23)", 2, True, "evidencia_02.jpg")
        
        # Processando com segurança
        resultado = inspecao.processar_laudo()
        
        st.write("### Relatório de Saída:")
        st.json(resultado)
        
    except Exception as e:
        log_rastreio("ERRO: O processamento falhou ou demorou demais.")[cite: 1, 2] interrompida.")[cite: 1, 2]
            st.error(f"Falha ao processar imagem: {e}")
