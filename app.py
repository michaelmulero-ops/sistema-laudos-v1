import streamlit as st
from PIL import Image, ImageOps, ImageDraw

# Função para o Zoom de Evidência (Estilo a análise técnica que fizemos)
def processar_zoom_tecnico(imagem, x, y):
    img = Image.open(imagem)
    # Define a área de corte (200px ao redor do ponto)
    caixa = (x-100, y-100, x+100, y+100)
    zoom = img.crop(caixa).resize((400, 400))
    # Adiciona a borda vermelha de alerta
    zoom = ImageOps.expand(zoom, border=5, fill='red')
    return zoom
