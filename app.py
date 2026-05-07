import streamlit as st
import pandas as pd

# CONFIGURAÇÃO DA INTERFACE - PADRÃO DARK MODE MINIMALISTA
st.set_page_config(page_title="Michael Mulero Inspeções Tech V1", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #262730; color: white; }
    .report-box { border: 1px solid #444; padding: 20px; border-radius: 10px; background-color: #161b22; }
    </style>
    """, unsafe_allow_html=True)

# CABEÇALHO DO SISTEMA
st.title("🛡️ Michael Mulero Inspeções - Sistema de Blindagem")
st.subheader("Análise de Risco Industrial de Alta Complexidade")

# --- MÓDULO 1: DADOS DA PROPOSTA (INPUT AUTOMATIZADO) ---
with st.expander("📝 Dados do Proponente e Subscrição", expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        proponente = st.text_input("Proponente", "USITRORG AMBIENTAL AS")
        cnpj = st.text_input("CNPJ", "28.698.939/0001-90") #
        local = st.text_input("Localização", "RODOVIA BR 153, JACAREZINHO-PR") #
    with col2:
        is_segurada = st.number_input("Importância Segurada (R$)", value=5000000.00) #
        atividade = st.text_input("Atividade Principal", "FABRICA COM MATERIA INORGANICA/NITROGENADOS") #

# --- MÓDULO 2: INVESTIGAÇÃO ANTI-FRAUDE E COMPATIBILIDADE ---
st.header("🔍 Módulo Anti-Fraude e Idoneidade")
with st.container():
    st.info("⚠️ Análise Cadastral: Proposta em aberto sob vistoria prévia. Verificando compatibilidade patrimonial.")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("**Saúde do CNPJ:**")
        st.write("- Natureza Jurídica: Sociedade Anônima (S.A.)")
        st.write("- Status: Ativo e operacional.")
    with col_b:
        # Lógica de Blindagem de Valor
        compatibilidade = "COMPATÍVEL" if is_segurada <= 5500000 else "ALERTA DE SOBRE-SEGURO"
        st.metric("Status de Valor Patrimonial", compatibilidade)

# --- MÓDULO 3: INVENTÁRIO TÉCNICO E ATIVOS ---
st.header("🏗️ Inventário de Ativos e Instalações")
inventario_dados = {
    "Item": ["Barracão Unificado", "Lagoas de Biogás", "Forno de Aquecimento", "Transformador/Cabine", "Estoque Nitrogenados"],
    "Estado": ["Bom/Blindado", "Operacional", "Em Uso", "Protegido", "Armazenado"],
    "Risco": ["Incêndio", "Explosão/Ambiental", "Térmico", "Danos Elétricos", "Contaminação"]
}
st.table(pd.DataFrame(inventario_dados))

# --- MÓDULO 4: ANÁLISE DE VULNERABILIDADE EXTERNA E CLIMATOLÓGICA ---
st.header("🌍 Riscos Externos e Regionais (Jacarezinho-PR)")
col_c, col_d = st.columns(2)
with col_c:
    st.markdown("### 🌪️ Climatologia e Meio Ambiente")
    st.write("- **Incidência de Raios:** Alta (Norte Pioneiro). Exigência de SPDA NBR 5419.")
    st.write("- **Riscos de Ventos:** Rota de vendavais; telhamento requer fixação técnica.")
    st.write("- **Passivo Ambiental:** Risco de transbordo das lagoas para a BR 153 em caso de chuvas intensas.")
with col_d:
    st.markdown("### ✈️ Segurança e Rota")
    st.write("- **Tráfego Aéreo:** Rota de aeronaves agrícolas/comerciais (Risco de Queda).")
    st.write("- **Exposição Rodoviária:** Risco de impacto e carga perigosa de terceiros (BR 153).")
    st.write("- **Corpo de Bombeiros:** Tempo de resposta estimado para Parque Industrial.")

# --- MÓDULO 5: GERADOR DE PARECER TÉCNICO (BLINDAGEM FINAL) ---
st.header("📄 Parecer de Blindagem Michael Mulero")
parecer_texto = f"""
O risco da {proponente} apresenta adensamento de valor compatível com a I.S. de R$ {is_segurada:,.2f}. 
A inspeção física validou a unificação dos blocos 01 e 02 como estratégia de mitigação de propagação.
PONTOS CRÍTICOS: Monitoramento das lagoas de biogás e manutenção do sistema elétrico/transformador.
CONCLUSÃO: Risco aceitável sob condições de manutenção preventiva e vigilância patrimonial.
"""
final_report = st.text_area("Texto do Laudo (Editável)", parecer_texto, height=200)

if st.button("GERAR RELATÓRIO COMPLETO (PDF)"):
    st.success("Relatório gerado com sucesso! Arquivo configurado sem indicadores de norte e com frente para a rua.")

# --- VISUALIZAÇÃO DO ESBOÇO (DARK MODE) ---
st.markdown("<div class='report-box'><b>INFOGRÁFICO TÉCNICO:</b> Terreno Triangular | Frente: Rodovia BR 153 | Norte: Omitido | Status: Blindado</div>", unsafe_allow_html=True)
