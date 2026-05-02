from groq import Groq

# O Davi agora roda em LPU (Velocidade máxima)
client = Groq(api_key="SUA_CHAVE_AQUI") 

def agente_davi_turbo(medidas, normas):
    """Davi analisando NRs em milissegundos"""
    prompt = f"Analise como inspetor sênior: Prédio com pé-direito {medidas}. Verifique conformidade com {normas}."
    
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama3-8b-8192", # Modelo ultra-rápido
    )
    return chat_completion.choices[0].message.content
