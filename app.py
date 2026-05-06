from PIL import Image, ImageDraw, ImageFont

def gerar_infografico_localizacao(endereco, cidade, output_path):
    # Carrega o modelo padrão da Michael Mulero Inspeções
    template = Image.open('modelo_localizacao_padrao.png')
    draw = ImageDraw.Draw(template)
    
    # Configuração de Fonte (ajuste o caminho da fonte no seu servidor/PC)
    font_titulo = ImageFont.truetype("Arial_Bold.ttf", 40)
    
    # Insere os dados dinâmicos no modelo
    draw.text((100, 50), f"RISCO: {endereco}", fill="black", font=font_titulo)
    draw.text((100, 100), f"CIDADE: {cidade}", fill="black", font=font_titulo)
    
    # Salva o arquivo final pronto para o laudo
    template.save(output_path)
    return output_path

# Exemplo de uso rápido
gerar_infografico_localizacao("Rua Alexander Graham Bell, 255", "Londrina/PR", "anexo_localizacao.png") 
