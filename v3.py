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
st.set_page_config(page_title="MULERO ULTRA V18", layout="wide")
st.title("🛡️ Michael Mulero: Perícia Visual Ultra")

with st.sidebar:
    st.header("📸 Central de Laudos")
    arquivos = st.file_uploader("Fotos (Limite de 10MB total)", type=['jpg', 'png', 'jpeg'], accept_multiple_files=True)
    doc_id = st.text_input("CNPJ/CPF")

# --- LÓGICA DE COMPRESSÃO E ANÁLISE ---
if arquivos and doc_id:
    if st.button("GERAR LAUDO AGORA"):
        with st.spinner("Jane comprimindo e analisando as evidências..."):
            
            fotos_leves = []
            cols = st.columns(min(len(arquivos), 4))
            
            for i, arq in enumerate(arquivos):
                # Redimensionando a foto para não dar o erro 413
                img = Image.open(arq)
                img.thumbnail((800, 800)) # Deixa a foto leve mas nítida
                cols[i % 4].image(img, use_container_width=True)
                fotos_leves.append(img)

            prompt = f"Perícia rápida Michael Mulero (Risco {doc_id}). Liste os 3 riscos críticos de incêndio/pane elétrica nessas fotos."
            
            try:
                # Envia as fotos já "encolhidas" para a IA
                res = model.generate_content([prompt] + fotos_leves)
                st.divider()
                st.warning("🚨 ANÁLISE TÉCNICA")
                st.markdown(res.text)
                st.success("✅ Laudo gerado sem erros de servidor!")
            except Exception as e:
                st.error(f"Erro na Jane: {e}")
else:
    st.info("Suba as fotos para testar o sistema otimizado.")
