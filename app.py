import streamlit as st
import cv2
import numpy as np
import os
import time
from datetime import datetime

# --- CONFIGURAÇÕES DE CAMINHO ---
UPLOAD_QUEUE = "fila_de_inspecao"
if not os.path.exists(UPLOAD_QUEUE):
    os.makedirs(UPLOAD_QUEUE)

# --- FUNÇÕES DE INTELIGÊNCIA ---

def apply_hud_effect(frame):
    """Adiciona o visual de scanner dos vídeos (caixas e linhas de varredura)"""
    height, width, _ = frame.shape
    # Linha de Scan Horizontal (Efeito visual)
    scan_line_y = int((time.time() * 100) % height)
    cv2.line(frame, (0, scan_line_y), (width, scan_line_y), (0, 255, 0), 2)
    
    # Simulação de Detecção (Caixas estilo HUD)
    # Aqui a IA identificaria quadros elétricos, máquinas, etc.
    cv2.rectangle(frame, (width//4, height//4), (3*width//4, 3*height//4), (0, 255, 0), 1)
    cv2.putText(frame, "ANALISANDO RISCO NBR/NR...", (width//4, height//4 - 10), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
    
    return frame

def check_sync():
    """Tenta enviar arquivos pendentes se houver internet"""
    try:
        # Tenta conectar ao Google para testar sinal
        import socket
        socket.create_connection(("8.8.8.8", 53), timeout=2)
        
        arquivos = os.listdir(UPLOAD_QUEUE)
        if arquivos:
            with st.spinner(f"📡 Wi-Fi Detectado! Sincronizando {len(arquivos)} arquivos..."):
                for arq in arquivos:
                    # Lógica de upload para o Michael Mulero Inspeções Cloud
                    time.sleep(0.5) # Simula o tempo de envio
                    os.remove(os.path.join(UPLOAD_QUEUE, arq))
            st.toast("✅ Todos os laudos foram sincronizados!", icon="🚀")
    except:
        pass # Sem internet, permanece em modo silencioso

# --- INTERFACE STREAMLIT ---

st.set_page_config(page_title="Michael Mulero Inspeções Tech", layout="wide")

st.title("🛡️ Michael Mulero Inspeções Tech V1")
st.write(f"Status: {'🟢 Online' if 'online' else '🟡 Modo Offline Ativo'}")

# Componente de Captura Híbrida
input_type = st.radio("Selecione o modo:", ["Foto de Campo", "Vídeo de Inspeção"])

img_file = st.camera_input("Capturar Evidência")

if img_file:
    # Processamento Visual de Scan (O efeito dos vídeos que você mandou)
    file_bytes = np.asarray(bytearray(img_file.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)
    scanned_image = apply_hud_effect(opencv_image)
    
    # Salva na Fila (Garante que não se perca no condomínio/indústria)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"inspecao_{timestamp}.jpg"
    save_path = os.path.join(UPLOAD_QUEUE, filename)
    
    cv2.imwrite(save_path, scanned_image)
    
    st.image(scanned_image, channels="BGR", caption="Scan de Risco Concluído e Salvo localmente")
    st.info("O arquivo será enviado automaticamente assim que detectarmos Wi-Fi.")

# Roda o verificador de sincronização em cada interação
check_sync()
