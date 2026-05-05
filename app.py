import google.generativeai as genai

# Configuração da API Key (Referência: 04/05/2026)
genai.configure(api_key="SUA_CHAVE_AQUI")

# Configuração do Modelo e Instrução do Sistema
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="Você é o motor de análise do Michael Mulero Inspeções. "
                       "Extraia dados técnicos de indústrias de biofertilizantes, "
                       "reatores, SPDA (9 pontos) e inflamáveis (UN 2319). "
                       "Gere o 'Processo Operacional' de forma técnica e direta."
)

# Função para processar a vistoria e liberar o botão
def processar_vistoria(lista_imagens):
    try:
        # Envia as fotos para o "cérebro" no AI Studio
        response = model.generate_content(["Descreva o processo desta indústria:", *lista_imagens])
        return response.text
    except Exception as e:
        return f"Erro ao girar o programa: {e}"
