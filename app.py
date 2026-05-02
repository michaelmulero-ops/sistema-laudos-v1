import streamlit as st
import os
import time

# Pasta temporária para salvar arquivos quando estiver offline
OFFLINE_FOLDER = "pendente_upload"
if not os.path.exists(OFFLINE_FOLDER):
    os.makedirs(OFFLINE_FOLDER)

def check_connectivity():
    # Lógica simples para testar se o sistema consegue "pingar" o servidor
    # Se falhar, entramos no modo offline
    return True # Simulação de conexão

st.title("Sistema de Inspeção Híbrido")

# Componente de Captura (Foto ou Vídeo)
upload_file = st.camera_input("Capturar Evidência Técnica")

if upload_file:
    if check_connectivity():
        st.success("Sinal detectado! Enviando para o relatório principal...")
        # Lógica de upload direto para nuvem
    else:
        # MODO OFFLINE: Salva localmente para não perder o trabalho
        file_path = os.path.join(OFFLINE_FOLDER, f"inspecao_{int(time.time())}.jpg")
        with open(file_path, "wb") as f:
            f.write(upload_file.getbuffer())
        st.warning(f"Sem sinal. Foto salva localmente em: {file_path}. Será enviada automaticamente com Wi-Fi.")

# Botão de Sincronização (aparece quando houver arquivos pendentes)
if len(os.listdir(OFFLINE_FOLDER)) > 0:
    if st.button("Sincronizar Arquivos Pendentes"):
        st.info("Subindo inspeções armazenadas...")
        # Lógica para limpar a pasta e subir para o sistema
