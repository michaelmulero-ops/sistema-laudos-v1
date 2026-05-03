import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av

st.header("🛡️ Croqui de Blindagem com Realidade Aumentada")
st.write("Aponte a câmera para a estrutura para sobrepor o mapa de blindagem técnica.")

# Função que desenha a 'camada' de blindagem sobre o vídeo em tempo real
def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")
    
    # Adicionando uma malha técnica (overlay) de auditoria
    # Isso simula a blindagem projetada na visão do inspetor
    height, width, _ = img.shape
    # Desenha bordas de zona segura (verde)
    img[0:height, 0:20] = [0, 255, 0] 
    img[0:height, width-20:width] = [0, 255, 0]
    
    return av.VideoFrame.from_ndarray(img, format="bgr24")

webrtc_streamer(
    key="RA-Vistoria-Forense",
    video_frame_callback=video_frame_callback,
    media_stream_constraints={"video": True, "audio": False},
    rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
)
