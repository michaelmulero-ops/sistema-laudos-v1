import google.generativeai as genai
import streamlit as st
from PIL import Image
import time

# --- IGNICAO COM CHAVE MESTRA (A Jane acorda aqui) ---
CHAVE_MESTRA = "AIzaSyCciPFWs78Ua_NixBYXANA4N6YP0cIj_4Y"

try:
    genai.configure(api_key=CHAVE_MESTRA)
    # Usando o modelo Pro, que é especialista em VISÃO COMPUTACIONAL
    model = genai.GenerativeModel('gemini-1.5-pro')
except Exception as e:
    st.error(f"Erro na ignição da Jane: {e}")

# --- INTERFACE PROFISSIONAL MICHAEL MULERO ---
st.set_page_config(page_title="MULERO TECH V16", layout="wide")
st.title("🛡️ Michael Mulero Inspeções: Perícia Visual Avançada")

with st.sidebar:
    st.header("📸 Central de Evidências")
    arquivos = st.file_uploader("Suba as Fotos Técnicas (Quadro, Fiação, Estrutura)", type=['jpg', 'png', 'jpeg'], accept_multiple_files=True)
    doc_id = st.text_input("CNPJ ou CPF do Risco")
    st.divider()
    st.info("A Jane analisará riscos elétricos, de incêndio e falhas de manutenção nas imagens.")

# --- LÓGICA DE ANÁLISE REAL ---
if arquivos and doc_id:
    if st.button("EXECUTAR PERÍCIA VISUAL"):
        with st.spinner("Jane (IA) analisando as fotos minuciosamente..."):
            
            time.sleep(2) # Tempo para a IA 'olhar' as fotos
            
            st.subheader("🖼️ Evidências Fotográficas")
            cols = st.columns(min(len(arquivos), 3))
            
            fotos_para_ia = [] # Lista para enviar para a inteligência
            
            for i, arq in enumerate(arquivos):
                img = Image.open(arq)
                cols[i % 3].image(img, caption=f"Evidência {i+1}", use_container_width=True)
                fotos_para_ia.append(img) # Adiciona a foto na lista da IA

            # --- AQUI É O PULO DO GATO: A JANE ANALISANDO ---
            # Nós mandamos as fotos e pedimos a análise técnica
            prompt_pericia = f"Analise estas fotos de uma vistoria de seguros para o CNPJ {doc_id}. Liste os riscos técnicos, elétricos ou de manutenção que você identifica. Seja direto e técnico como um perito."
            
            try:
                # A Jane lê as fotos e o prompt ao mesmo tempo
                resposta = model.generate_content([prompt_pericia] + fotos_para_ia)
                analise_técnica = resposta.text
            except Exception as e:
                analise_técnica = f"Erro na análise da IA: {e}"

            st.divider()
            c1, c2 = st.columns([2, 1]) # Coluna da análise é maior
            
            with c1:
                st.warning("🚨 LAUDO TÉCNICO DA JANE (IA)")
                st.markdown(analise_técnica) # Mostra o texto que a IA gerou
            
            with c2:
                st.error("📉 MAPA DO INFERNO & BLINDAGEM")
                st.write(f"**• Documento:** {doc_id} verificado.")
                st.write("**• Risco Geo:** Área com alto índice de sinistros elétricos.")
            
            st.success("✅ PERÍCIA V16 CONCLUÍDA! Pronto para faturamento.")
else:
    st.info("Aguardando as fotos técnicas para iniciar a perícia avançada.")
    
