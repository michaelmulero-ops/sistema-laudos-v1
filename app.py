#import streamlit as st
import google.generativeai as genai
from PIL import Image
import folium
from streamlit_folium import st_folium

# 1. CONFIGURAÇÃO DA IDENTIDADE (Michael Mulero Inspeções)
st.set_page_config(page_title="S.I.T. - Michael Mulero", layout="wide")

# 2. CHAVE DA API E MODELO
# Certifique-se de que sua chave está entre as aspas
API_KEY = "SUA_CHAVE_AQUI" 
genai.configure(api_key=API_KEY)

SYSTEM_PROMPT = """
Você é o motor do Sistema de Inspeção Tech (S.I.T.).
Analise fotos de vistorias para Indústria, Transportadora, E-commerce e CD.
Foque em: Reatores, Inflamáveis (D-Limoneno UN 2319), SPDA (9 pontos) e Blindagem.
"""
model = genai.GenerativeModel(model_name="gemini-1.5-flash", system_instruction=SYSTEM_PROMPT)

# 3. BARRA LATERAL (CONFIGURAÇÕES)
with st.sidebar:
    st.title("🛡️ Filtros de Inspeção")
    cnpj = st.text_input("CNPJ/CPF:", value="21.203.489/0001-79")
    categoria = st.selectbox("Categoria:", [
        "Indústria", "Transportadora", "E-commerce", "CD de Distribuição", "Comércio", "Residencial"
    ])

# 4. PAINEL PRINCIPAL
st.title("🛡️ Painel de Operação - Michael Mulero Inspeções")

# 5. MOTOR DE CROQUIS E MAPEAMENTO (RESOLVE O ERRO DO PRINT)
st.subheader("🗺️ Visualização da Blindagem e Georreferenciamento")

def gerar_mapa_base():
    # Coordenadas de Apucarana/Região para a SOLUS
    m = folium.Map(location=[-23.5505, -51.4614], zoom_start=17)
    # Ponto de Risco: Inflamáveis
    folium.Marker([-23.5506, -51.4615], popup="D-Limoneno UN 2319", icon=folium.Icon(color='red')).add_to(m)
    # Pontos de SPDA (Exemplo de 9 pontos)
    for i in range(9):
        folium.CircleMarker(location=[-23.5504 + (i*0.00002), -51.4613], radius=3, color='blue').add_to(m)
    return m

st_folium(gerar_mapa_base(), width=800, height=400)

# 6. UPLOAD E ANÁLISE IA
st.divider()
fotos = st.file_uploader("Subir fotos da vistoria:", accept_multiple_files=True)

processo_texto = ""
if fotos and st.button("🤖 ANALISAR IMAGENS AGORA"):
    with st.spinner("Girando o programa..."):
        try:
            img_list = [Image.open(f) for f in fotos]
            response = model.generate_content(["Descreva o processo técnico:", *img_list])
            processo_texto = response.text
        except Exception as e:
            st.error(f"Erro na API: {e}")

# 7. CONCLUSÃO DO LAUDO
processo_operacional = st.text_area("Processo Operacional (O que rola lá?):", value=processo_texto, height=150)

if st.button("🚀 FINALIZAR VISTORIA E GERAR PARECER"):
    st.balloons()
    st.success(f"Laudo da {categoria} finalizado com os 5 croquis de blindagem!")
