import streamlit as st
import google.generativeai as genai
from PIL import Image

# Configuração de Segurança
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
except:
    st.error("Configure a GOOGLE_API_KEY nos Secrets do Streamlit!")

# Título da sua Marca
st.set_page_config(page_title="Michael Mulero Inspeções Tech V1", layout="wide")
st.title("🛡️ Michael Mulero Inspeções - Tech V1")
st.subheader("Fábrica de Laudos Automatizada")

# Upload da Foto de Campo
arquivo = st.file_uploader("Arraste a foto da inspeção aqui", type=['jpg', 'png', 'jpeg'])

if arquivo:
    col1, col2 = st.columns(2)
    img = Image.open(arquivo)
    
    with col1:
        st.image(img, caption="Foto de Campo", use_container_width=True)
    
    with col2:
        with st.spinner('O Google Lens está analisando o equipamento...'):
            model = genai.GenerativeModel('gemini-1.5-flash')
            prompt = "Identifique este equipamento técnico para seguro, extraia dados da placa e sugira o estado de conservação."
            response = model.generate_content([prompt, img])
            
            st.success("Análise Concluída!")
            st.text_area("Texto para o Relatório:", value=response.text, height=300)
            
            # Rodapé padrão conforme seu novo requisito
            st.info("📌 Orientação: Frente-para-Rua | Norte Magnético Ignorado")
