import streamlit as st
try:
    from streamlit_webrtc import webrtc_streamer
    import av
except ImportError:
    st.error("O motor de Realidade Aumentada está sendo inicializado. Por favor, aguarde 1 minuto.")
