import streamlit as st
import os

# --- CONFIGURAÇÃO DE EXPORTAÇÃO MICHAEL MULERO ---
st.markdown("""
    <style>
    .croqui-page {
        width: 600px; /* Simulação do tamanho 10x10 em pixels */
        height: 600px;
        border: 2px solid #00FF00;
        margin-bottom: 50px;
        padding: 20px;
        background-color: #1E1E1E;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

def gerar_laudo_6_paginas(lista_croquis):
    st.header("📋 Exportação de Laudo Técnico (6 Páginas - 10x10)")
    
    for i, croqui in enumerate(lista_croquis):
        st.write(f"### Página {i+1}: {croqui['titulo']}")
        
        # Container que simula a página 10x10
        with st.container():
            st.markdown(f'<div class="croqui-page">', unsafe_allow_html=True)
            st.image(croqui['imagem'], use_container_width=True)
            st.write(f"**Análise Davi/Sofia:** {croqui['detalhe']}")
            if 'investigacao' in croqui:
                st.error(f"🔍 Investigação 5 anos: {croqui['investigacao']}")
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.divider() # Salto de página visual no sistema

# --- EXECUÇÃO DO SISTEMA ---
# Aqui o sistema puxa os 6 níveis que consolidamos
meus_croquis = [
    {"titulo": "Frente à Rua", "imagem": "https://via.placeholder.com/600", "detalhe": "Visão técnica frontal exata."},
    {"titulo": "Vizinhança", "imagem": "https://via.placeholder.com/600", "detalhe": "Riscos de exposição lateral."},
    {"titulo": "Ativos Lens", "imagem": "https://via.placeholder.com/600", "detalhe": "Inventário de máquinas NR-10/NR-13."},
    {"titulo": "Geo-Riscos", "imagem": "https://via.placeholder.com/600", "detalhe": "Análise ambiental e infraestrutura."},
    {"titulo": "Segurança/Crime", "imagem": "https://via.placeholder.com/600", "detalhe": "Mapa de calor de ocorrências."},
    {"titulo": "Fluxo 3D Investigativo", "imagem": "https://via.placeholder.com/600", "detalhe": "Processo produtivo com auditoria.", "investigacao": "Sinistros e processos 2021-2026."}
]

if st.button("🚀 Gerar Laudo de 6 Níveis"):
    gerar_laudo_6_paginas(meus_croquis)
