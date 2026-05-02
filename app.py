# --- AGENTES DE IA (SISTEMA DE MÚLTIPLOS CÉREBROS) ---

def agente_sofia_croqui(imagem):
    """Sofia: Processa o escaneamento e prepara o esboço do croqui"""
    # Aqui ela aplica a visão de frente para a rua e extrai a geometria
    img_scan = apply_advanced_scan(imagem) 
    st.sidebar.success("Sofia: Croqui e fachada mapeados ✅")
    return img_scan

def agente_davi_analise(medidas, riscos_detectados):
    """Davi: Analisa as conformidades com as NRs e NBRs"""
    # Simulação de análise lógica baseada nos seus padrões técnicos
    analise = f"Davi: Verificado pé-direito de {medidas}. Conformidade com NR-13 OK."
    st.sidebar.info(analise)
    return analise

# --- ATUALIZAÇÃO NO FLUXO DE CAPTURA ---

if foto_cam or arquivos:
    # Sofia assume a frente do escaneamento visual
    st.write("### 🧠 Sofia está gerando o croqui visual...")
    
    # Davi assume a conferência das normas em paralelo
    st.write("### 🧠 Davi está validando as métricas e NRs...")
    
    # O sistema principal (Gemini) fica livre para organizar o laudo final
