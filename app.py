import google.generativeai as genai
from PIL import Image

# Configura sua chave que você já tem nos "Secrets" do Colab
from google.colab import userdata
genai.configure(api_key=userdata.get('GOOGLE_API_KEY'))

def identificar_equipamento_com_lens(caminho_foto):
    # Carrega a imagem
    img = Image.open(caminho_foto)
    
    # Usa o modelo vision para analisar a foto
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # Prompt focado no seu padrão Michael Mulero Inspeções
    prompt = """
    Analise esta imagem de inspeção técnica. 
    1. Identifique o equipamento (Ex: Transformador, Extintor, Painel).
    2. Extraia dados de placas técnicas (Potência, Modelo, Fabricante).
    3. Resuma o estado de conservação para um laudo de seguros.
    Resposta curta e técnica.
    """
    
    response = model.generate_content([prompt, img])
    return response.text

# Exemplo de uso:
# resultado = identificar_equipamento_com_lens('foto_da_serraria.jpg')
# print(resultado)
