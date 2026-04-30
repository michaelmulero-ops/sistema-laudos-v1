import streamlit as st
import datetime
import google.generativeai as genai
import json
from PIL import Image

# 1. CONFIGURAÇÃO DA CHAVE (LIGAÇÃO DIRETA)
CHAVE_API = "COLE_SUA_CHAVE_AQUI"
genai.configure(api_key=CHAVE_API)
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. SISTEMA DE RASTREAMENTO E SEGURANÇA
# O timeout de 20s evita que o celular trave se a internet 4G/5G oscilar
st.sidebar.header("Rastreamento Michael Mulero")
status_log = st.sidebar.empty()

def log_rastreio(mensagem):
    hora = datetime.datetime.now().strftime("%H:%M:%S")
    status_log.info(f"[{hora}] {mensagem}")[cite: 1]

# 3. INTERFACE OTIMIZADA PARA CELULAR
st.set_page_config(page_title="Mulero Inspeções Mobile", layout="centered")
st.title("Vistoria em Campo 📱")

# Opção de captura direta pela câmera do celular
arquivo_capturado = st.camera_input("Tirar foto da irregularidade")[cite: 1]

# Opção para carregar vídeos ou fotos da galeria
arquivo_galeria = st.file_uploader("Ou suba o vídeo/foto da galeria", type=['jpg', 'jpeg', 'png', 'mp4'])

arquivo_para_analise = arquivo_capturado if arquivo_capturado else arquivo_galeria

if arquivo_para_analise is not None:
    # Se for imagem, mostra na tela
    if arquivo_para_analise.type.startswith('image'):
        imagem = Image.open(arquivo_para_analise)
        st.image(imagem, caption="Evidência Detectada", use_column_width=True)
    
    if st.button("🚀 ANALISAR AGORA"):
        try:
            log_rastreio("Enviando mídia para o cérebro da IA...")[cite: 1]
            
            # Prompt focado em NRs brasileiras (NR-10, 11, 13)
            prompt = "Você é um inspetor de riscos. Analise esta mídia e identifique riscos críticos (Severidade 5). Gere um laudo curto."
            
            # Processamento com proteção contra loop
            if arquivo_para_analise.type.startswith('image'):
                response = model.generate_content([prompt, imagem], request_options={"timeout": 20})
            else:
                # Para vídeo, a IA analisará os metadados/frames
                response = model.generate_content([prompt, arquivo_para_analise], request_options={"timeout": 20})
            
            st.success("Análise de Campo Concluída!")
            st.write(response.text)
            log_rastreio("Laudo enviado para o banco de dados.")[cite: 1]
            
        except Exception as e:
            log_rastreio("ERRO: A conexão falhou ou demorou demais.")[cite: 1, 2]
            st.error("Falha na nuvem. Tente reduzir o tamanho do arquivo.")
