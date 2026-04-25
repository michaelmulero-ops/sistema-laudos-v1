import google.generativeai as genai
import streamlit as st
from PIL import Image
import io

# --- MOTOR DE ALTA PERFORMANCE ---
CHAVE_MESTRA = "AIzaSyCciPFWs78Ua_NixBYXANA4N6YP0cIj_4Y"

try:
    genai.configure(api_key=CHAVE_MESTRA)
    model = genai.GenerativeModel('gemini-1.5-pro')
except Exception as e:
    st.error(f"Erro na ignição: {e}")

# --- INTERFACE ---
st.set_page_config(page_title="MULERO ULTRA V19", layout="wide")
st.title("🛡️ Michael Mulero: Perícia Visual Ultra")

with st.sidebar:
    st.header("📸 Central de Laudos")
    # Reduzi o limite visual para voce saber que estamos otimizando
    arquivos = st.file_uploader("Suba suas fotos aqui", type=['jpg', 'png', 'jpeg'], accept_multiple_files=True)
    doc_id = st.text_input("CNPJ/CPF")

# --- LÓGICA DE COMPRESSÃO RADICAL ---
if arquivos and doc_id:
    if st.button("GERAR LAUDO AGORA"):
        with st.spinner("Jane triturando o peso e analisando..."):
            
            fotos_leves = []
            
            for arq in arquivos:
                img = Image.open(arq)
                
                # Redimensionamento agressivo para passar em qualquer servidor
                img.thumbnail((600, 600)) 
                
                # Converte para JPEG super leve
                buffer = io.BytesIO()
                img.save(buffer, format="JPEG", quality=50) # Qualidade 50% ja basta para a IA ver o erro
                img_final = Image.open(buffer)
                
                fotos_leves.append(img_final)

            prompt = f"Perícia rápida Michael Mulero (Risco {doc_id}). Liste os 3 riscos críticos nestas fotos."
            
            try:
                res = model.generate_content([prompt] + fotos_leves)
                st.divider()
                st.warning("🚨 ANÁLISE TÉCNICA FINAL")
                st.markdown(res.text)
                st.success("✅ Sistema rodou limpo!")
            except Exception as e:
                st.error(f"Erro na análise: {e}")
else:
    st.info("Aguardando evidências.")
