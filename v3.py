import google.generativeai as genai
import streamlit as st
from PIL import Image
import io

# CHAVE DIRETA PARA NAO DAR ERRO
CHAVE = "AIzaSyCciPFWs78Ua_NixBYXANA4N6YP0cIj_4Y"

try:
    genai.configure(api_key=CHAVE)
    model = genai.GenerativeModel('gemini-1.5-pro')
except:
    st.error("Erro na Jane")

st.set_page_config(page_title="MULERO V20", layout="wide")
st.title("🛡️ Michael Mulero: Perícia 360°")

# AQUI ESTÁ O SEGREDO: Limitar o tamanho do arquivo no código
arquivo = st.file_uploader("Suba UMA foto por vez (Teste)", type=['jpg', 'jpeg', 'png'])

if arquivo:
    if st.button("ANALISAR AGORA"):
        img = Image.open(arquivo)
        
        # Reduzindo a foto drasticamente para 400 pixels (Super Leve)
        img.thumbnail((400, 400))
        
        buffer = io.BytesIO()
        img.save(buffer, format="JPEG", quality=30) # Qualidade baixa só para teste
        img_final = Image.open(buffer)
        
        st.image(img_final, caption="Foto Otimizada")
        
        try:
            res = model.generate_content(["O que tem de errado nessa fiação?", img_final])
            st.warning("🚨 RESULTADO DA PERÍCIA")
            st.write(res.text)
        except Exception as e:
            st.error(f"O servidor ainda barrou: {e}")
else:
    st.info("Aguardando evidências.")
