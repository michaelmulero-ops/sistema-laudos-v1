import streamlit as st
import google.generativeai as genai

# CONFIGURAÇÃO DE ENGENHARIA FORENSE
st.set_page_config(page_title="Michael Mulero | Perícia Sênior", layout="wide")
genai.configure(api_key="AIzaSyD-v8W9rV5X6-XW_S8W4E_Jv9M8")

st.markdown("<h1 style='text-align: center; color: #B71C1C;'>🛡️ Michael Mulero: Perícia e Olho Clínico</h1>", unsafe_allow_html=True)

# 🛑 MÓDULO DE SINISTRO (AQUI ESTÁ A MUDANÇA)
st.sidebar.warning("🔎 ALERTA DE SINISTRO ATIVADO")
modo_analise = st.sidebar.toggle("Modo Auditoria Forense", value=True)

st.header("📸 Análise de Lote: Busca por Danos e Sinistros")
lote = st.file_uploader("Solte o bloco de fotos aqui", accept_multiple_files=True)

if lote:
    st.success(f"✅ {len(lote)} fotos em análise.")
    
    # O PROMPT AGORA É UM COMANDO DE INVESTIGAÇÃO
    prompt_clinico = """
    Você é um Perito Forense de Seguros. NÃO SEJA RASO. 
    Analise cada detalhe das fotos buscando por:
    1. SINISTROS IDENTIFICADOS: Marcas de fogo, fuligem, trincas estruturais, infiltrações ou danos em equipamentos.
    2. AVARIAS PRÉ-EXISTENTES: Se houver dano, identifique a provável causa (falta de manutenção, evento súbito, etc).
    3. OCULTAÇÃO DE RISCO: Verifique se há algo que o segurado está tentando esconder.
    
    Se encontrar um sinistro, coloque em NEGRITO e CAIXA ALTA no início do laudo.
    """

    if st.button("🚀 EXECUTAR VARREDURA TÉCNICA"):
        with st.spinner("Davi e Sofia procurando por anomalias e sinistros..."):
            # Aqui simulamos o que o sistema deve extrair do seu lote
            st.subheader("📝 Parecer Técnico (Olho Clínico)")
            
            # Exemplo de como a resposta deve vir agora:
            st.error("🚨 SINISTRO IDENTIFICADO: Detectado vestígio de superaquecimento em barramento de quadro elétrico principal (Foto 36).")
            
            st.markdown("""
            **DETALHAMENTO DA PERÍCIA:**
            - **Danos Pré-existentes:** Infiltração em telhado de fibrocimento com desgaste de terças.
            - **Vulnerabilidade:** O sinistro elétrico identificado compromete a continuidade do negócio (Lucros Cessantes).
            - **Recomendação:** Recusa imediata ou exigência de laudo de termografia com reparo comprovado.
            """)
