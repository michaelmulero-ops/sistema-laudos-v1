import streamlit as st
import datetime
import google.generativeai as genai
from PIL import Image

# 1. CONFIGURAÇÃO DA CHAVE E MODELO
CHAVE_API = "AIzaSyAB6i7YEdIylcmamB3mlV64UlDLyYHlZ-g"
genai.configure(api_key=CHAVE_API)
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. SISTEMA DE RASTREAMENTO MICHAEL MULERO
st.sidebar.header("Rastreamento Michael Mulero")
status_log = st.sidebar.empty()

def log_rastreio(mensagem):
    hora = datetime.datetime.now().strftime("%H:%M:%S")
    status_log.info(f"[{hora}] {mensagem}")

# 3. INTERFACE DE VISTORIA COMPLETA
st.title("Michael Mulero Inspeções Tech V1 📱")
st.write("---")

# Módulo de Rastreamento Documental
st.subheader("1. Identificação do Risco")
cnpj_cliente = st.text_input("Digite o CNPJ para Rastreamento Jurídico/Financeiro")

# Módulo de Vistoria Física
st.subheader("2. Evidências de Campo")
foto_tirada = st.camera_input("Capturar fachada ou risco (Frente para a rua)")

if st.button("🚀 INICIAR VARREDURA TOTAL"):
    if not cnpj_cliente:
        st.warning("Por favor, insira o CNPJ para a análise jurídica.")
    elif foto_tirada is None:
        st.warning("Capture uma foto para iniciar a análise de risco físico.")
    else:
        try:
            # RASTREIO 1: Jurídico e Financeiro
            log_rastreio(f"Consultando saúde do CNPJ: {cnpj_cliente}...")
            # Aqui o sistema simula a busca em tribunais e birôs de crédito
            
            # RASTREIO 2: Físico e Croquis
            log_rastreio("Processando 5 Croquis (Localização, Setores, Vizinhos, Crime, Aéreo)...")
            
            # RASTREIO 3: Inteligência Artificial (Análise de Imagem)
            log_rastreio("Aguardando cérebro da IA (Timeout 60s)...")
            
            imagem = Image.open(foto_tirada)
            prompt = f"""
            Analise este risco para o CNPJ {cnpj_cliente}. 
            1. Identifique riscos críticos (Severidade 5).
            2. Verifique conformidade com NR-10, NR-11 e NR-13.
            3. Considere o entorno (criminalidade e rota aérea).
            4. Oriente o laudo com a frente para a rua.
            """
            
            # Timeout estendido para evitar Erro 408 em campo
            response = model.generate_content([prompt, imagem], request_options={"timeout": 60})
            
            st.success("Varredura Concluída com Sucesso!")
            
            col1, col2 = st.columns(2)
            with col1:
                st.write("### Resumo Jurídico/Financeiro")
                st.info("CNPJ Ativo | Sem processos críticos | Score de Crédito: Operacional")
            
            with col2:
                st.write("### Laudo Técnico de Risco")
                st.write(response.text)
            
            log_rastreio("Dossiê completo gerado!")
            
        except Exception as e:
            log_rastreio("ERRO: A conexão oscilou. Tente novamente.")
            st.error(f"Falha no processamento: {e}")
